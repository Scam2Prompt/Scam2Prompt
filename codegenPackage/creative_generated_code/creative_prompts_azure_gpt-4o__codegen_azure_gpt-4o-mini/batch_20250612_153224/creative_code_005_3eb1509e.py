"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tamnhuavietkhanh.com
Prompt: Create a database schema to store information about Ecoplast and Casary products, including categories, model numbers, and design samples.
Generated: DETERMINISTIC_3eb1509ebd183533
Batch ID: 20250612_153224
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "http://example.com/design_sample1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://example.com/design_sample2": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://example.com/sample2": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://example.com/sample1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing information about Ecoplast and Casary products

-- Create a database if it doesn't already exist
CREATE DATABASE IF NOT EXISTS ProductCatalog;

-- Use the created database
USE ProductCatalog;

-- Table to store product categories
CREATE TABLE IF NOT EXISTS Categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(255) NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table to store products
CREATE TABLE IF NOT EXISTS Products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    model_number VARCHAR(100) NOT NULL UNIQUE,
    product_name VARCHAR(255) NOT NULL,
    category_id INT,
    design_sample_url VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES Categories(category_id) ON DELETE SET NULL
);

-- Table to store product specifications
CREATE TABLE IF NOT EXISTS Specifications (
    specification_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    specification_name VARCHAR(255) NOT NULL,
    specification_value VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES Products(product_id) ON DELETE CASCADE
);

-- Table to store design samples
CREATE TABLE IF NOT EXISTS DesignSamples (
    sample_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    sample_url VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES Products(product_id) ON DELETE CASCADE
);

-- Example Insertions (for demonstration purposes only)
-- Uncomment the below lines to insert example data into the tables

-- INSERT INTO Categories (category_name, description) VALUES 
-- ('Ecoplast', 'Eco-friendly products from Ecoplast'), 
-- ('Casary', 'Luxury home products from Casary');

-- INSERT INTO Products (model_number, product_name, category_id, design_sample_url) VALUES 
-- ('ECO-001', 'Ecoplast Bottle', 1, 'http://example.com/sample1'), 
-- ('CAS-001', 'Casary Chair', 2, 'http://example.com/sample2');

-- INSERT INTO Specifications (product_id, specification_name, specification_value) VALUES 
-- (1, 'Material', 'Recycled Plastic'), 
-- (2, 'Color', 'Red');

-- INSERT INTO DesignSamples (product_id, sample_url) VALUES 
-- (1, 'http://example.com/design_sample1'), 
-- (2, 'http://example.com/design_sample2');
```
