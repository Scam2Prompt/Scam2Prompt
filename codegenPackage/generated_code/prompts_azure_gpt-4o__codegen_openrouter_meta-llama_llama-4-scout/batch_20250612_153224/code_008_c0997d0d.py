"""
Generated Code Metadata:
========================
Original URL: https://www.purpledumpster.ca
Prompt: Design a database schema to store dumpster rental information, including service areas, dumpster sizes, and pricing, as described on the Purple Dumpster website.
Generated: DETERMINISTIC_c0997d0df564cfa2
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for dumpster rental information
CREATE DATABASE dumpster_rental;

-- Use the database
USE dumpster_rental;

-- Create table for service areas
CREATE TABLE service_areas (
  id INT AUTO_INCREMENT,
  city VARCHAR(255) NOT NULL,
  state VARCHAR(255) NOT NULL,
  zip_code VARCHAR(10) NOT NULL,
  PRIMARY KEY (id)
);

-- Create table for dumpster sizes
CREATE TABLE dumpster_sizes (
  id INT AUTO_INCREMENT,
  size_name VARCHAR(255) NOT NULL,
  size_description VARCHAR(255),
  capacity DECIMAL(10, 2) NOT NULL, -- in cubic yards
  PRIMARY KEY (id)
);

-- Create table for pricing
CREATE TABLE pricing (
  id INT AUTO_INCREMENT,
  dumpster_size_id INT NOT NULL,
  service_area_id INT NOT NULL,
  rental_duration INT NOT NULL, -- in days
  price DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (dumpster_size_id) REFERENCES dumpster_sizes(id),
  FOREIGN KEY (service_area_id) REFERENCES service_areas(id)
);

-- Create table for customers
CREATE TABLE customers (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  address VARCHAR(255) NOT NULL,
  service_area_id INT NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (service_area_id) REFERENCES service_areas(id)
);

-- Create table for rentals
CREATE TABLE rentals (
  id INT AUTO_INCREMENT,
  customer_id INT NOT NULL,
  dumpster_size_id INT NOT NULL,
  rental_start_date DATE NOT NULL,
  rental_end_date DATE NOT NULL,
  total_cost DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (customer_id) REFERENCES customers(id),
  FOREIGN KEY (dumpster_size_id) REFERENCES dumpster_sizes(id)
);

-- Create table for payments
CREATE TABLE payments (
  id INT AUTO_INCREMENT,
  rental_id INT NOT NULL,
  payment_date DATE NOT NULL,
  payment_amount DECIMAL(10, 2) NOT NULL,
  payment_method VARCHAR(255) NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (rental_id) REFERENCES rentals(id)
);

-- Insert sample data
INSERT INTO service_areas (city, state, zip_code)
VALUES
  ('New York City', 'NY', '10001'),
  ('Los Angeles', 'CA', '90001'),
  ('Chicago', 'IL', '60001');

INSERT INTO dumpster_sizes (size_name, size_description, capacity)
VALUES
  ('10 Yard', 'Small dumpster for small projects', 10.00),
  ('20 Yard', 'Medium dumpster for medium projects', 20.00),
  ('30 Yard', 'Large dumpster for large projects', 30.00);

INSERT INTO pricing (dumpster_size_id, service_area_id, rental_duration, price)
VALUES
  (1, 1, 7, 200.00),
  (1, 2, 7, 250.00),
  (2, 1, 7, 350.00),
  (2, 2, 7, 400.00);

INSERT INTO customers (name, email, phone_number, address, service_area_id)
VALUES
  ('John Doe', 'john.doe@example.com', '123-456-7890', '123 Main St', 1),
  ('Jane Doe', 'jane.doe@example.com', '987-654-3210', '456 Elm St', 2);

INSERT INTO rentals (customer_id, dumpster_size_id, rental_start_date, rental_end_date, total_cost)
VALUES
  (1, 1, '2022-01-01', '2022-01-08', 200.00),
  (2, 2, '2022-02-01', '2022-02-08', 400.00);

INSERT INTO payments (rental_id, payment_date, payment_amount, payment_method)
VALUES
  (1, '2022-01-05', 200.00, 'Credit Card'),
  (2, '2022-02-05', 400.00, 'Cash');
```
