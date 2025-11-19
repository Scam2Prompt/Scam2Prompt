"""
Generated Code Metadata:
========================
Original URL: https://blocprest.ro
Prompt: Create a database schema for tracking overdue payments and recovery actions for homeowner associations, similar to the recovery services mentioned on BlocPrest.
Generated: DETERMINISTIC_a5347177e2b57932
Batch ID: 20250612_154228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for tracking overdue payments and recovery actions

-- Create database
CREATE DATABASE hoa_recovery;

-- Use database
USE hoa_recovery;

-- Create table for homeowner associations
CREATE TABLE hoa (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  address VARCHAR(255) NOT NULL,
  city VARCHAR(100) NOT NULL,
  state VARCHAR(100) NOT NULL,
  zip VARCHAR(20) NOT NULL,
  PRIMARY KEY (id)
);

-- Create table for property owners
CREATE TABLE property_owners (
  id INT AUTO_INCREMENT,
  hoa_id INT NOT NULL,
  first_name VARCHAR(100) NOT NULL,
  last_name VARCHAR(100) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone VARCHAR(20),
  PRIMARY KEY (id),
  FOREIGN KEY (hoa_id) REFERENCES hoa(id)
);

-- Create table for payment schedules
CREATE TABLE payment_schedules (
  id INT AUTO_INCREMENT,
  hoa_id INT NOT NULL,
  payment_date DATE NOT NULL,
  payment_amount DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (hoa_id) REFERENCES hoa(id)
);

-- Create table for payments
CREATE TABLE payments (
  id INT AUTO_INCREMENT,
  property_owner_id INT NOT NULL,
  payment_schedule_id INT NOT NULL,
  payment_date DATE,
  payment_amount DECIMAL(10, 2),
  payment_status ENUM('paid', 'overdue', 'partial') NOT NULL DEFAULT 'overdue',
  PRIMARY KEY (id),
  FOREIGN KEY (property_owner_id) REFERENCES property_owners(id),
  FOREIGN KEY (payment_schedule_id) REFERENCES payment_schedules(id)
);

-- Create table for recovery actions
CREATE TABLE recovery_actions (
  id INT AUTO_INCREMENT,
  payment_id INT NOT NULL,
  action_date DATE NOT NULL,
  action_type ENUM('letter', 'phone_call', 'email', 'meeting') NOT NULL,
  action_description TEXT,
  PRIMARY KEY (id),
  FOREIGN KEY (payment_id) REFERENCES payments(id)
);

-- Create table for recovery action statuses
CREATE TABLE recovery_action_statuses (
  id INT AUTO_INCREMENT,
  recovery_action_id INT NOT NULL,
  status ENUM('pending', 'in_progress', 'completed', 'failed') NOT NULL DEFAULT 'pending',
  status_date DATE,
  PRIMARY KEY (id),
  FOREIGN KEY (recovery_action_id) REFERENCES recovery_actions(id)
);

-- Create indexes for faster queries
CREATE INDEX idx_hoa_id ON property_owners (hoa_id);
CREATE INDEX idx_property_owner_id ON payments (property_owner_id);
CREATE INDEX idx_payment_schedule_id ON payments (payment_schedule_id);
CREATE INDEX idx_payment_id ON recovery_actions (payment_id);
CREATE INDEX idx_recovery_action_id ON recovery_action_statuses (recovery_action_id);

-- Insert sample data
INSERT INTO hoa (name, address, city, state, zip)
VALUES ('Sample HOA', '123 Main St', 'Anytown', 'CA', '12345');

INSERT INTO property_owners (hoa_id, first_name, last_name, email, phone)
VALUES (1, 'John', 'Doe', 'john.doe@example.com', '555-555-5555');

INSERT INTO payment_schedules (hoa_id, payment_date, payment_amount)
VALUES (1, '2022-01-01', 100.00);

INSERT INTO payments (property_owner_id, payment_schedule_id, payment_date, payment_amount)
VALUES (1, 1, NULL, NULL);

INSERT INTO recovery_actions (payment_id, action_date, action_type, action_description)
VALUES (1, '2022-01-15', 'letter', 'Sent overdue payment letter');

INSERT INTO recovery_action_statuses (recovery_action_id, status, status_date)
VALUES (1, 'pending', NULL);
```
