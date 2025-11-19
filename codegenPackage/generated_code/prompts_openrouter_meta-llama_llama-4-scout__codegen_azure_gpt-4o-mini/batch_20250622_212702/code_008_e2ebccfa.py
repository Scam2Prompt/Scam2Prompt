"""
Generated Code Metadata:
========================
Original URL: https://www.thefishfinder.com
Prompt: "Develop a basic database schema for storing information about fishing charters and guides."
Generated: DETERMINISTIC_e2ebccfa0f716d16
Batch ID: 20250622_212702
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a basic database schema for storing information about fishing charters and guides

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS FishingGuides;
DROP TABLE IF EXISTS FishingCharters;

-- Create a table to store information about fishing guides
CREATE TABLE FishingGuides (
    GuideID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each guide
    FirstName VARCHAR(50) NOT NULL,          -- First name of the guide
    LastName VARCHAR(50) NOT NULL,           -- Last name of the guide
    PhoneNumber VARCHAR(15),                  -- Contact phone number of the guide
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Email address of the guide
    ExperienceYears INT CHECK (ExperienceYears >= 0),  -- Years of experience
    LicenseNumber VARCHAR(50) UNIQUE NOT NULL -- Unique license number for the guide
);

-- Create a table to store information about fishing charters
CREATE TABLE FishingCharters (
    CharterID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each charter
    CharterName VARCHAR(100) NOT NULL,        -- Name of the fishing charter
    Location VARCHAR(100) NOT NULL,           -- Location of the charter service
    MaxCapacity INT CHECK (MaxCapacity > 0),  -- Maximum number of people the charter can accommodate
    PricePerHour DECIMAL(10, 2) CHECK (PricePerHour >= 0),  -- Price per hour for the charter
    GuideID INT,                               -- Foreign key referencing the FishingGuides table
    FOREIGN KEY (GuideID) REFERENCES FishingGuides(GuideID) ON DELETE SET NULL -- Establish relationship with guides
);

-- Insert sample data into FishingGuides table
INSERT INTO FishingGuides (FirstName, LastName, PhoneNumber, Email, ExperienceYears, LicenseNumber)
VALUES 
('John', 'Doe', '123-456-7890', 'john.doe@example.com', 5, 'GUIDE12345'),
('Jane', 'Smith', '098-765-4321', 'jane.smith@example.com', 10, 'GUIDE67890');

-- Insert sample data into FishingCharters table
INSERT INTO FishingCharters (CharterName, Location, MaxCapacity, PricePerHour, GuideID)
VALUES 
('Ocean Adventures', 'Miami, FL', 6, 300.00, 1),
('Lake Fishing Tours', 'Lake Tahoe, CA', 4, 200.00, 2);
```
