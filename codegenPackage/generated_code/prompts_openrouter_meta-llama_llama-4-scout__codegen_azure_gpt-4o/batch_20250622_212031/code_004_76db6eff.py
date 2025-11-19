"""
Generated Code Metadata:
========================
Original URL: https://frigoterm.ro
Prompt: "Design a database schema to store information about various air conditioning systems, including their specifications and prices, similar to those listed on frigoterm.ro."
Generated: DETERMINISTIC_76db6eff4a9e177a
Batch ID: 20250622_212031
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about air conditioning systems

-- Table to store manufacturers
CREATE TABLE Manufacturers (
    ManufacturerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each manufacturer
    Name VARCHAR(255) NOT NULL,                    -- Name of the manufacturer
    Country VARCHAR(100),                          -- Country of origin
    Website VARCHAR(255)                           -- Manufacturer's website
);

-- Table to store air conditioning systems
CREATE TABLE AirConditioningSystems (
    SystemID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each air conditioning system
    ManufacturerID INT NOT NULL,                   -- Foreign key referencing the manufacturer
    ModelName VARCHAR(255) NOT NULL,               -- Model name of the air conditioning system
    Type ENUM('Split', 'Window', 'Portable', 'Central', 'Other') NOT NULL, -- Type of air conditioning system
    CoolingCapacity FLOAT NOT NULL,                -- Cooling capacity in kW or BTU
    HeatingCapacity FLOAT,                         -- Heating capacity in kW or BTU (optional)
    EnergyEfficiencyRating VARCHAR(50),            -- Energy efficiency rating (e.g., A++, A+, etc.)
    NoiseLevel FLOAT,                              -- Noise level in dB
    Price DECIMAL(10, 2) NOT NULL,                 -- Price of the system
    Stock INT DEFAULT 0,                           -- Number of units available in stock
    Description TEXT,                              -- Additional description or specifications
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store reviews for air conditioning systems
CREATE TABLE Reviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each review
    SystemID INT NOT NULL,                         -- Foreign key referencing the air conditioning system
    ReviewerName VARCHAR(255),                     -- Name of the reviewer
    Rating INT CHECK (Rating BETWEEN 1 AND 5),     -- Rating given by the reviewer (1 to 5)
    Comment TEXT,                                  -- Review comment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Timestamp for when the review was created
);

-- Foreign key constraints
ALTER TABLE AirConditioningSystems
ADD CONSTRAINT FK_Manufacturer FOREIGN KEY (ManufacturerID) REFERENCES Manufacturers(ManufacturerID)
ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE Reviews
ADD CONSTRAINT FK_System FOREIGN KEY (SystemID) REFERENCES AirConditioningSystems(SystemID)
ON DELETE CASCADE ON UPDATE CASCADE;

-- Indexes for faster queries
CREATE INDEX IDX_ManufacturerName ON Manufacturers(Name);
CREATE INDEX IDX_SystemModelName ON AirConditioningSystems(ModelName);
CREATE INDEX IDX_ReviewSystemID ON Reviews(SystemID);
```
