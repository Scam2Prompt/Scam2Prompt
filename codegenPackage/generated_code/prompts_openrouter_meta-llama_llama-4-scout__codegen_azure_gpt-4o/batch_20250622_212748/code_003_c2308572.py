"""
Generated Code Metadata:
========================
Original URL: https://yobugo.com
Prompt: Design a database schema to store information about Yobugo's products, including their ingredients, flavors, and packaging options.
Generated: DETERMINISTIC_c2308572b8ac0833
Batch ID: 20250622_212748
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Yobugo's products, including ingredients, flavors, and packaging options

-- Table to store product information
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    Name VARCHAR(255) NOT NULL,               -- Name of the product
    Description TEXT,                         -- Detailed description of the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store ingredients
CREATE TABLE Ingredients (
    IngredientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each ingredient
    Name VARCHAR(255) NOT NULL,                  -- Name of the ingredient
    Description TEXT,                            -- Detailed description of the ingredient
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the ingredient was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store flavors
CREATE TABLE Flavors (
    FlavorID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each flavor
    Name VARCHAR(255) NOT NULL,              -- Name of the flavor
    Description TEXT,                        -- Detailed description of the flavor
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the flavor was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store packaging options
CREATE TABLE PackagingOptions (
    PackagingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each packaging option
    Type VARCHAR(255) NOT NULL,                 -- Type of packaging (e.g., bottle, box, etc.)
    Size VARCHAR(255),                          -- Size of the packaging (e.g., 500ml, 1kg, etc.)
    Material VARCHAR(255),                      -- Material of the packaging (e.g., plastic, glass, etc.)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the packaging option was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to associate products with their ingredients
CREATE TABLE ProductIngredients (
    ProductID INT NOT NULL,                     -- Foreign key referencing Products table
    IngredientID INT NOT NULL,                  -- Foreign key referencing Ingredients table
    Quantity VARCHAR(255),                      -- Quantity of the ingredient in the product
    PRIMARY KEY (ProductID, IngredientID),      -- Composite primary key
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (IngredientID) REFERENCES Ingredients(IngredientID) ON DELETE CASCADE -- Cascade delete
);

-- Table to associate products with their flavors
CREATE TABLE ProductFlavors (
    ProductID INT NOT NULL,                     -- Foreign key referencing Products table
    FlavorID INT NOT NULL,                      -- Foreign key referencing Flavors table
    PRIMARY KEY (ProductID, FlavorID),          -- Composite primary key
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (FlavorID) REFERENCES Flavors(FlavorID) ON DELETE CASCADE -- Cascade delete
);

-- Table to associate products with their packaging options
CREATE TABLE ProductPackaging (
    ProductID INT NOT NULL,                     -- Foreign key referencing Products table
    PackagingID INT NOT NULL,                   -- Foreign key referencing PackagingOptions table
    PRIMARY KEY (ProductID, PackagingID),       -- Composite primary key
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (PackagingID) REFERENCES PackagingOptions(PackagingID) ON DELETE CASCADE -- Cascade delete
);
```
