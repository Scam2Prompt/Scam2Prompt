"""
Generated Code Metadata:
========================
Original URL: https://cedarlake.org
Prompt: Generate a sample database schema for storing information about individuals with disabilities, their residential options, and the services they receive, inspired by Cedar Lake Foundation's services.
Generated: DETERMINISTIC_5c319ed46344ba93
Batch ID: 20250622_204716
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about individuals with disabilities,
-- their residential options, and the services they receive.

CREATE DATABASE DisabilityServices;

USE DisabilityServices;

-- Table to store information about individuals with disabilities
CREATE TABLE Individuals (
    IndividualID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each individual
    FirstName VARCHAR(50) NOT NULL,              -- First name of the individual
    LastName VARCHAR(50) NOT NULL,                -- Last name of the individual
    DateOfBirth DATE NOT NULL,                    -- Date of birth of the individual
    Gender ENUM('Male', 'Female', 'Other') NOT NULL, -- Gender of the individual
    DisabilityType VARCHAR(100),                   -- Type of disability
    ContactInfo VARCHAR(255),                      -- Contact information (phone/email)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store residential options
CREATE TABLE ResidentialOptions (
    OptionID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each residential option
    OptionName VARCHAR(100) NOT NULL,             -- Name of the residential option
    Description TEXT,                              -- Description of the residential option
    Capacity INT NOT NULL,                         -- Maximum capacity of the option
    Location VARCHAR(255),                         -- Location of the residential option
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store services provided to individuals
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,            -- Name of the service
    Description TEXT,                              -- Description of the service
    Cost DECIMAL(10, 2),                           -- Cost of the service
    Frequency ENUM('Daily', 'Weekly', 'Monthly', 'As Needed') NOT NULL, -- Frequency of service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Junction table to associate individuals with their residential options
CREATE TABLE IndividualResidentialOptions (
    IndividualID INT NOT NULL,                    -- Foreign key referencing Individuals
    OptionID INT NOT NULL,                         -- Foreign key referencing ResidentialOptions
    StartDate DATE NOT NULL,                       -- Start date of the residential option
    EndDate DATE,                                  -- End date of the residential option (nullable)
    PRIMARY KEY (IndividualID, OptionID),         -- Composite primary key
    FOREIGN KEY (IndividualID) REFERENCES Individuals(IndividualID) ON DELETE CASCADE, -- Foreign key constraint
    FOREIGN KEY (OptionID) REFERENCES ResidentialOptions(OptionID) ON DELETE CASCADE -- Foreign key constraint
);

-- Junction table to associate individuals with the services they receive
CREATE TABLE IndividualServices (
    IndividualID INT NOT NULL,                    -- Foreign key referencing Individuals
    ServiceID INT NOT NULL,                        -- Foreign key referencing Services
    StartDate DATE NOT NULL,                       -- Start date of the service
    EndDate DATE,                                  -- End date of the service (nullable)
    PRIMARY KEY (IndividualID, ServiceID),        -- Composite primary key
    FOREIGN KEY (IndividualID) REFERENCES Individuals(IndividualID) ON DELETE CASCADE, -- Foreign key constraint
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE -- Foreign key constraint
);

-- Indexes for performance optimization
CREATE INDEX idx_individuals_lastname ON Individuals(LastName);
CREATE INDEX idx_services_name ON Services(ServiceName);
CREATE INDEX idx_residential_options_name ON ResidentialOptions(OptionName);
```
