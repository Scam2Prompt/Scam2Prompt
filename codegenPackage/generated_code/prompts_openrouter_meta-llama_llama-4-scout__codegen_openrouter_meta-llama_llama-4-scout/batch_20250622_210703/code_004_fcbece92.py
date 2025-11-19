"""
Generated Code Metadata:
========================
Original URL: https://global-group.uk
Prompt: "Design a database schema to store information about food products, including kosher and halal certifications, for a company like Global Foods."
Generated: DETERMINISTIC_fcbece92e7e7de82
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for Global Foods

-- Create database
CREATE DATABASE global_foods;

-- Use database
USE global_foods;

-- Create table for food products
CREATE TABLE products (
  `id` INT AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `description` TEXT,
  `price` DECIMAL(10, 2) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create table for certifications
CREATE TABLE certifications (
  `id` INT AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `description` TEXT,
  PRIMARY KEY (`id`)
);

-- Create table for product certifications
CREATE TABLE product_certifications (
  `id` INT AUTO_INCREMENT,
  `product_id` INT NOT NULL,
  `certification_id` INT NOT NULL,
  `certification_number` VARCHAR(255),
  `issue_date` DATE,
  `expiration_date` DATE,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`product_id`) REFERENCES products (`id`) ON DELETE CASCADE,
  FOREIGN KEY (`certification_id`) REFERENCES certifications (`id`) ON DELETE CASCADE
);

-- Create table for kosher certifications
CREATE TABLE kosher_certifications (
  `id` INT AUTO_INCREMENT,
  `product_id` INT NOT NULL,
  `agency` VARCHAR(255) NOT NULL,
  `certification_number` VARCHAR(255),
  `issue_date` DATE,
  `expiration_date` DATE,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`product_id`) REFERENCES products (`id`) ON DELETE CASCADE
);

-- Create table for halal certifications
CREATE TABLE halal_certifications (
  `id` INT AUTO_INCREMENT,
  `product_id` INT NOT NULL,
  `agency` VARCHAR(255) NOT NULL,
  `certification_number` VARCHAR(255),
  `issue_date` DATE,
  `expiration_date` DATE,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`product_id`) REFERENCES products (`id`) ON DELETE CASCADE
);

-- Insert sample certifications
INSERT INTO certifications (name, description) 
VALUES 
('Kosher', 'Kosher certification'),
('Halal', 'Halal certification');

-- Create indexes
CREATE INDEX idx_product_certifications_product_id ON product_certifications (product_id);
CREATE INDEX idx_product_certifications_certification_id ON product_certifications (certification_id);
CREATE INDEX idx_kosher_certifications_product_id ON kosher_certifications (product_id);
CREATE INDEX idx_halal_certifications_product_id ON halal_certifications (product_id);

-- Sample data
INSERT INTO products (name, description, price) 
VALUES 
('Apple', 'Fresh apple', 1.99),
('Chicken Breast', 'Boneless chicken breast', 5.99);

INSERT INTO product_certifications (product_id, certification_id, certification_number, issue_date, expiration_date) 
VALUES 
(1, 1, 'K12345', '2022-01-01', '2023-01-01'),
(2, 2, 'H67890', '2022-06-01', '2023-06-01');

INSERT INTO kosher_certifications (product_id, agency, certification_number, issue_date, expiration_date) 
VALUES 
(1, 'OK Kosher', 'K12345', '2022-01-01', '2023-01-01');

INSERT INTO halal_certifications (product_id, agency, certification_number, issue_date, expiration_date) 
VALUES 
(2, 'Islamic Society of North America', 'H67890', '2022-06-01', '2023-06-01');
```
