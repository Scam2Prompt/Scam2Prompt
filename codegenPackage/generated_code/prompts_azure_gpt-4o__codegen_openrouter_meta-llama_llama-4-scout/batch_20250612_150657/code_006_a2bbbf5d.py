"""
Generated Code Metadata:
========================
Original URL: https://perucotiza.com
Prompt: Design a database schema in SQL to store information retrieved from PeruCotiza, including categories like "repuestos" (e.g., motor, frenos) and "accesorios" (e.g., alarmas, seguridad).
Generated: DETERMINISTIC_a2bbbf5daeef16de
Batch ID: 20250612_150657
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- peru_cotiza_schema.sql

-- Create database
CREATE DATABASE peru_cotiza;

-- Use database
USE peru_cotiza;

-- Create table for categories
CREATE TABLE categories (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for repuestos (spare parts)
CREATE TABLE repuestos (
  id INT AUTO_INCREMENT,
  category_id INT NOT NULL,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  price DECIMAL(10, 2) NOT NULL,
  stock INT NOT NULL DEFAULT 0,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE
);

-- Create table for accesorios (accessories)
CREATE TABLE accesorios (
  id INT AUTO_INCREMENT,
  category_id INT NOT NULL,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  price DECIMAL(10, 2) NOT NULL,
  stock INT NOT NULL DEFAULT 0,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE
);

-- Create table for suppliers
CREATE TABLE suppliers (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  contact_name VARCHAR(255) NOT NULL,
  contact_email VARCHAR(255) NOT NULL,
  phone VARCHAR(20),
  address TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for repuesto suppliers
CREATE TABLE repuesto_suppliers (
  id INT AUTO_INCREMENT,
  repuesto_id INT NOT NULL,
  supplier_id INT NOT NULL,
  price DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (repuesto_id) REFERENCES repuestos(id) ON DELETE CASCADE,
  FOREIGN KEY (supplier_id) REFERENCES suppliers(id) ON DELETE CASCADE,
  UNIQUE KEY (repuesto_id, supplier_id)
);

-- Create table for accesorio suppliers
CREATE TABLE accesorio_suppliers (
  id INT AUTO_INCREMENT,
  accesorio_id INT NOT NULL,
  supplier_id INT NOT NULL,
  price DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (accesorio_id) REFERENCES accesorios(id) ON DELETE CASCADE,
  FOREIGN KEY (supplier_id) REFERENCES suppliers(id) ON DELETE CASCADE,
  UNIQUE KEY (accesorio_id, supplier_id)
);

-- Insert sample categories
INSERT INTO categories (name, description) VALUES
  ('Motor', 'Motor repuestos'),
  ('Frenos', 'Frenos repuestos'),
  ('Alarmas', 'Alarmas accesorios'),
  ('Seguridad', 'Seguridad accesorios');

-- Insert sample repuestos
INSERT INTO repuestos (category_id, name, description, price, stock) VALUES
  (1, 'Motor 1.8L', 'Motor 1.8L repuesto', 5000.00, 10),
  (2, 'Freno ABS', 'Freno ABS repuesto', 2000.00, 5);

-- Insert sample accesorios
INSERT INTO accesorios (category_id, name, description, price, stock) VALUES
  (3, 'Alarma GPS', 'Alarma GPS accesorio', 300.00, 20),
  (4, 'Cámara Seguridad', 'Cámara Seguridad accesorio', 500.00, 10);

-- Insert sample suppliers
INSERT INTO suppliers (name, contact_name, contact_email, phone, address) VALUES
  ('Supplier 1', 'John Doe', 'john.doe@example.com', '123456789', 'Calle 123'),
  ('Supplier 2', 'Jane Doe', 'jane.doe@example.com', '987654321', 'Calle 456');

-- Insert sample repuesto suppliers
INSERT INTO repuesto_suppliers (repuesto_id, supplier_id, price) VALUES
  (1, 1, 4500.00),
  (1, 2, 4800.00),
  (2, 1, 1800.00);

-- Insert sample accesorio suppliers
INSERT INTO accesorio_suppliers (accesorio_id, supplier_id, price) VALUES
  (1, 1, 250.00),
  (1, 2, 280.00),
  (2, 1, 450.00);
```
