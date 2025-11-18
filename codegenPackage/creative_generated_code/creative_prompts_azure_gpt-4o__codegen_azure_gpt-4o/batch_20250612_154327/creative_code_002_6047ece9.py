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
-- Database schema for managing global apparel sourcing operations.
-- This schema includes tables for manufacturers, quality control agents, and production specifications.

-- Table: Manufacturers
CREATE TABLE Manufacturers (
    ManufacturerID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for the manufacturer
    Name VARCHAR(255) NOT NULL,                       -- Manufacturer's name
    Country VARCHAR(100) NOT NULL,                    -- Country where the manufacturer is located
    Email VARCHAR(255),                               -- Contact email of the manufacturer
    PhoneNumber VARCHAR(20),                          -- Contact phone number of the manufacturer
    Address TEXT,                                     -- Manufacturer's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table: QualityControlAgents
CREATE TABLE QualityControlAgents (
    AgentID INT AUTO_INCREMENT PRIMARY KEY,           -- Unique identifier for the quality control agent
    Name VARCHAR(255) NOT NULL,                       -- Agent's name
    Company VARCHAR(255) NOT NULL,                    -- Company the agent works for
    Email VARCHAR(255),                               -- Contact email of the agent
    PhoneNumber VARCHAR(20),                          -- Contact phone number of the agent
    Country VARCHAR(100),                             -- Country where the agent operates
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table: ProductionSpecifications
CREATE TABLE ProductionSpecifications (
    SpecificationID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for the production specification
    ManufacturerID INT NOT NULL,                      -- Foreign key referencing the Manufacturer
    QCAgentID INT NOT NULL,                           -- Foreign key referencing the Quality Control Agent
    ProductType VARCHAR(100) NOT NULL,                -- Type of product being produced
    Material VARCHAR(255) NOT NULL,                   -- Material used for production
    Quantity INT NOT NULL,                            -- Quantity of items being produced
    SizeSpecification TEXT,                           -- Size details for the product
    ColorSpecification TEXT,                          -- Color details for the product
    Deadline DATE NOT NULL,                           -- Deadline for production completion
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (ManufacturerID) REFERENCES Manufacturers(ManufacturerID) ON DELETE CASCADE, -- Cascading delete
    FOREIGN KEY (QCAgentID) REFERENCES QualityControlAgents(AgentID) ON DELETE SET NULL         -- Nullify on delete
);

-- Ensure proper indexing for efficient queries
CREATE INDEX idx_ManufacturerID ON ProductionSpecifications(ManufacturerID);
CREATE INDEX idx_QCAgentID ON ProductionSpecifications(QCAgentID);

-- Add error handling support through database constraints
-- For example, a check constraint could be added to ensure positive quantities
ALTER TABLE ProductionSpecifications
ADD CONSTRAINT chk_Quantity_Positive CHECK (Quantity > 0);
```
