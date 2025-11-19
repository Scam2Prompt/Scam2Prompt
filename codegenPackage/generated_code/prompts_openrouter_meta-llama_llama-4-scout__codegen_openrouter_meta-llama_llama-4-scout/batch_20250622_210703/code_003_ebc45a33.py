"""
Generated Code Metadata:
========================
Original URL: https://fenceguys4u.com
Prompt: "Design a database schema to store information about customers, projects, and services offered by a fence, deck, and pergola installation company, including fields for customer satisfaction ratings and project completion dates."
Generated: DETERMINISTIC_ebc45a33555c8a23
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
CREATE DATABASE IF NOT EXISTS installation_company;

-- Use database
USE installation_company;

-- Create customers table
CREATE TABLE IF NOT EXISTS customers (
  `customer_id` INT AUTO_INCREMENT,
  `first_name` VARCHAR(255) NOT NULL,
  `last_name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) UNIQUE NOT NULL,
  `phone` VARCHAR(20) NOT NULL,
  `address` TEXT,
  PRIMARY KEY (`customer_id`)
);

-- Create projects table
CREATE TABLE IF NOT EXISTS projects (
  `project_id` INT AUTO_INCREMENT,
  `customer_id` INT NOT NULL,
  `project_type` ENUM('fence', 'deck', 'pergola') NOT NULL,
  `project_description` TEXT,
  `project_start_date` DATE NOT NULL,
  `project_completion_date` DATE,
  `project_status` ENUM('in_progress', 'completed', 'cancelled') NOT NULL DEFAULT 'in_progress',
  PRIMARY KEY (`project_id`),
  FOREIGN KEY (`customer_id`) REFERENCES customers(`customer_id`) ON DELETE CASCADE
);

-- Create services table
CREATE TABLE IF NOT EXISTS services (
  `service_id` INT AUTO_INCREMENT,
  `service_name` VARCHAR(255) NOT NULL,
  `service_description` TEXT,
  `service_price` DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (`service_id`)
);

-- Create project_services table (many-to-many relationship)
CREATE TABLE IF NOT EXISTS project_services (
  `project_id` INT NOT NULL,
  `service_id` INT NOT NULL,
  PRIMARY KEY (`project_id`, `service_id`),
  FOREIGN KEY (`project_id`) REFERENCES projects(`project_id`) ON DELETE CASCADE,
  FOREIGN KEY (`service_id`) REFERENCES services(`service_id`) ON DELETE CASCADE
);

-- Create customer_satisfaction_ratings table
CREATE TABLE IF NOT EXISTS customer_satisfaction_ratings (
  `rating_id` INT AUTO_INCREMENT,
  `project_id` INT NOT NULL,
  `rating` TINYINT NOT NULL CHECK (`rating` BETWEEN 1 AND 5),
  `review` TEXT,
  PRIMARY KEY (`rating_id`),
  FOREIGN KEY (`project_id`) REFERENCES projects(`project_id`) ON DELETE CASCADE
);

-- Example data
INSERT INTO customers (first_name, last_name, email, phone, address)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St'),
('Jane', 'Doe', 'jane.doe@example.com', '987-654-3210', '456 Elm St');

INSERT INTO projects (customer_id, project_type, project_description, project_start_date)
VALUES 
(1, 'fence', 'Install a 6ft wooden fence', '2022-01-01'),
(2, 'deck', 'Build a 10x10 deck', '2022-06-01');

INSERT INTO services (service_name, service_description, service_price)
VALUES 
('Fence Installation', 'Install a fence', 1000.00),
('Deck Building', 'Build a deck', 2000.00),
('Pergola Installation', 'Install a pergola', 1500.00);

INSERT INTO project_services (project_id, service_id)
VALUES 
(1, 1),
(2, 2);

INSERT INTO customer_satisfaction_ratings (project_id, rating, review)
VALUES 
(1, 5, 'Great job!'),
(2, 4, 'Good work, but some delays.');
```
