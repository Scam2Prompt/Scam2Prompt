"""
Generated Code Metadata:
========================
Original URL: https://praiasdeminas.eng.br
Prompt: Develop a database schema for managing pool construction projects, including details like pool type, additional features (e.g., saunas, spas), and customer preferences, inspired by Praias de Minas services.
Generated: DETERMINISTIC_e88d5ab55c970ae0
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing pool construction projects

-- Create a table for storing customer information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,             -- Customer's first name
    LastName VARCHAR(50) NOT NULL,               -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,          -- Customer's email address
    Phone VARCHAR(15),                           -- Customer's phone number
    Address VARCHAR(255)                          -- Customer's address
);

-- Create a table for storing pool types
CREATE TABLE PoolTypes (
    PoolTypeID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each pool type
    TypeName VARCHAR(50) NOT NULL,               -- Name of the pool type (e.g., In-ground, Above-ground)
    Description TEXT                              -- Description of the pool type
);

-- Create a table for storing additional features
CREATE TABLE AdditionalFeatures (
    FeatureID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each feature
    FeatureName VARCHAR(50) NOT NULL,             -- Name of the feature (e.g., Sauna, Spa)
    Description TEXT                              -- Description of the feature
);

-- Create a table for storing pool construction projects
CREATE TABLE PoolProjects (
    ProjectID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each project
    CustomerID INT NOT NULL,                      -- Foreign key referencing Customers
    PoolTypeID INT NOT NULL,                      -- Foreign key referencing PoolTypes
    ProjectStartDate DATE NOT NULL,               -- Start date of the project
    ProjectEndDate DATE,                          -- End date of the project (nullable)
    Status ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') NOT NULL, -- Current status of the project
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (PoolTypeID) REFERENCES PoolTypes(PoolTypeID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Create a junction table for managing many-to-many relationships between projects and additional features
CREATE TABLE ProjectFeatures (
    ProjectID INT NOT NULL,                       -- Foreign key referencing PoolProjects
    FeatureID INT NOT NULL,                       -- Foreign key referencing AdditionalFeatures
    PRIMARY KEY (ProjectID, FeatureID),          -- Composite primary key
    FOREIGN KEY (ProjectID) REFERENCES PoolProjects(ProjectID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (FeatureID) REFERENCES AdditionalFeatures(FeatureID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create an index on the CustomerID in the PoolProjects table for faster lookups
CREATE INDEX idx_customer ON PoolProjects(CustomerID);

-- Create an index on the PoolTypeID in the PoolProjects table for faster lookups
CREATE INDEX idx_pooltype ON PoolProjects(PoolTypeID);
```
