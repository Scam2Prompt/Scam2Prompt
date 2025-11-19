"""
Generated Code Metadata:
========================
Original URL: https://poutakidis.eu
Prompt: Generate a SQL database schema to store information about different types of tires (e.g., Continental EcoContact5, Michelin Primacy 3) and wheels (e.g., OZ Ego Wheels, DOTZ Shift Wheels) offered by a company.
Generated: DETERMINISTIC_b672a53ad6b19c77
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- tire_wheel_schema.sql

-- Create a database schema to store information about tires and wheels

CREATE DATABASE tire_wheel_database;

USE tire_wheel_database;

-- Create a table to store manufacturers
CREATE TABLE manufacturers (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY (name)
);

-- Create a table to store tire types
CREATE TABLE tire_types (
  id INT AUTO_INCREMENT,
  manufacturer_id INT NOT NULL,
  model_name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (manufacturer_id) REFERENCES manufacturers(id) ON DELETE CASCADE
);

-- Create a table to store wheel types
CREATE TABLE wheel_types (
  id INT AUTO_INCREMENT,
  manufacturer_id INT NOT NULL,
  model_name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (manufacturer_id) REFERENCES manufacturers(id) ON DELETE CASCADE
);

-- Create a table to store tire specifications
CREATE TABLE tire_specs (
  id INT AUTO_INCREMENT,
  tire_type_id INT NOT NULL,
  size VARCHAR(20) NOT NULL,
  load_index INT NOT NULL,
  speed_rating VARCHAR(5) NOT NULL,
  tread_depth DECIMAL(3, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (tire_type_id) REFERENCES tire_types(id) ON DELETE CASCADE
);

-- Create a table to store wheel specifications
CREATE TABLE wheel_specs (
  id INT AUTO_INCREMENT,
  wheel_type_id INT NOT NULL,
  size VARCHAR(20) NOT NULL,
  bolt_pattern VARCHAR(20) NOT NULL,
  offset DECIMAL(5, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (wheel_type_id) REFERENCES wheel_types(id) ON DELETE CASCADE
);

-- Create a table to store products (tires and wheels)
CREATE TABLE products (
  id INT AUTO_INCREMENT,
  product_type ENUM('tire', 'wheel') NOT NULL,
  tire_type_id INT,
  wheel_type_id INT,
  price DECIMAL(10, 2) NOT NULL,
  stock_quantity INT NOT NULL DEFAULT 0,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (tire_type_id) REFERENCES tire_types(id) ON DELETE SET NULL,
  FOREIGN KEY (wheel_type_id) REFERENCES wheel_types(id) ON DELETE SET NULL,
  CHECK ((product_type = 'tire' AND tire_type_id IS NOT NULL AND wheel_type_id IS NULL) OR 
         (product_type = 'wheel' AND tire_type_id IS NULL AND wheel_type_id IS NOT NULL))
);

-- Insert sample data
INSERT INTO manufacturers (name) VALUES
  ('Continental'),
  ('Michelin'),
  ('OZ'),
  ('DOTZ');

INSERT INTO tire_types (manufacturer_id, model_name) VALUES
  (1, 'EcoContact5'),
  (2, 'Primacy3');

INSERT INTO wheel_types (manufacturer_id, model_name) VALUES
  (3, 'Ego Wheels'),
  (4, 'Shift Wheels');

INSERT INTO tire_specs (tire_type_id, size, load_index, speed_rating, tread_depth) VALUES
  (1, '225/60R17', 98, 'H', 8.5),
  (2, '235/55R18', 100, 'V', 9.0);

INSERT INTO wheel_specs (wheel_type_id, size, bolt_pattern, offset) VALUES
  (1, '17x7.5', '5x112', 35.00),
  (2, '18x8.5', '5x120', 40.00);

INSERT INTO products (product_type, tire_type_id, wheel_type_id, price, stock_quantity) VALUES
  ('tire', 1, NULL, 120.00, 100),
  ('tire', 2, NULL, 150.00, 50),
  ('wheel', NULL, 1, 200.00, 20),
  ('wheel', NULL, 2, 250.00, 30);
```
