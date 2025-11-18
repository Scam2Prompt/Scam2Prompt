"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mesogia.com
Prompt: Create a SQL database schema for storing directory listings with fields for name, category, address, coordinates, and contact information, as seen on "https://mesogia.com."
Generated: DETERMINISTIC_f49e2ce8a1043695
Batch ID: 20250612_151044
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL script to create a database schema for storing directory listings

-- Create the database
CREATE DATABASE DirectoryListings;

-- Use the created database
USE DirectoryListings;

-- Create a table to store directory listings
CREATE TABLE Listings (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each listing
    name VARCHAR(255) NOT NULL, -- Name of the listing, cannot be null
    category VARCHAR(100) NOT NULL, -- Category of the listing, cannot be null
    address VARCHAR(255) NOT NULL, -- Address of the listing, cannot be null
    latitude DECIMAL(9, 6) NOT NULL, -- Latitude coordinate of the listing, cannot be null
    longitude DECIMAL(9, 6) NOT NULL, -- Longitude coordinate of the listing, cannot be null
    contact_info VARCHAR(255), -- Contact information for the listing (optional)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the listing was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- INDEX for efficient querying by category
CREATE INDEX idx_category ON Listings (category);

-- Sample data insertion (for demonstration purposes)
INSERT INTO Listings (name, category, address, latitude, longitude, contact_info)
VALUES
    ('Sample Business', 'Restaurant', '123 Sample St, Sample City, ST 12345', 35.123456, 25.123456, '555-1234');

-- Error handling in MySQL is typically done via TRY/CATCH in stored procedures or by checking error codes in applications.
-- Ensure to implement necessary application-level error handling when interacting with the database.
```
