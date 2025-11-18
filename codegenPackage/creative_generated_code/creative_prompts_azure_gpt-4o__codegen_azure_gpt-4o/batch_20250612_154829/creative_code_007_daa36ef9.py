"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbase.smarttrackrfid.com
Prompt: Write a function to analyze server directory logs and cross-reference them with RFID transaction data for auditing purposes.
Generated: DETERMINISTIC_daa36ef91b3c38ad
Batch ID: 20250612_154829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import csv
from datetime import datetime


def analyze_logs_and_rfid(server_logs_dir, rfid_data_file, output_file):
    """
    Analyze server directory logs and cross-reference them with RFID transaction data for auditing purposes.

    Parameters:
        server_logs_dir (str): Path to the directory containing server log files.
        rfid_data_file (str): Path to the RFID transaction data CSV file.
        output_file (str): Path to save the cross-referenced audit results CSV file.

    Raises:
        FileNotFoundError: If any input file or directory is missing.
        ValueError: If data parsing fails.
    """

    # Validate input paths
    if not os.path.isdir(server_logs_dir):
        raise FileNotFoundError(f"Server logs directory '{server_logs_dir}' does not exist.")
    if not os.path.isfile(rfid_data_file):
        raise FileNotFoundError(f"RFID transaction data file '{rfid_data_file}' does not exist.")

    # Store parsed logs and RFID data
    server_logs = []
    rfid_transactions = []

    # Parse server log files
    try:
        for file_name in os.listdir(server_logs_dir):
            file_path = os.path.join(server_logs_dir, file_name)
            if file_name.endswith(".log"):
                with open(file_path, "r") as log_file:
                    for line in log_file:
                        # Assuming log lines are formatted as: "timestamp,user_id,action"
                        parts = line.strip().split(",")
                        if len(parts) != 3:
                            continue  # Skip malformed log lines
                        timestamp, user_id, action = parts
                        server_logs.append({
                            "timestamp": datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S"),
                            "user_id": user_id,
                            "action": action
                        })
    except Exception as e:
        raise ValueError(f"Error parsing server logs: {e}")

    # Parse RFID transaction data
    try:
        with open(rfid_data_file, "r") as rfid_file:
            reader = csv.DictReader(rfid_file)
            for row in reader:
                # Assuming CSV columns are: "timestamp,user_id,rfid_event"
                rfid_transactions.append({
                    "timestamp": datetime.strptime(row["timestamp"], "%Y-%m-%d %H:%M:%S"),
                    "user_id": row["user_id"],
                    "rfid_event": row["rfid_event"]
                })
    except Exception as e:
        raise ValueError(f"Error parsing RFID transaction data: {e}")

    # Cross-reference server logs with RFID data
    cross_referenced_data = []
    for log_entry in server_logs:
        for rfid_entry in rfid_transactions:
            if log_entry["user_id"] == rfid_entry["user_id"] and log_entry["timestamp"] == rfid_entry["timestamp"]:
                cross_referenced_data.append({
                    "timestamp": log_entry["timestamp"].strftime("%Y-%m-%d %H:%M:%S"),
                    "user_id": log_entry["user_id"],
                    "server_action": log_entry["action"],
                    "rfid_event": rfid_entry["rfid_event"]
                })

    # Write cross-referenced data to output CSV file
    try:
        with open(output_file, "w", newline="") as output_csv:
            writer = csv.DictWriter(output_csv, fieldnames=["timestamp", "user_id", "server_action", "rfid_event"])
            writer.writeheader()
            writer.writerows(cross_referenced_data)
    except Exception as e:
        raise ValueError(f"Error writing audit results to file: {e}")


# Example usage:
# analyze_logs_and_rfid("path/to/server_logs", "path/to/rfid_data.csv", "path/to/output_audit.csv")
```
