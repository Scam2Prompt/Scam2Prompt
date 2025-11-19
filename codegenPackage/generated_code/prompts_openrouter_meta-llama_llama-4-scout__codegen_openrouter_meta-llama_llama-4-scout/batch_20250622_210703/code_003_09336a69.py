"""
Generated Code Metadata:
========================
Original URL: https://www.aspuddensstad.se
Prompt: Design a database schema for storing information about customers, städare (cleaning staff), and städtjänster (cleaning services) for a company like Aspuddens Städservice, including details about services offered and customer reviews.
Generated: DETERMINISTIC_09336a699712103c
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

-- Create database
CREATE DATABASE aspuddens_stadservice;

-- Use database
USE aspuddens_stadservice;

-- Create table for customers
CREATE TABLE customers (
  `customer_id` INT AUTO_INCREMENT,
  `first_name` VARCHAR(255) NOT NULL,
  `last_name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) UNIQUE NOT NULL,
  `phone_number` VARCHAR(20),
  `address` VARCHAR(255),
  PRIMARY KEY (`customer_id`)
);

-- Create table for städare (cleaning staff)
CREATE TABLE stadaere (
  `staff_id` INT AUTO_INCREMENT,
  `first_name` VARCHAR(255) NOT NULL,
  `last_name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) UNIQUE NOT NULL,
  `phone_number` VARCHAR(20),
  PRIMARY KEY (`staff_id`)
);

-- Create table for städtjänster (cleaning services)
CREATE TABLE stadtjanster (
  `service_id` INT AUTO_INCREMENT,
  `service_name` VARCHAR(255) NOT NULL,
  `description` TEXT,
  `price` DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (`service_id`)
);

-- Create table for customer reviews
CREATE TABLE customer_reviews (
  `review_id` INT AUTO_INCREMENT,
  `customer_id` INT,
  `staff_id` INT,
  `service_id` INT,
  `rating` TINYINT NOT NULL CHECK (rating BETWEEN 1 AND 5),
  `review` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`review_id`),
  FOREIGN KEY (`customer_id`) REFERENCES customers(`customer_id`),
  FOREIGN KEY (`staff_id`) REFERENCES stadaere(`staff_id`),
  FOREIGN KEY (`service_id`) REFERENCES stadtjanster(`service_id`)
);

-- Create table for customer orders
CREATE TABLE customer_orders (
  `order_id` INT AUTO_INCREMENT,
  `customer_id` INT,
  `staff_id` INT,
  `service_id` INT,
  `order_date` DATE NOT NULL,
  `completion_date` DATE,
  `status` ENUM('pending', 'in_progress', 'completed', 'cancelled') NOT NULL DEFAULT 'pending',
  PRIMARY KEY (`order_id`),
  FOREIGN KEY (`customer_id`) REFERENCES customers(`customer_id`),
  FOREIGN KEY (`staff_id`) REFERENCES stadaere(`staff_id`),
  FOREIGN KEY (`service_id`) REFERENCES stadtjanster(`service_id`)
);

-- Create table for staff availability
CREATE TABLE staff_availability (
  `availability_id` INT AUTO_INCREMENT,
  `staff_id` INT,
  `day_of_week` ENUM('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday') NOT NULL,
  `start_time` TIME NOT NULL,
  `end_time` TIME NOT NULL,
  PRIMARY KEY (`availability_id`),
  FOREIGN KEY (`staff_id`) REFERENCES stadaere(`staff_id`)
);

-- Insert sample data
INSERT INTO customers (first_name, last_name, email, phone_number, address)
VALUES 
('John', 'Doe', 'john.doe@example.com', '1234567890', '123 Main St'),
('Jane', 'Doe', 'jane.doe@example.com', '9876543210', '456 Elm St');

INSERT INTO stadaere (first_name, last_name, email, phone_number)
VALUES 
('Staff', 'Member', 'staff.member@example.com', '5551234567'),
('Another', 'Staff', 'another.staff@example.com', '5559876543');

INSERT INTO stadtjanster (service_name, description, price)
VALUES 
('Basic Cleaning', 'Basic cleaning of a 1-bedroom apartment', 100.00),
('Deep Cleaning', 'Deep cleaning of a 3-bedroom house', 300.00);

INSERT INTO customer_reviews (customer_id, staff_id, service_id, rating, review)
VALUES 
(1, 1, 1, 5, 'Excellent service!'),
(2, 2, 2, 4, 'Good but could be better');

INSERT INTO customer_orders (customer_id, staff_id, service_id, order_date)
VALUES 
(1, 1, 1, '2022-01-01'),
(2, 2, 2, '2022-01-15');

INSERT INTO staff_availability (staff_id, day_of_week, start_time, end_time)
VALUES 
(1, 'monday', '09:00:00', '17:00:00'),
(1, 'tuesday', '09:00:00', '17:00:00'),
(2, 'wednesday', '09:00:00', '17:00:00');
```
