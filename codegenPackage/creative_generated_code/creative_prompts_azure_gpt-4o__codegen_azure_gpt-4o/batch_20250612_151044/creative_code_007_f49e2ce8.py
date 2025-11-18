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
-- SQL Schema for storing directory listings

-- Create the table to store directory listings
CREATE TABLE DirectoryListings (
    ListingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each listing
    Name VARCHAR(255) NOT NULL,               -- Name of the directory listing
    Category VARCHAR(100),                    -- Category of the listing (e.g., Restaurant, Shop)
    Address TEXT,                             -- Address of the listing
    Latitude DECIMAL(9, 6),                   -- Latitude for coordinates
    Longitude DECIMAL(9, 6),                  -- Longitude for coordinates
    ContactInfo TEXT,                         -- Contact information (phone, email, etc.)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the listing is created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create an index on Category for faster lookups
CREATE INDEX idx_category ON DirectoryListings (Category);

-- Create an index on Latitude and Longitude for spatial search optimization
CREATE INDEX idx_coordinates ON DirectoryListings (Latitude, Longitude);

-- Example of proper error handling during table creation
-- Wrapping the table creation in a transaction block to ensure atomicity
BEGIN;

-- Ensure table does not already exist before creating
DROP TABLE IF EXISTS DirectoryListings;

-- Create the table again (if dropped)
CREATE TABLE DirectoryListings (
    ListingID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL,
);

COMMIT;

```
