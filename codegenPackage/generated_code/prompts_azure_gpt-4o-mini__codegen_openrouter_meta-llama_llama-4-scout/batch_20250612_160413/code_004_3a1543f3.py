"""
Generated Code Metadata:
========================
Original URL: https://myflowfoundationke.org
Prompt: Design a data model in SQL to manage the records of girls impacted by menstrual health initiatives, similar to the tracking done by My Flow Foundation.
Generated: DETERMINISTIC_3a1543f3ceb01dfb
Batch ID: 20250612_160413
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for menstrual health initiative records
CREATE DATABASE menstrual_health;

-- Use the database
USE menstrual_health;

-- Create a table for girls impacted
CREATE TABLE girls_impacted (
  `id` INT AUTO_INCREMENT,
  `first_name` VARCHAR(255) NOT NULL,
  `last_name` VARCHAR(255) NOT NULL,
  `date_of_birth` DATE NOT NULL,
  `address` VARCHAR(255),
  `phone_number` VARCHAR(20),
  `email` VARCHAR(100) UNIQUE,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create a table for initiatives
CREATE TABLE initiatives (
  `id` INT AUTO_INCREMENT,
  `initiative_name` VARCHAR(255) NOT NULL,
  `description` TEXT,
  `start_date` DATE NOT NULL,
  `end_date` DATE,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create a table for interventions
CREATE TABLE interventions (
  `id` INT AUTO_INCREMENT,
  `girl_id` INT NOT NULL,
  `initiative_id` INT NOT NULL,
  `intervention_type` ENUM('menstrual_product_distribution', 'education_session', 'health_checkup') NOT NULL,
  `intervention_date` DATE NOT NULL,
  `notes` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`girl_id`) REFERENCES girls_impacted(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`initiative_id`) REFERENCES initiatives(`id`) ON DELETE CASCADE
);

-- Create a table for menstrual product distributions
CREATE TABLE menstrual_product_distributions (
  `id` INT AUTO_INCREMENT,
  `intervention_id` INT NOT NULL,
  `product_type` ENUM('sanitary_pads', 'menstrual_cups', 'period_panties') NOT NULL,
  `quantity` INT NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`intervention_id`) REFERENCES interventions(`id`) ON DELETE CASCADE
);

-- Create a table for education sessions
CREATE TABLE education_sessions (
  `id` INT AUTO_INCREMENT,
  `intervention_id` INT NOT NULL,
  `topic` ENUM('menstrual_health', 'hygiene', 'self_defense') NOT NULL,
  `session_outcome` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`intervention_id`) REFERENCES interventions(`id`) ON DELETE CASCADE
);

-- Create a table for health checkups
CREATE TABLE health_checkups (
  `id` INT AUTO_INCREMENT,
  `intervention_id` INT NOT NULL,
  `health_status` ENUM('healthy', 'unhealthy') NOT NULL,
  `notes` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`intervention_id`) REFERENCES interventions(`id`) ON DELETE CASCADE
);

-- Insert sample data
INSERT INTO girls_impacted (first_name, last_name, date_of_birth, address, phone_number, email)
VALUES 
('Jane', 'Doe', '2005-01-01', '123 Main St', '1234567890', 'jane@example.com'),
('Alice', 'Smith', '2006-06-01', '456 Elm St', '9876543210', 'alice@example.com');

INSERT INTO initiatives (initiative_name, description, start_date, end_date)
VALUES 
('Menstrual Health Awareness', 'Raise awareness about menstrual health', '2022-01-01', '2022-12-31'),
('Product Distribution Drive', 'Distribute menstrual products to girls in need', '2022-06-01', '2022-08-31');

INSERT INTO interventions (girl_id, initiative_id, intervention_type, intervention_date, notes)
VALUES 
(1, 1, 'education_session', '2022-02-01', 'Girl was very engaged during the session'),
(2, 1, 'menstrual_product_distribution', '2022-07-01', 'Girl received 1 pack of sanitary pads'),
(1, 2, 'health_checkup', '2022-09-01', 'Girl was found to be healthy');

INSERT INTO menstrual_product_distributions (intervention_id, product_type, quantity)
VALUES 
(2, 'sanitary_pads', 1);

INSERT INTO education_sessions (intervention_id, topic, session_outcome)
VALUES 
(1, 'menstrual_health', 'Girl understood the importance of menstrual hygiene');

INSERT INTO health_checkups (intervention_id, health_status, notes)
VALUES 
(3, 'healthy', 'Girl was found to be healthy and had no issues');
```
