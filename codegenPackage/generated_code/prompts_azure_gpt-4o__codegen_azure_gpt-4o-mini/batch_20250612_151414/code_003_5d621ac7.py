"""
Generated Code Metadata:
========================
Original URL: https://esp-gala-games-app.blogspot.com
Prompt: Create a database schema for an online store selling sports items, including tables for "Medalhas," "Slackline," and "Chuteira."
Generated: DETERMINISTIC_5d621ac760ee49fb
Batch ID: 20250612_151414
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an online store selling sports items

-- Create the database
CREATE DATABASE SportsStore;

-- Use the created database
USE SportsStore;

-- Table for Medalhas (Medals)
CREATE TABLE Medalhas (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each medal
    name VARCHAR(100) NOT NULL,         -- Name of the medal
    material VARCHAR(50) NOT NULL,      -- Material of the medal
    weight DECIMAL(5,2) NOT NULL,       -- Weight of the medal in grams
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table for Slackline
CREATE TABLE Slackline (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each slackline
    length DECIMAL(5,2) NOT NULL,      -- Length of the slackline in meters
    width DECIMAL(5,2) NOT NULL,       -- Width of the slackline in centimeters
    material VARCHAR(50) NOT NULL,      -- Material of the slackline
    max_weight DECIMAL(7,2) NOT NULL,  -- Maximum weight capacity in kilograms
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table for Chuteira (Soccer Shoes)
CREATE TABLE Chuteira (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each shoe
    brand VARCHAR(50) NOT NULL,        -- Brand of the shoe
    size DECIMAL(3,1) NOT NULL,        -- Size of the shoe
    color VARCHAR(30) NOT NULL,        -- Color of the shoe
    price DECIMAL(10,2) NOT NULL,      -- Price of the shoe
    stock INT NOT NULL DEFAULT 0,      -- Stock quantity available
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Optional: Create indexes for better performance
CREATE INDEX idx_medalhas_name ON Medalhas(name);
CREATE INDEX idx_slackline_length ON Slackline(length);
CREATE INDEX idx_chuteira_brand ON Chuteira(brand);
```
