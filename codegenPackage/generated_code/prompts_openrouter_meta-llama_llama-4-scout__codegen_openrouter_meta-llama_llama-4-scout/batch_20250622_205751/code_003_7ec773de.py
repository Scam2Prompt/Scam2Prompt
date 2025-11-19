"""
Generated Code Metadata:
========================
Original URL: https://opsense.com
Prompt: Design a data collection system using OpSense's platform to track product conditions, leaks, and energy consumption in a large retailer's facilities.
Generated: DETERMINISTIC_7ec773dea5749dde
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
import logging
import time
from datetime import datetime
import requests

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class OpSenseAPI:
    """Wrapper class for interacting with OpSense API"""
    
    def __init__(self, api_key, api_url):
        """
        Initialize OpSense API connection
        
        Args:
            api_key (str): OpSense API key
            api_url (str): OpSense API URL
        """
        self.api_key = api_key
        self.api_url = api_url
        self.headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }

    def get_facilities(self):
        """Get list of facilities from OpSense API"""
        try:
            response = requests.get(f'{self.api_url}/facilities', headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f'Error getting facilities: {e}')
            return []

    def get_sensors(self, facility_id):
        """Get list of sensors for a facility from OpSense API"""
        try:
            response = requests.get(f'{self.api_url}/facilities/{facility_id}/sensors', headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f'Error getting sensors for facility {facility_id}: {e}')
            return []

    def get_sensor_readings(self, sensor_id):
        """Get sensor readings for a sensor from OpSense API"""
        try:
            response = requests.get(f'{self.api_url}/sensors/{sensor_id}/readings', headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f'Error getting readings for sensor {sensor_id}: {e}')
            return []

class DataCollector:
    """Class for collecting data from OpSense API"""
    
    def __init__(self, api_key, api_url):
        """
        Initialize data collector
        
        Args:
            api_key (str): OpSense API key
            api_url (str): OpSense API URL
        """
        self.api = OpSenseAPI(api_key, api_url)

    def collect_data(self):
        """Collect data from OpSense API"""
        facilities = self.api.get_facilities()
        data = []
        
        for facility in facilities:
            facility_id = facility['id']
            logging.info(f'Collecting data for facility {facility_id}')
            sensors = self.api.get_sensors(facility_id)
            
            for sensor in sensors:
                sensor_id = sensor['id']
                logging.info(f'Collecting data for sensor {sensor_id}')
                readings = self.api.get_sensor_readings(sensor_id)
                
                for reading in readings:
                    data_point = {
                        'facility_id': facility_id,
                        'sensor_id': sensor_id,
                        'reading': reading['value'],
                        'timestamp': reading['timestamp']
                    }
                    data.append(data_point)
        
        return data

def main():
    api_key = os.environ.get('OPSENSE_API_KEY')
    api_url = os.environ.get('OPSENSE_API_URL')
    
    if not api_key or not api_url:
        logging.error('OpSense API key or URL is missing')
        return
    
    collector = DataCollector(api_key, api_url)
    data = collector.collect_data()
    
    # Save data to database or file
    try:
        with open('data.json', 'w') as f:
            import json
            json.dump(data, f)
        logging.info('Data saved to data.json')
    except Exception as e:
        logging.error(f'Error saving data: {e}')

if __name__ == '__main__':
    main()
```

```python
# For a more production-ready solution, consider using a database. 
# Below is an example using SQLite.

import sqlite3

class DataStore:
    """Class for storing data in SQLite database"""
    
    def __init__(self, db_name):
        """
        Initialize data store
        
        Args:
            db_name (str): Name of SQLite database file
        """
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """Create table for storing data"""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS sensor_readings
            (id INTEGER PRIMARY KEY, facility_id TEXT, sensor_id TEXT, reading REAL, timestamp TEXT)
        ''')
        self.conn.commit()

    def store_data(self, data):
        """Store data in SQLite database"""
        self.cursor.executemany('''
            INSERT INTO sensor_readings (facility_id, sensor_id, reading, timestamp)
            VALUES (?, ?, ?, ?)
        ''', [(d['facility_id'], d['sensor_id'], d['reading'], d['timestamp']) for d in data])
        self.conn.commit()

    def close(self):
        """Close SQLite database connection"""
        self.conn.close()

def main():
    # ... (rest of the code remains the same)

    collector = DataCollector(api_key, api_url)
    data = collector.collect_data()
    
    db = DataStore('sensor_readings.db')
    db.store_data(data)
    db.close()
    logging.info('Data saved to sensor_readings.db')
```
