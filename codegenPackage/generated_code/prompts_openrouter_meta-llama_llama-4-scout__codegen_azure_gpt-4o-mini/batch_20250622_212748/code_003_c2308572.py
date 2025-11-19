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
-- Database schema for Yobugo's products

-- Table to store product information
CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each product
    ProductName VARCHAR(255) NOT NULL,         -- Name of the product
    Description TEXT,                           -- Description of the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the product was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of the last update
);

-- Table to store ingredient information
CREATE TABLE Ingredients (
    IngredientID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each ingredient
    IngredientName VARCHAR(255) NOT NULL,         -- Name of the ingredient
    Allergen BOOLEAN DEFAULT FALSE,                -- Indicates if the ingredient is an allergen
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the ingredient was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of the last update
);

-- Table to store flavors
CREATE TABLE Flavors (
    FlavorID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each flavor
    FlavorName VARCHAR(255) NOT NULL,             -- Name of the flavor
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the flavor was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of the last update
);

-- Table to store packaging options
CREATE TABLE PackagingOptions (
    PackagingID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each packaging option
    PackagingType VARCHAR(255) NOT NULL,           -- Type of packaging (e.g., bottle, box)
    Size VARCHAR(50),                              -- Size of the packaging
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the packaging option was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of the last update
);

-- Junction table to associate products with their ingredients
CREATE TABLE ProductIngredients (
    ProductID INT,                                 -- Foreign key referencing Products
    IngredientID INT,                              -- Foreign key referencing Ingredients
    PRIMARY KEY (ProductID, IngredientID),        -- Composite primary key
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE,  -- Ensures referential integrity
    FOREIGN KEY (IngredientID) REFERENCES Ingredients(IngredientID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Junction table to associate products with their flavors
CREATE TABLE ProductFlavors (
    ProductID INT,                                 -- Foreign key referencing Products
    FlavorID INT,                                  -- Foreign key referencing Flavors
    PRIMARY KEY (ProductID, FlavorID),            -- Composite primary key
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE,  -- Ensures referential integrity
    FOREIGN KEY (FlavorID) REFERENCES Flavors(FlavorID) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Junction table to associate products with their packaging options
CREATE TABLE ProductPackaging (
    ProductID INT,                                 -- Foreign key referencing Products
    PackagingID INT,                               -- Foreign key referencing PackagingOptions
    PRIMARY KEY (ProductID, PackagingID),         -- Composite primary key
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE,  -- Ensures referential integrity
    FOREIGN KEY (PackagingID) REFERENCES PackagingOptions(PackagingID) ON DELETE CASCADE  -- Ensures referential integrity
);
```
