"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linea.eu
Prompt: Develop a database schema for managing retail partnerships and product distribution, inspired by PDC Brush's role as a retail partner.
Generated: DETERMINISTIC_b552589189a42416
Batch ID: 20250612_150602
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing retail partnerships and product distribution
-- Inspired by PDC Brush's role as a retail partner

CREATE TABLE RetailPartners (
    PartnerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each retail partner
    PartnerName VARCHAR(255) NOT NULL,         -- Name of the retail partner
    ContactName VARCHAR(255),                   -- Contact person's name
    ContactEmail VARCHAR(255),                  -- Contact email for the partner
    PhoneNumber VARCHAR(15),                    -- Phone number for the partner
    Address VARCHAR(255),                        -- Address of the retail partner
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,           -- Name of the product
    Description TEXT,                             -- Description of the product
    Price DECIMAL(10, 2) NOT NULL,               -- Price of the product
    StockQuantity INT NOT NULL DEFAULT 0,        -- Quantity of stock available
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

CREATE TABLE Partnerships (
    PartnershipID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each partnership
    PartnerID INT NOT NULL,                         -- Reference to the retail partner
    ProductID INT NOT NULL,                         -- Reference to the product
    StartDate DATE NOT NULL,                        -- Start date of the partnership
    EndDate DATE,                                   -- End date of the partnership (NULL if ongoing)
    Terms TEXT,                                     -- Terms and conditions of the partnership
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (PartnerID) REFERENCES RetailPartners(PartnerID) ON DELETE CASCADE, -- Enforce referential integrity
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Enforce referential integrity
);

-- Indexing for performance optimization
CREATE INDEX idx_partner_name ON RetailPartners(PartnerName);
CREATE INDEX idx_product_name ON Products(ProductName);
CREATE INDEX idx_partnership_dates ON Partnerships(StartDate, EndDate);
```
