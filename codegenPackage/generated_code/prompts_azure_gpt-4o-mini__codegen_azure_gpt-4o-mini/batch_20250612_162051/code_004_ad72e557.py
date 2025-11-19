"""
Generated Code Metadata:
========================
Original URL: https://perfectfoodcorner.com
Prompt: Construct a SQL database schema to store information about various food items, their dietary options, and packaging details, inspired by the menu structure of Perfect Food Corner.
Generated: DETERMINISTIC_ad72e5577a0d3489
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for Food Items, Dietary Options, and Packaging Details

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS DietaryOptions;
DROP TABLE IF EXISTS PackagingDetails;
DROP TABLE IF EXISTS FoodItems;

-- Table to store dietary options (e.g., Vegan, Gluten-Free, etc.)
CREATE TABLE DietaryOptions (
    id SERIAL PRIMARY KEY, -- Unique identifier for each dietary option
    name VARCHAR(100) NOT NULL UNIQUE, -- Name of the dietary option
    description TEXT -- Description of the dietary option
);

-- Table to store packaging details (e.g., Box, Bag, etc.)
CREATE TABLE PackagingDetails (
    id SERIAL PRIMARY KEY, -- Unique identifier for each packaging type
    type VARCHAR(100) NOT NULL UNIQUE, -- Type of packaging
    material VARCHAR(100), -- Material used for packaging
    dimensions VARCHAR(50) -- Dimensions of the packaging
);

-- Table to store food items
CREATE TABLE FoodItems (
    id SERIAL PRIMARY KEY, -- Unique identifier for each food item
    name VARCHAR(100) NOT NULL, -- Name of the food item
    description TEXT, -- Description of the food item
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0), -- Price of the food item
    dietary_option_id INT, -- Foreign key referencing DietaryOptions
    packaging_id INT, -- Foreign key referencing PackagingDetails
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (dietary_option_id) REFERENCES DietaryOptions(id) ON DELETE SET NULL, -- Handle deletion of dietary options
    FOREIGN KEY (packaging_id) REFERENCES PackagingDetails(id) ON DELETE SET NULL -- Handle deletion of packaging details
);

-- Sample data insertion for DietaryOptions
INSERT INTO DietaryOptions (name, description) VALUES
('Vegan', 'No animal products used.'),
('Gluten-Free', 'Contains no gluten.'),
('Nut-Free', 'Does not contain nuts.'),
('Organic', 'Made with organic ingredients.');

-- Sample data insertion for PackagingDetails
INSERT INTO PackagingDetails (type, material, dimensions) VALUES
('Box', 'Cardboard', '10x10x5 cm'),
('Bag', 'Plastic', '15x20 cm'),
('Container', 'Glass', '500 ml');

-- Sample data insertion for FoodItems
INSERT INTO FoodItems (name, description, price, dietary_option_id, packaging_id) VALUES
('Quinoa Salad', 'A healthy salad with quinoa and vegetables.', 8.99, 1, 1),
('Gluten-Free Pasta', 'Pasta made from gluten-free ingredients.', 7.49, 2, 1),
('Nut-Free Energy Bar', 'An energy bar without nuts.', 2.99, 3, 2),
('Organic Fruit Juice', 'Freshly squeezed organic fruit juice.', 3.49, 4, 3);
```
