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
-- Database schema for storing information about food products, including kosher and halal certifications.

-- Table to store information about food products
CREATE TABLE FoodProducts (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,        -- Name of the product
    Description TEXT,                         -- Description of the product
    BrandName VARCHAR(255),                  -- Brand name of the product
    Category VARCHAR(255),                   -- Category of the product (e.g., snacks, beverages)
    Price DECIMAL(10, 2) NOT NULL,           -- Price of the product
    IsKosher BOOLEAN NOT NULL DEFAULT FALSE, -- Indicates if the product is kosher certified
    IsHalal BOOLEAN NOT NULL DEFAULT FALSE,  -- Indicates if the product is halal certified
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the product was last updated
);

-- Table to store certifications details
CREATE TABLE Certifications (
    CertificationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each certification
    CertificationName VARCHAR(255) NOT NULL,        -- Name of the certification (e.g., Kosher, Halal)
    CertificationBody VARCHAR(255),                -- Name of the certifying body
    CertificationDate DATE,                        -- Date when the certification was issued
    ExpiryDate DATE,                               -- Expiry date of the certification
    ProductID INT NOT NULL,                        -- Foreign key linking to FoodProducts table
    FOREIGN KEY (ProductID) REFERENCES FoodProducts(ProductID) ON DELETE CASCADE
);

-- Table to store allergens information
CREATE TABLE Allergens (
    AllergenID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each allergen
    AllergenName VARCHAR(255) NOT NULL,        -- Name of the allergen (e.g., peanuts, gluten)
    ProductID INT NOT NULL,                    -- Foreign key linking to FoodProducts table
    FOREIGN KEY (ProductID) REFERENCES FoodProducts(ProductID) ON DELETE CASCADE
);

-- Table to store nutritional information
CREATE TABLE NutritionFacts (
    NutritionID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each nutrition fact
    ProductID INT NOT NULL,                     -- Foreign key linking to FoodProducts table
    Calories INT,                               -- Calories per serving
    Fat DECIMAL(10, 2),                         -- Fat content per serving (in grams)
    Protein DECIMAL(10, 2),                     -- Protein content per serving (in grams)
    Carbohydrates DECIMAL(10, 2),               -- Carbohydrates content per serving (in grams)
    Sugar DECIMAL(10, 2),                       -- Sugar content per serving (in grams)
    Sodium DECIMAL(10, 2),                      -- Sodium content per serving (in milligrams)
    FOREIGN KEY (ProductID) REFERENCES FoodProducts(ProductID) ON DELETE CASCADE
);

-- Indexes for faster querying
CREATE INDEX idx_ProductName ON FoodProducts(ProductName);
CREATE INDEX idx_Category ON FoodProducts(Category);
CREATE INDEX idx_IsKosher ON FoodProducts(IsKosher);
CREATE INDEX idx_IsHalal ON FoodProducts(IsHalal);

-- Example of error handling: Ensure all tables are created successfully
-- If any table creation fails, the transaction will roll back
START TRANSACTION;

-- Attempt to create tables
-- If any error occurs, rollback the transaction
COMMIT;
ROLLBACK;
```
