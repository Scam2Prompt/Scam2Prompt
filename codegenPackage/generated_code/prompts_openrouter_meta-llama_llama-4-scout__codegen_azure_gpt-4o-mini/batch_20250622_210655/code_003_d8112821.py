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

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Ingredients;
DROP TABLE IF EXISTS Formulations;
DROP TABLE IF EXISTS Products;
DROP TABLE IF EXISTS Efficacy;

-- Table to store information about ingredients
CREATE TABLE Ingredients (
    ingredient_id SERIAL PRIMARY KEY, -- Unique identifier for each ingredient
    name VARCHAR(255) NOT NULL,        -- Name of the ingredient
    description TEXT,                   -- Description of the ingredient
    is_active BOOLEAN DEFAULT TRUE      -- Indicates if the ingredient is active
);

-- Table to store information about formulations
CREATE TABLE Formulations (
    formulation_id SERIAL PRIMARY KEY,  -- Unique identifier for each formulation
    name VARCHAR(255) NOT NULL,         -- Name of the formulation
    type VARCHAR(100) NOT NULL,         -- Type of formulation (e.g., cream, serum)
    description TEXT                    -- Description of the formulation
);

-- Table to store information about skincare products
CREATE TABLE Products (
    product_id SERIAL PRIMARY KEY,      -- Unique identifier for each product
    name VARCHAR(255) NOT NULL,         -- Name of the product
    brand VARCHAR(255) NOT NULL,        -- Brand of the product
    formulation_id INT NOT NULL,        -- Foreign key referencing Formulations
    price DECIMAL(10, 2) NOT NULL,      -- Price of the product
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of product creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (formulation_id) REFERENCES Formulations(formulation_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store information about medical efficacy of products
CREATE TABLE Efficacy (
    efficacy_id SERIAL PRIMARY KEY,      -- Unique identifier for each efficacy record
    product_id INT NOT NULL,             -- Foreign key referencing Products
    claim VARCHAR(255) NOT NULL,         -- Claim of efficacy (e.g., anti-aging, moisturizing)
    evidence TEXT,                       -- Evidence supporting the claim
    FOREIGN KEY (product_id) REFERENCES Products(product_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for faster querying
CREATE INDEX idx_product_name ON Products(name);
CREATE INDEX idx_ingredient_name ON Ingredients(name);
CREATE INDEX idx_formulation_name ON Formulations(name);
CREATE INDEX idx_efficacy_claim ON Efficacy(claim);
```
