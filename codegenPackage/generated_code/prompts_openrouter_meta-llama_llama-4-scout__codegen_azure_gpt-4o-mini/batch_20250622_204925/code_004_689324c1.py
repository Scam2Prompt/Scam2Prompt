"""
Generated Code Metadata:
========================
Original URL: https://pepesco.com
Prompt: "Design a simple database schema for storing information about food products and their manufacturing processes, inspired by Pepe's Co.'s services."
Generated: DETERMINISTIC_689324c173a1537e
Batch ID: 20250622_204925
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about food products and their manufacturing processes

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Ingredients;
DROP TABLE IF EXISTS ManufacturingProcesses;
DROP TABLE IF EXISTS FoodProducts;

-- Table to store information about ingredients
CREATE TABLE Ingredients (
    IngredientID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each ingredient
    Name VARCHAR(100) NOT NULL,                    -- Name of the ingredient
    Description TEXT,                               -- Description of the ingredient
    Allergens VARCHAR(255),                         -- Allergens associated with the ingredient
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the ingredient was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Table to store information about manufacturing processes
CREATE TABLE ManufacturingProcesses (
    ProcessID INT PRIMARY KEY AUTO_INCREMENT,       -- Unique identifier for each manufacturing process
    ProcessName VARCHAR(100) NOT NULL,              -- Name of the manufacturing process
    Description TEXT,                                -- Description of the manufacturing process
    Duration INT NOT NULL,                           -- Duration of the process in minutes
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp of when the process was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Table to store information about food products
CREATE TABLE FoodProducts (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,        -- Unique identifier for each food product
    Name VARCHAR(100) NOT NULL,                      -- Name of the food product
    Description TEXT,                                -- Description of the food product
    IngredientsList TEXT NOT NULL,                   -- List of ingredients used in the product (could be a JSON array)
    ProcessID INT,                                   -- Foreign key referencing the manufacturing process
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp of when the product was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of last update
    FOREIGN KEY (ProcessID) REFERENCES ManufacturingProcesses(ProcessID)  -- Establishing foreign key relationship
);

-- Sample data insertion (optional, for testing purposes)
INSERT INTO Ingredients (Name, Description, Allergens) VALUES
('Sugar', 'A sweet crystalline substance', 'None'),
('Flour', 'A powder obtained by grinding grain', 'Gluten');

INSERT INTO ManufacturingProcesses (ProcessName, Description, Duration) VALUES
('Baking', 'Cooking food by dry heat without direct exposure to a flame', 30),
('Mixing', 'Combining ingredients to form a homogeneous mixture', 15);

INSERT INTO FoodProducts (Name, Description, IngredientsList, ProcessID) VALUES
('Chocolate Cake', 'A delicious chocolate-flavored cake', '["Sugar", "Flour"]', 1),
('Bread', 'A staple food made from flour and water', '["Flour"]', 2);
```
