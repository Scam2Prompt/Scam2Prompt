"""
Generated Code Metadata:
========================
Original URL: https://bllabs.co
Prompt: "Design a database schema to store information about research peptides, bioregulators, and small molecules, including product details, pricing, and shipping information for a supplier like BioLongevity Labs."
Generated: DETERMINISTIC_b8284ab93e194dd8
Batch ID: 20250622_212712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about research peptides, bioregulators, and small molecules
-- including product details, pricing, and shipping information for a supplier like BioLongevity Labs.

-- Create a table to store product categories
CREATE TABLE ProductCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    CategoryName VARCHAR(255) NOT NULL,        -- Name of the category (e.g., Peptides, Bioregulators, Small Molecules)
    Description TEXT                           -- Optional description of the category
);

-- Create a table to store product details
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,         -- Name of the product
    CategoryID INT NOT NULL,                   -- Foreign key linking to ProductCategories
    Description TEXT,                          -- Detailed description of the product
    MolecularFormula VARCHAR(255),            -- Molecular formula of the product
    MolecularWeight DECIMAL(10, 4),           -- Molecular weight of the product
    CASNumber VARCHAR(50),                    -- CAS number for the product
    StockQuantity INT DEFAULT 0,              -- Quantity available in stock
    IsActive BOOLEAN DEFAULT TRUE,            -- Flag to indicate if the product is active
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID) ON DELETE CASCADE
);

-- Create a table to store pricing information
CREATE TABLE Pricing (
    PricingID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each pricing entry
    ProductID INT NOT NULL,                    -- Foreign key linking to Products
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the product
    Currency VARCHAR(10) DEFAULT 'USD',        -- Currency of the price
    Discount DECIMAL(5, 2) DEFAULT 0.00,       -- Discount percentage (if applicable)
    EffectiveDate DATE NOT NULL,               -- Date when the pricing becomes effective
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);

-- Create a table to store shipping information
CREATE TABLE ShippingInfo (
    ShippingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each shipping entry
    ProductID INT NOT NULL,                    -- Foreign key linking to Products
    ShippingMethod VARCHAR(255) NOT NULL,      -- Shipping method (e.g., Standard, Express)
    ShippingCost DECIMAL(10, 2) NOT NULL,      -- Cost of shipping
    EstimatedDeliveryDays INT NOT NULL,        -- Estimated delivery time in days
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
);

-- Create a table to store supplier information
CREATE TABLE Suppliers (
    SupplierID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each supplier
    SupplierName VARCHAR(255) NOT NULL,        -- Name of the supplier
    ContactEmail VARCHAR(255),                 -- Contact email for the supplier
    ContactPhone VARCHAR(50),                  -- Contact phone number for the supplier
    Address TEXT,                              -- Address of the supplier
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the supplier was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table to associate products with suppliers
CREATE TABLE ProductSuppliers (
    ProductSupplierID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each association
    ProductID INT NOT NULL,                           -- Foreign key linking to Products
    SupplierID INT NOT NULL,                          -- Foreign key linking to Suppliers
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE,
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID) ON DELETE CASCADE
);

-- Create indexes for faster querying
CREATE INDEX idx_product_category ON Products(CategoryID);
CREATE INDEX idx_pricing_product ON Pricing(ProductID);
CREATE INDEX idx_shipping_product ON ShippingInfo(ProductID);
CREATE INDEX idx_product_supplier ON ProductSuppliers(ProductID, SupplierID);
```
