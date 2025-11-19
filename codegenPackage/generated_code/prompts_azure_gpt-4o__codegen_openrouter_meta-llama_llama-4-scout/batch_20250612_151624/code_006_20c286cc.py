"""
Generated Code Metadata:
========================
Original URL: https://unitedcabinetry.com.au
Prompt: Create a database schema in SQL to store cabinetry project details, including design specifications, trades coordination, and after-sales support, inspired by United Cabinetry's workflow.
Generated: DETERMINISTIC_20c286cc776ecfa9
Batch ID: 20250612_151624
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for cabinetry project details

-- Create database
CREATE DATABASE cabinetry_projects;

-- Use database
USE cabinetry_projects;

-- Create table for projects
CREATE TABLE projects (
  `project_id` INT AUTO_INCREMENT,
  `project_name` VARCHAR(255) NOT NULL,
  `client_name` VARCHAR(255) NOT NULL,
  `project_date` DATE NOT NULL,
  `project_status` ENUM('in_progress', 'completed', 'cancelled') DEFAULT 'in_progress',
  `designer_id` INT,
  PRIMARY KEY (`project_id`)
);

-- Create table for designers
CREATE TABLE designers (
  `designer_id` INT AUTO_INCREMENT,
  `designer_name` VARCHAR(255) NOT NULL,
  `designer_email` VARCHAR(255) UNIQUE NOT NULL,
  `designer_phone` VARCHAR(20),
  PRIMARY KEY (`designer_id`)
);

-- Create table for design specifications
CREATE TABLE design_specs (
  `spec_id` INT AUTO_INCREMENT,
  `project_id` INT NOT NULL,
  `cabinet_style` VARCHAR(50) NOT NULL,
  `material` VARCHAR(50) NOT NULL,
  `finish` VARCHAR(50) NOT NULL,
  `layout` TEXT,
  PRIMARY KEY (`spec_id`),
  FOREIGN KEY (`project_id`) REFERENCES projects(`project_id`) ON DELETE CASCADE
);

-- Create table for trades
CREATE TABLE trades (
  `trade_id` INT AUTO_INCREMENT,
  `trade_name` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`trade_id`)
);

-- Create table for trades coordination
CREATE TABLE trade_coordination (
  `coord_id` INT AUTO_INCREMENT,
  `project_id` INT NOT NULL,
  `trade_id` INT NOT NULL,
  `trade_status` ENUM('scheduled', 'in_progress', 'completed') DEFAULT 'scheduled',
  `scheduled_date` DATE,
  `completed_date` DATE,
  PRIMARY KEY (`coord_id`),
  FOREIGN KEY (`project_id`) REFERENCES projects(`project_id`) ON DELETE CASCADE,
  FOREIGN KEY (`trade_id`) REFERENCES trades(`trade_id`) ON DELETE RESTRICT
);

-- Create table for after-sales support
CREATE TABLE after_sales (
  `support_id` INT AUTO_INCREMENT,
  `project_id` INT NOT NULL,
  `support_type` ENUM('issue', 'question', 'complaint') NOT NULL,
  `description` TEXT NOT NULL,
  `status` ENUM('open', 'in_progress', 'resolved') DEFAULT 'open',
  `created_date` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`support_id`),
  FOREIGN KEY (`project_id`) REFERENCES projects(`project_id`) ON DELETE CASCADE
);

-- Create table for support interactions
CREATE TABLE support_interactions (
  `interaction_id` INT AUTO_INCREMENT,
  `support_id` INT NOT NULL,
  `interaction_date` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `interaction_type` ENUM('email', 'phone', 'in_person') NOT NULL,
  `description` TEXT,
  PRIMARY KEY (`interaction_id`),
  FOREIGN KEY (`support_id`) REFERENCES after_sales(`support_id`) ON DELETE CASCADE
);

-- Insert sample data
INSERT INTO designers (designer_name, designer_email, designer_phone)
VALUES 
('John Doe', 'john.doe@example.com', '123-456-7890'),
('Jane Smith', 'jane.smith@example.com', '987-654-3210');

INSERT INTO projects (project_name, client_name, project_date, designer_id)
VALUES 
('Project 1', 'Client 1', '2022-01-01', 1),
('Project 2', 'Client 2', '2022-02-01', 2);

INSERT INTO design_specs (project_id, cabinet_style, material, finish, layout)
VALUES 
(1, 'Modern', 'Wood', 'White', 'Simple layout'),
(2, 'Traditional', 'MDF', 'Brown', 'Complex layout');

INSERT INTO trades (trade_name)
VALUES 
('Carpentry'),
('Electrical'),
('Plumbing');

INSERT INTO trade_coordination (project_id, trade_id, trade_status, scheduled_date)
VALUES 
(1, 1, 'scheduled', '2022-01-15'),
(1, 2, 'in_progress', NULL),
(2, 3, 'scheduled', '2022-03-01');

INSERT INTO after_sales (project_id, support_type, description)
VALUES 
(1, 'issue', 'Door not closing properly'),
(2, 'question', 'How to clean the cabinets?');

INSERT INTO support_interactions (support_id, interaction_type, description)
VALUES 
(1, 'email', 'Sent email to client about door issue'),
(2, 'phone', 'Discussed cleaning instructions with client');
```
