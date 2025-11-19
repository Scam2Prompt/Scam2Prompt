"""
Generated Code Metadata:
========================
Original URL: https://prosync.online
Prompt: Create a database schema to manage appointments, messages, and follow-up calls for a virtual receptionist service like ProSync.
Generated: DETERMINISTIC_e73821c228515435
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for virtual receptionist service
CREATE DATABASE virtual_receptionist;

-- Use the database
USE virtual_receptionist;

-- Create table for clients
CREATE TABLE clients (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  address VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for appointment types
CREATE TABLE appointment_types (
  id INT AUTO_INCREMENT,
  name VARCHAR(100) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for appointments
CREATE TABLE appointments (
  id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  appointment_type_id INT NOT NULL,
  scheduled_date DATE NOT NULL,
  scheduled_time TIME NOT NULL,
  duration INT NOT NULL, -- in minutes
  location VARCHAR(255),
  notes TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (client_id) REFERENCES clients(id) ON DELETE CASCADE,
  FOREIGN KEY (appointment_type_id) REFERENCES appointment_types(id) ON DELETE RESTRICT
);

-- Create table for messages
CREATE TABLE messages (
  id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  message TEXT NOT NULL,
  sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (client_id) REFERENCES clients(id) ON DELETE CASCADE
);

-- Create table for follow-up calls
CREATE TABLE follow_up_calls (
  id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  scheduled_date DATE NOT NULL,
  scheduled_time TIME NOT NULL,
  notes TEXT,
  outcome TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (client_id) REFERENCES clients(id) ON DELETE CASCADE
);

-- Create table for users (receptionists)
CREATE TABLE users (
  id INT AUTO_INCREMENT,
  username VARCHAR(100) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  role ENUM('admin', 'receptionist') NOT NULL DEFAULT 'receptionist',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for appointment reminders
CREATE TABLE appointment_reminders (
  id INT AUTO_INCREMENT,
  appointment_id INT NOT NULL,
  reminder_date DATE NOT NULL,
  reminder_time TIME NOT NULL,
  sent BOOLEAN NOT NULL DEFAULT FALSE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (appointment_id) REFERENCES appointments(id) ON DELETE CASCADE
);

-- Indexes for performance optimization
CREATE INDEX idx_appointments_client_id ON appointments(client_id);
CREATE INDEX idx_appointments_appointment_type_id ON appointments(appointment_type_id);
CREATE INDEX idx_messages_client_id ON messages(client_id);
CREATE INDEX idx_follow_up_calls_client_id ON follow_up_calls(client_id);
```

```sql
-- sample_data.sql

-- Insert sample data into tables
INSERT INTO clients (name, email, phone_number, address)
VALUES
  ('John Doe', 'john.doe@example.com', '123-456-7890', '123 Main St'),
  ('Jane Smith', 'jane.smith@example.com', '987-654-3210', '456 Elm St');

INSERT INTO appointment_types (name, description)
VALUES
  ('Initial Consultation', 'Initial consultation for new clients'),
  ('Follow-up Meeting', 'Follow-up meeting for existing clients');

INSERT INTO appointments (client_id, appointment_type_id, scheduled_date, scheduled_time, duration)
VALUES
  (1, 1, '2024-09-20', '10:00:00', 60),
  (2, 2, '2024-09-22', '14:00:00', 30);

INSERT INTO messages (client_id, message)
VALUES
  (1, 'Hello, I have a question about my appointment'),
  (2, 'Hi, I need to reschedule my appointment');

INSERT INTO follow_up_calls (client_id, scheduled_date, scheduled_time, notes)
VALUES
  (1, '2024-09-25', '11:00:00', 'Follow-up on initial consultation'),
  (2, '2024-09-28', '16:00:00', 'Follow-up on follow-up meeting');

INSERT INTO users (username, email, password_hash, role)
VALUES
  ('admin', 'admin@example.com', 'password_hash', 'admin'),
  ('receptionist', 'receptionist@example.com', 'password_hash', 'receptionist');
```
