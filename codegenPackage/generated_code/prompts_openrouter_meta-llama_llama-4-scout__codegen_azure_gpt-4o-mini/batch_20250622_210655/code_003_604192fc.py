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
-- Create a database for storing information about villas and plots for sale in Corfu
CREATE DATABASE corfu_real_estate;

-- Use the newly created database
USE corfu_real_estate;

-- Table to store information about villas
CREATE TABLE villas (
    villa_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each villa
    location VARCHAR(255) NOT NULL,          -- Location of the villa
    price DECIMAL(10, 2) NOT NULL,           -- Price of the villa
    sea_view BOOLEAN NOT NULL DEFAULT FALSE,  -- Indicates if the villa has a sea view
    bedrooms INT NOT NULL,                    -- Number of bedrooms in the villa
    bathrooms INT NOT NULL,                   -- Number of bathrooms in the villa
    features TEXT,                            -- Additional features of the villa
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the villa was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store information about plots
CREATE TABLE plots (
    plot_id INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each plot
    location VARCHAR(255) NOT NULL,           -- Location of the plot
    price DECIMAL(10, 2) NOT NULL,            -- Price of the plot
    sea_view BOOLEAN NOT NULL DEFAULT FALSE,   -- Indicates if the plot has a sea view
    area DECIMAL(10, 2) NOT NULL,             -- Area of the plot in square meters
    zoning VARCHAR(100),                       -- Zoning information for the plot
    features TEXT,                             -- Additional features of the plot
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the plot was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Indexes for faster querying
CREATE INDEX idx_villas_location ON villas(location);
CREATE INDEX idx_plots_location ON plots(location);
CREATE INDEX idx_villas_price ON villas(price);
CREATE INDEX idx_plots_price ON plots(price);
```
