"""
Generated Code Metadata:
========================
Original URL: https://rawcakesandcandy.ro
Prompt: "Design a database schema to store information about raw vegan desserts, including cakes, pastries, and their ingredients, as seen on the Raw Cakes And Candy website."
Generated: DETERMINISTIC_523e60bab3f4ff9a
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about raw vegan desserts

CREATE DATABASE RawVeganDesserts;

USE RawVeganDesserts;

-- Table to store dessert categories (e.g., cakes, pastries)
CREATE TABLE DessertCategories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table to store desserts
CREATE TABLE Desserts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    category_id INT NOT NULL,
    description TEXT,
    preparation_time INT, -- in minutes
    serving_size INT, -- number of servings
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES DessertCategories(id) ON DELETE CASCADE
);

-- Table to store ingredients
CREATE TABLE Ingredients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table to link desserts and their ingredients (many-to-many relationship)
CREATE TABLE DessertIngredients (
    dessert_id INT NOT NULL,
    ingredient_id INT NOT NULL,
    quantity VARCHAR(50), -- e.g., "1 cup", "2 tbsp"
    PRIMARY KEY (dessert_id, ingredient_id),
    FOREIGN KEY (dessert_id) REFERENCES Desserts(id) ON DELETE CASCADE,
    FOREIGN KEY (ingredient_id) REFERENCES Ingredients(id) ON DELETE CASCADE
);

-- Table to store nutritional information for each dessert
CREATE TABLE NutritionalInfo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    dessert_id INT NOT NULL,
    calories INT,
    fat DECIMAL(5, 2), -- in grams
    carbohydrates DECIMAL(5, 2), -- in grams
    protein DECIMAL(5, 2), -- in grams
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (dessert_id) REFERENCES Desserts(id) ON DELETE CASCADE
);

-- Sample data insertion for categories
INSERT INTO DessertCategories (name, description) VALUES
('Cakes', 'Delicious raw vegan cakes made from natural ingredients.'),
('Pastries', 'Tasty raw vegan pastries for a delightful treat.');

-- Sample data insertion for ingredients
INSERT INTO Ingredients (name, description) VALUES
('Almonds', 'Raw almonds, a great source of protein and healthy fats.'),
('Coconut Oil', 'Organic coconut oil, used for its rich flavor and health benefits.'),
('Dates', 'Natural sweetener and binder for raw desserts.'),
('Cacao Powder', 'Raw cacao powder for a rich chocolate flavor.');

-- Sample data insertion for desserts
INSERT INTO Desserts (name, category_id, description, preparation_time, serving_size) VALUES
('Raw Chocolate Cake', 1, 'A rich and decadent raw chocolate cake.', 30, 8),
('Raw Berry Tart', 2, 'A refreshing tart filled with seasonal berries.', 25, 6);

-- Sample data insertion for dessert ingredients
INSERT INTO DessertIngredients (dessert_id, ingredient_id, quantity) VALUES
(1, 1, '2 cups'),
(1, 3, '1 cup'),
(1, 4, '1/2 cup'),
(2, 1, '1 cup'),
(2, 3, '1/2 cup');

-- Sample data insertion for nutritional information
INSERT INTO NutritionalInfo (dessert_id, calories, fat, carbohydrates, protein) VALUES
(1, 350, 20.00, 30.00, 5.00),
(2, 250, 15.00, 20.00, 4.00);
```
