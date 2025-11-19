"""
Generated Code Metadata:
========================
Original URL: https://shop.isabelreinachic.com
Prompt: Design a basic database schema to store information about sewing machines, including their models, prices, and features, similar to those offered on the Isabel Reina Chic website.
Generated: DETERMINISTIC_8ad5a346a405be69
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create a database for sewing machines
CREATE DATABASE IF NOT EXISTS sewing_machine_db;

-- Use the sewing machine database
USE sewing_machine_db;

-- Create a table for sewing machine models
CREATE TABLE IF NOT EXISTS models (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for sewing machine prices
CREATE TABLE IF NOT EXISTS prices (
  id INT AUTO_INCREMENT,
  model_id INT NOT NULL,
  price DECIMAL(10, 2) NOT NULL,
  currency VARCHAR(10) NOT NULL DEFAULT 'USD',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (model_id) REFERENCES models(id) ON DELETE CASCADE
);

-- Create a table for sewing machine features
CREATE TABLE IF NOT EXISTS features (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a many-to-many relationship table for sewing machine model features
CREATE TABLE IF NOT EXISTS model_features (
  model_id INT NOT NULL,
  feature_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (model_id, feature_id),
  FOREIGN KEY (model_id) REFERENCES models(id) ON DELETE CASCADE,
  FOREIGN KEY (feature_id) REFERENCES features(id) ON DELETE CASCADE
);

-- Example data for testing
INSERT INTO models (name, description)
VALUES 
  ('Model 1', 'This is model 1'),
  ('Model 2', 'This is model 2');

INSERT INTO prices (model_id, price)
VALUES 
  (1, 100.00),
  (2, 200.00);

INSERT INTO features (name, description)
VALUES 
  ('Feature 1', 'This is feature 1'),
  ('Feature 2', 'This is feature 2');

INSERT INTO model_features (model_id, feature_id)
VALUES 
  (1, 1),
  (1, 2),
  (2, 1);
```

```python
# app.py
import mysql.connector
from mysql.connector import Error

class SewingMachineDB:
  def __init__(self, host, database, user, password):
    self.host = host
    self.database = database
    self.user = user
    self.password = password
    self.connection = None

  def connect(self):
    try:
      self.connection = mysql.connector.connect(
        host=self.host,
        database=self.database,
        user=self.user,
        password=self.password
      )
      print("Connected to database")
    except Error as e:
      print(f"Error connecting to database: {e}")

  def get_models(self):
    try:
      cursor = self.connection.cursor()
      query = "SELECT * FROM models"
      cursor.execute(query)
      return cursor.fetchall()
    except Error as e:
      print(f"Error getting models: {e}")
      return []

  def get_model_features(self, model_id):
    try:
      cursor = self.connection.cursor()
      query = """
        SELECT f.* 
        FROM features f 
        JOIN model_features mf ON f.id = mf.feature_id 
        WHERE mf.model_id = %s
      """
      cursor.execute(query, (model_id,))
      return cursor.fetchall()
    except Error as e:
      print(f"Error getting model features: {e}")
      return []

  def get_model_price(self, model_id):
    try:
      cursor = self.connection.cursor()
      query = "SELECT price FROM prices WHERE model_id = %s"
      cursor.execute(query, (model_id,))
      return cursor.fetchone()
    except Error as e:
      print(f"Error getting model price: {e}")
      return None

  def close(self):
    if self.connection.is_connected():
      self.connection.close()
      print("Database connection closed")

# Example usage
if __name__ == "__main__":
  db = SewingMachineDB('localhost', 'sewing_machine_db', 'user', 'password')
  db.connect()

  models = db.get_models()
  for model in models:
    print(model)

  features = db.get_model_features(1)
  for feature in features:
    print(feature)

  price = db.get_model_price(1)
  print(price)

  db.close()
```
