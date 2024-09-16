import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

# Anomaly Detection Model for Network Traffic
def detect_anomalies(network_data):
    # Feature selection and preprocessing
    features = network_data.drop(['timestamp', 'label'], axis=1)

    # Load or train the Isolation Forest model
    try:
        with open('models/anomaly_detector.pkl', 'rb') as f:
            model = pickle.load(f)
    except FileNotFoundError:
        model = IsolationForest(n_estimators=100, contamination=0.01, random_state=42)
        model.fit(features)
        with open('models/anomaly_detector.pkl', 'wb') as f:
            pickle.dump(model, f)

    # Predict anomalies
    predictions = model.predict(features)
    network_data['anomaly'] = predictions
    anomalies = network_data[network_data['anomaly'] == -1]
    return anomalies

# Log File Classification Model
def classify_logs(log_data):
    # Load or train the log classifier
    try:
        with open('models/log_classifier.pkl', 'rb') as f:
            classifier = pickle.load(f)
            vectorizer = pickle.load(f)
    except FileNotFoundError:
        # Sample labeled data for training
        logs = ['Failed login attempt from IP 192.168.1.1',
                'User admin logged in successfully',
                'Error: Disk space low on /dev/sda1',
                'Suspicious activity detected from IP 10.0.0.5']
        labels = [1, 0, 0, 1]  # 1 for threat, 0 for normal

        vectorizer = TfidfVectorizer()
        X_train = vectorizer.fit_transform(logs)
        y_train = labels

        classifier = LogisticRegression()
        classifier.fit(X_train, y_train)

        with open('models/log_classifier.pkl', 'wb') as f:
            pickle.dump(classifier, f)
            pickle.dump(vectorizer, f)

    # Transform log data and predict threats
    X_test = vectorizer.transform(log_data)
    predictions = classifier.predict(X_test)
    log_results = pd.DataFrame({'log': log_data, 'threat': predictions})
    threats = log_results[log_results['threat'] == 1]
    return threats
