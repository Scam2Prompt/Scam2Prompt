"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.trendsetterzs.com
Prompt: Create a database schema for managing global apparel sourcing operations, including tables for manufacturers, quality control agents, and production specifications, as highlighted by Trend Setterzs.
Generated: DETERMINISTIC_6047ece98778eca6
Batch ID: 20250612_154327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing global apparel sourcing operations

-- Create a database for the apparel sourcing operations
CREATE DATABASE ApparelSourcing;

-- Use the created database
USE ApparelSourcing;

-- Table to store information about manufacturers
CREATE TABLE Manufacturers (
    ManufacturerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each manufacturer
    Name VARCHAR(255) NOT NULL,                     -- Manufacturer's name
    ContactEmail VARCHAR(255) NOT NULL UNIQUE,      -- Contact email for the manufacturer
    PhoneNumber VARCHAR(15),                         -- Contact phone number
    Address TEXT,                                    -- Manufacturer's address
    Country VARCHAR(100) NOT NULL,                  -- Country where the manufacturer is located
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp of when the manufacturer was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store information about quality control agents
CREATE TABLE QualityControlAgents (
    AgentID INT AUTO_INCREMENT PRIMARY KEY,          -- Unique identifier for each quality control agent
    Name VARCHAR(255) NOT NULL,                      -- Agent's name
    ContactEmail VARCHAR(255) NOT NULL UNIQUE,       -- Contact email for the quality control agent
    PhoneNumber VARCHAR(15),                          -- Contact phone number
    AgencyName VARCHAR(255),                          -- Name of the agency the agent belongs to
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Timestamp of when the agent was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store production specifications
CREATE TABLE ProductionSpecifications (
    SpecificationID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each specification
    ManufacturerID INT NOT NULL,                      -- Foreign key referencing the manufacturer
    QualityControlAgentID INT NOT NULL,               -- Foreign key referencing the quality control agent
    FabricType VARCHAR(100) NOT NULL,                 -- Type of fabric used in production
    SizeChart JSON,                                   -- Size chart in JSON format
    ProductionLeadTime INT NOT NULL,                  -- Lead time for production in days
    MinimumOrderQuantity INT NOT NULL,                -- Minimum quantity to be ordered
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,     -- Timestamp of when the specification was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (ManufacturerID) REFERENCES Manufacturers(ManufacturerID) ON DELETE CASCADE, -- Cascading delete
    FOREIGN KEY (QualityControlAgentID) REFERENCES QualityControlAgents(AgentID) ON DELETE CASCADE -- Cascading delete
);

-- Indexes for optimization
CREATE INDEX idx_manufacturer_name ON Manufacturers(Name);
CREATE INDEX idx_agent_name ON QualityControlAgents(Name);
CREATE INDEX idx_fabric_type ON ProductionSpecifications(FabricType);
```
