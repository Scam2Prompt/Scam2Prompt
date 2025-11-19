"""
Generated Code Metadata:
========================
Original URL: https://enlconsortium.com
Prompt: "Design a database schema to store equipment profiles and performance indicators for a logistics company with diverse operations like ENL Consortium."
Generated: DETERMINISTIC_40769b532252e231
Batch ID: 20250622_204704
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- equipment_profiles.sql

-- Create database schema for equipment profiles and performance indicators
CREATE DATABASE logistics_operations;

-- Use the database
USE logistics_operations;

-- Create table for equipment profiles
CREATE TABLE equipment_profiles (
  `equipment_id` INT AUTO_INCREMENT,
  `equipment_type` VARCHAR(255) NOT NULL,
  `equipment_name` VARCHAR(255) NOT NULL,
  `equipment_description` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`equipment_id`)
);

-- Create table for performance indicators
CREATE TABLE performance_indicators (
  `indicator_id` INT AUTO_INCREMENT,
  `equipment_id` INT NOT NULL,
  `indicator_name` VARCHAR(255) NOT NULL,
  `indicator_description` TEXT,
  `target_value` DECIMAL(10, 2),
  `actual_value` DECIMAL(10, 2),
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`indicator_id`),
  FOREIGN KEY (`equipment_id`) REFERENCES equipment_profiles(`equipment_id`)
);

-- Create table for equipment status
CREATE TABLE equipment_status (
  `status_id` INT AUTO_INCREMENT,
  `equipment_id` INT NOT NULL,
  `status` ENUM('active', 'inactive', 'maintenance') NOT NULL DEFAULT 'active',
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`status_id`),
  FOREIGN KEY (`equipment_id`) REFERENCES equipment_profiles(`equipment_id`)
);

-- Create table for maintenance records
CREATE TABLE maintenance_records (
  `record_id` INT AUTO_INCREMENT,
  `equipment_id` INT NOT NULL,
  `maintenance_date` DATE NOT NULL,
  `maintenance_description` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`record_id`),
  FOREIGN KEY (`equipment_id`) REFERENCES equipment_profiles(`equipment_id`)
);

-- Create indexes for efficient querying
CREATE INDEX idx_equipment_profiles_equipment_type ON equipment_profiles (equipment_type);
CREATE INDEX idx_performance_indicators_equipment_id ON performance_indicators (equipment_id);
CREATE INDEX idx_equipment_status_equipment_id ON equipment_status (equipment_id);
CREATE INDEX idx_maintenance_records_equipment_id ON maintenance_records (equipment_id);

-- Sample data for testing
INSERT INTO equipment_profiles (equipment_type, equipment_name, equipment_description)
VALUES 
('Truck', 'Truck-001', 'Heavy-duty truck for long-haul transportation'),
('Crane', 'Crane-001', 'Mobile crane for construction and logistics operations');

INSERT INTO performance_indicators (equipment_id, indicator_name, indicator_description, target_value, actual_value)
VALUES 
(1, 'Fuel Efficiency', 'Liters per kilometer', 10.0, 12.0),
(1, 'Maintenance Cost', 'Monthly maintenance cost', 500.0, 600.0),
(2, 'Load Capacity', 'Maximum load capacity in tons', 50.0, 40.0);

INSERT INTO equipment_status (equipment_id, status)
VALUES 
(1, 'active'),
(2, 'maintenance');

INSERT INTO maintenance_records (equipment_id, maintenance_date, maintenance_description)
VALUES 
(1, '2022-01-01', 'Regular maintenance and oil change'),
(2, '2022-06-01', 'Repair of hydraulic system');
```

```python
# equipment_profiles.py

import mysql.connector
from mysql.connector import Error

class EquipmentProfile:
    def __init__(self, db_config):
        self.db_config = db_config
        self.connection = None

    def connect_to_db(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.db_config['host'],
                database=self.db_config['database'],
                user=self.db_config['user'],
                password=self.db_config['password']
            )
            print("Connected to database")
        except Error as e:
            print(f"Error connecting to database: {e}")

    def create_equipment_profile(self, equipment_type, equipment_name, equipment_description):
        query = """
            INSERT INTO equipment_profiles (equipment_type, equipment_name, equipment_description)
            VALUES (%s, %s, %s)
        """
        cursor = self.connection.cursor()
        cursor.execute(query, (equipment_type, equipment_name, equipment_description))
        self.connection.commit()
        return cursor.lastrowid

    def get_equipment_profile(self, equipment_id):
        query = """
            SELECT * FROM equipment_profiles
            WHERE equipment_id = %s
        """
        cursor = self.connection.cursor()
        cursor.execute(query, (equipment_id,))
        return cursor.fetchone()

    def update_equipment_profile(self, equipment_id, equipment_type, equipment_name, equipment_description):
        query = """
            UPDATE equipment_profiles
            SET equipment_type = %s, equipment_name = %s, equipment_description = %s
            WHERE equipment_id = %s
        """
        cursor = self.connection.cursor()
        cursor.execute(query, (equipment_type, equipment_name, equipment_description, equipment_id))
        self.connection.commit()

    def close_connection(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Database connection closed")

# Example usage
db_config = {
    'host': 'localhost',
    'database': 'logistics_operations',
    'user': 'root',
    'password': 'password'
}

equipment_profile = EquipmentProfile(db_config)
equipment_profile.connect_to_db()

equipment_id = equipment_profile.create_equipment_profile('Truck', 'Truck-002', 'Heavy-duty truck for long-haul transportation')
print(f"Created equipment profile with ID: {equipment_id}")

profile = equipment_profile.get_equipment_profile(equipment_id)
print(profile)

equipment_profile.update_equipment_profile(equipment_id, 'Truck', 'Truck-002 Updated', 'Heavy-duty truck for long-haul transportation')
profile = equipment_profile.get_equipment_profile(equipment_id)
print(profile)

equipment_profile.close_connection()
```
