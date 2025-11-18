"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trackdieselperu.com
Prompt: Generate a database schema in SQL to store and manage high-quality machinery parts and accessories, including fields for brand (e.g., FIATALLIS, KOMATSU), part type, quality certification, and supplier details.
Generated: DETERMINISTIC_47e998067eb6058e
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL schema to store and manage high-quality machinery parts and accessories

-- Create a table to manage suppliers
CREATE TABLE Suppliers (
    SupplierID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for a supplier
    Name VARCHAR(255) NOT NULL,                -- Name of the supplier
    ContactEmail VARCHAR(255),                 -- Contact email for the supplier
    PhoneNumber VARCHAR(20),                   -- Contact phone number for the supplier
    Address TEXT,                              -- Address of the supplier
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the record was created
);

-- Create a table to manage quality certifications
CREATE TABLE QualityCertifications (
    CertificationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for a certification
    CertificationName VARCHAR(255) NOT NULL,        -- Name of the quality certification
    IssuedBy VARCHAR(255),                          -- Organization or authority that issued the certification
    ValidUntil DATE,                                -- Expiry date of the certification
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP   -- Timestamp for when the record was created
);

-- Create a table for machinery parts
CREATE TABLE MachineryParts (
    PartID INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for a machinery part
    BrandName VARCHAR(100) NOT NULL,               -- Brand name (e.g., FIATALLIS, KOMATSU)
    PartType VARCHAR(100) NOT NULL,                -- Type of the part
    SupplierID INT,                                -- Foreign key referencing Suppliers table
    CertificationID INT,                           -- Foreign key referencing QualityCertifications table
    Description TEXT,                              -- Description of the part
    Price DECIMAL(10, 2) NOT NULL,                 -- Price of the part
    Stock INT NOT NULL DEFAULT 0,                  -- Quantity of the part in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for the last update
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID)
        ON DELETE SET NULL ON UPDATE CASCADE,      -- Cascade updates and set to NULL on delete
    FOREIGN KEY (CertificationID) REFERENCES QualityCertifications(CertificationID)
        ON DELETE SET NULL ON UPDATE CASCADE       -- Cascade updates and set to NULL on delete
);

-- Indexes for faster lookups
CREATE INDEX idx_brand_part_type ON MachineryParts (BrandName, PartType);

-- End of schema
```
