"""
Generated Code Metadata:
========================
Original URL: https://ristorantelafenice.ch
Prompt: Design a database schema to store information about restaurant menus, including tables for dishes, prices, and ingredients, inspired by the offerings at Ristorante La Fenice.
Generated: DETERMINISTIC_6ebd6d24896b8c52
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the restaurant menu
CREATE DATABASE RistoranteLaFenice;

-- Use the database
USE RistoranteLaFenice;

-- Create a table for ingredients
CREATE TABLE Ingredients (
    IngredientID INT AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    Unit VARCHAR(50) NOT NULL,
    PRIMARY KEY (IngredientID)
);

-- Create a table for dishes
CREATE TABLE Dishes (
    DishID INT AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    Description TEXT,
    PRIMARY KEY (DishID)
);

-- Create a table for dish ingredients
CREATE TABLE DishIngredients (
    DishID INT NOT NULL,
    IngredientID INT NOT NULL,
    Quantity DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (DishID, IngredientID),
    FOREIGN KEY (DishID) REFERENCES Dishes(DishID),
    FOREIGN KEY (IngredientID) REFERENCES Ingredients(IngredientID)
);

-- Create a table for prices
CREATE TABLE Prices (
    PriceID INT AUTO_INCREMENT,
    DishID INT NOT NULL,
    Price DECIMAL(10, 2) NOT NULL,
    EffectiveDate DATE NOT NULL,
    ExpirationDate DATE,
    PRIMARY KEY (PriceID),
    FOREIGN KEY (DishID) REFERENCES Dishes(DishID)
);

-- Create a table for menu sections
CREATE TABLE MenuSections (
    SectionID INT AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    Description TEXT,
    PRIMARY KEY (SectionID)
);

-- Create a table for dish menu sections
CREATE TABLE DishMenuSections (
    DishID INT NOT NULL,
    SectionID INT NOT NULL,
    PRIMARY KEY (DishID, SectionID),
    FOREIGN KEY (DishID) REFERENCES Dishes(DishID),
    FOREIGN KEY (SectionID) REFERENCES MenuSections(SectionID)
);

-- Insert sample data
INSERT INTO Ingredients (Name, Unit)
VALUES 
('Tomato', 'piece'),
('Mozzarella Cheese', 'slice'),
('Fresh Basil', 'leaf'),
('Extra Virgin Olive Oil', 'ml'),
('Garlic', 'clove');

INSERT INTO Dishes (Name, Description)
VALUES 
('Bruschetta', ' Toasted bread with fresh tomatoes and basil'),
('Margherita Pizza', 'Neapolitan-style pizza with tomato sauce, mozzarella, and basil');

INSERT INTO DishIngredients (DishID, IngredientID, Quantity)
VALUES 
(1, 1, 2.00),
(1, 3, 2.00),
(2, 1, 1.00),
(2, 2, 1.00),
(2, 3, 1.00);

INSERT INTO Prices (DishID, Price, EffectiveDate)
VALUES 
(1, 8.99, '2022-01-01'),
(2, 14.99, '2022-01-01');

INSERT INTO MenuSections (Name, Description)
VALUES 
('Appetizers', 'Light bites to start your meal'),
('Pizzas', 'Our signature pizzas');

INSERT INTO DishMenuSections (DishID, SectionID)
VALUES 
(1, 1),
(2, 2);
```
