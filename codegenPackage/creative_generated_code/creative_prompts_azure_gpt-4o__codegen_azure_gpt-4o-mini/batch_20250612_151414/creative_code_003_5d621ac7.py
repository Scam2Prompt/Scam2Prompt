"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://esp-gala-games-app.blogspot.com
Prompt: Create a database schema for an online store selling sports items, including tables for "Medalhas," "Slackline," and "Chuteira."
Generated: DETERMINISTIC_5d621ac760ee49fb
Batch ID: 20250612_151414
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for an online store selling sports items

CREATE DATABASE SportsStore;

USE SportsStore;

-- Table for storing information about medals
CREATE TABLE Medalhas (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each medal
    name VARCHAR(100) NOT NULL,         -- Name of the medal
    material VARCHAR(50),                -- Material of the medal (e.g., gold, silver, bronze)
    weight DECIMAL(5, 2),                -- Weight of the medal in grams
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the medal was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the medal was last updated
);

-- Table for storing information about slacklines
CREATE TABLE Slackline (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each slackline
    brand VARCHAR(100) NOT NULL,       -- Brand of the slackline
    length DECIMAL(5, 2) NOT NULL,     -- Length of the slackline in meters
    width DECIMAL(5, 2) NOT NULL,      -- Width of the slackline in centimeters
    max_weight_capacity DECIMAL(10, 2), -- Maximum weight capacity in kilograms
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the slackline was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the slackline was last updated
);

-- Table for storing information about soccer shoes (chuteira)
CREATE TABLE Chuteira (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each pair of shoes
    brand VARCHAR(100) NOT NULL,        -- Brand of the shoes
    size DECIMAL(4, 1) NOT NULL,        -- Size of the shoes (e.g., 40.5)
    color VARCHAR(50),                   -- Color of the shoes
    type VARCHAR(50),                    -- Type of shoes (e.g., indoor, outdoor)
    price DECIMAL(10, 2) NOT NULL,      -- Price of the shoes
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the shoes were added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the shoes were last updated
);

-- Optional: Creating indexes for better performance (if needed later)
CREATE INDEX idx_medalhas_name ON Medalhas(name);
CREATE INDEX idx_slackline_brand ON Slackline(brand);
CREATE INDEX idx_chuteira_brand ON Chuteira(brand);
```
