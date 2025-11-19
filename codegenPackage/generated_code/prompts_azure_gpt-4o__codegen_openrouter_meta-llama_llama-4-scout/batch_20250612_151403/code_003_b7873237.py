"""
Generated Code Metadata:
========================
Original URL: https://gala-games-ezx.blogspot.com
Prompt: Create a database schema in SQL for storing tool information, including fields for "brand," "price," "category," and "availability," inspired by the Anhanguera Ferramentas catalog.
Generated: DETERMINISTIC_b7873237fd7f1ef8
Batch ID: 20250612_151403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for storing tool information
CREATE DATABASE IF NOT EXISTS anhanguera_ferramentas;

-- Use the created database
USE anhanguera_ferramentas;

-- Create a table for tool categories
CREATE TABLE IF NOT EXISTS tool_categories (
  category_id INT AUTO_INCREMENT,
  category_name VARCHAR(255) NOT NULL,
  PRIMARY KEY (category_id),
  UNIQUE KEY (category_name)
);

-- Create a table for tool brands
CREATE TABLE IF NOT EXISTS tool_brands (
  brand_id INT AUTO_INCREMENT,
  brand_name VARCHAR(255) NOT NULL,
  PRIMARY KEY (brand_id),
  UNIQUE KEY (brand_name)
);

-- Create a table for tool information
CREATE TABLE IF NOT EXISTS tools (
  tool_id INT AUTO_INCREMENT,
  brand_id INT NOT NULL,
  tool_name VARCHAR(255) NOT NULL,
  price DECIMAL(10, 2) NOT NULL,
  category_id INT NOT NULL,
  availability BOOLEAN NOT NULL DEFAULT TRUE,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (tool_id),
  FOREIGN KEY (brand_id) REFERENCES tool_brands(brand_id) ON DELETE RESTRICT,
  FOREIGN KEY (category_id) REFERENCES tool_categories(category_id) ON DELETE RESTRICT
);

-- Create indexes for better query performance
CREATE INDEX idx_tool_brands_brand_name ON tool_brands (brand_name);
CREATE INDEX idx_tool_categories_category_name ON tool_categories (category_name);
CREATE INDEX idx_tools_brand_id ON tools (brand_id);
CREATE INDEX idx_tools_category_id ON tools (category_id);

-- Example data for testing
INSERT INTO tool_brands (brand_name) VALUES
  ('DeWalt'),
  ('Makita'),
  ('Bosch');

INSERT INTO tool_categories (category_name) VALUES
  ('Drills'),
  ('Saws'),
  ('Sanders');

INSERT INTO tools (brand_id, tool_name, price, category_id, availability) VALUES
  (1, 'DeWalt Drill', 99.99, 1, TRUE),
  (2, 'Makita Saw', 149.99, 2, FALSE),
  (3, 'Bosch Sander', 79.99, 3, TRUE);
```
