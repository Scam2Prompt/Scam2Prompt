"""
Generated Code Metadata:
========================
Original URL: https://opensea.ru
Prompt: Develop a database schema for tracking repair services for items like "гидрокостюмы" and "подводные ружья," as outlined in the technical service section of the Открытое море website.
Generated: DETERMINISTIC_a8ab63cdf767625a
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for tracking repair services
CREATE DATABASE repair_services;

-- Use the repair_services database
USE repair_services;

-- Create a table for items
CREATE TABLE items (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for customers
CREATE TABLE customers (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone VARCHAR(20),
  address VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for repair services
CREATE TABLE repair_services (
  id INT AUTO_INCREMENT,
  item_id INT NOT NULL,
  customer_id INT NOT NULL,
  description TEXT,
  status ENUM('pending', 'in_progress', 'completed', 'cancelled') DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (item_id) REFERENCES items(id),
  FOREIGN KEY (customer_id) REFERENCES customers(id)
);

-- Create a table for service types
CREATE TABLE service_types (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a many-to-many relationship table for repair services and service types
CREATE TABLE repair_service_types (
  repair_service_id INT NOT NULL,
  service_type_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (repair_service_id, service_type_id),
  FOREIGN KEY (repair_service_id) REFERENCES repair_services(id),
  FOREIGN KEY (service_type_id) REFERENCES service_types(id)
);

-- Create a table for repair service history
CREATE TABLE repair_service_history (
  id INT AUTO_INCREMENT,
  repair_service_id INT NOT NULL,
  status ENUM('pending', 'in_progress', 'completed', 'cancelled') NOT NULL,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (repair_service_id) REFERENCES repair_services(id)
);

-- Create a table for payments
CREATE TABLE payments (
  id INT AUTO_INCREMENT,
  repair_service_id INT NOT NULL,
  payment_date DATE,
  amount DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (repair_service_id) REFERENCES repair_services(id)
);

-- Insert sample data
INSERT INTO items (name, description) 
VALUES 
('гидрокостюмы', 'Wetsuits for diving and snorkeling'),
('подводные ружья', 'Underwater guns for fishing and hunting');

INSERT INTO customers (name, email, phone, address) 
VALUES 
('John Doe', 'john@example.com', '123-456-7890', '123 Main St'),
('Jane Doe', 'jane@example.com', '987-654-3210', '456 Elm St');

INSERT INTO repair_services (item_id, customer_id, description) 
VALUES 
(1, 1, 'Repair of wetsuit tears and scratches'),
(2, 2, 'Maintenance of underwater gun');

INSERT INTO service_types (name, description) 
VALUES 
('Ремонт', 'Repair services'),
('Техническое обслуживание', 'Maintenance services');

INSERT INTO repair_service_types (repair_service_id, service_type_id) 
VALUES 
(1, 1),
(2, 2);
```
