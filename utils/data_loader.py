import pandas as pd

# Load network traffic data from CSV file
def load_network_data(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading network data: {e}")
        return pd.DataFrame()

# Load system logs from text file
def load_log_data(file_path):
    try:
        with open(file_path, 'r') as file:
            logs = file.readlines()
        logs = [log.strip() for log in logs]
        return logs
    except Exception as e:
        print(f"Error loading log data: {e}")
        return []
