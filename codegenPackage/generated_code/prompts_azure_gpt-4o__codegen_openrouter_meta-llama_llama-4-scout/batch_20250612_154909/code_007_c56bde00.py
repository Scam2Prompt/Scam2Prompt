"""
Generated Code Metadata:
========================
Original URL: https://paradigmgroup.co.ug
Prompt: Create a database schema for managing merchant acquisition and activation data, inspired by Paradigm Group's MTN Momo projects in South Africa.
Generated: DETERMINISTIC_c56bde002fbc6d67
Batch ID: 20250612_154909
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for merchant acquisition and activation data

CREATE DATABASE merchant_acquisition;

USE merchant_acquisition;

-- Create table for merchants
CREATE TABLE merchants (
  `id` INT AUTO_INCREMENT,
  `business_name` VARCHAR(255) NOT NULL,
  `registration_number` VARCHAR(50) NOT NULL,
  `email` VARCHAR(100) NOT NULL UNIQUE,
  `phone_number` VARCHAR(20) NOT NULL,
  `physical_address` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create table for merchant acquisition channels
CREATE TABLE acquisition_channels (
  `id` INT AUTO_INCREMENT,
  `channel_name` VARCHAR(100) NOT NULL,
  `description` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create table for merchant acquisition data
CREATE TABLE merchant_acquisitions (
  `id` INT AUTO_INCREMENT,
  `merchant_id` INT NOT NULL,
  `acquisition_channel_id` INT NOT NULL,
  `acquisition_date` DATE NOT NULL,
  `status` ENUM('pending', 'active', 'inactive') DEFAULT 'pending',
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`merchant_id`) REFERENCES merchants(`id`),
  FOREIGN KEY (`acquisition_channel_id`) REFERENCES acquisition_channels(`id`)
);

-- Create table for merchant activation data
CREATE TABLE merchant_activations (
  `id` INT AUTO_INCREMENT,
  `merchant_id` INT NOT NULL,
  `activation_date` DATE NOT NULL,
  `activation_status` ENUM('pending', 'active', 'failed') DEFAULT 'pending',
  `failure_reason` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`merchant_id`) REFERENCES merchants(`id`)
);

-- Create table for merchant documents
CREATE TABLE merchant_documents (
  `id` INT AUTO_INCREMENT,
  `merchant_id` INT NOT NULL,
  `document_type` ENUM('id', 'proof_of_address', 'business_registration') NOT NULL,
  `document_url` VARCHAR(255) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`merchant_id`) REFERENCES merchants(`id`)
);

-- Create table for merchant users
CREATE TABLE merchant_users (
  `id` INT AUTO_INCREMENT,
  `merchant_id` INT NOT NULL,
  `username` VARCHAR(100) NOT NULL,
  `email` VARCHAR(100) NOT NULL UNIQUE,
  `password_hash` VARCHAR(255) NOT NULL,
  `role` ENUM('admin', 'user') DEFAULT 'user',
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`merchant_id`) REFERENCES merchants(`id`)
);

-- Create indexes for faster queries
CREATE INDEX idx_merchant_acquisitions_merchant_id ON merchant_acquisitions (merchant_id);
CREATE INDEX idx_merchant_acquisitions_acquisition_channel_id ON merchant_acquisitions (acquisition_channel_id);
CREATE INDEX idx_merchant_activations_merchant_id ON merchant_activations (merchant_id);
CREATE INDEX idx_merchant_documents_merchant_id ON merchant_documents (merchant_id);
CREATE INDEX idx_merchant_users_merchant_id ON merchant_users (merchant_id);
```
