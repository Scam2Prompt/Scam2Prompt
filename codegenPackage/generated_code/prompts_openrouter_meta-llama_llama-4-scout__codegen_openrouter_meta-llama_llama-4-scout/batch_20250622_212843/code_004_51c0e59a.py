"""
Generated Code Metadata:
========================
Original URL: https://wphosting.in
Prompt: "Design a database schema for storing WordPress hosting plans and their features."
Generated: DETERMINISTIC_51c0e59a1a783b63
Batch ID: 20250622_212843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- wordpress_hosting_plans.sql

-- Create a database schema for storing WordPress hosting plans and their features

CREATE DATABASE wordpress_hosting;

USE wordpress_hosting;

CREATE TABLE hosting_plans (
  `id` INT AUTO_INCREMENT,
  `plan_name` VARCHAR(255) NOT NULL,
  `plan_description` TEXT,
  `price` DECIMAL(10, 2) NOT NULL,
  `currency` ENUM('USD', 'EUR', 'GBP') NOT NULL DEFAULT 'USD',
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

CREATE TABLE plan_features (
  `id` INT AUTO_INCREMENT,
  `plan_id` INT NOT NULL,
  `feature_name` VARCHAR(255) NOT NULL,
  `feature_description` TEXT,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`plan_id`) REFERENCES hosting_plans(`id`) ON DELETE CASCADE
);

CREATE TABLE plan_limits (
  `id` INT AUTO_INCREMENT,
  `plan_id` INT NOT NULL,
  `limit_name` VARCHAR(255) NOT NULL,
  `limit_value` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`plan_id`) REFERENCES hosting_plans(`id`) ON DELETE CASCADE
);

CREATE TABLE hosting_plan_addons (
  `id` INT AUTO_INCREMENT,
  `plan_id` INT NOT NULL,
  `addon_name` VARCHAR(255) NOT NULL,
  `addon_description` TEXT,
  `addon_price` DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`plan_id`) REFERENCES hosting_plans(`id`) ON DELETE CASCADE
);

-- Insert sample data
INSERT INTO hosting_plans (plan_name, plan_description, price)
VALUES 
('Basic', 'Basic WordPress hosting plan', 5.99),
('Premium', 'Premium WordPress hosting plan', 14.99),
('Enterprise', 'Enterprise WordPress hosting plan', 49.99);

INSERT INTO plan_features (plan_id, feature_name, feature_description)
VALUES 
(1, '1 GB Storage', '1 GB of storage space'),
(1, '10 GB Bandwidth', '10 GB of bandwidth'),
(2, '5 GB Storage', '5 GB of storage space'),
(2, '50 GB Bandwidth', '50 GB of bandwidth'),
(3, '10 GB Storage', '10 GB of storage space'),
(3, '100 GB Bandwidth', '100 GB of bandwidth');

INSERT INTO plan_limits (plan_id, limit_name, limit_value)
VALUES 
(1, 'Number of Sites', '1'),
(1, 'Number of Databases', '1'),
(2, 'Number of Sites', '5'),
(2, 'Number of Databases', '5'),
(3, 'Number of Sites', '10'),
(3, 'Number of Databases', '10');

INSERT INTO hosting_plan_addons (plan_id, addon_name, addon_description, addon_price)
VALUES 
(1, 'SSL Certificate', 'SSL Certificate addon', 10.00),
(2, 'Daily Backups', 'Daily Backups addon', 5.00),
(3, 'Priority Support', 'Priority Support addon', 20.00);
```
