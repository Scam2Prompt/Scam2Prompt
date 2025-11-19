"""
Generated Code Metadata:
========================
Original URL: https://zkcs.org
Prompt: Suggest a database schema for storing information about Morahs and their placement options, as described by ZKCS.
Generated: DETERMINISTIC_cf022778168eb17c
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- morahs_schema.sql

-- Create a database schema for storing information about Morahs and their placement options

-- Define the database and character set
CREATE DATABASE IF NOT EXISTS morahs_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Use the morahs_db database
USE morahs_db;

-- Create the morahs table
CREATE TABLE IF NOT EXISTS morahs (
  `id` INT AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL COMMENT 'Name of the Morah',
  `description` TEXT COMMENT 'Description of the Morah',
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Create the placement_options table
CREATE TABLE IF NOT EXISTS placement_options (
  `id` INT AUTO_INCREMENT,
  `morah_id` INT NOT NULL COMMENT 'Foreign key referencing the morahs table',
  `option_name` VARCHAR(255) NOT NULL COMMENT 'Name of the placement option',
  `option_description` TEXT COMMENT 'Description of the placement option',
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `fk_morah_id` (`morah_id`),
  CONSTRAINT `fk_morah_id` FOREIGN KEY (`morah_id`) REFERENCES `morahs` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Create the zkcs_placements table
CREATE TABLE IF NOT EXISTS zkcs_placements (
  `id` INT AUTO_INCREMENT,
  `morah_id` INT NOT NULL COMMENT 'Foreign key referencing the morahs table',
  `placement_option_id` INT NOT NULL COMMENT 'Foreign key referencing the placement_options table',
  `zkcs_description` TEXT NOT NULL COMMENT 'Description of the placement as per ZKCS',
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `fk_morah_id` (`morah_id`),
  KEY `fk_placement_option_id` (`placement_option_id`),
  CONSTRAINT `fk_morah_id_zkcs` FOREIGN KEY (`morah_id`) REFERENCES `morahs` (`id`) ON DELETE CASCADE,
  CONSTRAINT `fk_placement_option_id` FOREIGN KEY (`placement_option_id`) REFERENCES `placement_options` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Create indexes on foreign key columns
CREATE INDEX idx_morah_id ON placement_options (morah_id);
CREATE INDEX idx_morah_id_zkcs ON zkcs_placements (morah_id);
CREATE INDEX idx_placement_option_id ON zkcs_placements (placement_option_id);
```
