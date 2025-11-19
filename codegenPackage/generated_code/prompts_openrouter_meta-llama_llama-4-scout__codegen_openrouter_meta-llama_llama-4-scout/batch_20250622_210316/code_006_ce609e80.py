"""
Generated Code Metadata:
========================
Original URL: https://suzuki-capital.com
Prompt: Design a database schema for storing information about Suzuki motorcycles, heavy bikes, and cars sold by Suzuki Capital Motors.
Generated: DETERMINISTIC_ce609e80a3430627
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create a database for Suzuki Capital Motors
CREATE DATABASE suzuki_capital_motors;

-- Use the database
USE suzuki_capital_motors;

-- Create a table for motorcycle manufacturers
CREATE TABLE manufacturers (
  manufacturer_id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  PRIMARY KEY (manufacturer_id)
);

-- Create a table for motorcycle models
CREATE TABLE motorcycle_models (
  model_id INT AUTO_INCREMENT,
  manufacturer_id INT NOT NULL,
  model_name VARCHAR(255) NOT NULL,
  model_type ENUM('heavy bike', 'motorcycle') NOT NULL,
  engine_capacity DECIMAL(4, 2) NOT NULL,
  horsepower INT NOT NULL,
  PRIMARY KEY (model_id),
  FOREIGN KEY (manufacturer_id) REFERENCES manufacturers(manufacturer_id)
);

-- Create a table for car models
CREATE TABLE car_models (
  model_id INT AUTO_INCREMENT,
  manufacturer_id INT NOT NULL,
  model_name VARCHAR(255) NOT NULL,
  engine_capacity DECIMAL(4, 2) NOT NULL,
  horsepower INT NOT NULL,
  PRIMARY KEY (model_id),
  FOREIGN KEY (manufacturer_id) REFERENCES manufacturers(manufacturer_id)
);

-- Create a table for vehicles
CREATE TABLE vehicles (
  vehicle_id INT AUTO_INCREMENT,
  model_id INT,
  model_type ENUM('motorcycle', 'heavy bike', 'car') NOT NULL,
  vehicle_type_id INT,
  vin VARCHAR(17) NOT NULL,
  purchase_date DATE NOT NULL,
  sale_date DATE,
  sale_price DECIMAL(10, 2),
  PRIMARY KEY (vehicle_id)
);

-- Create a table for motorcycle vehicle details
CREATE TABLE motorcycle_vehicle_details (
  vehicle_id INT NOT NULL,
  mileage INT,
  fuel_type ENUM('gasoline', 'diesel', 'electric') NOT NULL,
  PRIMARY KEY (vehicle_id),
  FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id)
);

-- Create a table for car vehicle details
CREATE TABLE car_vehicle_details (
  vehicle_id INT NOT NULL,
  mileage INT,
  transmission_type ENUM('automatic', 'manual') NOT NULL,
  PRIMARY KEY (vehicle_id),
  FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id)
);

-- Create a table for customers
CREATE TABLE customers (
  customer_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  address VARCHAR(255) NOT NULL,
  PRIMARY KEY (customer_id)
);

-- Create a table for sales
CREATE TABLE sales (
  sale_id INT AUTO_INCREMENT,
  vehicle_id INT NOT NULL,
  customer_id INT NOT NULL,
  sale_date DATE NOT NULL,
  sale_price DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (sale_id),
  FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id),
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Create a table for employees
CREATE TABLE employees (
  employee_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  role ENUM('sales', 'manager') NOT NULL,
  PRIMARY KEY (employee_id)
);

-- Create a table for employee sales
CREATE TABLE employee_sales (
  employee_id INT NOT NULL,
  sale_id INT NOT NULL,
  PRIMARY KEY (employee_id, sale_id),
  FOREIGN KEY (employee_id) REFERENCES employees(employee_id),
  FOREIGN KEY (sale_id) REFERENCES sales(sale_id)
);

-- Insert sample data
INSERT INTO manufacturers (name) 
VALUES 
('Suzuki');

INSERT INTO motorcycle_models (manufacturer_id, model_name, model_type, engine_capacity, horsepower) 
VALUES 
(1, 'Hayabusa', 'heavy bike', 1340.00, 187),
(1, 'GSX-R1000', 'motorcycle', 999.00, 186);

INSERT INTO car_models (manufacturer_id, model_name, engine_capacity, horsepower) 
VALUES 
(1, 'Swift', 1197.00, 82),
(1, 'S-Cross', 1598.00, 103);

INSERT INTO customers (first_name, last_name, email, phone_number, address) 
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St'),
('Jane', 'Doe', 'jane.doe@example.com', '987-654-3210', '456 Elm St');

INSERT INTO employees (first_name, last_name, email, phone_number, role) 
VALUES 
('Bob', 'Smith', 'bob.smith@example.com', '555-123-4567', 'sales'),
('Alice', 'Johnson', 'alice.johnson@example.com', '555-987-6543', 'manager');

INSERT INTO vehicles (model_id, model_type, vehicle_type_id, vin, purchase_date) 
VALUES 
(1, 'heavy bike', 1, 'KTMXSXSUZ123', '2022-01-01'),
(2, 'motorcycle', 2, 'GSXRKNT12345', '2022-02-01'),
(3, 'car', 3, 'SZCX123456789', '2022-03-01');

INSERT INTO motorcycle_vehicle_details (vehicle_id, mileage, fuel_type) 
VALUES 
(1, 0, 'gasoline'),
(2, 0, 'gasoline');

INSERT INTO car_vehicle_details (vehicle_id, mileage, transmission_type) 
VALUES 
(3, 0, 'automatic');

INSERT INTO sales (vehicle_id, customer_id, sale_date, sale_price) 
VALUES 
(1, 1, '2022-04-01', 14999.99),
(2, 2, '2022-05-01', 12999.99),
(3, 1, '2022-06-01', 17999.99);

INSERT INTO employee_sales (employee_id, sale_id) 
VALUES 
(1, 1),
(1, 2),
(2, 3);
```
