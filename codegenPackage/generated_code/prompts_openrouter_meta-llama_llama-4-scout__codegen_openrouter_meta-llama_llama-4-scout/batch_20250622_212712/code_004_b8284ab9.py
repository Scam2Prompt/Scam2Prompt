"""
Generated Code Metadata:
========================
Original URL: https://bllabs.co
Prompt: "Design a database schema to store information about research peptides, bioregulators, and small molecules, including product details, pricing, and shipping information for a supplier like BioLongevity Labs."
Generated: DETERMINISTIC_b8284ab93e194dd8
Batch ID: 20250622_212712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for BioLongevity Labs
CREATE DATABASE bio_longevity_labs;

-- Use the database
USE bio_longevity_labs;

-- Create a table for product categories
CREATE TABLE product_categories (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for products
CREATE TABLE products (
  id INT AUTO_INCREMENT,
  category_id INT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  molecular_weight DECIMAL(10, 2),
  purity DECIMAL(5, 2),
  concentration DECIMAL(10, 2),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (category_id) REFERENCES product_categories(id) ON DELETE CASCADE
);

-- Create a table for product types (peptides, bioregulators, small molecules)
CREATE TABLE product_types (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a many-to-many relationship table for products and product types
CREATE TABLE product_type_associations (
  product_id INT,
  product_type_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (product_id, product_type_id),
  FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE,
  FOREIGN KEY (product_type_id) REFERENCES product_types(id) ON DELETE CASCADE
);

-- Create a table for pricing information
CREATE TABLE pricing (
  id INT AUTO_INCREMENT,
  product_id INT,
  price DECIMAL(15, 2) NOT NULL,
  currency VARCHAR(10) NOT NULL DEFAULT 'USD',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
);

-- Create a table for shipping information
CREATE TABLE shipping (
  id INT AUTO_INCREMENT,
  product_id INT,
  shipping_cost DECIMAL(10, 2) NOT NULL,
  estimated_delivery_time VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
);

-- Create a table for product aliases or synonyms
CREATE TABLE product_aliases (
  id INT AUTO_INCREMENT,
  product_id INT,
  alias VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
);

-- Create a table for product references or citations
CREATE TABLE product_references (
  id INT AUTO_INCREMENT,
  product_id INT,
  reference VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
);

-- Example insert statements
INSERT INTO product_categories (name, description) 
VALUES 
('Peptides', 'Peptide products'),
('Bioregulators', 'Bioregulator products'),
('Small Molecules', 'Small molecule products');

INSERT INTO product_types (name, description) 
VALUES 
('Peptide', 'A peptide molecule'),
('Bioregulator', 'A bioregulator molecule'),
('Small Molecule', 'A small molecule');

INSERT INTO products (category_id, name, description, molecular_weight, purity, concentration) 
VALUES 
(1, 'Peptide A', 'A peptide product', 1000.00, 98.00, 1.00),
(2, 'Bioregulator B', 'A bioregulator product', 500.00, 95.00, 2.00),
(3, 'Small Molecule C', 'A small molecule product', 200.00, 99.00, 3.00);

INSERT INTO product_type_associations (product_id, product_type_id) 
VALUES 
(1, 1),
(2, 2),
(3, 3);

INSERT INTO pricing (product_id, price) 
VALUES 
(1, 100.00),
(2, 200.00),
(3, 50.00);

INSERT INTO shipping (product_id, shipping_cost, estimated_delivery_time) 
VALUES 
(1, 10.00, '3-5 business days'),
(2, 20.00, '5-7 business days'),
(3, 5.00, '2-3 business days');
```
