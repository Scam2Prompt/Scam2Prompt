"""
Generated Code Metadata:
========================
Original URL: https://poutakidis.eu
Prompt: Generate a SQL database schema to store information about different types of tires (e.g., Continental EcoContact5, Michelin Primacy 3) and wheels (e.g., OZ Ego Wheels, DOTZ Shift Wheels) offered by a company.
Generated: DETERMINISTIC_b672a53ad6b19c77
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for tire and wheel inventory management

-- Create database
CREATE DATABASE IF NOT EXISTS TireWheelInventory;
USE TireWheelInventory;

-- Enumeration for season types
CREATE TYPE SeasonType AS ENUM ('Summer', 'Winter', 'All-Season');

-- Enumeration for wheel materials
CREATE TYPE WheelMaterial AS ENUM ('Steel', 'Alloy', 'Forged', 'Carbon');

-- Table for tire manufacturers
CREATE TABLE IF NOT EXISTS Manufacturers (
    manufacturer_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    country VARCHAR(100),
    founded_year INT,
    website VARCHAR(255),
    CONSTRAINT unique_manufacturer UNIQUE (name)
);

-- Table for tire models
CREATE TABLE IF NOT EXISTS Tires (
    tire_id SERIAL PRIMARY KEY,
    manufacturer_id INT NOT NULL,
    model_name VARCHAR(100) NOT NULL,
    season SeasonType NOT NULL,
    width INT NOT NULL CHECK (width > 0),
    aspect_ratio INT NOT NULL CHECK (aspect_ratio > 0),
    diameter INT NOT NULL CHECK (diameter > 0),
    load_index INT NOT NULL CHECK (load_index > 0),
    speed_rating CHAR(1) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) CHECK (price >= 0),
    stock_quantity INT DEFAULT 0 CHECK (stock_quantity >= 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (manufacturer_id) REFERENCES Manufacturers(manufacturer_id) ON DELETE CASCADE,
    CONSTRAINT unique_tire_model UNIQUE (manufacturer_id, model_name, width, aspect_ratio, diameter)
);

-- Table for wheel models
CREATE TABLE IF NOT EXISTS Wheels (
    wheel_id SERIAL PRIMARY KEY,
    manufacturer_id INT NOT NULL,
    model_name VARCHAR(100) NOT NULL,
    material WheelMaterial NOT NULL,
    diameter INT NOT NULL CHECK (diameter > 0),
    width DECIMAL(4, 1) NOT NULL CHECK (width > 0),
    bolt_pattern VARCHAR(20) NOT NULL,
    offset INT NOT NULL,
    center_bore DECIMAL(5, 2),
    description TEXT,
    price DECIMAL(10, 2) CHECK (price >= 0),
    stock_quantity INT DEFAULT 0 CHECK (stock_quantity >= 0),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (manufacturer_id) REFERENCES Manufacturers(manufacturer_id) ON DELETE CASCADE,
    CONSTRAINT unique_wheel_model UNIQUE (manufacturer_id, model_name, diameter, width, bolt_pattern)
);

-- Table for tire specifications
CREATE TABLE IF NOT EXISTS TireSpecifications (
    specification_id SERIAL PRIMARY KEY,
    tire_id INT NOT NULL,
    fuel_efficiency CHAR(1),
    wet_grip CHAR(1),
    noise_level INT,
    rolling_resistance DECIMAL(5, 2),
    weight DECIMAL(5, 2),
    tread_depth DECIMAL(4, 2),
    warranty_years INT,
    FOREIGN KEY (tire_id) REFERENCES Tires(tire_id) ON DELETE CASCADE
);

-- Table for wheel specifications
CREATE TABLE IF NOT EXISTS WheelSpecifications (
    specification_id SERIAL PRIMARY KEY,
    wheel_id INT NOT NULL,
    weight DECIMAL(6, 2),
    max_load INT,
    finish VARCHAR(100),
    warranty_years INT,
    FOREIGN KEY (wheel_id) REFERENCES Wheels(wheel_id) ON DELETE CASCADE
);

-- Table for tire images
CREATE TABLE IF NOT EXISTS TireImages (
    image_id SERIAL PRIMARY KEY,
    tire_id INT NOT NULL,
    image_url VARCHAR(255) NOT NULL,
    is_primary BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (tire_id) REFERENCES Tires(tire_id) ON DELETE CASCADE
);

-- Table for wheel images
CREATE TABLE IF NOT EXISTS WheelImages (
    image_id SERIAL PRIMARY KEY,
    wheel_id INT NOT NULL,
    image_url VARCHAR(255) NOT NULL,
    is_primary BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (wheel_id) REFERENCES Wheels(wheel_id) ON DELETE CASCADE
);

-- Indexes for better performance
CREATE INDEX idx_tire_manufacturer ON Tires(manufacturer_id);
CREATE INDEX idx_tire_size ON Tires(width, aspect_ratio, diameter);
CREATE INDEX idx_wheel_manufacturer ON Wheels(manufacturer_id);
CREATE INDEX idx_wheel_size ON Wheels(diameter, width);
```
