"""
Generated Code Metadata:
========================
Original URL: https://kallimos.com
Prompt: Design a database schema for storing information about residents in a Kallimos community, ensuring it supports multi-generational and multi-ability inclusivity.
Generated: DETERMINISTIC_558cfecaa0260f13
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- kallimos_community_schema.sql

-- Create a database for the Kallimos community
CREATE DATABASE kallimos_community;

-- Use the kallimos_community database
USE kallimos_community;

-- Create a table for residents
CREATE TABLE residents (
  `id` INT AUTO_INCREMENT,
  `first_name` VARCHAR(255) NOT NULL,
  `last_name` VARCHAR(255) NOT NULL,
  `date_of_birth` DATE,
  `email` VARCHAR(255) UNIQUE,
  `phone_number` VARCHAR(20),
  `address` VARCHAR(255),
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create a table for abilities
CREATE TABLE abilities (
  `id` INT AUTO_INCREMENT,
  `ability_name` VARCHAR(255) NOT NULL,
  `description` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create a table for resident abilities
CREATE TABLE resident_abilities (
  `id` INT AUTO_INCREMENT,
  `resident_id` INT,
  `ability_id` INT,
  `level` ENUM('beginner', 'intermediate', 'advanced'),
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`resident_id`) REFERENCES residents(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`ability_id`) REFERENCES abilities(`id`) ON DELETE CASCADE
);

-- Create a table for family relationships
CREATE TABLE family_relationships (
  `id` INT AUTO_INCREMENT,
  `resident_id` INT,
  `relative_id` INT,
  `relationship` ENUM('parent', 'child', 'spouse', 'sibling'),
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`resident_id`) REFERENCES residents(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`relative_id`) REFERENCES residents(`id`) ON DELETE CASCADE
);

-- Create a table for accessibility needs
CREATE TABLE accessibility_needs (
  `id` INT AUTO_INCREMENT,
  `need_name` VARCHAR(255) NOT NULL,
  `description` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create a table for resident accessibility needs
CREATE TABLE resident_accessibility_needs (
  `id` INT AUTO_INCREMENT,
  `resident_id` INT,
  `need_id` INT,
  `accommodation` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`resident_id`) REFERENCES residents(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`need_id`) REFERENCES accessibility_needs(`id`) ON DELETE CASCADE
);

-- Example insert statements
INSERT INTO residents (first_name, last_name, date_of_birth, email, phone_number, address)
VALUES 
('John', 'Doe', '1990-01-01', 'john.doe@example.com', '123-456-7890', '123 Main St'),
('Jane', 'Doe', '1995-01-01', 'jane.doe@example.com', '987-654-3210', '456 Elm St');

INSERT INTO abilities (ability_name, description)
VALUES 
('Swimming', 'Ability to swim'),
('Cooking', 'Ability to cook');

INSERT INTO resident_abilities (resident_id, ability_id, level)
VALUES 
(1, 1, 'advanced'),
(2, 2, 'beginner');

INSERT INTO family_relationships (resident_id, relative_id, relationship)
VALUES 
(1, 2, 'spouse');

INSERT INTO accessibility_needs (need_name, description)
VALUES 
('Wheelchair accessibility', 'Need for wheelchair accessible areas');

INSERT INTO resident_accessibility_needs (resident_id, need_id, accommodation)
VALUES 
(1, 1, 'Ramps and elevators');
```
