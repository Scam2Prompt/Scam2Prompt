"""
Generated Code Metadata:
========================
Original URL: https://graylinegeneva.com
Prompt: Create a sample database schema for storing information about Gray Line Geneva's tours, including details such as tour name, location, duration, and price.
Generated: DETERMINISTIC_06326786a8574502
Batch ID: 20250622_205335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about Gray Line Geneva's tours

-- Create a table to store tour information
CREATE TABLE Tours (
    TourID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each tour
    TourName VARCHAR(255) NOT NULL,        -- Name of the tour
    Location VARCHAR(255) NOT NULL,        -- Location of the tour
    Duration INT NOT NULL,                 -- Duration of the tour in minutes
    Price DECIMAL(10, 2) NOT NULL,         -- Price of the tour in USD
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the record was last updated
);

-- Create a table to store additional details about locations (optional)
CREATE TABLE Locations (
    LocationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each location
    LocationName VARCHAR(255) NOT NULL,        -- Name of the location
    Description TEXT,                          -- Description of the location
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the record was last updated
);

-- Create a foreign key relationship between Tours and Locations (optional)
ALTER TABLE Tours
ADD CONSTRAINT FK_Tours_Location
FOREIGN KEY (Location) REFERENCES Locations(LocationName)
ON DELETE SET NULL
ON UPDATE CASCADE;

-- Example indexes for optimizing queries
CREATE INDEX IDX_TourName ON Tours (TourName); -- Index for faster search by tour name
CREATE INDEX IDX_LocationName ON Locations (LocationName); -- Index for faster search by location name

-- Error handling and rollback mechanism can be implemented in application code
-- when interacting with this schema.
```
