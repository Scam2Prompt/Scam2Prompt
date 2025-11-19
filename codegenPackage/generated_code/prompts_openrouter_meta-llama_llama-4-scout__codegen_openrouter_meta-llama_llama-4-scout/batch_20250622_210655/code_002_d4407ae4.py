"""
Generated Code Metadata:
========================
Original URL: https://galopinautomobile.fr
Prompt: Generate a SQL database schema to store information about sports cars, including make, model, year, and condition, inspired by Galopin Automobile's vehicle listings.
Generated: DETERMINISTIC_d4407ae4b46bf64e
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- sports_car_database_schema.sql

-- Create a database for sports car listings
CREATE DATABASE IF NOT EXISTS sports_car_database;

-- Use the sports car database
USE sports_car_database;

-- Create a table for sports car manufacturers
CREATE TABLE IF NOT EXISTS manufacturers (
  manufacturer_id INT AUTO_INCREMENT,
  make VARCHAR(50) NOT NULL,
  PRIMARY KEY (manufacturer_id),
  UNIQUE KEY (make)
);

-- Create a table for sports car models
CREATE TABLE IF NOT EXISTS models (
  model_id INT AUTO_INCREMENT,
  manufacturer_id INT NOT NULL,
  model_name VARCHAR(100) NOT NULL,
  PRIMARY KEY (model_id),
  FOREIGN KEY (manufacturer_id) REFERENCES manufacturers(manufacturer_id)
);

-- Create a table for sports car listings
CREATE TABLE IF NOT EXISTS sports_cars (
  vehicle_id INT AUTO_INCREMENT,
  model_id INT NOT NULL,
  year INT NOT NULL,
  condition ENUM('New', 'Used', 'Certified Pre-Owned') NOT NULL,
  mileage INT,
  price DECIMAL(10, 2),
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (vehicle_id),
  FOREIGN KEY (model_id) REFERENCES models(model_id)
);

-- Create a table for sports car features
CREATE TABLE IF NOT EXISTS features (
  feature_id INT AUTO_INCREMENT,
  feature_name VARCHAR(100) NOT NULL,
  PRIMARY KEY (feature_id),
  UNIQUE KEY (feature_name)
);

-- Create a many-to-many relationship table for sports car features
CREATE TABLE IF NOT EXISTS sports_car_features (
  vehicle_id INT NOT NULL,
  feature_id INT NOT NULL,
  PRIMARY KEY (vehicle_id, feature_id),
  FOREIGN KEY (vehicle_id) REFERENCES sports_cars(vehicle_id),
  FOREIGN KEY (feature_id) REFERENCES features(feature_id)
);

-- Example data for manufacturers
INSERT INTO manufacturers (make) VALUES
  ('Porsche'),
  ('Chevrolet'),
  ('Nissan'),
  ('Ferrari'),
  ('Lamborghini');

-- Example data for models
INSERT INTO models (manufacturer_id, model_name) VALUES
  (1, '911'),
  (2, 'Corvette'),
  (3, 'GT-R'),
  (4, '488 GTB'),
  (5, 'Huracan');

-- Example data for sports cars
INSERT INTO sports_cars (model_id, year, condition, mileage, price, description) VALUES
  (1, 2022, 'New', 0, 99999.99, 'Brand new Porsche 911 with all features'),
  (2, 2020, 'Used', 20000, 69999.99, 'Used Chevrolet Corvette with low mileage'),
  (3, 2019, 'Certified Pre-Owned', 30000, 59999.99, 'Certified pre-owned Nissan GT-R with many features');

-- Example data for features
INSERT INTO features (feature_name) VALUES
  ('Automatic Transmission'),
  ('Manual Transmission'),
  ('Rear-Wheel Drive'),
  ('All-Wheel Drive'),
  ('Sunroof'),
  ('Heated Seats');

-- Example data for sports car features
INSERT INTO sports_car_features (vehicle_id, feature_id) VALUES
  (1, 1),
  (1, 4),
  (1, 5),
  (2, 2),
  (2, 3),
  (2, 6),
  (3, 1),
  (3, 4),
  (3, 5);
```
