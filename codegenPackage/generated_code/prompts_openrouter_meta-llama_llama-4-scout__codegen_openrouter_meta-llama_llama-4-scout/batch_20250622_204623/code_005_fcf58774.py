"""
Generated Code Metadata:
========================
Original URL: https://sandiegosleepandtmjcenter.com
Prompt: Design a database schema to store patient information, treatment plans, and services offered by the San Diego Sleep and TMJ Center, including information about their doctors and staff.
Generated: DETERMINISTIC_fcf587744cd5a692
Batch ID: 20250622_204623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the San Diego Sleep and TMJ Center
CREATE DATABASE sd_sleep_tmj_center;

-- Use the database
USE sd_sleep_tmj_center;

-- Create a table for doctors and staff
CREATE TABLE personnel (
  `id` INT AUTO_INCREMENT,
  `first_name` VARCHAR(50) NOT NULL,
  `last_name` VARCHAR(50) NOT NULL,
  `email` VARCHAR(100) UNIQUE NOT NULL,
  `role` ENUM('doctor', 'staff') NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create a table for patients
CREATE TABLE patients (
  `id` INT AUTO_INCREMENT,
  `first_name` VARCHAR(50) NOT NULL,
  `last_name` VARCHAR(50) NOT NULL,
  `email` VARCHAR(100) UNIQUE NOT NULL,
  `phone` VARCHAR(20),
  `address` VARCHAR(255),
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create a table for services offered
CREATE TABLE services (
  `id` INT AUTO_INCREMENT,
  `name` VARCHAR(100) NOT NULL,
  `description` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
);

-- Create a table for treatment plans
CREATE TABLE treatment_plans (
  `id` INT AUTO_INCREMENT,
  `patient_id` INT NOT NULL,
  `doctor_id` INT NOT NULL,
  `service_id` INT NOT NULL,
  `plan_details` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`patient_id`) REFERENCES patients(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`doctor_id`) REFERENCES personnel(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`service_id`) REFERENCES services(`id`) ON DELETE CASCADE
);

-- Create a table for appointments
CREATE TABLE appointments (
  `id` INT AUTO_INCREMENT,
  `patient_id` INT NOT NULL,
  `doctor_id` INT NOT NULL,
  `appointment_date` DATE NOT NULL,
  `appointment_time` TIME NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`patient_id`) REFERENCES patients(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`doctor_id`) REFERENCES personnel(`id`) ON DELETE CASCADE
);

-- Create a table for patient medical history
CREATE TABLE medical_history (
  `id` INT AUTO_INCREMENT,
  `patient_id` INT NOT NULL,
  `condition` VARCHAR(100) NOT NULL,
  `description` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`patient_id`) REFERENCES patients(`id`) ON DELETE CASCADE
);

-- Create a table for patient treatment history
CREATE TABLE treatment_history (
  `id` INT AUTO_INCREMENT,
  `patient_id` INT NOT NULL,
  `treatment_plan_id` INT NOT NULL,
  `service_id` INT NOT NULL,
  `treatment_date` DATE NOT NULL,
  `treatment_details` TEXT,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `updated_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`patient_id`) REFERENCES patients(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`treatment_plan_id`) REFERENCES treatment_plans(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`service_id`) REFERENCES services(`id`) ON DELETE CASCADE
);
```

```sql
-- Example insert statements
INSERT INTO personnel (`first_name`, `last_name`, `email`, `role`)
VALUES 
('John', 'Doe', 'john.doe@example.com', 'doctor'),
('Jane', 'Smith', 'jane.smith@example.com', 'staff');

INSERT INTO patients (`first_name`, `last_name`, `email`, `phone`, `address`)
VALUES 
('Bob', 'Johnson', 'bob.johnson@example.com', '123-456-7890', '123 Main St');

INSERT INTO services (`name`, `description`)
VALUES 
('Sleep Study', 'Overnight sleep study'),
('TMJ Treatment', 'Treatment for TMJ disorders');

INSERT INTO treatment_plans (`patient_id`, `doctor_id`, `service_id`, `plan_details`)
VALUES 
(1, 1, 1, 'Patient will undergo a sleep study');

INSERT INTO appointments (`patient_id`, `doctor_id`, `appointment_date`, `appointment_time`)
VALUES 
(1, 1, '2024-09-17', '10:00:00');

INSERT INTO medical_history (`patient_id`, `condition`, `description`)
VALUES 
(1, 'Insomnia', 'Patient has difficulty sleeping');

INSERT INTO treatment_history (`patient_id`, `treatment_plan_id`, `service_id`, `treatment_date`, `treatment_details`)
VALUES 
(1, 1, 1, '2024-09-16', 'Patient completed a sleep study');
```
