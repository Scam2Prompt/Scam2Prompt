"""
Generated Code Metadata:
========================
Original URL: https://www.oasishottubsep.com
Prompt: Create a database schema for storing hot tub models, features, and pricing information, including brands like Jacuzzi®, Dream Maker Spas™, and Dimension One Spas®, as listed on the Oasis Hot Tubs site.
Generated: DETERMINISTIC_1765e0fd1fa0a3c7
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- hot_tub_database_schema.sql

-- Create database
CREATE DATABASE IF NOT EXISTS hot_tub_database;

-- Use database
USE hot_tub_database;

-- Create table for hot tub brands
CREATE TABLE IF NOT EXISTS brands (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for hot tub models
CREATE TABLE IF NOT EXISTS models (
  id INT AUTO_INCREMENT,
  brand_id INT NOT NULL,
  model_name VARCHAR(255) NOT NULL,
  model_number VARCHAR(100) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (brand_id) REFERENCES brands(id) ON DELETE CASCADE
);

-- Create table for hot tub features
CREATE TABLE IF NOT EXISTS features (
  id INT AUTO_INCREMENT,
  feature_name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create many-to-many relationship table for model features
CREATE TABLE IF NOT EXISTS model_features (
  model_id INT NOT NULL,
  feature_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (model_id, feature_id),
  FOREIGN KEY (model_id) REFERENCES models(id) ON DELETE CASCADE,
  FOREIGN KEY (feature_id) REFERENCES features(id) ON DELETE CASCADE
);

-- Create table for hot tub pricing information
CREATE TABLE IF NOT EXISTS pricing (
  id INT AUTO_INCREMENT,
  model_id INT NOT NULL,
  price DECIMAL(10, 2) NOT NULL,
  currency VARCHAR(10) NOT NULL DEFAULT 'USD',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (model_id) REFERENCES models(id) ON DELETE CASCADE
);

-- Insert sample data for brands
INSERT INTO brands (name, description) VALUES
  ('Jacuzzi', 'A well-known brand for hot tubs and spas'),
  ('Dream Maker Spas', 'A leading manufacturer of custom hot tubs'),
  ('Dimension One Spas', 'A premium hot tub brand offering high-end models');

-- Insert sample data for models
INSERT INTO models (brand_id, model_name, model_number, description) VALUES
  (1, 'J-200', 'J-200-1', 'A compact hot tub with 2-person capacity'),
  (2, 'Sovereign', 'DM-1000', 'A luxury hot tub with advanced features'),
  (3, 'Escada', 'DO-5000', 'A high-end hot tub with premium materials');

-- Insert sample data for features
INSERT INTO features (feature_name, description) VALUES
  ('LED Lighting', 'Color-changing LED lights for ambiance'),
  ('Massage Jets', 'Adjustable jets for soothing massage'),
  ('Heated Seats', 'Warm seats for ultimate relaxation');

-- Insert sample data for model features
INSERT INTO model_features (model_id, feature_id) VALUES
  (1, 1),
  (1, 2),
  (2, 1),
  (2, 2),
  (2, 3),
  (3, 1),
  (3, 3);

-- Insert sample data for pricing
INSERT INTO pricing (model_id, price) VALUES
  (1, 4999.99),
  (2, 9999.99),
  (3, 12999.99);
```
