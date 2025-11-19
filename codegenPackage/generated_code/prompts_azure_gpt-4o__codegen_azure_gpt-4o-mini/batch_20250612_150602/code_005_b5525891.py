"""
Generated Code Metadata:
========================
Original URL: https://linea.eu
Prompt: Develop a database schema for managing retail partnerships and product distribution, inspired by PDC Brush's role as a retail partner.
Generated: DETERMINISTIC_b552589189a42416
Batch ID: 20250612_150602
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing retail partnerships and product distribution

-- Create a table for Retail Partners
CREATE TABLE RetailPartners (
    PartnerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each retail partner
    PartnerName VARCHAR(255) NOT NULL,         -- Name of the retail partner
    ContactEmail VARCHAR(255) UNIQUE NOT NULL, -- Contact email for the retail partner
    PhoneNumber VARCHAR(15),                    -- Phone number for the retail partner
    Address VARCHAR(255),                       -- Address of the retail partner
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the partner was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table for Products
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,          -- Name of the product
    Description TEXT,                            -- Description of the product
    Price DECIMAL(10, 2) NOT NULL,              -- Price of the product
    StockQuantity INT NOT NULL DEFAULT 0,       -- Quantity of the product in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table for Product Distribution
CREATE TABLE ProductDistribution (
    DistributionID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each distribution record
    PartnerID INT NOT NULL,                         -- Foreign key referencing RetailPartners
    ProductID INT NOT NULL,                         -- Foreign key referencing Products
    DistributionDate DATE NOT NULL,                 -- Date of distribution
    QuantityDistributed INT NOT NULL,               -- Quantity of product distributed
    FOREIGN KEY (PartnerID) REFERENCES RetailPartners(PartnerID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE, -- Ensures referential integrity
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the distribution record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table for Sales Records
CREATE TABLE SalesRecords (
    SaleID INT PRIMARY KEY AUTO_INCREMENT,         -- Unique identifier for each sale
    PartnerID INT NOT NULL,                        -- Foreign key referencing RetailPartners
    ProductID INT NOT NULL,                        -- Foreign key referencing Products
    SaleDate DATE NOT NULL,                        -- Date of the sale
    QuantitySold INT NOT NULL,                     -- Quantity of product sold
    SaleAmount DECIMAL(10, 2) NOT NULL,           -- Total sale amount
    FOREIGN KEY (PartnerID) REFERENCES RetailPartners(PartnerID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE, -- Ensures referential integrity
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the sale record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table for Product Reviews
CREATE TABLE ProductReviews (
    ReviewID INT PRIMARY KEY AUTO_INCREMENT,       -- Unique identifier for each review
    ProductID INT NOT NULL,                        -- Foreign key referencing Products
    PartnerID INT NOT NULL,                        -- Foreign key referencing RetailPartners
    ReviewText TEXT NOT NULL,                      -- Text of the review
    Rating INT CHECK (Rating BETWEEN 1 AND 5),    -- Rating out of 5
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the review was created
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (PartnerID) REFERENCES RetailPartners(PartnerID) ON DELETE CASCADE -- Ensures referential integrity
);
```
