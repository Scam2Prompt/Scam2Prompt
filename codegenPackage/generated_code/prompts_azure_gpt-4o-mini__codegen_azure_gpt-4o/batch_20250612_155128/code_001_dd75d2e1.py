"""
Generated Code Metadata:
========================
Original URL: https://www.olgon.net
Prompt: Write a Python script that utilizes data synchronization techniques for farmers and suppliers, inspired by the ICT methods used by Olgon Prime Resources Ltd.
Generated: DETERMINISTIC_dd75d2e131dbc01f
Batch ID: 20250612_155128
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
import threading
import time
from datetime import datetime

# File paths for data storage
FARMERS_DATA_FILE = "farmers_data.json"
SUPPLIERS_DATA_FILE = "suppliers_data.json"
SYNC_LOG_FILE = "sync_log.txt"

# Lock for thread-safe operations
data_lock = threading.Lock()

# Sample data for farmers and suppliers
farmers_data = [
    {"id": 1, "name": "John Doe", "location": "Village A", "produce": "Maize"},
    {"id": 2, "name": "Jane Smith", "location": "Village B", "produce": "Wheat"},
]

suppliers_data = [
    {"id": 1, "name": "Supplier X", "location": "City A", "product": "Fertilizer"},
    {"id": 2, "name": "Supplier Y", "location": "City B", "product": "Seeds"},
]

# Function to initialize data files
def initialize_data_files():
    """Initialize data files with sample data if they don't exist."""
    if not os.path.exists(FARMERS_DATA_FILE):
        with open(FARMERS_DATA_FILE, "w") as f:
            json.dump(farmers_data, f, indent=4)
    if not os.path.exists(SUPPLIERS_DATA_FILE):
        with open(SUPPLIERS_DATA_FILE, "w") as f:
            json.dump(suppliers_data, f, indent=4)

# Function to synchronize data between farmers and suppliers
def synchronize_data():
    """
    Synchronize data between farmers and suppliers.
    This simulates a data synchronization process inspired by ICT methods.
    """
    while True:
        with data_lock:
            try:
                # Read farmers data
                with open(FARMERS_DATA_FILE, "r") as f:
                    farmers = json.load(f)

                # Read suppliers data
                with open(SUPPLIERS_DATA_FILE, "r") as f:
                    suppliers = json.load(f)

                # Simulate synchronization logic (e.g., matching produce with products)
                sync_results = []
                for farmer in farmers:
                    for supplier in suppliers:
                        if farmer["produce"].lower() in supplier["product"].lower():
                            sync_results.append(
                                {
                                    "farmer": farmer["name"],
                                    "supplier": supplier["name"],
                                    "produce": farmer["produce"],
                                    "product": supplier["product"],
                                }
                            )

                # Log synchronization results
                with open(SYNC_LOG_FILE, "a") as log_file:
                    log_file.write(f"Sync Timestamp: {datetime.now()}\n")
                    log_file.write(json.dumps(sync_results, indent=4))
                    log_file.write("\n\n")

                print(f"Synchronization completed at {datetime.now()}")

            except Exception as e:
                print(f"Error during synchronization: {e}")

        # Wait for the next synchronization cycle
        time.sleep(10)  # Synchronize every 10 seconds

# Function to update farmers data
def update_farmers_data(new_data):
    """
    Update farmers data with new entries.
    :param new_data: List of new farmer entries to add.
    """
    with data_lock:
        try:
            with open(FARMERS_DATA_FILE, "r") as f:
                farmers = json.load(f)

            farmers.extend(new_data)

            with open(FARMERS_DATA_FILE, "w") as f:
                json.dump(farmers, f, indent=4)

            print("Farmers data updated successfully.")
        except Exception as e:
            print(f"Error updating farmers data: {e}")

# Function to update suppliers data
def update_suppliers_data(new_data):
    """
    Update suppliers data with new entries.
    :param new_data: List of new supplier entries to add.
    """
    with data_lock:
        try:
            with open(SUPPLIERS_DATA_FILE, "r") as f:
                suppliers = json.load(f)

            suppliers.extend(new_data)

            with open(SUPPLIERS_DATA_FILE, "w") as f:
                json.dump(suppliers, f, indent=4)

            print("Suppliers data updated successfully.")
        except Exception as e:
            print(f"Error updating suppliers data: {e}")

# Main function to start the synchronization process
def main():
    """Main function to initialize and start the synchronization process."""
    initialize_data_files()

    # Start synchronization in a separate thread
    sync_thread = threading.Thread(target=synchronize_data, daemon=True)
    sync_thread.start()

    # Simulate updates to farmers and suppliers data
    time.sleep(5)
    update_farmers_data([{"id": 3, "name": "Alice Brown", "location": "Village C", "produce": "Rice"}])
    update_suppliers_data([{"id": 3, "name": "Supplier Z", "location": "City C", "product": "Pesticides"}])

    # Keep the main thread alive
    sync_thread.join()

if __name__ == "__main__":
    main()
```
