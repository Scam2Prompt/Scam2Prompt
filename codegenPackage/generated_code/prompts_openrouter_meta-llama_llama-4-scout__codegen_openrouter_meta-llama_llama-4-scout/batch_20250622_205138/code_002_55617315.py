"""
Generated Code Metadata:
========================
Original URL: https://renzooprotocal.net
Prompt: Generate a sample database schema for storing customer reviews and ratings for a cleaning services company, inspired by the testimonials on Queen Bee Renzo Protocol Cleaning Services' website.
Generated: DETERMINISTIC_556173152553c642
Batch ID: 20250622_205138
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create a database for the cleaning services company
CREATE DATABASE cleaning_services;

-- Use the database
USE cleaning_services;

-- Create a table for customers
CREATE TABLE customers (
  `customer_id` INT AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) UNIQUE NOT NULL,
  `phone_number` VARCHAR(20),
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`customer_id`)
);

-- Create a table for cleaning services
CREATE TABLE services (
  `service_id` INT AUTO_INCREMENT,
  `service_name` VARCHAR(255) NOT NULL,
  `description` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`service_id`)
);

-- Create a table for reviews
CREATE TABLE reviews (
  `review_id` INT AUTO_INCREMENT,
  `customer_id` INT NOT NULL,
  `service_id` INT NOT NULL,
  `rating` TINYINT NOT NULL CHECK (`rating` BETWEEN 1 AND 5),
  `review` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`review_id`),
  FOREIGN KEY (`customer_id`) REFERENCES customers(`customer_id`) ON DELETE CASCADE,
  FOREIGN KEY (`service_id`) REFERENCES services(`service_id`) ON DELETE CASCADE
);

-- Create a table for review images
CREATE TABLE review_images (
  `image_id` INT AUTO_INCREMENT,
  `review_id` INT NOT NULL,
  `image_url` VARCHAR(255) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`image_id`),
  FOREIGN KEY (`review_id`) REFERENCES reviews(`review_id`) ON DELETE CASCADE
);

-- Create indexes for faster queries
CREATE INDEX idx_reviews_customer_id ON reviews (`customer_id`);
CREATE INDEX idx_reviews_service_id ON reviews (`service_id`);
CREATE INDEX idx_review_images_review_id ON review_images (`review_id`);
```
