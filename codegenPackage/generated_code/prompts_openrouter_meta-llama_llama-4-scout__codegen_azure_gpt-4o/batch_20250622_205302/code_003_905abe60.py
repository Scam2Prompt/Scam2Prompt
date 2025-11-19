"""
Generated Code Metadata:
========================
Original URL: https://regency-towel.com
Prompt: Design a database schema to store information about different types of cotton used in textile production, including carded, combed, Egyptian, Turkish, and American cotton, as mentioned in Regency Towel's product range.
Generated: DETERMINISTIC_905abe60147f182c
Batch ID: 20250622_205302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema to store information about different types of cotton used in textile production

-- Create a table to store cotton types
CREATE TABLE CottonTypes (
    CottonID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each cotton type
    Name VARCHAR(50) NOT NULL,               -- Name of the cotton type (e.g., Carded, Combed, Egyptian, etc.)
    Description TEXT,                        -- Detailed description of the cotton type
    Origin VARCHAR(50),                      -- Country or region of origin (e.g., Egypt, Turkey, USA)
    QualityRating INT CHECK (QualityRating BETWEEN 1 AND 10), -- Quality rating (1-10 scale)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the record was last updated
);

-- Create a table to store additional attributes or properties of cotton types
CREATE TABLE CottonProperties (
    PropertyID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each property
    CottonID INT NOT NULL,                     -- Foreign key referencing CottonTypes
    PropertyName VARCHAR(50) NOT NULL,         -- Name of the property (e.g., Fiber Length, Softness, etc.)
    PropertyValue VARCHAR(100),                -- Value of the property (e.g., "Long", "Extra Soft", etc.)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the record was last updated
    FOREIGN KEY (CottonID) REFERENCES CottonTypes(CottonID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to store suppliers or manufacturers of cotton
CREATE TABLE CottonSuppliers (
    SupplierID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each supplier
    Name VARCHAR(100) NOT NULL,                -- Name of the supplier or manufacturer
    ContactInfo TEXT,                          -- Contact information (e.g., phone, email, address)
    Country VARCHAR(50),                       -- Country of the supplier
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the record was last updated
);

-- Create a table to link cotton types to suppliers
CREATE TABLE CottonSupplierLinks (
    LinkID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each link
    CottonID INT NOT NULL,                 -- Foreign key referencing CottonTypes
    SupplierID INT NOT NULL,               -- Foreign key referencing CottonSuppliers
    SupplyVolume INT,                      -- Volume of cotton supplied (e.g., in kilograms)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the record was last updated
    FOREIGN KEY (CottonID) REFERENCES CottonTypes(CottonID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (SupplierID) REFERENCES CottonSuppliers(SupplierID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Example indexes for optimizing queries
CREATE INDEX idx_cotton_name ON CottonTypes(Name); -- Index for quick lookup by cotton name
CREATE INDEX idx_supplier_name ON CottonSuppliers(Name); -- Index for quick lookup by supplier name
```
