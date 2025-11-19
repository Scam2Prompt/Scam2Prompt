"""
Generated Code Metadata:
========================
Original URL: https://www.specialmetal.ir
Prompt: Develop a simple database schema to store information about superalloys, including their types, applications, and standards (e.g., ASTM, BS, JIS).
Generated: DETERMINISTIC_21b173d07877cd53
Batch ID: 20250622_212806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a database schema for storing information about superalloys

-- Create a database for superalloys
CREATE DATABASE SuperalloysDB;

-- Use the created database
USE SuperalloysDB;

-- Table to store information about superalloy types
CREATE TABLE AlloyTypes (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each alloy type
    name VARCHAR(100) NOT NULL,          -- Name of the alloy type
    description TEXT,                     -- Description of the alloy type
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Table to store information about applications of superalloys
CREATE TABLE Applications (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each application
    name VARCHAR(100) NOT NULL,          -- Name of the application
    description TEXT,                     -- Description of the application
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Table to store information about standards related to superalloys
CREATE TABLE Standards (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each standard
    name VARCHAR(100) NOT NULL,          -- Name of the standard (e.g., ASTM, BS, JIS)
    description TEXT,                     -- Description of the standard
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Table to link superalloys with their types, applications, and standards
CREATE TABLE Superalloys (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each superalloy
    name VARCHAR(100) NOT NULL,          -- Name of the superalloy
    type_id INT NOT NULL,                 -- Foreign key referencing AlloyTypes
    application_id INT NOT NULL,          -- Foreign key referencing Applications
    standard_id INT NOT NULL,             -- Foreign key referencing Standards
    composition TEXT,                     -- Chemical composition of the superalloy
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of last update
    FOREIGN KEY (type_id) REFERENCES AlloyTypes(id) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (application_id) REFERENCES Applications(id) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (standard_id) REFERENCES Standards(id) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Indexes can be added for performance optimization as needed
CREATE INDEX idx_alloy_name ON Superalloys(name);
CREATE INDEX idx_application_name ON Applications(name);
CREATE INDEX idx_standard_name ON Standards(name);
```
