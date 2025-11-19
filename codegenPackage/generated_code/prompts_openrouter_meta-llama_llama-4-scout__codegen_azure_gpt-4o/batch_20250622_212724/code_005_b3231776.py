"""
Generated Code Metadata:
========================
Original URL: https://batteryaustralia.com.au
Prompt: Design a simple database schema to store information about different battery products, including their specifications, prices, and applications, based on the structure of Battery Australia's online catalog.
Generated: DETERMINISTIC_b3231776da447acf
Batch ID: 20250622_212724
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing battery product information

-- Create a table to store battery categories
CREATE TABLE BatteryCategories (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    CategoryName VARCHAR(255) NOT NULL,        -- Name of the category (e.g., "Car Batteries", "Solar Batteries")
    Description TEXT                           -- Optional description of the category
);

-- Create a table to store battery products
CREATE TABLE BatteryProducts (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,         -- Name of the battery product
    CategoryID INT NOT NULL,                   -- Foreign key linking to BatteryCategories
    Price DECIMAL(10, 2) NOT NULL,             -- Price of the battery product
    StockQuantity INT NOT NULL DEFAULT 0,      -- Quantity available in stock
    Manufacturer VARCHAR(255),                 -- Manufacturer of the battery
    WarrantyPeriod INT,                        -- Warranty period in months
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (CategoryID) REFERENCES BatteryCategories(CategoryID) ON DELETE CASCADE
);

-- Create a table to store battery specifications
CREATE TABLE BatterySpecifications (
    SpecificationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each specification
    ProductID INT NOT NULL,                         -- Foreign key linking to BatteryProducts
    Voltage DECIMAL(5, 2) NOT NULL,                 -- Voltage of the battery (e.g., 12.00V)
    Capacity DECIMAL(10, 2) NOT NULL,               -- Capacity of the battery in Ah (Ampere-hours)
    Dimensions VARCHAR(255),                        -- Dimensions of the battery (e.g., "200x150x100 mm")
    Weight DECIMAL(10, 2),                          -- Weight of the battery in kilograms
    TerminalType VARCHAR(255),                      -- Type of terminal (e.g., "Flat", "Round")
    FOREIGN KEY (ProductID) REFERENCES BatteryProducts(ProductID) ON DELETE CASCADE
);

-- Create a table to store battery applications
CREATE TABLE BatteryApplications (
    ApplicationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each application
    ProductID INT NOT NULL,                       -- Foreign key linking to BatteryProducts
    ApplicationName VARCHAR(255) NOT NULL,        -- Name of the application (e.g., "Automotive", "Marine", "Solar")
    Description TEXT,                             -- Optional description of the application
    FOREIGN KEY (ProductID) REFERENCES BatteryProducts(ProductID) ON DELETE CASCADE
);

-- Create a table to store customer reviews for battery products
CREATE TABLE CustomerReviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each review
    ProductID INT NOT NULL,                      -- Foreign key linking to BatteryProducts
    CustomerName VARCHAR(255),                   -- Name of the customer
    Rating INT CHECK (Rating BETWEEN 1 AND 5),   -- Rating given by the customer (1 to 5)
    ReviewText TEXT,                             -- Optional review text
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the review was added
    FOREIGN KEY (ProductID) REFERENCES BatteryProducts(ProductID) ON DELETE CASCADE
);

-- Indexes for optimizing queries
CREATE INDEX idx_category_name ON BatteryCategories(CategoryName);
CREATE INDEX idx_product_name ON BatteryProducts(ProductName);
CREATE INDEX idx_application_name ON BatteryApplications(ApplicationName);
```
