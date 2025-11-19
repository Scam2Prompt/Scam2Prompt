"""
Generated Code Metadata:
========================
Original URL: https://www.trendsetterzs.com
Prompt: Create a database schema for managing global apparel sourcing operations, including tables for manufacturers, quality control agents, and production specifications, as highlighted by Trend Setterzs.
Generated: DETERMINISTIC_6047ece98778eca6
Batch ID: 20250612_154327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing global apparel sourcing operations

-- Create a table for manufacturers
CREATE TABLE Manufacturers (
    ManufacturerID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each manufacturer
    Name VARCHAR(255) NOT NULL,                    -- Name of the manufacturer
    Location VARCHAR(255) NOT NULL,                -- Location of the manufacturer
    ContactEmail VARCHAR(255) UNIQUE NOT NULL,     -- Contact email for the manufacturer
    PhoneNumber VARCHAR(20),                        -- Phone number for the manufacturer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the record was last updated
);

-- Create a table for quality control agents
CREATE TABLE QualityControlAgents (
    AgentID INT PRIMARY KEY AUTO_INCREMENT,         -- Unique identifier for each quality control agent
    Name VARCHAR(255) NOT NULL,                     -- Name of the quality control agent
    Email VARCHAR(255) UNIQUE NOT NULL,             -- Email of the quality control agent
    PhoneNumber VARCHAR(20),                         -- Phone number for the quality control agent
    ManufacturerID INT,                              -- Foreign key referencing the manufacturer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the record was last updated
    FOREIGN KEY (ManufacturerID) REFERENCES Manufacturers(ManufacturerID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table for production specifications
CREATE TABLE ProductionSpecifications (
    SpecificationID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each production specification
    ManufacturerID INT,                               -- Foreign key referencing the manufacturer
    QualityControlAgentID INT,                       -- Foreign key referencing the quality control agent
    FabricType VARCHAR(100) NOT NULL,                -- Type of fabric used in production
    SizeChart JSON NOT NULL,                         -- Size chart in JSON format
    ProductionLeadTime INT NOT NULL,                 -- Lead time for production in days
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the record was last updated
    FOREIGN KEY (ManufacturerID) REFERENCES Manufacturers(ManufacturerID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (QualityControlAgentID) REFERENCES QualityControlAgents(AgentID) ON DELETE SET NULL -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_manufacturer_name ON Manufacturers(Name);
CREATE INDEX idx_agent_email ON QualityControlAgents(Email);
CREATE INDEX idx_specification_fabric ON ProductionSpecifications(FabricType);
```
