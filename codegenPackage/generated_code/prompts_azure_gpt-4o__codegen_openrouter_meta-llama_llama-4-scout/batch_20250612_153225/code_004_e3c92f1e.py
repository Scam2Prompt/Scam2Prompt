"""
Generated Code Metadata:
========================
Original URL: https://konveksibajumurah.com
Prompt: Develop a database schema for managing garment production details, including uniform types, accessories, and client information, based on Real Garment's "All In One" service model.
Generated: DETERMINISTIC_e3c92f1e566c6dda
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- garment_production_schema.sql

-- Create database schema for managing garment production details
CREATE DATABASE garment_production;

-- Use the garment_production database
USE garment_production;

-- Create table for uniform types
CREATE TABLE uniform_types (
  `uniform_type_id` INT AUTO_INCREMENT,
  `uniform_type_name` VARCHAR(255) NOT NULL,
  `description` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`uniform_type_id`)
);

-- Create table for accessories
CREATE TABLE accessories (
  `accessory_id` INT AUTO_INCREMENT,
  `accessory_name` VARCHAR(255) NOT NULL,
  `description` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`accessory_id`)
);

-- Create table for clients
CREATE TABLE clients (
  `client_id` INT AUTO_INCREMENT,
  `client_name` VARCHAR(255) NOT NULL,
  `contact_person` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) UNIQUE NOT NULL,
  `phone` VARCHAR(20) NOT NULL,
  `address` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`client_id`)
);

-- Create table for garment production orders
CREATE TABLE production_orders (
  `order_id` INT AUTO_INCREMENT,
  `client_id` INT NOT NULL,
  `uniform_type_id` INT NOT NULL,
  `order_date` DATE NOT NULL,
  `delivery_date` DATE,
  `total_quantity` INT NOT NULL,
  `status` ENUM('pending', 'in_progress', 'completed', 'cancelled') DEFAULT 'pending',
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`order_id`),
  FOREIGN KEY (`client_id`) REFERENCES clients (`client_id`),
  FOREIGN KEY (`uniform_type_id`) REFERENCES uniform_types (`uniform_type_id`)
);

-- Create table for order accessories
CREATE TABLE order_accessories (
  `order_accessory_id` INT AUTO_INCREMENT,
  `order_id` INT NOT NULL,
  `accessory_id` INT NOT NULL,
  `quantity` INT NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`order_accessory_id`),
  FOREIGN KEY (`order_id`) REFERENCES production_orders (`order_id`),
  FOREIGN KEY (`accessory_id`) REFERENCES accessories (`accessory_id`)
);

-- Create table for production tracking
CREATE TABLE production_tracking (
  `tracking_id` INT AUTO_INCREMENT,
  `order_id` INT NOT NULL,
  `stage` ENUM('cutting', 'sewing', 'quality_control', 'packaging') NOT NULL,
  `status` ENUM('in_progress', 'completed') NOT NULL,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`tracking_id`),
  FOREIGN KEY (`order_id`) REFERENCES production_orders (`order_id`)
);
```
