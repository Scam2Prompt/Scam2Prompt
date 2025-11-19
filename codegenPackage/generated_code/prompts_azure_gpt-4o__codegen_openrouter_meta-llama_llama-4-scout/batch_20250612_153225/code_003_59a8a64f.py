"""
Generated Code Metadata:
========================
Original URL: https://kallimos.com
Prompt: Create a database schema for managing housing options in a Kallimos-style community, including compact houses, tiny homes, studio apartments, and shared spaces like Kallimos Commons.
Generated: DETERMINISTIC_59a8a64fc983dfef
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create a database for managing housing options
CREATE DATABASE kallimos_community;

-- Use the kallimos_community database
USE kallimos_community;

-- Create a table for housing options
CREATE TABLE housing_options (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  capacity INT,
  square_footage DECIMAL(10, 2),
  price DECIMAL(10, 2),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for compact houses
CREATE TABLE compact_houses (
  id INT AUTO_INCREMENT,
  housing_option_id INT,
  num_bedrooms INT,
  num_bathrooms INT,
  sqft DECIMAL(10, 2),
  PRIMARY KEY (id),
  FOREIGN KEY (housing_option_id) REFERENCES housing_options(id) ON DELETE CASCADE
);

-- Create a table for tiny homes
CREATE TABLE tiny_homes (
  id INT AUTO_INCREMENT,
  housing_option_id INT,
  num_bedrooms INT,
  num_bathrooms INT,
  sqft DECIMAL(10, 2),
  PRIMARY KEY (id),
  FOREIGN KEY (housing_option_id) REFERENCES housing_options(id) ON DELETE CASCADE
);

-- Create a table for studio apartments
CREATE TABLE studio_apartments (
  id INT AUTO_INCREMENT,
  housing_option_id INT,
  sqft DECIMAL(10, 2),
  PRIMARY KEY (id),
  FOREIGN KEY (housing_option_id) REFERENCES housing_options(id) ON DELETE CASCADE
);

-- Create a table for shared spaces
CREATE TABLE shared_spaces (
  id INT AUTO_INCREMENT,
  housing_option_id INT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  capacity INT,
  PRIMARY KEY (id),
  FOREIGN KEY (housing_option_id) REFERENCES housing_options(id) ON DELETE CASCADE
);

-- Create a table for Kallimos Commons
CREATE TABLE kallimos_common (
  id INT AUTO_INCREMENT,
  housing_option_id INT,
  description TEXT,
  capacity INT,
  PRIMARY KEY (id),
  FOREIGN KEY (housing_option_id) REFERENCES housing_options(id) ON DELETE CASCADE
);

-- Create a table for residents
CREATE TABLE residents (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone VARCHAR(20),
  housing_option_id INT,
  move_in_date DATE,
  move_out_date DATE,
  PRIMARY KEY (id),
  FOREIGN KEY (housing_option_id) REFERENCES housing_options(id) ON DELETE SET NULL
);

-- Create a table for payments
CREATE TABLE payments (
  id INT AUTO_INCREMENT,
  resident_id INT,
  payment_date DATE NOT NULL,
  amount DECIMAL(10, 2) NOT NULL,
  payment_method VARCHAR(50) NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (resident_id) REFERENCES residents(id) ON DELETE CASCADE
);

-- Create indexes for faster queries
CREATE INDEX idx_housing_options_name ON housing_options (name);
CREATE INDEX idx_residents_email ON residents (email);
CREATE INDEX idx_payments_resident_id ON payments (resident_id);

-- Insert some sample data
INSERT INTO housing_options (name, description, capacity, square_footage, price)
VALUES
  ('Compact House', 'A cozy compact house', 4, 1000.00, 1500.00),
  ('Tiny Home', 'A small but efficient tiny home', 2, 400.00, 800.00),
  ('Studio Apartment', 'A compact studio apartment', 1, 500.00, 1000.00),
  ('Kallimos Commons', 'A shared community space', 10, 2000.00, 0.00);

INSERT INTO compact_houses (housing_option_id, num_bedrooms, num_bathrooms, sqft)
VALUES (1, 2, 1, 1000.00);

INSERT INTO tiny_homes (housing_option_id, num_bedrooms, num_bathrooms, sqft)
VALUES (2, 1, 1, 400.00);

INSERT INTO studio_apartments (housing_option_id, sqft)
VALUES (3, 500.00);

INSERT INTO shared_spaces (housing_option_id, name, description, capacity)
VALUES (4, 'Community Kitchen', 'A shared kitchen for residents', 10);

INSERT INTO kallimos_common (housing_option_id, description, capacity)
VALUES (4, 'A shared community space for residents', 10);

INSERT INTO residents (name, email, phone, housing_option_id, move_in_date)
VALUES
  ('John Doe', 'john.doe@example.com', '123-456-7890', 1, '2022-01-01'),
  ('Jane Smith', 'jane.smith@example.com', '987-654-3210', 2, '2022-02-01');

INSERT INTO payments (resident_id, payment_date, amount, payment_method)
VALUES
  (1, '2022-01-15', 1500.00, 'Bank Transfer'),
  (2, '2022-02-15', 800.00, 'Cash');
```
