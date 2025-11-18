"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thewallethub.com
Prompt: Generate SQL queries to manage a database for an online gifting store, including tables for "Vendor," "Collections," and "Product Profiles," inspired by https://thewallethub.com.
Generated: DETERMINISTIC_c3c1e5f122fb60bf
Batch ID: 20250612_154351
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL script to manage the database for an online gifting store

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS ProductProfiles CASCADE;
DROP TABLE IF EXISTS Collections CASCADE;
DROP TABLE IF EXISTS Vendors CASCADE;

-- Create table for Vendors
CREATE TABLE Vendors (
    VendorID SERIAL PRIMARY KEY,               -- Unique identifier for each vendor
    VendorName VARCHAR(255) NOT NULL,         -- Name of the vendor
    ContactEmail VARCHAR(255) UNIQUE NOT NULL, -- Vendor's contact email
    PhoneNumber VARCHAR(20),                   -- Vendor's contact phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Create table for Collections
CREATE TABLE Collections (
    CollectionID SERIAL PRIMARY KEY,           -- Unique identifier for each collection
    CollectionName VARCHAR(255) NOT NULL,     -- Name of the collection
    Description TEXT,                          -- Description of the collection
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last update timestamp
);

-- Create table for Product Profiles
CREATE TABLE ProductProfiles (
    ProductID SERIAL PRIMARY KEY,              -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,        -- Name of the product
    Description TEXT,                          -- Description of the product
    Price DECIMAL(10, 2) NOT NULL CHECK (Price >= 0), -- Product price with a non-negative constraint
    QuantityAvailable INT NOT NULL CHECK (QuantityAvailable >= 0), -- Available stock count
    VendorID INT NOT NULL,                     -- Foreign key referencing Vendors
    CollectionID INT,                          -- Foreign key referencing Collections (optional)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last update timestamp
    FOREIGN KEY (VendorID) REFERENCES Vendors(VendorID) ON DELETE CASCADE, -- Ensure integrity on vendor deletion
    FOREIGN KEY (CollectionID) REFERENCES Collections(CollectionID) ON DELETE SET NULL -- Set to NULL if collection deleted
);

-- Insert sample data into Vendors
INSERT INTO Vendors (VendorName, ContactEmail, PhoneNumber) VALUES
('Gifts Galore', 'info@giftsgalore.com', '123-456-7890'),
('Happy Moments', 'contact@happymoments.com', '098-765-4321');

-- Insert sample data into Collections
INSERT INTO Collections (CollectionName, Description) VALUES
('Birthday Gifts', 'A collection of gifts suitable for birthdays'),
('Anniversary Specials', 'Unique gifts to celebrate love and togetherness');

-- Insert sample data into Product Profiles
INSERT INTO ProductProfiles (ProductName, Description, Price, QuantityAvailable, VendorID, CollectionID) VALUES
('Teddy Bear', 'A soft teddy bear', 19.99, 100, 1, 1),
('Chocolate Box', 'Assorted chocolates', 29.99, 50, 2, 1),
('Personalized Mug', 'A mug with a custom message', 15.99, 200, 1, NULL);

-- Query to retrieve all products with their vendor and collection information
SELECT 
    pp.ProductID,
    pp.ProductName,
    pp.Description,
    pp.Price,
    pp.QuantityAvailable,
    v.VendorName,
    c.CollectionName
FROM 
    ProductProfiles pp
LEFT JOIN 
    Vendors v ON pp.VendorID = v.VendorID
LEFT JOIN 
    Collections c ON pp.CollectionID = c.CollectionID;

-- Ensure to handle potential errors during database operations by checking
-- for unique constraints, foreign key constraints, and data types.
```
