"""
Generated Code Metadata:
========================
Original URL: https://fabricarecosmeticos.ind.br
Prompt: Design a database schema for managing client projects in a cosmetic manufacturing business, reflecting the full-service approach outlined by Fabricare Cosmeticos.
Generated: DETERMINISTIC_250a8f375eaeb49d
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for cosmetic manufacturing business
CREATE DATABASE fabricare_cosmeticos;

-- Use the database
USE fabricare_cosmeticos;

-- Create table for clients
CREATE TABLE clients (
  client_id INT AUTO_INCREMENT,
  company_name VARCHAR(255) NOT NULL,
  contact_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  address VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (client_id)
);

-- Create table for projects
CREATE TABLE projects (
  project_id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  project_name VARCHAR(255) NOT NULL,
  project_description TEXT,
  start_date DATE,
  end_date DATE,
  status ENUM('pending', 'in_progress', 'completed', 'cancelled') DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (project_id),
  FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
);

-- Create table for products
CREATE TABLE products (
  product_id INT AUTO_INCREMENT,
  product_name VARCHAR(255) NOT NULL,
  product_description TEXT,
  product_type ENUM('skincare', 'haircare', 'makeup', 'fragrance') NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (product_id)
);

-- Create table for project products
CREATE TABLE project_products (
  project_id INT NOT NULL,
  product_id INT NOT NULL,
  quantity INT NOT NULL,
  PRIMARY KEY (project_id, product_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
  FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Create table for services
CREATE TABLE services (
  service_id INT AUTO_INCREMENT,
  service_name VARCHAR(255) NOT NULL,
  service_description TEXT,
  service_type ENUM('formulation', 'manufacturing', 'packaging', 'labeling') NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (service_id)
);

-- Create table for project services
CREATE TABLE project_services (
  project_id INT NOT NULL,
  service_id INT NOT NULL,
  service_status ENUM('pending', 'in_progress', 'completed') NOT NULL,
  PRIMARY KEY (project_id, service_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
  FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE CASCADE
);

-- Create table for deliveries
CREATE TABLE deliveries (
  delivery_id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  delivery_date DATE NOT NULL,
  delivery_status ENUM('pending', 'shipped', 'delivered') NOT NULL,
  tracking_number VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (delivery_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Create table for payments
CREATE TABLE payments (
  payment_id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  payment_date DATE NOT NULL,
  payment_amount DECIMAL(10, 2) NOT NULL,
  payment_method ENUM('bank_transfer', 'credit_card', 'paypal') NOT NULL,
  payment_status ENUM('pending', 'paid', 'overdue') NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (payment_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);
```
