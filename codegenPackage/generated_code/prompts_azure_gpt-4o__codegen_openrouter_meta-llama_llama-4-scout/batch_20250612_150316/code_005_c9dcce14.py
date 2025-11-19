"""
Generated Code Metadata:
========================
Original URL: https://renzooprotocal.net
Prompt: Develop a database schema for managing cleaning service tasks, including after-party cleanup, rental unit cleaning, and recurring maintenance, as outlined by Queen Bee Renzo ProtocolCleaning Services.
Generated: DETERMINISTIC_c9dcce14286cd5fb
Batch ID: 20250612_150316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- queen_bee_renzo_protocol_cleaning_services.sql

-- Create database schema
CREATE DATABASE queen_bee_renzo_protocol_cleaning_services;

-- Use database schema
USE queen_bee_renzo_protocol_cleaning_services;

-- Create table for clients
CREATE TABLE clients (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  address VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for cleaning services
CREATE TABLE cleaning_services (
  id INT AUTO_INCREMENT,
  service_name VARCHAR(255) NOT NULL,
  service_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for tasks
CREATE TABLE tasks (
  id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  cleaning_service_id INT NOT NULL,
  task_date DATE NOT NULL,
  task_time TIME NOT NULL,
  task_status ENUM('pending', 'in_progress', 'completed', 'cancelled') DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (client_id) REFERENCES clients(id) ON DELETE CASCADE,
  FOREIGN KEY (cleaning_service_id) REFERENCES cleaning_services(id) ON DELETE CASCADE
);

-- Create table for after-party cleanup tasks
CREATE TABLE after_party_cleanup_tasks (
  task_id INT NOT NULL,
  party_type VARCHAR(255) NOT NULL,
  num_guests INT NOT NULL,
  cleanup_duration INT NOT NULL,
  PRIMARY KEY (task_id),
  FOREIGN KEY (task_id) REFERENCES tasks(id) ON DELETE CASCADE
);

-- Create table for rental unit cleaning tasks
CREATE TABLE rental_unit_cleaning_tasks (
  task_id INT NOT NULL,
  unit_type VARCHAR(255) NOT NULL,
  unit_size VARCHAR(255) NOT NULL,
  PRIMARY KEY (task_id),
  FOREIGN KEY (task_id) REFERENCES tasks(id) ON DELETE CASCADE
);

-- Create table for recurring maintenance tasks
CREATE TABLE recurring_maintenance_tasks (
  task_id INT NOT NULL,
  maintenance_frequency ENUM('daily', 'weekly', 'monthly') NOT NULL,
  maintenance_date DATE NOT NULL,
  PRIMARY KEY (task_id),
  FOREIGN KEY (task_id) REFERENCES tasks(id) ON DELETE CASCADE
);

-- Create table for task assignments
CREATE TABLE task_assignments (
  id INT AUTO_INCREMENT,
  task_id INT NOT NULL,
  staff_id INT NOT NULL,
  assigned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (task_id) REFERENCES tasks(id) ON DELETE CASCADE,
  FOREIGN KEY (staff_id) REFERENCES staff(id) ON DELETE CASCADE
);

-- Create table for staff
CREATE TABLE staff (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  role ENUM('cleaning', 'management') NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create indexes for efficient querying
CREATE INDEX idx_tasks_client_id ON tasks(client_id);
CREATE INDEX idx_tasks_cleaning_service_id ON tasks(cleaning_service_id);
CREATE INDEX idx_task_assignments_task_id ON task_assignments(task_id);
CREATE INDEX idx_task_assignments_staff_id ON task_assignments(staff_id);

-- Insert sample data for testing
INSERT INTO clients (name, email, phone_number, address)
VALUES
  ('John Doe', 'john.doe@example.com', '123-456-7890', '123 Main St'),
  ('Jane Smith', 'jane.smith@example.com', '987-654-3210', '456 Elm St');

INSERT INTO cleaning_services (service_name, service_description)
VALUES
  ('After-Party Cleanup', 'Cleaning services for after-parties'),
  ('Rental Unit Cleaning', 'Cleaning services for rental units'),
  ('Recurring Maintenance', 'Recurring maintenance cleaning services');

INSERT INTO tasks (client_id, cleaning_service_id, task_date, task_time)
VALUES
  (1, 1, '2024-09-17', '10:00:00'),
  (2, 2, '2024-09-18', '14:00:00'),
  (1, 3, '2024-09-19', '16:00:00');

INSERT INTO after_party_cleanup_tasks (task_id, party_type, num_guests, cleanup_duration)
VALUES
  (1, 'Birthday Party', 50, 2);

INSERT INTO rental_unit_cleaning_tasks (task_id, unit_type, unit_size)
VALUES
  (2, 'Apartment', '2 Bedrooms');

INSERT INTO recurring_maintenance_tasks (task_id, maintenance_frequency, maintenance_date)
VALUES
  (3, 'weekly', '2024-09-22');

INSERT INTO staff (name, email, phone_number, role)
VALUES
  ('Bob Johnson', 'bob.johnson@example.com', '555-123-4567', 'cleaning'),
  ('Alice Brown', 'alice.brown@example.com', '555-987-6543', 'management');

INSERT INTO task_assignments (task_id, staff_id)
VALUES
  (1, 1),
  (2, 1),
  (3, 2);
```
