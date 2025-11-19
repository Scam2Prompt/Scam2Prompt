"""
Generated Code Metadata:
========================
Original URL: https://fdanongbualamphu.com
Prompt: How can I create a database schema to manage documents for health product regulations and consultations as outlined by the หนองบัวลำภู health authorities?
Generated: DETERMINISTIC_fe34fafc2c8bca5d
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for health product regulations and consultations
CREATE DATABASE health_regulations;

-- Use the database
USE health_regulations;

-- Create a table for health products
CREATE TABLE health_products (
  `id` INT AUTO_INCREMENT,
  `product_name` VARCHAR(255) NOT NULL,
  `product_description` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create a table for regulations
CREATE TABLE regulations (
  `id` INT AUTO_INCREMENT,
  `regulation_name` VARCHAR(255) NOT NULL,
  `regulation_description` TEXT,
  `regulation_type` ENUM('law', 'guideline', 'policy') NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create a table for consultations
CREATE TABLE consultations (
  `id` INT AUTO_INCREMENT,
  `consultation_date` DATE NOT NULL,
  `consultation_description` TEXT,
  `health_product_id` INT,
  `regulation_id` INT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`health_product_id`) REFERENCES health_products(`id`),
  FOREIGN KEY (`regulation_id`) REFERENCES regulations(`id`)
);

-- Create a table for documents
CREATE TABLE documents (
  `id` INT AUTO_INCREMENT,
  `document_name` VARCHAR(255) NOT NULL,
  `document_type` ENUM('regulation', 'consultation', 'health_product') NOT NULL,
  `document_content` BLOB,
  `health_product_id` INT,
  `regulation_id` INT,
  `consultation_id` INT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`health_product_id`) REFERENCES health_products(`id`),
  FOREIGN KEY (`regulation_id`) REFERENCES regulations(`id`),
  FOREIGN KEY (`consultation_id`) REFERENCES consultations(`id`)
);

-- Create a table for users
CREATE TABLE users (
  `id` INT AUTO_INCREMENT,
  `username` VARCHAR(255) NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `role` ENUM('admin', 'staff', 'public') NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create a table for document revisions
CREATE TABLE document_revisions (
  `id` INT AUTO_INCREMENT,
  `document_id` INT NOT NULL,
  `revision_date` DATE NOT NULL,
  `revision_description` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`document_id`) REFERENCES documents(`id`)
);

-- Create indexes on foreign key columns
CREATE INDEX idx_health_product_id ON consultations (health_product_id);
CREATE INDEX idx_regulation_id ON consultations (regulation_id);
CREATE INDEX idx_health_product_id ON documents (health_product_id);
CREATE INDEX idx_regulation_id ON documents (regulation_id);
CREATE INDEX idx_consultation_id ON documents (consultation_id);
CREATE INDEX idx_document_id ON document_revisions (document_id);
```
