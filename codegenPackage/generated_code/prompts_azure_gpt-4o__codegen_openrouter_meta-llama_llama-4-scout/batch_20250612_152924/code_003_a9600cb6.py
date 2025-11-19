"""
Generated Code Metadata:
========================
Original URL: https://blueraygroup.com
Prompt: Create a database schema for managing logistics operations, including fields for sender and recipient details, shipment status, and delivery confirmation, inspired by Blue Ray Logistic's service workflow.
Generated: DETERMINISTIC_a9600cb675eb764e
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- logistics_schema.sql

-- Create database schema for logistics operations
CREATE DATABASE LogisticsDB;

-- Use the LogisticsDB database
USE LogisticsDB;

-- Create table for sender details
CREATE TABLE Senders (
  SenderID INT AUTO_INCREMENT,
  Name VARCHAR(255) NOT NULL,
  Address VARCHAR(255) NOT NULL,
  City VARCHAR(100) NOT NULL,
  State VARCHAR(100) NOT NULL,
  Country VARCHAR(100) NOT NULL,
  PostalCode VARCHAR(20) NOT NULL,
  Phone VARCHAR(20) NOT NULL,
  Email VARCHAR(100) NOT NULL,
  PRIMARY KEY (SenderID)
);

-- Create table for recipient details
CREATE TABLE Recipients (
  RecipientID INT AUTO_INCREMENT,
  Name VARCHAR(255) NOT NULL,
  Address VARCHAR(255) NOT NULL,
  City VARCHAR(100) NOT NULL,
  State VARCHAR(100) NOT NULL,
  Country VARCHAR(100) NOT NULL,
  PostalCode VARCHAR(20) NOT NULL,
  Phone VARCHAR(20) NOT NULL,
  Email VARCHAR(100) NOT NULL,
  PRIMARY KEY (RecipientID)
);

-- Create table for shipment status
CREATE TABLE ShipmentStatus (
  StatusID INT AUTO_INCREMENT,
  StatusName VARCHAR(100) NOT NULL,
  Description TEXT,
  PRIMARY KEY (StatusID)
);

-- Insert initial shipment statuses
INSERT INTO ShipmentStatus (StatusName, Description)
VALUES
  ('Pending', 'Shipment is pending processing'),
  ('In Transit', 'Shipment is in transit'),
  ('Delivered', 'Shipment has been delivered'),
  ('Failed Delivery', 'Shipment delivery failed');

-- Create table for shipments
CREATE TABLE Shipments (
  ShipmentID INT AUTO_INCREMENT,
  SenderID INT NOT NULL,
  RecipientID INT NOT NULL,
  ShipmentDate DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  ExpectedDeliveryDate DATE NOT NULL,
  ActualDeliveryDate DATE,
  StatusID INT NOT NULL DEFAULT 1,
  TrackingNumber VARCHAR(100),
  PRIMARY KEY (ShipmentID),
  FOREIGN KEY (SenderID) REFERENCES Senders(SenderID),
  FOREIGN KEY (RecipientID) REFERENCES Recipients(RecipientID),
  FOREIGN KEY (StatusID) REFERENCES ShipmentStatus(StatusID)
);

-- Create table for delivery confirmation
CREATE TABLE DeliveryConfirmations (
  ConfirmationID INT AUTO_INCREMENT,
  ShipmentID INT NOT NULL,
  ConfirmationDate DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  ConfirmedBy VARCHAR(100) NOT NULL,
  PRIMARY KEY (ConfirmationID),
  FOREIGN KEY (ShipmentID) REFERENCES Shipments(ShipmentID)
);

-- Create indexes for efficient querying
CREATE INDEX idx_Shipments_SenderID ON Shipments(SenderID);
CREATE INDEX idx_Shipments_RecipientID ON Shipments(RecipientID);
CREATE INDEX idx_Shipments_StatusID ON Shipments(StatusID);
CREATE INDEX idx_DeliveryConfirmations_ShipmentID ON DeliveryConfirmations(ShipmentID);
```

```python
# logistics_service.py

import mysql.connector
from mysql.connector import Error

class LogisticsService:
  def __init__(self, db_config):
    self.db_config = db_config
    self.connection = None

  def connect(self):
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

  def create_shipment(self, sender_id, recipient_id, expected_delivery_date):
    try:
      cursor = self.connection.cursor()
      query = "INSERT INTO Shipments (SenderID, RecipientID, ExpectedDeliveryDate) VALUES (%s, %s, %s)"
      cursor.execute(query, (sender_id, recipient_id, expected_delivery_date))
      self.connection.commit()
      return cursor.lastrowid
    except Error as e:
      print(f"Error creating shipment: {e}")
      return None

  def update_shipment_status(self, shipment_id, status_id):
    try:
      cursor = self.connection.cursor()
      query = "UPDATE Shipments SET StatusID = %s WHERE ShipmentID = %s"
      cursor.execute(query, (status_id, shipment_id))
      self.connection.commit()
    except Error as e:
      print(f"Error updating shipment status: {e}")

  def confirm_delivery(self, shipment_id, confirmed_by):
    try:
      cursor = self.connection.cursor()
      query = "INSERT INTO DeliveryConfirmations (ShipmentID, ConfirmedBy) VALUES (%s, %s)"
      cursor.execute(query, (shipment_id, confirmed_by))
      self.connection.commit()
    except Error as e:
      print(f"Error confirming delivery: {e}")

  def close(self):
    if self.connection:
      self.connection.close()
      print("Database connection closed")

# Example usage
db_config = {
  'host': 'localhost',
  'database': 'LogisticsDB',
  'user': 'your_username',
  'password': 'your_password'
}

logistics_service = LogisticsService(db_config)
logistics_service.connect()

shipment_id = logistics_service.create_shipment(1, 1, '2024-09-20')
logistics_service.update_shipment_status(shipment_id, 2)
logistics_service.confirm_delivery(shipment_id, 'John Doe')

logistics_service.close()
```
