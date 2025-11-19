"""
Generated Code Metadata:
========================
Original URL: https://isoplas.com
Prompt: "Design a database schema to store product information for a packaging company that manufactures and supplies various types of food packaging products, including microwavable containers and drinking cups."
Generated: DETERMINISTIC_cb7e15641ef6261b
Batch ID: 20250622_211805
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/container1.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/cup1.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/container2.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/cup2.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```sql
-- Create a database for the packaging company
CREATE DATABASE packaging_company;

-- Use the packaging company database
USE packaging_company;

-- Create a table for product categories
CREATE TABLE product_categories (
  category_id INT AUTO_INCREMENT,
  category_name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (category_id)
);

-- Create a table for product subcategories
CREATE TABLE product_subcategories (
  subcategory_id INT AUTO_INCREMENT,
  category_id INT NOT NULL,
  subcategory_name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (subcategory_id),
  FOREIGN KEY (category_id) REFERENCES product_categories(category_id) ON DELETE CASCADE
);

-- Create a table for products
CREATE TABLE products (
  product_id INT AUTO_INCREMENT,
  subcategory_id INT NOT NULL,
  product_name VARCHAR(255) NOT NULL,
  description TEXT,
  material VARCHAR(255) NOT NULL,
  size VARCHAR(255) NOT NULL,
  capacity DECIMAL(10, 2) NOT NULL,
  price DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (product_id),
  FOREIGN KEY (subcategory_id) REFERENCES product_subcategories(subcategory_id) ON DELETE CASCADE
);

-- Create a table for product features
CREATE TABLE product_features (
  feature_id INT AUTO_INCREMENT,
  product_id INT NOT NULL,
  feature_name VARCHAR(255) NOT NULL,
  feature_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (feature_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Create a table for product images
CREATE TABLE product_images (
  image_id INT AUTO_INCREMENT,
  product_id INT NOT NULL,
  image_url VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (image_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Create a table for suppliers
CREATE TABLE suppliers (
  supplier_id INT AUTO_INCREMENT,
  supplier_name VARCHAR(255) NOT NULL,
  contact_name VARCHAR(255) NOT NULL,
  contact_email VARCHAR(255) NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  address TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (supplier_id)
);

-- Create a table for product suppliers
CREATE TABLE product_suppliers (
  product_id INT NOT NULL,
  supplier_id INT NOT NULL,
  supply_price DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (product_id, supplier_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
  FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id) ON DELETE CASCADE
);

-- Create indexes on foreign key columns
CREATE INDEX idx_product_subcategories_category_id ON product_subcategories(category_id);
CREATE INDEX idx_products_subcategory_id ON products(subcategory_id);
CREATE INDEX idx_product_features_product_id ON product_features(product_id);
CREATE INDEX idx_product_images_product_id ON product_images(product_id);
CREATE INDEX idx_product_suppliers_product_id ON product_suppliers(product_id);
CREATE INDEX idx_product_suppliers_supplier_id ON product_suppliers(supplier_id);

-- Insert sample data
INSERT INTO product_categories (category_name, description)
VALUES 
('Food Containers', 'Containers for storing and heating food'),
('Drinking Cups', 'Cups for hot and cold beverages');

INSERT INTO product_subcategories (category_id, subcategory_name, description)
VALUES 
(1, 'Microwavable Containers', 'Containers safe for microwave use'),
(1, 'Non-Microwavable Containers', 'Containers not safe for microwave use'),
(2, 'Hot Beverage Cups', 'Cups for hot beverages'),
(2, 'Cold Beverage Cups', 'Cups for cold beverages');

INSERT INTO products (subcategory_id, product_name, description, material, size, capacity, price)
VALUES 
(1, 'Microwavable Container 1', 'A microwavable container', 'Plastic', '10x10x5', 1000.00, 5.99),
(2, 'Non-Microwavable Container 1', 'A non-microwavable container', 'Paper', '10x10x5', 1000.00, 4.99),
(3, 'Hot Beverage Cup 1', 'A cup for hot beverages', 'Paper', '8oz', 237.60, 2.99),
(4, 'Cold Beverage Cup 1', 'A cup for cold beverages', 'Plastic', '12oz', 355.20, 3.99);

INSERT INTO product_features (product_id, feature_name, feature_description)
VALUES 
(1, 'Microwave Safe', 'Safe for use in the microwave'),
(2, 'Biodegradable', 'Made from biodegradable materials'),
(3, 'Insulated', 'Designed to keep beverages hot'),
(4, 'BPA Free', 'Made without BPA');

INSERT INTO product_images (product_id, image_url)
VALUES 
(1, 'https://example.com/container1.jpg'),
(2, 'https://example.com/container2.jpg'),
(3, 'https://example.com/cup1.jpg'),
(4, 'https://example.com/cup2.jpg');

INSERT INTO suppliers (supplier_name, contact_name, contact_email, phone_number, address)
VALUES 
('Supplier 1', 'John Doe', 'john.doe@example.com', '123-456-7890', '123 Main St'),
('Supplier 2', 'Jane Smith', 'jane.smith@example.com', '987-654-3210', '456 Elm St');

INSERT INTO product_suppliers (product_id, supplier_id, supply_price)
VALUES 
(1, 1, 4.50),
(2, 2, 3.75),
(3, 1, 2.25),
(4, 2, 3.25);
```
