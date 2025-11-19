"""
Generated Code Metadata:
========================
Original URL: https://mirrorsshadows.com
Prompt: "Design a database schema for an art studio that stores information about artists, sculptures, paintings, and other creative products, and provide a sample query to retrieve product details."
Generated: DETERMINISTIC_1997dd7f3a2570bc
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create a database for the art studio
CREATE DATABASE art_studio;

-- Use the art_studio database
USE art_studio;

-- Create a table for artists
CREATE TABLE artists (
  artist_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  address VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (artist_id)
);

-- Create a table for product categories
CREATE TABLE product_categories (
  category_id INT AUTO_INCREMENT,
  category_name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (category_id)
);

-- Create a table for products
CREATE TABLE products (
  product_id INT AUTO_INCREMENT,
  artist_id INT,
  category_id INT,
  product_name VARCHAR(255) NOT NULL,
  description TEXT,
  price DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (product_id),
  FOREIGN KEY (artist_id) REFERENCES artists(artist_id) ON DELETE CASCADE,
  FOREIGN KEY (category_id) REFERENCES product_categories(category_id) ON DELETE CASCADE
);

-- Create a table for sculptures
CREATE TABLE sculptures (
  product_id INT,
  material VARCHAR(255) NOT NULL,
  height DECIMAL(10, 2) NOT NULL,
  width DECIMAL(10, 2) NOT NULL,
  depth DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (product_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Create a table for paintings
CREATE TABLE paintings (
  product_id INT,
  medium VARCHAR(255) NOT NULL,
  size VARCHAR(255) NOT NULL,
  PRIMARY KEY (product_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Insert sample data
INSERT INTO artists (first_name, last_name, email, phone_number, address)
VALUES
  ('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St'),
  ('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210', '456 Elm St');

INSERT INTO product_categories (category_name, description)
VALUES
  ('Sculpture', 'Three-dimensional artwork'),
  ('Painting', 'Two-dimensional artwork');

INSERT INTO products (artist_id, category_id, product_name, description, price)
VALUES
  (1, 1, 'Sculpture 1', 'A beautiful sculpture', 1000.00),
  (2, 2, 'Painting 1', 'A stunning painting', 500.00);

INSERT INTO sculptures (product_id, material, height, width, depth)
VALUES
  (1, 'Marble', 10.00, 5.00, 3.00);

INSERT INTO paintings (product_id, medium, size)
VALUES
  (2, 'Acrylic', '24x36');

-- Sample query to retrieve product details
SELECT 
  p.product_id,
  p.product_name,
  p.description,
  p.price,
  a.first_name AS artist_first_name,
  a.last_name AS artist_last_name,
  pc.category_name,
  CASE 
    WHEN s.product_id IS NOT NULL THEN 'Sculpture'
    WHEN pa.product_id IS NOT NULL THEN 'Painting'
  END AS product_type,
  COALESCE(s.material, pa.medium) AS product_details
FROM 
  products p
  JOIN artists a ON p.artist_id = a.artist_id
  JOIN product_categories pc ON p.category_id = pc.category_id
  LEFT JOIN sculptures s ON p.product_id = s.product_id
  LEFT JOIN paintings pa ON p.product_id = pa.product_id;
```
