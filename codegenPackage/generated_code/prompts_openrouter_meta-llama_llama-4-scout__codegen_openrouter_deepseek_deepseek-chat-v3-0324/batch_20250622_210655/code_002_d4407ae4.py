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
-- SQL Schema for Sports Car Database (Inspired by Galopin Automobile)

-- Create database
CREATE DATABASE IF NOT EXISTS galopin_automobile;
USE galopin_automobile;

-- Manufacturers table
CREATE TABLE IF NOT EXISTS manufacturers (
    manufacturer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    country VARCHAR(50),
    founded_year INT,
    website VARCHAR(255),
    UNIQUE KEY (name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Models table
CREATE TABLE IF NOT EXISTS models (
    model_id INT AUTO_INCREMENT PRIMARY KEY,
    manufacturer_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    production_start_year INT NOT NULL,
    production_end_year INT,
    body_style VARCHAR(50),
    engine_type VARCHAR(50),
    FOREIGN KEY (manufacturer_id) REFERENCES manufacturers(manufacturer_id) ON DELETE CASCADE,
    UNIQUE KEY (manufacturer_id, name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Vehicles table
CREATE TABLE IF NOT EXISTS vehicles (
    vehicle_id INT AUTO_INCREMENT PRIMARY KEY,
    model_id INT NOT NULL,
    year INT NOT NULL,
    vin VARCHAR(17) UNIQUE,
    mileage INT,
    color VARCHAR(50),
    transmission_type ENUM('Manual', 'Automatic', 'Semi-Automatic', 'Other') NOT NULL,
    drivetrain ENUM('RWD', 'FWD', 'AWD', '4WD') NOT NULL,
    condition ENUM('New', 'Used', 'Certified Pre-Owned', 'Restored') NOT NULL,
    price DECIMAL(12, 2),
    description TEXT,
    date_added DATETIME DEFAULT CURRENT_TIMESTAMP,
    last_updated DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (model_id) REFERENCES models(model_id) ON DELETE CASCADE,
    CHECK (year >= 1900 AND year <= YEAR(CURRENT_DATE) + 1),
    CHECK (mileage >= 0)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Features table
CREATE TABLE IF NOT EXISTS features (
    feature_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    category VARCHAR(50),
    UNIQUE KEY (name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Vehicle features junction table
CREATE TABLE IF NOT EXISTS vehicle_features (
    vehicle_id INT NOT NULL,
    feature_id INT NOT NULL,
    PRIMARY KEY (vehicle_id, feature_id),
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id) ON DELETE CASCADE,
    FOREIGN KEY (feature_id) REFERENCES features(feature_id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Images table
CREATE TABLE IF NOT EXISTS images (
    image_id INT AUTO_INCREMENT PRIMARY KEY,
    vehicle_id INT NOT NULL,
    url VARCHAR(255) NOT NULL,
    is_primary BOOLEAN DEFAULT FALSE,
    caption VARCHAR(255),
    upload_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Performance specs table
CREATE TABLE IF NOT EXISTS performance_specs (
    spec_id INT AUTO_INCREMENT PRIMARY KEY,
    model_id INT NOT NULL,
    horsepower INT,
    torque INT,
    top_speed INT,
    acceleration_0_to_60 DECIMAL(4, 2),
    fuel_efficiency_city DECIMAL(4, 1),
    fuel_efficiency_highway DECIMAL(4, 1),
    FOREIGN KEY (model_id) REFERENCES models(model_id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Create indexes for performance optimization
CREATE INDEX idx_vehicle_year ON vehicles(year);
CREATE INDEX idx_vehicle_price ON vehicles(price);
CREATE INDEX idx_vehicle_condition ON vehicles(condition);
CREATE INDEX idx_model_name ON models(name);
```
