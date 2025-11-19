"""
Generated Code Metadata:
========================
Original URL: https://frigoterm.ro
Prompt: "Design a database schema to store information about various air conditioning systems, including their specifications and prices, similar to those listed on frigoterm.ro."
Generated: DETERMINISTIC_76db6eff4a9e177a
Batch ID: 20250622_212031
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/samsung_ar09txhq.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/lg_s09eq.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/daikin_ftxs35axv.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```sql
-- air_conditioning_systems.sql

-- Create database schema
CREATE DATABASE IF NOT EXISTS air_conditioning_systems;

-- Use database schema
USE air_conditioning_systems;

-- Create table for manufacturers
CREATE TABLE IF NOT EXISTS manufacturers (
  `id` INT AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `description` TEXT,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_manufacturer_name` (`name`)
);

-- Create table for air conditioning systems
CREATE TABLE IF NOT EXISTS air_conditioning_systems (
  `id` INT AUTO_INCREMENT,
  `manufacturer_id` INT NOT NULL,
  `model` VARCHAR(255) NOT NULL,
  `type` ENUM('window', 'split', 'inverter', 'portable') NOT NULL,
  `cooling_capacity` DECIMAL(10, 2) NOT NULL, -- in BTU
  `heating_capacity` DECIMAL(10, 2), -- in BTU
  `energy_efficiency_class` ENUM('A', 'A+', 'A++', 'A+++') NOT NULL,
  `noise_level` DECIMAL(5, 2) NOT NULL, -- in dB
  `refrigerant` VARCHAR(50) NOT NULL,
  `weight` DECIMAL(10, 2) NOT NULL, -- in kg
  `dimensions` VARCHAR(100), -- LxWxH in cm
  PRIMARY KEY (`id`),
  FOREIGN KEY (`manufacturer_id`) REFERENCES manufacturers(`id`)
);

-- Create table for prices
CREATE TABLE IF NOT EXISTS prices (
  `id` INT AUTO_INCREMENT,
  `air_conditioning_system_id` INT NOT NULL,
  `price` DECIMAL(15, 2) NOT NULL, -- in RON
  `vat_included` BOOLEAN NOT NULL DEFAULT 1,
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`air_conditioning_system_id`) REFERENCES air_conditioning_systems(`id`)
);

-- Create table for product images
CREATE TABLE IF NOT EXISTS product_images (
  `id` INT AUTO_INCREMENT,
  `air_conditioning_system_id` INT NOT NULL,
  `image_url` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`air_conditioning_system_id`) REFERENCES air_conditioning_systems(`id`)
);

-- Insert sample data
INSERT INTO manufacturers (`name`, `description`) 
VALUES 
('Daikin', 'Japanese multinational company'),
('LG', 'South Korean multinational company'),
('Samsung', 'South Korean multinational company');

INSERT INTO air_conditioning_systems (
  `manufacturer_id`, 
  `model`, 
  `type`, 
  `cooling_capacity`, 
  `energy_efficiency_class`, 
  `noise_level`, 
  `refrigerant`, 
  `weight`, 
  `dimensions`
) 
VALUES 
(1, 'FTXS35AXV', 'inverter', 12000.00, 'A++', 22.00, 'R-410A', 45.00, '95x25x78'),
(2, 'S09EQ', 'split', 9000.00, 'A+', 21.00, 'R-32', 30.00, '75x20x55'),
(3, 'AR09TXHQ', 'inverter', 9000.00, 'A+++', 20.00, 'R-410A', 40.00, '85x24x65');

INSERT INTO prices (`air_conditioning_system_id`, `price`, `vat_included`) 
VALUES 
(1, 3499.00, 1),
(2, 2499.00, 1),
(3, 3999.00, 1);

INSERT INTO product_images (`air_conditioning_system_id`, `image_url`) 
VALUES 
(1, 'https://example.com/daikin_ftxs35axv.jpg'),
(2, 'https://example.com/lg_s09eq.jpg'),
(3, 'https://example.com/samsung_ar09txhq.jpg');
```
