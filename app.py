from flask import Flask, render_template, request, redirect, url_for
import os
from model import detect_anomalies, classify_logs
from utils.data_loader import load_network_data, load_log_data

app = Flask(__name__)

# Load sample data at start
network_data = load_network_data('data/network_traffic.csv')
log_data = load_log_data('data/system_logs.txt')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze_network', methods=['POST'])
def analyze_network():
    anomalies = detect_anomalies(network_data)
    return render_template('index.html', anomalies=anomalies.to_html())

@app.route('/analyze_logs', methods=['POST'])
def analyze_logs():
    threats = classify_logs(log_data)
    return render_template('index.html', threats=threats.to_html())

if __name__ == '__main__':
    app.run(debug=True)
