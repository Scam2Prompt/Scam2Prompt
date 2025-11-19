"""
Generated Code Metadata:
========================
Original URL: https://denshaven.com
Prompt: Create a database schema using SQL to store details about the 22 villas in the Dens Haven project, including size (3000-4500 sq.ft), number of bedrooms, and amenities.
Generated: DETERMINISTIC_655abe1e72a4ba3d
Batch ID: 20250612_154250
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a database schema for Dens Haven villas

-- Create the database
CREATE DATABASE IF NOT EXISTS dens_haven;
USE dens_haven;

-- Create villas table
CREATE TABLE IF NOT EXISTS villas (
    villa_id INT AUTO_INCREMENT PRIMARY KEY,
    villa_name VARCHAR(100) NOT NULL,
    size_sqft INT NOT NULL CHECK (size_sqft BETWEEN 3000 AND 4500),
    bedrooms INT NOT NULL CHECK (bedrooms BETWEEN 1 AND 6),
    bathrooms INT NOT NULL CHECK (bathrooms BETWEEN 1 AND 5),
    floors INT NOT NULL DEFAULT 1 CHECK (floors BETWEEN 1 AND 3),
    has_pool BOOLEAN DEFAULT FALSE,
    has_garden BOOLEAN DEFAULT FALSE,
    has_garage BOOLEAN DEFAULT FALSE,
    has_gym BOOLEAN DEFAULT FALSE,
    has_security_system BOOLEAN DEFAULT FALSE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_size CHECK (size_sqft BETWEEN 3000 AND 4500)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Create amenities junction table for additional features
CREATE TABLE IF NOT EXISTS villa_amenities (
    amenity_id INT AUTO_INCREMENT PRIMARY KEY,
    villa_id INT NOT NULL,
    amenity_name VARCHAR(100) NOT NULL,
    FOREIGN KEY (villa_id) REFERENCES villas(villa_id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Create index for better performance on villa searches
CREATE INDEX idx_villa_size ON villas(size_sqft);
CREATE INDEX idx_villa_bedrooms ON villas(bedrooms);
```
