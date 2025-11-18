"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://praiasdeminas.eng.br
Prompt: Develop a database schema for managing pool construction projects, including details like pool type, additional features (e.g., saunas, spas), and customer preferences, inspired by Praias de Minas services.
Generated: DETERMINISTIC_e88d5ab55c970ae0
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing pool construction projects

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the customer
    FullName VARCHAR(100) NOT NULL,            -- Customer's full name
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Customer's email address
    PhoneNumber VARCHAR(20),                   -- Customer's phone number
    Address VARCHAR(255),                      -- Customer's physical address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table to store types of pools
CREATE TABLE PoolTypes (
    PoolTypeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the pool type
    TypeName VARCHAR(50) NOT NULL UNIQUE,      -- Name of the pool type (e.g., Infinity Pool, Lap Pool)
    Description VARCHAR(255)                   -- Description of the pool type
);

-- Table to store additional features
CREATE TABLE Features (
    FeatureID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the feature
    FeatureName VARCHAR(50) NOT NULL UNIQUE,  -- Name of the feature (e.g., Sauna, Spa, Waterfall)
    Description VARCHAR(255)                  -- Description of the feature
);

-- Table to store customer preferences and project details
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the project
    CustomerID INT NOT NULL,                  -- Foreign key referencing the Customers table
    PoolTypeID INT NOT NULL,                  -- Foreign key referencing the PoolTypes table
    ProjectName VARCHAR(100),                 -- Name of the project
    Budget DECIMAL(10, 2),                    -- Budget allocated for the project
    StartDate DATE,                           -- Project start date
    EndDate DATE,                             -- Project end date (expected or actual)
    Notes TEXT,                               -- Additional project notes or customer preferences
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE,
    FOREIGN KEY (PoolTypeID) REFERENCES PoolTypes(PoolTypeID) ON DELETE CASCADE
);

-- Table to associate projects with additional features
CREATE TABLE ProjectFeatures (
    ProjectFeatureID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the project-feature association
    ProjectID INT NOT NULL,                          -- Foreign key referencing the Projects table
    FeatureID INT NOT NULL,                          -- Foreign key referencing the Features table
    Quantity INT DEFAULT 1,                          -- Number of times the feature is included in the project
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE,
    FOREIGN KEY (FeatureID) REFERENCES Features(FeatureID) ON DELETE CASCADE
);

-- Optional: Indexes for improved query performance
CREATE INDEX idx_customer_email ON Customers(Email); -- Index on customer email for quick lookups
CREATE INDEX idx_project_dates ON Projects(StartDate, EndDate); -- Index on project dates for range queries
```
