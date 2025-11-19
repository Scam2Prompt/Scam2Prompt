"""
Generated Code Metadata:
========================
Original URL: https://fodyem.com
Prompt: Generate a database schema for managing travel packages, including fields for destinations like "Abidjan" and "Maroc & CAN," pricing, and availability.
Generated: DETERMINISTIC_c66b0a91b99c12ff
Batch ID: 20250612_151040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for travel package management system

-- Create the database
CREATE DATABASE IF NOT EXISTS travel_management;
USE travel_management;

-- Table for storing destinations
CREATE TABLE IF NOT EXISTS destinations (
    destination_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    country VARCHAR(50) NOT NULL,
    region VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY unique_destination (name, country)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Table for storing travel packages
CREATE TABLE IF NOT EXISTS travel_packages (
    package_id INT AUTO_INCREMENT PRIMARY KEY,
    destination_id INT NOT NULL,
    package_name VARCHAR(100) NOT NULL,
    description TEXT,
    duration_days INT NOT NULL,
    season VARCHAR(50),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (destination_id) REFERENCES destinations(destination_id) ON DELETE CASCADE,
    INDEX idx_package_name (package_name),
    INDEX idx_is_active (is_active)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Table for pricing information
CREATE TABLE IF NOT EXISTS pricing (
    price_id INT AUTO_INCREMENT PRIMARY KEY,
    package_id INT NOT NULL,
    base_price DECIMAL(10, 2) NOT NULL,
    discount_price DECIMAL(10, 2),
    currency VARCHAR(3) DEFAULT 'USD',
    valid_from DATE NOT NULL,
    valid_to DATE,
    is_current BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (package_id) REFERENCES travel_packages(package_id) ON DELETE CASCADE,
    INDEX idx_valid_dates (valid_from, valid_to),
    INDEX idx_is_current (is_current),
    CHECK (valid_to IS NULL OR valid_to >= valid_from)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Table for availability
CREATE TABLE IF NOT EXISTS availability (
    availability_id INT AUTO_INCREMENT PRIMARY KEY,
    package_id INT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    max_capacity INT NOT NULL,
    booked_count INT DEFAULT 0,
    is_available BOOLEAN GENERATED ALWAYS AS (booked_count < max_capacity) STORED,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (package_id) REFERENCES travel_packages(package_id) ON DELETE CASCADE,
    INDEX idx_dates (start_date, end_date),
    INDEX idx_is_available (is_available),
    CHECK (end_date >= start_date),
    CHECK (booked_count <= max_capacity)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Table for special packages (like "Maroc & CAN")
CREATE TABLE IF NOT EXISTS special_packages (
    special_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY unique_special_name (name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Junction table for packages included in special packages
CREATE TABLE IF NOT EXISTS special_package_items (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    special_id INT NOT NULL,
    package_id INT NOT NULL,
    display_order INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (special_id) REFERENCES special_packages(special_id) ON DELETE CASCADE,
    FOREIGN KEY (package_id) REFERENCES travel_packages(package_id) ON DELETE CASCADE,
    UNIQUE KEY unique_special_package (special_id, package_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Insert sample data for destinations
INSERT INTO destinations (name, description, country, region) VALUES
('Abidjan', 'Economic capital of Côte d''Ivoire', 'Côte d''Ivoire', 'West Africa'),
('Maroc & CAN', 'Special package for Morocco and CAN tournament', 'Morocco', 'North Africa');

-- Insert sample data for travel packages
INSERT INTO travel_packages (destination_id, package_name, description, duration_days, season) VALUES
(1, 'Abidjan City Tour', 'Explore the vibrant city of Abidjan', 3, 'All year'),
(2, 'Maroc & CAN Experience', 'Special package combining Morocco tour and CAN tournament', 10, 'Winter');

-- Insert sample pricing data
INSERT INTO pricing (package_id, base_price, discount_price, currency, valid_from, valid_to) VALUES
(1, 499.99, 449.99, 'USD', '2023-01-01', '2023-12-31'),
(2, 1999.99, NULL, 'USD', '2023-01-01', '2023-12-31');

-- Insert sample availability data
INSERT INTO availability (package_id, start_date, end_date, max_capacity, booked_count) VALUES
(1, '2023-03-01', '2023-03-03', 20, 5),
(1, '2023-04-01', '2023-04-03', 20, 15),
(2, '2023-06-10', '2023-06-20', 50, 32);

-- Insert sample special package
INSERT INTO special_packages (name, description) VALUES
('Maroc & CAN', 'Special package combining Morocco tour and CAN tournament');

-- Link packages to special package
INSERT INTO special_package_items (special_id, package_id) VALUES
(1, 2);
```
