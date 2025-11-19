"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fdanongbualamphu.com
Prompt: How can I create a database schema to manage documents for health product regulations and consultations as outlined by the หนองบัวลำภู health authorities?
Generated: DETERMINISTIC_fe34fafc2c8bca5d
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a schema for managing documents related to health product regulations and consultations
CREATE SCHEMA HealthProductRegulations;

-- Table to store health products
CREATE TABLE HealthProductRegulations.Products (
    ProductID SERIAL PRIMARY KEY,          -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,     -- Name of the health product
    ProductType VARCHAR(100) NOT NULL,     -- Type of health product (e.g., medicine, supplement)
    Description TEXT,                       -- Description of the health product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store regulations associated with health products
CREATE TABLE HealthProductRegulations.Regulations (
    RegulationID SERIAL PRIMARY KEY,        -- Unique identifier for each regulation
    RegulationTitle VARCHAR(255) NOT NULL, -- Title of the regulation
    RegulationDetails TEXT,                  -- Detailed description of the regulation
    EffectiveDate DATE NOT NULL,            -- Date when the regulation becomes effective
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to link health products and their respective regulations
CREATE TABLE HealthProductRegulations.ProductRegulations (
    ProductRegulationID SERIAL PRIMARY KEY, -- Unique identifier for the product-regulation link
    ProductID INT NOT NULL,                  -- Foreign key referencing the Products table
    RegulationID INT NOT NULL,               -- Foreign key referencing the Regulations table
    FOREIGN KEY (ProductID) REFERENCES HealthProductRegulations.Products(ProductID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (RegulationID) REFERENCES HealthProductRegulations.Regulations(RegulationID) ON DELETE CASCADE, -- Ensure referential integrity
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store consultations related to health products
CREATE TABLE HealthProductRegulations.Consultations (
    ConsultationID SERIAL PRIMARY KEY,       -- Unique identifier for each consultation
    ProductID INT NOT NULL,                  -- Foreign key referencing the Products table
    ConsultationDate TIMESTAMP NOT NULL,     -- Date of the consultation
    ConsultationDetails TEXT,                 -- Details of the consultation
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ProductID) REFERENCES HealthProductRegulations.Products(ProductID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for faster querying
CREATE INDEX idx_product_name ON HealthProductRegulations.Products(ProductName);
CREATE INDEX idx_regulation_title ON HealthProductRegulations.Regulations(RegulationTitle);
CREATE INDEX idx_consultation_date ON HealthProductRegulations.Consultations(ConsultationDate);
```
