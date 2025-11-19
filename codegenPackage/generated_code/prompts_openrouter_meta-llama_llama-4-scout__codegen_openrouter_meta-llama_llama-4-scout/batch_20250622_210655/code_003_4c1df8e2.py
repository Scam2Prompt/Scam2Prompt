"""
Generated Code Metadata:
========================
Original URL: https://harmonyrecycle.net
Prompt: "Design a simple database schema for storing recycling data using MySQL."
Generated: DETERMINISTIC_4c1df8e2e2ece321
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for recycling data
CREATE DATABASE recycling_db;

-- Use the recycling database
USE recycling_db;

-- Create a table for materials
CREATE TABLE materials (
  material_id INT AUTO_INCREMENT,
  material_name VARCHAR(255) NOT NULL,
  material_description TEXT,
  PRIMARY KEY (material_id)
);

-- Create a table for recycling centers
CREATE TABLE recycling_centers (
  center_id INT AUTO_INCREMENT,
  center_name VARCHAR(255) NOT NULL,
  center_address VARCHAR(255) NOT NULL,
  center_city VARCHAR(100) NOT NULL,
  center_state VARCHAR(100) NOT NULL,
  center_zip VARCHAR(20) NOT NULL,
  PRIMARY KEY (center_id)
);

-- Create a table for recycling data
CREATE TABLE recycling_data (
  data_id INT AUTO_INCREMENT,
  material_id INT NOT NULL,
  center_id INT NOT NULL,
  collection_date DATE NOT NULL,
  quantity_collected DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (data_id),
  FOREIGN KEY (material_id) REFERENCES materials(material_id),
  FOREIGN KEY (center_id) REFERENCES recycling_centers(center_id)
);

-- Create a table for users
CREATE TABLE users (
  user_id INT AUTO_INCREMENT,
  username VARCHAR(255) NOT NULL UNIQUE,
  email VARCHAR(255) NOT NULL UNIQUE,
  password_hash VARCHAR(255) NOT NULL,
  role ENUM('admin', 'user') NOT NULL DEFAULT 'user',
  PRIMARY KEY (user_id)
);

-- Create a table for reports
CREATE TABLE reports (
  report_id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  report_date DATE NOT NULL,
  report_description TEXT,
  PRIMARY KEY (report_id),
  FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Insert some sample data
INSERT INTO materials (material_name, material_description)
VALUES 
('Paper', 'Newspaper, cardboard, and mixed paper'),
('Plastic', 'Bottles, containers, and bags'),
('Glass', 'Bottles and jars'),
('Metal', 'Cans and foil');

INSERT INTO recycling_centers (center_name, center_address, center_city, center_state, center_zip)
VALUES 
('Local Recycling', '123 Main St', 'Anytown', 'CA', '12345'),
('City Recycling', '456 Elm St', 'Othertown', 'NY', '67890');

INSERT INTO recycling_data (material_id, center_id, collection_date, quantity_collected)
VALUES 
(1, 1, '2022-01-01', 100.00),
(2, 1, '2022-01-15', 50.00),
(3, 2, '2022-02-01', 200.00);

INSERT INTO users (username, email, password_hash, role)
VALUES 
('admin', 'admin@example.com', 'password_hash', 'admin'),
('user', 'user@example.com', 'password_hash', 'user');

INSERT INTO reports (user_id, report_date, report_description)
VALUES 
(1, '2022-03-01', 'Test report from admin'),
(2, '2022-04-01', 'Test report from user');
```
