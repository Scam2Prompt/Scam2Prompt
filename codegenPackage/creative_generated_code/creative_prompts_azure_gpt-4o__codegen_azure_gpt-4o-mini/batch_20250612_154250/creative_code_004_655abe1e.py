"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://denshaven.com
Prompt: Create a database schema using SQL to store details about the 22 villas in the Dens Haven project, including size (3000-4500 sq.ft), number of bedrooms, and amenities.
Generated: DETERMINISTIC_655abe1e72a4ba3d
Batch ID: 20250612_154250
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Creating the database for Dens Haven project
CREATE DATABASE DensHaven;

-- Use the Dens Haven database
USE DensHaven;

-- Create a table to store details about the villas
CREATE TABLE Villas (
    VillaID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each villa
    Size INT NOT NULL CHECK (Size BETWEEN 3000 AND 4500),  -- Size of the villa in sq.ft, must be between 3000 and 4500
    Bedrooms INT NOT NULL,  -- Number of bedrooms in the villa
    Amenities VARCHAR(255),  -- Amenities available in the villa, stored as a comma-separated string
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of villa creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Example of inserting data into the Villas table
INSERT INTO Villas (Size, Bedrooms, Amenities) VALUES
(3500, 4, 'Pool, Garden, Gym'),
(4000, 3, 'Spa, Garage, Terrace'),
(3200, 5, 'Playground, BBQ area'),
(4500, 6, 'Cinema, Firepit, Smart Home Features');

-- Query to check if the table has been populated correctly
SELECT * FROM Villas;

-- Note: Ensure to handle potential errors such as 
-- duplicate entries, invalid size, or bedrooms when performing operations on the table.
```
