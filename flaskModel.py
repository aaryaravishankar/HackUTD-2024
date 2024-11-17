import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from flask import Flask, request, jsonify
import io
import json

app = Flask(__name__)


@app.route('/detect-anomalies', methods=['POST'])
def detect_anomalies():
    # Get the uploaded CSV file from the frontend
    file = request.files.get('file')
    if not file:
        return jsonify({"error": "No file uploaded"}), 400

    # Load and preprocess the data
    df = pd.read_csv(file)
    df['Time'] = pd.to_datetime(df['Time'], format='%m/%d/%Y %I:%M:%S %p')

    df['Time Difference (minutes)'] = df['Time'].diff().dt.total_seconds() / 60
    df['Rate of Change Volume (per minute)'] = df['Inj Gas Meter Volume Instantaneous'].diff(
    ) / df['Time Difference (minutes)']

    df['Deviation'] = (df['Inj Gas Meter Volume Setpoint'] -
                       df['Inj Gas Meter Volume Instantaneous']) / df['Inj Gas Meter Volume Setpoint']
    df = df.dropna()

    features = ['Inj Gas Meter Volume Instantaneous',
                'Inj Gas Valve Percent Open',
                'Rate of Change Volume (per minute)',
                'Deviation']

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(df[features])

    iso_forest = IsolationForest(contamination=0.0085, random_state=42)
    df['Anomaly'] = iso_forest.fit_predict(X_scaled)
    df['Anomaly'] = df['Anomaly'].apply(lambda x: 1 if x == -1 else 0)

    # Filter anomalies
    detected_anomalies = df[df['Anomaly'] == 1][[
        'Time', 'Inj Gas Meter Volume Instantaneous', 'Deviation']]

    # Save the plot to a BytesIO object
    plt.figure(figsize=(12, 6))
    plt.plot(df['Time'], df['Inj Gas Meter Volume Instantaneous'],
             label='Inj Gas Meter Volume')
    plt.scatter(df['Time'][df['Anomaly'] == 1],
                df['Inj Gas Meter Volume Instantaneous'][df['Anomaly'] == 1],
                color='red', label='Anomalies')
    plt.xlabel('Time')
    plt.ylabel('Inj Gas Meter Volume Instantaneous')
    plt.title('Anomaly Detection for Hydrate Formation')
    plt.legend()

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    img_url = "data:image/png;base64," + \
        json.dumps(img.read().decode('latin1'))

    # Return anomalies and plot
    return jsonify({
        "anomalies": detected_anomalies.to_dict(orient='records'),
        "plot": img_url
    })


if __name__ == '__main__':
    app.run(debug=True)
