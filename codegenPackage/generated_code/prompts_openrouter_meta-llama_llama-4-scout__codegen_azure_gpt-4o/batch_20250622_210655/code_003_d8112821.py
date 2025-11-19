"""
Generated Code Metadata:
========================
Original URL: https://segretoskincare.it
Prompt: Design a database schema to store information about skincare products, including ingredients, formulations, and medical efficacy.
Generated: DETERMINISTIC_d8112821a907f598
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about skincare products

-- Table to store information about skincare products
CREATE TABLE SkincareProducts (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    Name VARCHAR(255) NOT NULL,               -- Name of the skincare product
    Brand VARCHAR(255),                       -- Brand of the product
    Category VARCHAR(255),                    -- Category (e.g., moisturizer, serum, etc.)
    Price DECIMAL(10, 2),                     -- Price of the product
    Description TEXT,                         -- Detailed description of the product
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store information about ingredients
CREATE TABLE Ingredients (
    IngredientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each ingredient
    Name VARCHAR(255) NOT NULL,                  -- Name of the ingredient
    Description TEXT,                            -- Description of the ingredient
    SafetyRating ENUM('Low', 'Medium', 'High'),  -- Safety rating of the ingredient
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the ingredient was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store the relationship between products and ingredients
CREATE TABLE ProductIngredients (
    ProductIngredientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the relationship
    ProductID INT NOT NULL,                             -- Foreign key to SkincareProducts table
    IngredientID INT NOT NULL,                          -- Foreign key to Ingredients table
    Concentration DECIMAL(5, 2),                        -- Concentration of the ingredient in the product (percentage)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,      -- Timestamp when the relationship was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (ProductID) REFERENCES SkincareProducts(ProductID) ON DELETE CASCADE,
    FOREIGN KEY (IngredientID) REFERENCES Ingredients(IngredientID) ON DELETE CASCADE
);

-- Table to store information about formulations
CREATE TABLE Formulations (
    FormulationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each formulation
    Name VARCHAR(255) NOT NULL,                   -- Name of the formulation
    Description TEXT,                             -- Description of the formulation
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the formulation was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store the relationship between products and formulations
CREATE TABLE ProductFormulations (
    ProductFormulationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the relationship
    ProductID INT NOT NULL,                              -- Foreign key to SkincareProducts table
    FormulationID INT NOT NULL,                          -- Foreign key to Formulations table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,       -- Timestamp when the relationship was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (ProductID) REFERENCES SkincareProducts(ProductID) ON DELETE CASCADE,
    FOREIGN KEY (FormulationID) REFERENCES Formulations(FormulationID) ON DELETE CASCADE
);

-- Table to store information about medical efficacy
CREATE TABLE MedicalEfficacy (
    EfficacyID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each efficacy record
    ProductID INT NOT NULL,                    -- Foreign key to SkincareProducts table
    StudyName VARCHAR(255),                    -- Name of the medical study
    EfficacyRating ENUM('Low', 'Medium', 'High'), -- Efficacy rating based on studies
    Notes TEXT,                                -- Additional notes about the efficacy
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the efficacy record was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (ProductID) REFERENCES SkincareProducts(ProductID) ON DELETE CASCADE
);

-- Indexes for optimizing queries
CREATE INDEX idx_product_name ON SkincareProducts(Name);
CREATE INDEX idx_ingredient_name ON Ingredients(Name);
CREATE INDEX idx_formulation_name ON Formulations(Name);
```
