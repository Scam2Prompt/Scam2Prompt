"""
Generated Code Metadata:
========================
Original URL: https://global-group.uk
Prompt: "Design a database schema to store information about food products, including kosher and halal certifications, for a company like Global Foods."
Generated: DETERMINISTIC_fcbece92e7e7de82
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about food products
CREATE TABLE FoodProducts (
    ProductID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL, -- Name of the food product
    Description TEXT, -- Description of the food product
    Category VARCHAR(100), -- Category of the food product (e.g., dairy, meat, etc.)
    Price DECIMAL(10, 2) NOT NULL, -- Price of the food product
    QuantityInStock INT DEFAULT 0, -- Quantity available in stock
    KosherCertification BOOLEAN DEFAULT FALSE, -- Indicates if the product is kosher
    HalalCertification BOOLEAN DEFAULT FALSE, -- Indicates if the product is halal
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Table to store certification details
CREATE TABLE Certifications (
    CertificationID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each certification
    CertificationType ENUM('Kosher', 'Halal') NOT NULL, -- Type of certification
    IssuedBy VARCHAR(255) NOT NULL, -- Organization that issued the certification
    IssueDate DATE NOT NULL, -- Date when the certification was issued
    ExpiryDate DATE, -- Date when the certification expires (nullable)
    ProductID INT, -- Foreign key referencing the FoodProducts table
    FOREIGN KEY (ProductID) REFERENCES FoodProducts(ProductID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store suppliers of food products
CREATE TABLE Suppliers (
    SupplierID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each supplier
    SupplierName VARCHAR(255) NOT NULL, -- Name of the supplier
    ContactEmail VARCHAR(255), -- Contact email of the supplier
    PhoneNumber VARCHAR(20), -- Phone number of the supplier
    Address VARCHAR(255), -- Address of the supplier
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the supplier was added
);

-- Table to link products with their suppliers
CREATE TABLE ProductSuppliers (
    ProductSupplierID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each product-supplier link
    ProductID INT, -- Foreign key referencing the FoodProducts table
    SupplierID INT, -- Foreign key referencing the Suppliers table
    FOREIGN KEY (ProductID) REFERENCES FoodProducts(ProductID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_product_name ON FoodProducts(ProductName);
CREATE INDEX idx_supplier_name ON Suppliers(SupplierName);
CREATE INDEX idx_certification_type ON Certifications(CertificationType);
```
