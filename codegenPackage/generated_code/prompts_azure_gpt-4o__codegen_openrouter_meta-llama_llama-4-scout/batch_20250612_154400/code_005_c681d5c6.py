"""
Generated Code Metadata:
========================
Original URL: https://elfworldvape.com
Prompt: Develop a database schema in SQL to store information about Elfworld vape products, including fields for model name, puff count, battery type, liquid display, and anti-counterfeiting verification status.
Generated: DETERMINISTIC_c681d5c6d5281a94
Batch ID: 20250612_154400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for Elfworld vape products
CREATE DATABASE ElfworldVapes;

-- Use the ElfworldVapes database
USE ElfworldVapes;

-- Create a table for vape products
CREATE TABLE VapeProducts (
    -- Unique identifier for each product
    ProductID INT AUTO_INCREMENT,
    
    -- Model name of the vape product
    ModelName VARCHAR(255) NOT NULL,
    
    -- Puff count of the vape product
    PuffCount INT,
    
    -- Battery type of the vape product
    BatteryType VARCHAR(100),
    
    -- Liquid display feature of the vape product (e.g., yes/no)
    LiquidDisplay BOOLEAN,
    
    -- Anti-counterfeiting verification status of the vape product (e.g., verified/not verified)
    AntiCounterfeitingStatus ENUM('verified', 'not_verified') DEFAULT 'not_verified',
    
    -- Timestamp for when the product was added to the database
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    -- Timestamp for when the product was last updated in the database
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    
    PRIMARY KEY (ProductID)
);

-- Create an index on ModelName for efficient querying
CREATE INDEX idx_ModelName ON VapeProducts(ModelName);

-- Create a table for product verification history
CREATE TABLE VerificationHistory (
    -- Unique identifier for each verification event
    VerificationID INT AUTO_INCREMENT,
    
    -- Foreign key referencing the ProductID in VapeProducts
    ProductID INT,
    
    -- Verification status
    VerificationStatus ENUM('verified', 'not_verified'),
    
    -- Timestamp for when the verification event occurred
    VerifiedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    PRIMARY KEY (VerificationID),
    
    -- Establish relationship with VapeProducts
    FOREIGN KEY (ProductID) REFERENCES VapeProducts(ProductID) ON DELETE CASCADE
);

-- Example insert statement
INSERT INTO VapeProducts (ModelName, PuffCount, BatteryType, LiquidDisplay, AntiCounterfeitingStatus)
VALUES ('Elfworld Pro', 1000, 'Rechargeable Lithium-ion', TRUE, 'verified');

-- Example update statement
UPDATE VapeProducts
SET AntiCounterfeitingStatus = 'verified'
WHERE ModelName = 'Elfworld Pro';

-- Example select statement
SELECT * FROM VapeProducts;
```
