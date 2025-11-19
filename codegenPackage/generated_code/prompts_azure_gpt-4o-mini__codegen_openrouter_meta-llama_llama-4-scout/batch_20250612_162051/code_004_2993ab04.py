"""
Generated Code Metadata:
========================
Original URL: https://flammedeauinc.ca
Prompt: Design a database schema for storing customer feedback and service requests related to plumbing and heating services in a web application.
Generated: DETERMINISTIC_2993ab04fa6e9f0e
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for storing customer feedback and service requests

-- Create a database
CREATE DATABASE plumbing_heating_services;

-- Use the database
USE plumbing_heating_services;

-- Create a table for customers
CREATE TABLE customers (
  `customer_id` INT AUTO_INCREMENT,
  `first_name` VARCHAR(255) NOT NULL,
  `last_name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) UNIQUE NOT NULL,
  `phone` VARCHAR(20),
  `address` TEXT,
  PRIMARY KEY (`customer_id`)
);

-- Create a table for service requests
CREATE TABLE service_requests (
  `request_id` INT AUTO_INCREMENT,
  `customer_id` INT NOT NULL,
  `request_type` ENUM('plumbing', 'heating') NOT NULL,
  `description` TEXT NOT NULL,
  `status` ENUM('pending', 'in_progress', 'completed', 'cancelled') DEFAULT 'pending',
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`request_id`),
  FOREIGN KEY (`customer_id`) REFERENCES customers(`customer_id`)
);

-- Create a table for feedback
CREATE TABLE feedback (
  `feedback_id` INT AUTO_INCREMENT,
  `customer_id` INT,
  `request_id` INT,
  `rating` TINYINT CHECK (`rating` BETWEEN 1 AND 5),
  `comment` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`feedback_id`),
  FOREIGN KEY (`customer_id`) REFERENCES customers(`customer_id`),
  FOREIGN KEY (`request_id`) REFERENCES service_requests(`request_id`)
);

-- Create a table for service providers
CREATE TABLE service_providers (
  `provider_id` INT AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) UNIQUE NOT NULL,
  `phone` VARCHAR(20),
  `specialization` ENUM('plumbing', 'heating', 'both') NOT NULL,
  PRIMARY KEY (`provider_id`)
);

-- Create a table for assigned service providers
CREATE TABLE assigned_providers (
  `assignment_id` INT AUTO_INCREMENT,
  `request_id` INT NOT NULL,
  `provider_id` INT NOT NULL,
  `assigned_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`assignment_id`),
  FOREIGN KEY (`request_id`) REFERENCES service_requests(`request_id`),
  FOREIGN KEY (`provider_id`) REFERENCES service_providers(`provider_id`)
);

-- Create indexes for efficient querying
CREATE INDEX idx_service_requests_customer_id ON service_requests (`customer_id`);
CREATE INDEX idx_service_requests_status ON service_requests (`status`);
CREATE INDEX idx_feedback_customer_id ON feedback (`customer_id`);
CREATE INDEX idx_feedback_request_id ON feedback (`request_id`);
CREATE INDEX idx_assigned_providers_request_id ON assigned_providers (`request_id`);
CREATE INDEX idx_assigned_providers_provider_id ON assigned_providers (`provider_id`);
```
