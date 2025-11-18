"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-200--nervous-kare-6f3c45.netlify.app
Prompt: Suggest a database schema for storing refuse and recycling collection data, including fields for collection dates, types of waste, and pickup locations specific to the City of York.
Generated: DETERMINISTIC_7cfd3561da29f436
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL script to create a database schema for storing refuse and recycling collection data

CREATE DATABASE CityOfYorkWasteManagement;

USE CityOfYorkWasteManagement;

-- Table to store information about different types of waste
CREATE TABLE WasteTypes (
    WasteTypeID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each waste type
    TypeName VARCHAR(100) NOT NULL,              -- Name of the waste type (e.g., 'General Waste', 'Recyclables')
    Description TEXT,                             -- Description of the waste type
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the waste type was created
);

-- Table to store pickup locations
CREATE TABLE PickupLocations (
    LocationID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each pickup location
    Address VARCHAR(255) NOT NULL,                -- Full address of the pickup location
    City VARCHAR(100) NOT NULL DEFAULT 'York',    -- City name, defaulting to 'York'
    Postcode VARCHAR(10) NOT NULL,                -- Postal code for the pickup location
    Latitude DECIMAL(9, 6),                       -- Latitude coordinate for mapping
    Longitude DECIMAL(9, 6),                      -- Longitude coordinate for mapping
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Timestamp for when the location was added
);

-- Table to store refuse and recycling collection data
CREATE TABLE CollectionSchedules (
    CollectionID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each collection record
    CollectionDate DATE NOT NULL,                  -- Date of the collection
    WasteTypeID INT NOT NULL,                      -- Foreign key to reference the waste type
    LocationID INT NOT NULL,                       -- Foreign key to reference the pickup location
    Frequency ENUM('Weekly', 'Bi-weekly', 'Monthly') NOT NULL, -- Collection frequency
    Notes TEXT,                                    -- Additional notes regarding the collection
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    FOREIGN KEY (WasteTypeID) REFERENCES WasteTypes(WasteTypeID) ON DELETE CASCADE,  -- Establishing foreign key relationship
    FOREIGN KEY (LocationID) REFERENCES PickupLocations(LocationID) ON DELETE CASCADE   -- Establishing foreign key relationship
);

-- Indexing for faster queries
CREATE INDEX idx_collection_date ON CollectionSchedules(CollectionDate);
CREATE INDEX idx_location ON CollectionSchedules(LocationID);
CREATE INDEX idx_waste_type ON CollectionSchedules(WasteTypeID);

-- Insert sample waste types
INSERT INTO WasteTypes (TypeName, Description) VALUES 
('General Waste', 'Non-recyclable waste including food waste, packaging, etc.'),
('Recyclables', 'Items that can be recycled including paper, plastics, and metals'),
('Garden Waste', 'Organic waste from gardening activities including grass clippings and leaves');

-- Insert sample pickup locations
INSERT INTO PickupLocations (Address, Postcode, Latitude, Longitude) VALUES 
('123 Main St', 'YO1 1AA', 53.959, -1.081), 
('456 South St', 'YO1 2BB', 53.960, -1.083);

-- Insert sample collection schedules
INSERT INTO CollectionSchedules (CollectionDate, WasteTypeID, LocationID, Frequency, Notes) VALUES 
('2023-10-01', 1, 1, 'Weekly', 'Regular collection for general waste.'),
('2023-10-02', 2, 1, 'Weekly', 'Recycling collection on Mondays.'),
('2023-10-05', 3, 2, 'Bi-weekly', 'Garden waste collection every other Thursday.');
```
