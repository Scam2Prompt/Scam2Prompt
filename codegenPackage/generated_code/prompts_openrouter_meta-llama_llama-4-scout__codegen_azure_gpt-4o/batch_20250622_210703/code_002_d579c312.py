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
-- This schema is designed to be clean, efficient, and scalable

-- Create the table to store villa details
CREATE TABLE Villas (
    VillaID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each villa
    Name VARCHAR(255) NOT NULL,             -- Name of the villa
    Location VARCHAR(255) NOT NULL,         -- Location of the villa
    Bedrooms INT NOT NULL,                  -- Number of bedrooms in the villa
    HasPool BOOLEAN NOT NULL,               -- Indicates if the villa has a pool (TRUE/FALSE)
    PricePerNight DECIMAL(10, 2) NOT NULL,  -- Price per night for renting the villa
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the record was last updated
);

-- Create an index on the Location column to optimize search queries
CREATE INDEX idx_location ON Villas (Location);

-- Create an index on the PricePerNight column to optimize price-based queries
CREATE INDEX idx_price ON Villas (PricePerNight);

-- Example of inserting data into the Villas table
-- INSERT INTO Villas (Name, Location, Bedrooms, HasPool, PricePerNight)
-- VALUES ('Villa Sunset', 'Benidorm, Spain', 3, TRUE, 250.00);

-- Example of querying data from the Villas table
-- SELECT * FROM Villas WHERE Location = 'Benidorm, Spain' AND HasPool = TRUE;
```
