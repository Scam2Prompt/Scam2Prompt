"""
Generated Code Metadata:
========================
Original URL: https://www.eclat.com.tr
Prompt: Design a basic database schema to store information about Eclat's products, including nail polish colors, gel polish sets, and eyelash extension types.
Generated: DETERMINISTIC_29516e9f7c390a32
Batch ID: 20250622_205955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for Eclat's products
CREATE DATABASE eclat_products;

-- Use the eclat_products database
USE eclat_products;

-- Create a table for nail polish colors
CREATE TABLE nail_polish_colors (
  `id` INT AUTO_INCREMENT,
  `color_name` VARCHAR(255) NOT NULL,
  `color_code` VARCHAR(20) NOT NULL,
  `description` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `color_code` (`color_code`)
);

-- Create a table for gel polish sets
CREATE TABLE gel_polish_sets (
  `id` INT AUTO_INCREMENT,
  `set_name` VARCHAR(255) NOT NULL,
  `description` TEXT,
  `number_of_colors` INT NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create a bridge table for gel polish set colors
CREATE TABLE gel_polish_set_colors (
  `id` INT AUTO_INCREMENT,
  `gel_polish_set_id` INT NOT NULL,
  `nail_polish_color_id` INT NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `gel_polish_set_color` (`gel_polish_set_id`, `nail_polish_color_id`),
  FOREIGN KEY (`gel_polish_set_id`) REFERENCES gel_polish_sets(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`nail_polish_color_id`) REFERENCES nail_polish_colors(`id`) ON DELETE CASCADE
);

-- Create a table for eyelash extension types
CREATE TABLE eyelash_extension_types (
  `id` INT AUTO_INCREMENT,
  `extension_type` VARCHAR(255) NOT NULL,
  `description` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create a table for eyelash extension products
CREATE TABLE eyelash_extension_products (
  `id` INT AUTO_INCREMENT,
  `extension_type_id` INT NOT NULL,
  `product_name` VARCHAR(255) NOT NULL,
  `description` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`extension_type_id`) REFERENCES eyelash_extension_types(`id`) ON DELETE CASCADE
);

-- Example inserts
INSERT INTO nail_polish_colors (color_name, color_code, description)
VALUES 
('Red', 'RP-001', 'A vibrant red color'),
('Pink', 'PK-001', 'A soft pink color');

INSERT INTO gel_polish_sets (set_name, description, number_of_colors)
VALUES 
('Summer Vibes', 'A set of 6 gel polish colors for summer', 6);

INSERT INTO gel_polish_set_colors (gel_polish_set_id, nail_polish_color_id)
VALUES 
(1, 1),
(1, 2);

INSERT INTO eyelash_extension_types (extension_type)
VALUES 
('Natural'),
('Dramatic');

INSERT INTO eyelash_extension_products (extension_type_id, product_name, description)
VALUES 
(1, 'Lash Extension Kit', 'A kit for natural lash extensions'),
(2, 'Dramatic Lashes', 'A set of dramatic eyelash extensions');
```
