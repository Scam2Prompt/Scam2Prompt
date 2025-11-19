"""
Generated Code Metadata:
========================
Original URL: https://magicenen-nfts.blogspot.com
Prompt: Design a database schema to store shoe products with attributes like name, price, brand, category, and payment options (e.g., 3x, 5x, 7x installments), inspired by the content of https://magicenen-nfts.blogspot.com.
Generated: DETERMINISTIC_d628ab41dd0cb2ae
Batch ID: 20250622_205007
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing shoe products

-- Table to store shoe brands
CREATE TABLE Brands (
    BrandID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each brand
    Name VARCHAR(100) NOT NULL,             -- Name of the brand
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store shoe categories
CREATE TABLE Categories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    Name VARCHAR(100) NOT NULL,                -- Name of the category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store payment options
CREATE TABLE PaymentOptions (
    PaymentOptionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each payment option
    Installments INT NOT NULL,                      -- Number of installments (e.g., 3, 5, 7)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store shoe products
CREATE TABLE Shoes (
    ShoeID INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for each shoe product
    Name VARCHAR(255) NOT NULL,                    -- Name of the shoe product
    Price DECIMAL(10, 2) NOT NULL,                 -- Price of the shoe product
    BrandID INT NOT NULL,                          -- Foreign key referencing the Brands table
    CategoryID INT NOT NULL,                       -- Foreign key referencing the Categories table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    FOREIGN KEY (BrandID) REFERENCES Brands(BrandID) ON DELETE CASCADE, -- Cascade delete for brand
    FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID) ON DELETE CASCADE -- Cascade delete for category
);

-- Table to associate shoes with payment options
CREATE TABLE ShoePaymentOptions (
    ShoeID INT NOT NULL,                           -- Foreign key referencing the Shoes table
    PaymentOptionID INT NOT NULL,                  -- Foreign key referencing the PaymentOptions table
    PRIMARY KEY (ShoeID, PaymentOptionID),         -- Composite primary key
    FOREIGN KEY (ShoeID) REFERENCES Shoes(ShoeID) ON DELETE CASCADE, -- Cascade delete for shoe
    FOREIGN KEY (PaymentOptionID) REFERENCES PaymentOptions(PaymentOptionID) ON DELETE CASCADE -- Cascade delete for payment option
);

-- Indexes for faster queries
CREATE INDEX idx_shoes_brand ON Shoes (BrandID);
CREATE INDEX idx_shoes_category ON Shoes (CategoryID);
CREATE INDEX idx_shoe_payment_options ON ShoePaymentOptions (PaymentOptionID);
```
