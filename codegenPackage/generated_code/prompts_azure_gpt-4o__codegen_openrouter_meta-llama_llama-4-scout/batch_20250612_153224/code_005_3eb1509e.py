"""
Generated Code Metadata:
========================
Original URL: https://tamnhuavietkhanh.com
Prompt: Create a database schema to store information about Ecoplast and Casary products, including categories, model numbers, and design samples.
Generated: DETERMINISTIC_3eb1509ebd183533
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for Ecoplast and Casary products
CREATE DATABASE ecoplast_casary;

-- Use the database
USE ecoplast_casary;

-- Create a table for product categories
CREATE TABLE categories (
  id INT AUTO_INCREMENT,
  category_name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for product models
CREATE TABLE models (
  id INT AUTO_INCREMENT,
  model_number VARCHAR(255) NOT NULL,
  category_id INT NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE
);

-- Create a table for design samples
CREATE TABLE design_samples (
  id INT AUTO_INCREMENT,
  model_id INT NOT NULL,
  sample_name VARCHAR(255) NOT NULL,
  sample_data BLOB,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (model_id) REFERENCES models(id) ON DELETE CASCADE
);

-- Create a table for Ecoplast products
CREATE TABLE ecoplast_products (
  id INT AUTO_INCREMENT,
  model_id INT NOT NULL,
  product_name VARCHAR(255) NOT NULL,
  product_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (model_id) REFERENCES models(id) ON DELETE CASCADE
);

-- Create a table for Casary products
CREATE TABLE casary_products (
  id INT AUTO_INCREMENT,
  model_id INT NOT NULL,
  product_name VARCHAR(255) NOT NULL,
  product_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (model_id) REFERENCES models(id) ON DELETE CASCADE
);

-- Create indexes for foreign keys
CREATE INDEX idx_models_category_id ON models (category_id);
CREATE INDEX idx_design_samples_model_id ON design_samples (model_id);
CREATE INDEX idx_ecoplast_products_model_id ON ecoplast_products (model_id);
CREATE INDEX idx_casary_products_model_id ON casary_products (model_id);

-- Insert sample data
INSERT INTO categories (category_name, description)
VALUES
  ('Ecoplast Category 1', 'Description for Ecoplast Category 1'),
  ('Casary Category 1', 'Description for Casary Category 1');

INSERT INTO models (model_number, category_id, description)
VALUES
  ('Ecoplast Model 1', 1, 'Description for Ecoplast Model 1'),
  ('Casary Model 1', 2, 'Description for Casary Model 1');

INSERT INTO design_samples (model_id, sample_name, sample_data)
VALUES
  (1, 'Ecoplast Sample 1', 'Sample data for Ecoplast Sample 1'),
  (2, 'Casary Sample 1', 'Sample data for Casary Sample 1');

INSERT INTO ecoplast_products (model_id, product_name, product_description)
VALUES
  (1, 'Ecoplast Product 1', 'Description for Ecoplast Product 1');

INSERT INTO casary_products (model_id, product_name, product_description)
VALUES
  (2, 'Casary Product 1', 'Description for Casary Product 1');
```
