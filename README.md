# **AI-Enhanced Cybersecurity Threat Detection**

This project applies **machine learning** and **NLP** techniques to detect potential cybersecurity threats by analyzing **network traffic data** and **system logs**. It uses an **Isolation Forest algorithm** to detect anomalies in network traffic and a **Logistic Regression classifier** with **TF-IDF vectorization** to identify threats in system logs. The project is designed with a simple **Flask web interface** for easy interaction and visualization.

## **Project Features**:
- **Network Traffic Anomaly Detection**: Detects anomalies in network traffic data using the **Isolation Forest** algorithm.
- **System Log Threat Classification**: Classifies log entries as normal or potential threats using **Logistic Regression** with **TF-IDF** vectorization.
- **Web Interface**: A user-friendly web interface that allows users to upload data files and perform analyses with a few clicks.
- **Pre-trained Models**: Includes pre-trained models for both **network traffic anomaly detection** and **log file classification**.

---

## **Project Structure**

```
AI-Cybersecurity-Threat-Detection/
│
├── app.py                          # Main Flask application
├── model.py                        # Machine learning models for anomaly detection and log classification
├── requirements.txt                # Python dependencies
├── README.md                       # Project documentation
├── static/
│   ├── style.css                   # Styling for the web interface
├── templates/
│   ├── index.html                  # Web interface
├── utils/
│   ├── data_loader.py              # Utility to load and preprocess network traffic data and system logs
├── data/
│   ├── network_traffic.csv         # Sample dataset for network traffic analysis
│   ├── system_logs.txt             # Sample log entries for threat detection
├── models/
│   ├── anomaly_detector.pkl        # Pre-trained Isolation Forest model for anomaly detection
│   ├── log_classifier.pkl          # Pre-trained Logistic Regression model for log file classification
```

### **Key Files Explained**:
- **`app.py`**: The main application file that runs the Flask server and handles the user interface for analyzing network traffic and system logs.
- **`model.py`**: Contains the code for anomaly detection and log classification models.
- **`requirements.txt`**: Specifies the dependencies required for the project, such as `Flask`, `pandas`, `scikit-learn`, and `transformers`.
- **`static/style.css`**: Basic CSS for styling the web interface.
- **`templates/index.html`**: The HTML file that provides the structure of the web interface for file upload and displaying results.
- **`utils/data_loader.py`**: Helper functions for loading and preprocessing network traffic data and log entries.
- **`data/network_traffic.csv`**: Sample network traffic data used for anomaly detection.
- **`data/system_logs.txt`**: Sample system logs used for detecting security threats.
- **`models/anomaly_detector.pkl`**: Pre-trained **Isolation Forest** model for detecting anomalies in network traffic data.
- **`models/log_classifier.pkl`**: Pre-trained **Logistic Regression** model with **TF-IDF** vectorization for classifying log file entries as normal or threats.

---

## **Data**

The project includes two sample data files:
1. **`network_traffic.csv`**:
   - A sample dataset containing network traffic records with columns like `source_ip`, `destination_ip`, `port`, `protocol`, `packet_size`, etc.
   - This data is used to detect anomalies in network traffic that might indicate security threats.

2. **`system_logs.txt`**:
   - A file containing sample system log entries, such as login attempts, error messages, and suspicious activity.
   - The log classifier analyzes these entries to detect potential security breaches or threats.

---

## **Models**

1. **`anomaly_detector.pkl`**:
   - This is a pre-trained **Isolation Forest** model used to identify unusual patterns in the network traffic dataset that may indicate anomalies or security breaches.
   - If the model file is not present, the system will train the model using the dataset provided in **`network_traffic.csv`**.

2. **`log_classifier.pkl`**:
   - A pre-trained **Logistic Regression** model with **TF-IDF vectorization** to classify system logs as normal or threats.
   - It analyzes textual log data and identifies potential security threats based on past patterns.
   - If the model file is not present, the system will train the model using predefined log samples.

---

## **Setup Instructions**

### **1. Clone the Repository:**
   ```bash
   git clone https://github.com/Shashwat1729/AI-Cybersecurity-Threat-Detection.git
   cd AI-Cybersecurity-Threat-Detection
   ```

### **2. Install Dependencies:**
   You can install the required Python libraries by running:
   ```bash
   pip install -r requirements.txt
   ```

### **3. Run the Flask Application:**
   After installing the dependencies, you can start the Flask server by running:
   ```bash
   python app.py
   ```

### **4. Open the Application:**
   Open your browser and go to:
   ```
   http://127.0.0.1:5000/
   ```

---

## **How to Use**

1. **Analyze Network Traffic:**
   - On the home page, click the **"Analyze Network Traffic"** button.
   - The system will process the **`network_traffic.csv`** file and display any detected anomalies in the traffic.
   - Anomalies indicate unusual behavior in the network that may require further investigation.

2. **Analyze System Logs:**
   - Click the **"Analyze System Logs"** button.
   - The system will analyze the **`system_logs.txt`** file and display any log entries that are classified as security threats.
   - Log entries indicating suspicious activities, failed logins, or unauthorized access attempts will be flagged.

---

## **Data Example**

- **`network_traffic.csv`**:
   ```csv
   timestamp,source_ip,destination_ip,port,protocol,packet_size,label
   2023-09-01 10:45:23,192.168.1.1,10.0.0.1,80,TCP,500,normal
   2023-09-01 10:46:10,10.0.0.5,192.168.1.1,443,TCP,450,suspicious
   ...
   ```

- **`system_logs.txt`**:
   ```txt
   Failed login attempt from IP 192.168.1.1
   User admin logged in successfully
   Error: Disk space low on /dev/sda1
   Suspicious activity detected from IP 10.0.0.5
   ...
   ```

---

## **Contributions**

Contributions are welcome! If you’d like to improve the models, enhance functionality, or add new features, feel free to fork the repository, make changes, and submit a pull request.

---

## **Future Enhancements**

- **Real-time Threat Detection**: Integrate real-time data streams for network traffic and logs to provide continuous monitoring and immediate threat detection.
- **Advanced Visualizations**: Add more advanced graphs and charts to visualize network traffic trends and log statistics.
- **Deep Learning Models**: Experiment with deep learning models like LSTMs or GRUs for log classification and time-series analysis of network traffic.

---

## **License**

This project is open-source and available under the **MIT License**. Feel free to use and modify it for your own purposes.

---
