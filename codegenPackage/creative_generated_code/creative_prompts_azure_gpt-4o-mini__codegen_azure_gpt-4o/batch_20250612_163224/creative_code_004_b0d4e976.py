"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jgtcom.com
Prompt: Design a database schema for an online store that includes tables for premium fabrics and customer reviews, based on JGT's product categories.
Generated: DETERMINISTIC_b0d4e97685b05445
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Online Store

-- Table: PremiumFabrics
-- This table stores information about premium fabric products.
CREATE TABLE PremiumFabrics (
    FabricID INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each fabric
    Name VARCHAR(255) NOT NULL,                     -- Name of the fabric
    Description TEXT,                               -- Detailed description of the fabric
    Category VARCHAR(100) NOT NULL,                 -- Product category (e.g., cotton, silk, wool)
    Price DECIMAL(10, 2) NOT NULL,                  -- Price of the fabric
    Stock INT NOT NULL,                             -- Quantity available in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp when the fabric entry was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP   -- Timestamp when the fabric entry was last updated
        ON UPDATE CURRENT_TIMESTAMP
);

-- Table: Customers
-- This table stores information about the customers.
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY,      -- Unique identifier for each customer
    FirstName VARCHAR(100) NOT NULL,                -- First name of the customer
    LastName VARCHAR(100) NOT NULL,                 -- Last name of the customer
    Email VARCHAR(255) UNIQUE NOT NULL,             -- Email address of the customer (must be unique)
    PhoneNumber VARCHAR(20),                        -- Contact number of the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp when the customer was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP   -- Timestamp when customer details were last updated
        ON UPDATE CURRENT_TIMESTAMP
);

-- Table: CustomerReviews
-- This table stores reviews provided by customers for premium fabrics.
CREATE TABLE CustomerReviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each review
    FabricID INT NOT NULL,                          -- Foreign key referencing PremiumFabrics(FabricID)
    CustomerID INT NOT NULL,                        -- Foreign key referencing Customers(CustomerID)
    Rating INT CHECK (Rating BETWEEN 1 AND 5),      -- Rating (1 to 5 stars)
    ReviewText TEXT,                                -- Text content of the review
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp when the review was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP   -- Timestamp when the review was last updated
        ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (FabricID) REFERENCES PremiumFabrics(FabricID) ON DELETE CASCADE,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE
);

-- Best practices:
-- 1. Applied normalization principles to structure data.
-- 2. Used foreign keys for relationships between tables.
-- 3. Added timestamps for auditing changes.
-- 4. Included CHECK constraint for review ratings to ensure valid data.

-- Error handling:
-- Ensure the database handles constraints such as unique emails and cascading deletes 
-- for dependent records in linked tables.
```
