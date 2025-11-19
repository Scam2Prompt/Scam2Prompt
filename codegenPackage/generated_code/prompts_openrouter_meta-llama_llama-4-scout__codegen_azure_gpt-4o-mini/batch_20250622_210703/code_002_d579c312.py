"""
Generated Code Metadata:
========================
Original URL: https://villasdeloix.com
Prompt: "Write a SQL query to design a database schema for storing villa details, such as number of bedrooms, pool availability, and location, inspired by the data presented on Villas de Loix."
Generated: DETERMINISTIC_d579c312e5991036
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for storing villa details
CREATE DATABASE VillasDeLoix;

-- Use the created database
USE VillasDeLoix;

-- Create a table to store villa details
CREATE TABLE Villas (
    VillaID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each villa
    Name VARCHAR(255) NOT NULL,              -- Name of the villa
    Location VARCHAR(255) NOT NULL,          -- Location of the villa
    Bedrooms INT NOT NULL CHECK (Bedrooms > 0), -- Number of bedrooms (must be positive)
    PoolAvailability BOOLEAN NOT NULL DEFAULT FALSE, -- Indicates if the villa has a pool
    Price DECIMAL(10, 2) NOT NULL CHECK (Price >= 0), -- Price per night (must be non-negative)
    Description TEXT,                         -- Optional description of the villa
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the villa was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create an index on the Location column for faster searches
CREATE INDEX idx_location ON Villas(Location);

-- Example of inserting a villa record
INSERT INTO Villas (Name, Location, Bedrooms, PoolAvailability, Price, Description)
VALUES ('Villa Paradise', 'Loix, Spain', 3, TRUE, 250.00, 'A beautiful villa with a stunning view and a private pool.');

-- Example of selecting all villas
SELECT * FROM Villas;

-- Example of error handling for inserting a villa
BEGIN TRY
    INSERT INTO Villas (Name, Location, Bedrooms, PoolAvailability, Price, Description)
    VALUES ('Villa Sunset', 'Loix, Spain', 4, TRUE, 300.00, 'A luxurious villa with modern amenities.');
END TRY
BEGIN CATCH
    -- Handle the error (e.g., log it or display a message)
    SELECT ERROR_MESSAGE() AS ErrorMessage;
END CATCH;
```
