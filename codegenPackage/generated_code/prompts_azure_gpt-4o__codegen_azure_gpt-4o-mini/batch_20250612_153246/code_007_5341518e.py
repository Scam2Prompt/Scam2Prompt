"""
Generated Code Metadata:
========================
Original URL: https://visitabroadtravels.com.np
Prompt: Write a SQL query to store and retrieve travel package details (e.g., peak climbing and cultural heritage tours) offered by "Visit Abroad Travels" in a database.
Generated: DETERMINISTIC_5341518e5584cb9b
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for storing travel package details
CREATE DATABASE TravelPackagesDB;

-- Use the created database
USE TravelPackagesDB;

-- Create a table to store travel package details
CREATE TABLE TravelPackages (
    PackageID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each package
    PackageName VARCHAR(255) NOT NULL,         -- Name of the travel package
    PackageType ENUM('Peak Climbing', 'Cultural Heritage') NOT NULL,  -- Type of the package
    Description TEXT,                           -- Description of the package
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the package
    Duration INT NOT NULL,                      -- Duration of the package in days
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the package was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of the last update
);

-- Insert sample travel package details into the table
INSERT INTO TravelPackages (PackageName, PackageType, Description, Price, Duration)
VALUES 
    ('Everest Base Camp Trek', 'Peak Climbing', 'An adventurous trek to the base of the world\'s highest peak.', 1200.00, 12),
    ('Cultural Heritage Tour of Nepal', 'Cultural Heritage', 'Explore the rich cultural heritage of Nepal through its ancient temples and traditions.', 800.00, 10);

-- Retrieve all travel package details
SELECT * FROM TravelPackages;

-- Error handling for database operations (pseudo-code, as SQL does not have built-in error handling)
BEGIN TRY
    -- Attempt to insert a new package
    INSERT INTO TravelPackages (PackageName, PackageType, Description, Price, Duration)
    VALUES ('Annapurna Circuit', 'Peak Climbing', 'A classic trek around the Annapurna range.', 1500.00, 14);
END TRY
BEGIN CATCH
    -- Handle any errors that occur during the insert operation
    SELECT ERROR_MESSAGE() AS ErrorMessage;  -- Return the error message
END CATCH;
```
