"""
Generated Code Metadata:
========================
Original URL: https://microrentacar.biz
Prompt: Create a database schema for managing car rental services, including categories like luxury cars, wedding cars, and trip vehicles, based on the offerings of Micro Rent a Car.
Generated: DETERMINISTIC_f448ae1321f8c406
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for car rental services
CREATE DATABASE car_rental;

-- Use the car_rental database
USE car_rental;

-- Create table for vehicle categories
CREATE TABLE vehicle_categories (
  id INT AUTO_INCREMENT,
  category_name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for vehicles
CREATE TABLE vehicles (
  id INT AUTO_INCREMENT,
  category_id INT NOT NULL,
  vehicle_type VARCHAR(255) NOT NULL,
  make VARCHAR(100) NOT NULL,
  model VARCHAR(100) NOT NULL,
  year INT NOT NULL,
  rental_price DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (category_id) REFERENCES vehicle_categories(id) ON DELETE CASCADE
);

-- Create table for luxury cars
CREATE TABLE luxury_cars (
  id INT AUTO_INCREMENT,
  vehicle_id INT NOT NULL,
  features TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (vehicle_id) REFERENCES vehicles(id) ON DELETE CASCADE
);

-- Create table for wedding cars
CREATE TABLE wedding_cars (
  id INT AUTO_INCREMENT,
  vehicle_id INT NOT NULL,
  wedding_features TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (vehicle_id) REFERENCES vehicles(id) ON DELETE CASCADE
);

-- Create table for trip vehicles
CREATE TABLE trip_vehicles (
  id INT AUTO_INCREMENT,
  vehicle_id INT NOT NULL,
  trip_features TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (vehicle_id) REFERENCES vehicles(id) ON DELETE CASCADE
);

-- Create table for customers
CREATE TABLE customers (
  id INT AUTO_INCREMENT,
  first_name VARCHAR(100) NOT NULL,
  last_name VARCHAR(100) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  address TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for rentals
CREATE TABLE rentals (
  id INT AUTO_INCREMENT,
  customer_id INT NOT NULL,
  vehicle_id INT NOT NULL,
  rental_date DATE NOT NULL,
  return_date DATE,
  rental_status VARCHAR(50) NOT NULL DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE CASCADE,
  FOREIGN KEY (vehicle_id) REFERENCES vehicles(id) ON DELETE CASCADE
);

-- Create table for payments
CREATE TABLE payments (
  id INT AUTO_INCREMENT,
  rental_id INT NOT NULL,
  payment_method VARCHAR(50) NOT NULL,
  payment_date DATE NOT NULL,
  amount DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (rental_id) REFERENCES rentals(id) ON DELETE CASCADE
);

-- Insert some sample data
INSERT INTO vehicle_categories (category_name, description) 
VALUES 
('Luxury Cars', 'High-end vehicles for special occasions'),
('Wedding Cars', 'Vehicles for wedding transportation'),
('Trip Vehicles', 'Cars for road trips and travel');

INSERT INTO vehicles (category_id, vehicle_type, make, model, year, rental_price) 
VALUES 
(1, 'Sedan', 'Mercedes-Benz', 'S-Class', 2022, 200.00),
(2, 'Limousine', 'Cadillac', 'Escalade', 2020, 300.00),
(3, 'SUV', 'Toyota', 'Land Cruiser', 2019, 150.00);

INSERT INTO luxury_cars (vehicle_id, features) 
VALUES 
(1, 'GPS, Leather Seats, Sunroof');

INSERT INTO wedding_cars (vehicle_id, wedding_features) 
VALUES 
(2, 'Decorated Interior, Champagne Cooler');

INSERT INTO trip_vehicles (vehicle_id, trip_features) 
VALUES 
(3, '4WD, Roof Rack, Navigation');

INSERT INTO customers (first_name, last_name, email, phone_number, address) 
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St');

INSERT INTO rentals (customer_id, vehicle_id, rental_date, return_date) 
VALUES 
(1, 1, '2024-09-01', '2024-09-05');

INSERT INTO payments (rental_id, payment_method, payment_date, amount) 
VALUES 
(1, 'Credit Card', '2024-09-01', 1000.00);
```
