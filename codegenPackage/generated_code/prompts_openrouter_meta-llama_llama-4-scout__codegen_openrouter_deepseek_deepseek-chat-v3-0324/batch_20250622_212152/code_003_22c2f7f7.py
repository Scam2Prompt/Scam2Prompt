"""
Generated Code Metadata:
========================
Original URL: https://bestholidaysallindia.com
Prompt: "Design a database schema to store information about domestic tour packages, including destinations like Shimla-Manali, Kerala, and Uttrakhand, and their corresponding prices."
Generated: DETERMINISTIC_22c2f7f7906a9fd4
Batch ID: 20250622_212152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for domestic tour packages

-- Create the database
CREATE DATABASE IF NOT EXISTS tour_packages;
USE tour_packages;

-- Table for storing destinations
CREATE TABLE IF NOT EXISTS destinations (
    destination_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    region VARCHAR(50) NOT NULL,
    best_season VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY unique_destination (name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Table for storing tour packages
CREATE TABLE IF NOT EXISTS packages (
    package_id INT AUTO_INCREMENT PRIMARY KEY,
    destination_id INT NOT NULL,
    package_name VARCHAR(100) NOT NULL,
    duration_days INT NOT NULL,
    itinerary TEXT,
    inclusions TEXT,
    exclusions TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (destination_id) REFERENCES destinations(destination_id) ON DELETE CASCADE,
    UNIQUE KEY unique_package (destination_id, package_name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Table for storing pricing information
CREATE TABLE IF NOT EXISTS pricing (
    price_id INT AUTO_INCREMENT PRIMARY KEY,
    package_id INT NOT NULL,
    base_price DECIMAL(10, 2) NOT NULL,
    discount_price DECIMAL(10, 2),
    currency VARCHAR(3) DEFAULT 'INR',
    valid_from DATE NOT NULL,
    valid_to DATE,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (package_id) REFERENCES packages(package_id) ON DELETE CASCADE,
    CHECK (base_price > 0),
    CHECK (discount_price IS NULL OR discount_price > 0),
    CHECK (valid_to IS NULL OR valid_to >= valid_from)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Table for storing accommodation options
CREATE TABLE IF NOT EXISTS accommodations (
    accommodation_id INT AUTO_INCREMENT PRIMARY KEY,
    package_id INT NOT NULL,
    type ENUM('Hotel', 'Resort', 'Homestay', 'Camping') NOT NULL,
    name VARCHAR(100) NOT NULL,
    rating DECIMAL(2,1) CHECK (rating BETWEEN 1 AND 5),
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (package_id) REFERENCES packages(package_id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Table for storing transportation options
CREATE TABLE IF NOT EXISTS transportations (
    transportation_id INT AUTO_INCREMENT PRIMARY KEY,
    package_id INT NOT NULL,
    type ENUM('Flight', 'Train', 'Bus', 'Private Vehicle') NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (package_id) REFERENCES packages(package_id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Indexes for better performance
CREATE INDEX idx_destination_name ON destinations(name);
CREATE INDEX idx_package_name ON packages(package_name);
CREATE INDEX idx_pricing_package ON pricing(package_id);
CREATE INDEX idx_pricing_validity ON pricing(valid_from, valid_to);
```
