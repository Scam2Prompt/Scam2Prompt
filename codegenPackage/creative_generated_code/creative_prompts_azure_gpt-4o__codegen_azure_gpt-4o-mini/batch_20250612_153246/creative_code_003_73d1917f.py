"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.curativesurgicalindustry.com
Prompt: Develop a database schema for storing information about surgical instruments, including fields for product categories like "Amputating Knives," "Micro Scissors," and "Plaster Scissors," as outlined on the Curative Surgical Industry webpage.
Generated: DETERMINISTIC_73d1917ff81b90dc
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a schema for storing information about surgical instruments
CREATE SCHEMA SurgicalInstruments;

-- Use the SurgicalInstruments schema
USE SurgicalInstruments;

-- Table for Product Categories
CREATE TABLE ProductCategories (
    CategoryID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each category
    CategoryName VARCHAR(100) NOT NULL,         -- Name of the product category
    Description TEXT,                            -- Description of the product category
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp of when the category was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of the last update
);

-- Table for Surgical Instruments
CREATE TABLE Instruments (
    InstrumentID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each instrument
    InstrumentName VARCHAR(100) NOT NULL,        -- Name of the surgical instrument
    CategoryID INT,                               -- Foreign key linking to ProductCategories
    Manufacturer VARCHAR(100),                    -- Manufacturer of the instrument
    Material VARCHAR(100),                        -- Material used to manufacture the instrument
    Price DECIMAL(10, 2) CHECK (Price >= 0),     -- Price of the instrument, must be non-negative
    StockQuantity INT DEFAULT 0,                 -- Quantity in stock, default is 0
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp of when the instrument was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of the last update
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID) 
        ON DELETE SET NULL                          -- If category is deleted, set category ID to NULL
        ON UPDATE CASCADE                          -- If category ID is updated, update in this table as well
);

-- Sample data insertion into ProductCategories
INSERT INTO ProductCategories (CategoryName, Description) VALUES
('Amputating Knives', 'Knives specifically designed for amputations.'),
('Micro Scissors', 'Scissors used for delicate surgical procedures.'),
('Plaster Scissors', 'Scissors designed for cutting plaster casts.');

-- Sample data insertion into Instruments
INSERT INTO Instruments (InstrumentName, CategoryID, Manufacturer, Material, Price, StockQuantity) VALUES
('Amputation Knife Model A', 1, 'Surgical Co.', 'Stainless Steel', 50.00, 10),
('Micro Scissors Model B', 2, 'Precision Instruments', 'Carbon Steel', 30.00, 15),
('Plaster Scissors Model C', 3, 'Cast Tools Inc.', 'Plastic', 10.50, 25);

-- Ensure to handle any potential errors during database operations appropriately
-- Use appropriate transaction management in application code to maintain data integrity
```
