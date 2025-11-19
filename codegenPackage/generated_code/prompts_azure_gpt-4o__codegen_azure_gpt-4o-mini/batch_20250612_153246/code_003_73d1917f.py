"""
Generated Code Metadata:
========================
Original URL: https://www.curativesurgicalindustry.com
Prompt: Develop a database schema for storing information about surgical instruments, including fields for product categories like "Amputating Knives," "Micro Scissors," and "Plaster Scissors," as outlined on the Curative Surgical Industry webpage.
Generated: DETERMINISTIC_73d1917ff81b90dc
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about surgical instruments

CREATE TABLE ProductCategories (
    id SERIAL PRIMARY KEY, -- Unique identifier for each product category
    name VARCHAR(255) NOT NULL UNIQUE, -- Name of the product category
    description TEXT, -- Description of the product category
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the category was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the category was last updated
);

CREATE TABLE SurgicalInstruments (
    id SERIAL PRIMARY KEY, -- Unique identifier for each surgical instrument
    name VARCHAR(255) NOT NULL, -- Name of the surgical instrument
    category_id INT NOT NULL, -- Foreign key referencing the product category
    manufacturer VARCHAR(255), -- Manufacturer of the surgical instrument
    model_number VARCHAR(255), -- Model number of the surgical instrument
    price DECIMAL(10, 2), -- Price of the surgical instrument
    stock_quantity INT DEFAULT 0, -- Quantity of the instrument in stock
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the instrument was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the instrument was last updated
    FOREIGN KEY (category_id) REFERENCES ProductCategories(id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Sample data insertion for product categories
INSERT INTO ProductCategories (name, description) VALUES
('Amputating Knives', 'Knives designed specifically for amputations.'),
('Micro Scissors', 'Scissors used for delicate surgical procedures.'),
('Plaster Scissors', 'Scissors designed for cutting plaster casts.');

-- Sample data insertion for surgical instruments
INSERT INTO SurgicalInstruments (name, category_id, manufacturer, model_number, price, stock_quantity) VALUES
('Amputation Knife Model A', 1, 'Surgical Co.', 'AK-001', 150.00, 10),
('Micro Scissors Model B', 2, 'Precision Tools', 'MS-002', 75.50, 20),
('Plaster Scissors Model C', 3, 'Cast Supplies', 'PS-003', 25.00, 50);
```
