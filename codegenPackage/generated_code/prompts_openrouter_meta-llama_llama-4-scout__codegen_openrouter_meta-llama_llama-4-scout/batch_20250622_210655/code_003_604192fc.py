"""
Generated Code Metadata:
========================
Original URL: https://corfucoastalcollection.com
Prompt: Create a SQL database schema to store information about villas and plots for sale in Corfu, including fields for location, price, and features like sea view.
Generated: DETERMINISTIC_604192fcac96a24d
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

-- Create a database for Corfu properties
CREATE DATABASE corfu_properties;

-- Use the corfu_properties database
USE corfu_properties;

-- Create a table for locations
CREATE TABLE locations (
  location_id INT AUTO_INCREMENT,
  address VARCHAR(255) NOT NULL,
  city VARCHAR(100) NOT NULL,
  region VARCHAR(100) NOT NULL,
  postal_code VARCHAR(20),
  latitude DECIMAL(10, 8),
  longitude DECIMAL(11, 8),
  PRIMARY KEY (location_id)
);

-- Create a table for villa features
CREATE TABLE villa_features (
  feature_id INT AUTO_INCREMENT,
  name VARCHAR(100) NOT NULL,
  description TEXT,
  PRIMARY KEY (feature_id)
);

-- Create a many-to-many relationship table for villa features
CREATE TABLE villa_feature_relationships (
  villa_id INT,
  feature_id INT,
  PRIMARY KEY (villa_id, feature_id),
  FOREIGN KEY (villa_id) REFERENCES villas(villa_id),
  FOREIGN KEY (feature_id) REFERENCES villa_features(feature_id)
);

-- Create a table for villas
CREATE TABLE villas (
  villa_id INT AUTO_INCREMENT,
  location_id INT,
  price DECIMAL(15, 2) NOT NULL,
  sea_view BOOLEAN,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (villa_id),
  FOREIGN KEY (location_id) REFERENCES locations(location_id)
);

-- Create a table for plot features
CREATE TABLE plot_features (
  feature_id INT AUTO_INCREMENT,
  name VARCHAR(100) NOT NULL,
  description TEXT,
  PRIMARY KEY (feature_id)
);

-- Create a many-to-many relationship table for plot features
CREATE TABLE plot_feature_relationships (
  plot_id INT,
  feature_id INT,
  PRIMARY KEY (plot_id, feature_id),
  FOREIGN KEY (plot_id) REFERENCES plots(plot_id),
  FOREIGN KEY (feature_id) REFERENCES plot_features(feature_id)
);

-- Create a table for plots
CREATE TABLE plots (
  plot_id INT AUTO_INCREMENT,
  location_id INT,
  price DECIMAL(15, 2) NOT NULL,
  area DECIMAL(10, 2) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (plot_id),
  FOREIGN KEY (location_id) REFERENCES locations(location_id)
);

-- Example insert statements
INSERT INTO locations (address, city, region, postal_code, latitude, longitude)
VALUES ('Example Address', 'Corfu City', 'Corfu', '49100', 39.600971, 19.934877);

INSERT INTO villa_features (name, description)
VALUES ('Pool', 'Private swimming pool');

INSERT INTO villas (location_id, price, sea_view, description)
VALUES (1, 500000.00, TRUE, 'Luxury villa with sea view');

INSERT INTO villa_feature_relationships (villa_id, feature_id)
VALUES (1, 1);

INSERT INTO plot_features (name, description)
VALUES ('Fenced', 'Fully fenced plot');

INSERT INTO plots (location_id, price, area, description)
VALUES (1, 200000.00, 1000.00, 'Building plot with sea view');

INSERT INTO plot_feature_relationships (plot_id, feature_id)
VALUES (1, 1);
```
