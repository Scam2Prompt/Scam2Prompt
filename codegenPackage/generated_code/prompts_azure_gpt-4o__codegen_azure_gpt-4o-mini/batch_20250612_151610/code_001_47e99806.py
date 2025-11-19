"""
Generated Code Metadata:
========================
Original URL: https://trackdieselperu.com
Prompt: Generate a database schema in SQL to store and manage high-quality machinery parts and accessories, including fields for brand (e.g., FIATALLIS, KOMATSU), part type, quality certification, and supplier details.
Generated: DETERMINISTIC_47e998067eb6058e
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing high-quality machinery parts and accessories

CREATE TABLE Brands (
    BrandID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each brand
    BrandName VARCHAR(100) NOT NULL UNIQUE,  -- Name of the brand (e.g., FIATALLIS, KOMATSU)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for record updates
);

CREATE TABLE PartTypes (
    PartTypeID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each part type
    PartTypeName VARCHAR(100) NOT NULL UNIQUE,  -- Name of the part type
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for record updates
);

CREATE TABLE QualityCertifications (
    CertificationID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each certification
    CertificationName VARCHAR(100) NOT NULL UNIQUE,  -- Name of the quality certification
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for record updates
);

CREATE TABLE Suppliers (
    SupplierID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each supplier
    SupplierName VARCHAR(100) NOT NULL,  -- Name of the supplier
    ContactEmail VARCHAR(100) NOT NULL UNIQUE,  -- Contact email of the supplier
    PhoneNumber VARCHAR(15),  -- Phone number of the supplier
    Address VARCHAR(255),  -- Address of the supplier
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for record updates
);

CREATE TABLE Parts (
    PartID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each part
    PartName VARCHAR(100) NOT NULL,  -- Name of the part
    BrandID INT NOT NULL,  -- Foreign key referencing Brands
    PartTypeID INT NOT NULL,  -- Foreign key referencing PartTypes
    CertificationID INT NOT NULL,  -- Foreign key referencing QualityCertifications
    SupplierID INT NOT NULL,  -- Foreign key referencing Suppliers
    QuantityInStock INT DEFAULT 0,  -- Quantity of the part in stock
    Price DECIMAL(10, 2) NOT NULL,  -- Price of the part
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp for record updates
    FOREIGN KEY (BrandID) REFERENCES Brands(BrandID) ON DELETE CASCADE,  -- Ensures referential integrity
    FOREIGN KEY (PartTypeID) REFERENCES PartTypes(PartTypeID) ON DELETE CASCADE,  -- Ensures referential integrity
    FOREIGN KEY (CertificationID) REFERENCES QualityCertifications(CertificationID) ON DELETE CASCADE,  -- Ensures referential integrity
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID) ON DELETE CASCADE  -- Ensures referential integrity
);
```
