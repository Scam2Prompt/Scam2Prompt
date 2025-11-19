"""
Generated Code Metadata:
========================
Original URL: https://superiortitlemontana.com
Prompt: Create a database schema for storing property information, title transaction details, and client communication logs, tailored to the services offered by Superior Title Montana.
Generated: DETERMINISTIC_14ffc20f30ddc9e5
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for Superior Title Montana

-- Create database
CREATE DATABASE superior_title_montana;

-- Use database
USE superior_title_montana;

-- Create table for properties
CREATE TABLE properties (
    `id` INT AUTO_INCREMENT,
    `property_address` VARCHAR(255) NOT NULL,
    `city` VARCHAR(100) NOT NULL,
    `state` VARCHAR(100) NOT NULL,
    `zip` VARCHAR(20) NOT NULL,
    `property_type` ENUM('residential', 'commercial') NOT NULL,
    `acreage` DECIMAL(10, 2),
    `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`)
);

-- Create table for title transactions
CREATE TABLE title_transactions (
    `id` INT AUTO_INCREMENT,
    `property_id` INT NOT NULL,
    `transaction_type` ENUM('title_search', 'title_insurance', 'escrow') NOT NULL,
    `transaction_date` DATE NOT NULL,
    `transaction_amount` DECIMAL(10, 2) NOT NULL,
    `status` ENUM('pending', 'completed', 'cancelled') NOT NULL DEFAULT 'pending',
    `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    FOREIGN KEY (`property_id`) REFERENCES properties(`id`) ON DELETE CASCADE
);

-- Create table for clients
CREATE TABLE clients (
    `id` INT AUTO_INCREMENT,
    `first_name` VARCHAR(100) NOT NULL,
    `last_name` VARCHAR(100) NOT NULL,
    `email` VARCHAR(255) UNIQUE NOT NULL,
    `phone` VARCHAR(20) NOT NULL,
    `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`)
);

-- Create table for client communication logs
CREATE TABLE communication_logs (
    `id` INT AUTO_INCREMENT,
    `client_id` INT NOT NULL,
    `property_id` INT,
    `communication_type` ENUM('email', 'phone', 'in_person') NOT NULL,
    `communication_date` DATE NOT NULL,
    `description` TEXT NOT NULL,
    `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    FOREIGN KEY (`client_id`) REFERENCES clients(`id`) ON DELETE CASCADE,
    FOREIGN KEY (`property_id`) REFERENCES properties(`id`) ON DELETE SET NULL
);

-- Create table for title officers
CREATE TABLE title_officers (
    `id` INT AUTO_INCREMENT,
    `first_name` VARCHAR(100) NOT NULL,
    `last_name` VARCHAR(100) NOT NULL,
    `email` VARCHAR(255) UNIQUE NOT NULL,
    `phone` VARCHAR(20) NOT NULL,
    `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`)
);

-- Create table for title transaction assignments
CREATE TABLE transaction_assignments (
    `id` INT AUTO_INCREMENT,
    `title_transaction_id` INT NOT NULL,
    `title_officer_id` INT NOT NULL,
    `assigned_date` DATE NOT NULL,
    `completed_date` DATE,
    `status` ENUM('assigned', 'in_progress', 'completed') NOT NULL DEFAULT 'assigned',
    `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    FOREIGN KEY (`title_transaction_id`) REFERENCES title_transactions(`id`) ON DELETE CASCADE,
    FOREIGN KEY (`title_officer_id`) REFERENCES title_officers(`id`) ON DELETE CASCADE
);
```
