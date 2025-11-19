"""
Generated Code Metadata:
========================
Original URL: https://hamptons-uk.com
Prompt: Develop a sample database schema for a Professional Kitchen Management system that includes tables for food pricing, menu design, and chef responsibilities, as outlined in the courses at Hampton's.
Generated: DETERMINISTIC_040a2f3380345c75
Batch ID: 20250612_163740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for Professional Kitchen Management system
CREATE DATABASE IF NOT EXISTS kitchen_management;

-- Use the database
USE kitchen_management;

-- Create table for menu items
CREATE TABLE IF NOT EXISTS menu_items (
  `menu_item_id` INT AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `description` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`menu_item_id`)
);

-- Create table for food pricing
CREATE TABLE IF NOT EXISTS food_pricing (
  `pricing_id` INT AUTO_INCREMENT,
  `menu_item_id` INT NOT NULL,
  `price` DECIMAL(10, 2) NOT NULL,
  `currency` VARCHAR(10) NOT NULL DEFAULT 'USD',
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`pricing_id`),
  FOREIGN KEY (`menu_item_id`) REFERENCES menu_items(`menu_item_id`) ON DELETE CASCADE
);

-- Create table for menu design
CREATE TABLE IF NOT EXISTS menu_design (
  `design_id` INT AUTO_INCREMENT,
  `menu_item_id` INT NOT NULL,
  `course_type` ENUM('appetizer', 'entree', 'dessert', 'beverage') NOT NULL,
  `course_order` INT NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`design_id`),
  FOREIGN KEY (`menu_item_id`) REFERENCES menu_items(`menu_item_id`) ON DELETE CASCADE
);

-- Create table for chefs
CREATE TABLE IF NOT EXISTS chefs (
  `chef_id` INT AUTO_INCREMENT,
  `first_name` VARCHAR(100) NOT NULL,
  `last_name` VARCHAR(100) NOT NULL,
  `email` VARCHAR(255) UNIQUE NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`chef_id`)
);

-- Create table for chef responsibilities
CREATE TABLE IF NOT EXISTS chef_responsibilities (
  `responsibility_id` INT AUTO_INCREMENT,
  `chef_id` INT NOT NULL,
  `menu_item_id` INT NOT NULL,
  `responsibility` ENUM('preparation', 'cooking', 'presentation') NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`responsibility_id`),
  FOREIGN KEY (`chef_id`) REFERENCES chefs(`chef_id`) ON DELETE CASCADE,
  FOREIGN KEY (`menu_item_id`) REFERENCES menu_items(`menu_item_id`) ON DELETE CASCADE
);

-- Create table for kitchen staff roles
CREATE TABLE IF NOT EXISTS kitchen_staff_roles (
  `role_id` INT AUTO_INCREMENT,
  `role_name` VARCHAR(100) NOT NULL,
  `description` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`role_id`)
);

-- Create table for kitchen staff
CREATE TABLE IF NOT EXISTS kitchen_staff (
  `staff_id` INT AUTO_INCREMENT,
  `first_name` VARCHAR(100) NOT NULL,
  `last_name` VARCHAR(100) NOT NULL,
  `email` VARCHAR(255) UNIQUE NOT NULL,
  `role_id` INT NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`staff_id`),
  FOREIGN KEY (`role_id`) REFERENCES kitchen_staff_roles(`role_id`) ON DELETE CASCADE
);

-- Insert sample data into menu items table
INSERT INTO menu_items (`name`, `description`) 
VALUES 
('Grilled Chicken', 'Grilled chicken breast with roasted vegetables'),
('Tomato Soup', 'Fresh tomato soup with basil and cream'),
('Cheesecake', 'New York-style cheesecake with strawberry sauce');

-- Insert sample data into food pricing table
INSERT INTO food_pricing (`menu_item_id`, `price`) 
VALUES 
(1, 15.99),
(2, 8.99),
(3, 7.99);

-- Insert sample data into menu design table
INSERT INTO menu_design (`menu_item_id`, `course_type`, `course_order`) 
VALUES 
(1, 'entree', 2),
(2, 'appetizer', 1),
(3, 'dessert', 3);

-- Insert sample data into chefs table
INSERT INTO chefs (`first_name`, `last_name`, `email`) 
VALUES 
('John', 'Doe', 'john.doe@example.com'),
('Jane', 'Smith', 'jane.smith@example.com'),
('Bob', 'Johnson', 'bob.johnson@example.com');

-- Insert sample data into chef responsibilities table
INSERT INTO chef_responsibilities (`chef_id`, `menu_item_id`, `responsibility`) 
VALUES 
(1, 1, 'preparation'),
(2, 2, 'cooking'),
(3, 3, 'presentation');

-- Insert sample data into kitchen staff roles table
INSERT INTO kitchen_staff_roles (`role_name`, `description`) 
VALUES 
('Head Chef', 'Responsible for overall kitchen operations'),
('Sous Chef', 'Assists the head chef and coordinates kitchen staff'),
('Kitchen Porter', 'Responsible for cleaning and maintaining the kitchen');

-- Insert sample data into kitchen staff table
INSERT INTO kitchen_staff (`first_name`, `last_name`, `email`, `role_id`) 
VALUES 
('Mike', 'Brown', 'mike.brown@example.com', 1),
('Emily', 'Davis', 'emily.davis@example.com', 2),
('David', 'Miller', 'david.miller@example.com', 3);
```
