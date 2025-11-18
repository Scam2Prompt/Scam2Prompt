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

CREATE DATABASE PoolConstructionDB;

USE PoolConstructionDB;

-- Table for storing customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Phone VARCHAR(15) NOT NULL,
    Address VARCHAR(255) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for storing different types of pools
CREATE TABLE PoolTypes (
    PoolTypeID INT AUTO_INCREMENT PRIMARY KEY,
    PoolTypeName VARCHAR(50) NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for additional features that can be added to pools
CREATE TABLE AdditionalFeatures (
    FeatureID INT AUTO_INCREMENT PRIMARY KEY,
    FeatureName VARCHAR(50) NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for storing pool construction projects
CREATE TABLE PoolProjects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY,
    CustomerID INT NOT NULL,
    PoolTypeID INT NOT NULL,
    ProjectStartDate DATE NOT NULL,
    ProjectEndDate DATE,
    Status ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') NOT NULL DEFAULT 'Pending',
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE,
    FOREIGN KEY (PoolTypeID) REFERENCES PoolTypes(PoolTypeID) ON DELETE CASCADE
);

-- Junction table for linking pool projects with additional features
CREATE TABLE ProjectFeatures (
    ProjectFeatureID INT AUTO_INCREMENT PRIMARY KEY,
    ProjectID INT NOT NULL,
    FeatureID INT NOT NULL,
    FOREIGN KEY (ProjectID) REFERENCES PoolProjects(ProjectID) ON DELETE CASCADE,
    FOREIGN KEY (FeatureID) REFERENCES AdditionalFeatures(FeatureID) ON DELETE CASCADE,
    UNIQUE (ProjectID, FeatureID) -- Ensure that a feature can only be added once per project
);

-- Table for storing customer preferences related to pool features
CREATE TABLE CustomerPreferences (
    PreferenceID INT AUTO_INCREMENT PRIMARY KEY,
    CustomerID INT NOT NULL,
    PreferredPoolType INT NOT NULL,
    AdditionalFeatures TEXT, -- A comma-separated list of feature IDs
    Notes TEXT,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE,
    FOREIGN KEY (PreferredPoolType) REFERENCES PoolTypes(PoolTypeID)
);

-- Sample data to populate tables (for testing purposes)
INSERT INTO PoolTypes (PoolTypeName, Description) VALUES 
('In-Ground Pool', 'A permanent pool built into the ground.'),
('Above Ground Pool', 'A pool that is above ground level.'),
('Infinity Pool', 'A pool with an edge that creates a visual effect of water extending to the horizon.');

INSERT INTO AdditionalFeatures (FeatureName, Description) VALUES 
('Heated Pool', 'Pool water is heated to a comfortable temperature.'),
('Spa', 'A hot tub or whirlpool spa adjacent to the pool.'),
('Sauna', 'A small room used as a hot-air or steam bath.');

-- Make sure to create indexes on foreign keys for performance
CREATE INDEX idx_customer_id ON PoolProjects(CustomerID);
CREATE INDEX idx_pool_type_id ON PoolProjects(PoolTypeID);
CREATE INDEX idx_project_id ON ProjectFeatures(ProjectID);
CREATE INDEX idx_feature_id ON ProjectFeatures(FeatureID);
CREATE INDEX idx_preferred_pool_type ON CustomerPreferences(PreferredPoolType);
```
