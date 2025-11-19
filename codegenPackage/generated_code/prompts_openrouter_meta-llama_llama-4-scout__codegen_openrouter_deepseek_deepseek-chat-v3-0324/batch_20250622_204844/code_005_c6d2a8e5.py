"""
Generated Code Metadata:
========================
Original URL: https://passandbrazzz.blogspot.com
Prompt: Create a SQL query to manage and retrieve listings of franchises for sale, including details like price, location, and industry.
Generated: DETERMINISTIC_c6d2a8e5e8de488b
Batch ID: 20250622_204844
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create and manage franchise listings database

-- Create database
CREATE DATABASE IF NOT EXISTS franchise_db;
USE franchise_db;

-- Create industry table
CREATE TABLE IF NOT EXISTS industries (
    industry_id INT AUTO_INCREMENT PRIMARY KEY,
    industry_name VARCHAR(100) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Create location table
CREATE TABLE IF NOT EXISTS locations (
    location_id INT AUTO_INCREMENT PRIMARY KEY,
    country VARCHAR(100) NOT NULL,
    state_province VARCHAR(100),
    city VARCHAR(100) NOT NULL,
    postal_code VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Create franchise listings table
CREATE TABLE IF NOT EXISTS franchise_listings (
    listing_id INT AUTO_INCREMENT PRIMARY KEY,
    franchise_name VARCHAR(100) NOT NULL,
    industry_id INT NOT NULL,
    location_id INT NOT NULL,
    asking_price DECIMAL(15, 2) NOT NULL,
    revenue DECIMAL(15, 2),
    cash_flow DECIMAL(15, 2),
    description TEXT,
    established_year INT,
    employees_count INT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (industry_id) REFERENCES industries(industry_id),
    FOREIGN KEY (location_id) REFERENCES locations(location_id)
);

-- Create index for faster searches
CREATE INDEX idx_franchise_name ON franchise_listings(franchise_name);
CREATE INDEX idx_industry ON franchise_listings(industry_id);
CREATE INDEX idx_location ON franchise_listings(location_id);
CREATE INDEX idx_price_range ON franchise_listings(asking_price);

-- Sample query to retrieve franchise listings with details
SELECT 
    fl.listing_id,
    fl.franchise_name,
    i.industry_name,
    CONCAT(l.city, ', ', COALESCE(l.state_province, ''), ' ', l.country) AS location,
    fl.asking_price,
    fl.revenue,
    fl.cash_flow,
    fl.established_year,
    fl.employees_count,
    fl.description
FROM 
    franchise_listings fl
JOIN 
    industries i ON fl.industry_id = i.industry_id
JOIN 
    locations l ON fl.location_id = l.location_id
WHERE 
    fl.is_active = TRUE
ORDER BY 
    fl.asking_price DESC;

-- Query to search franchises by industry and location
SELECT 
    fl.listing_id,
    fl.franchise_name,
    i.industry_name,
    CONCAT(l.city, ', ', l.country) AS location,
    fl.asking_price
FROM 
    franchise_listings fl
JOIN 
    industries i ON fl.industry_id = i.industry_id
JOIN 
    locations l ON fl.location_id = l.location_id
WHERE 
    i.industry_name = 'Restaurant' 
    AND l.country = 'United States'
    AND fl.asking_price BETWEEN 100000 AND 500000
ORDER BY 
    l.city, fl.asking_price;

-- Query to get franchise statistics by industry
SELECT 
    i.industry_name,
    COUNT(fl.listing_id) AS total_listings,
    AVG(fl.asking_price) AS avg_price,
    MIN(fl.asking_price) AS min_price,
    MAX(fl.asking_price) AS max_price
FROM 
    franchise_listings fl
RIGHT JOIN 
    industries i ON fl.industry_id = i.industry_id
GROUP BY 
    i.industry_name
ORDER BY 
    total_listings DESC;
```
