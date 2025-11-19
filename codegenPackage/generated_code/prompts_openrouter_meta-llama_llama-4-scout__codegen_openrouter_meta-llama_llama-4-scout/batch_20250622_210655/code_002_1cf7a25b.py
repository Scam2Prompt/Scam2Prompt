"""
Generated Code Metadata:
========================
Original URL: https://bandadorada.com
Prompt: Generate a sample database schema for managing client information, event details, and payment records for an orchestra service like Orquesta Dorada.
Generated: DETERMINISTIC_1cf7a25b2f1c2d1d
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for Orquesta Dorada
CREATE DATABASE orquesta_dorada;

-- Use the database
USE orquesta_dorada;

-- Create table for clients
CREATE TABLE clients (
  client_id INT AUTO_INCREMENT,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  address VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (client_id)
);

-- Create table for events
CREATE TABLE events (
  event_id INT AUTO_INCREMENT,
  client_id INT,
  event_date DATE NOT NULL,
  event_time TIME NOT NULL,
  event_type VARCHAR(50) NOT NULL,
  event_location VARCHAR(255) NOT NULL,
  num_guests INT,
  special_requests TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (event_id),
  FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
);

-- Create table for musicians
CREATE TABLE musicians (
  musician_id INT AUTO_INCREMENT,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  instrument VARCHAR(50) NOT NULL,
  rate DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (musician_id)
);

-- Create table for event musicians
CREATE TABLE event_musicians (
  event_id INT,
  musician_id INT,
  PRIMARY KEY (event_id, musician_id),
  FOREIGN KEY (event_id) REFERENCES events(event_id) ON DELETE CASCADE,
  FOREIGN KEY (musician_id) REFERENCES musicians(musician_id) ON DELETE CASCADE
);

-- Create table for payments
CREATE TABLE payments (
  payment_id INT AUTO_INCREMENT,
  event_id INT,
  payment_date DATE NOT NULL,
  payment_amount DECIMAL(10, 2) NOT NULL,
  payment_method VARCHAR(50) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (payment_id),
  FOREIGN KEY (event_id) REFERENCES events(event_id) ON DELETE CASCADE
);

-- Create table for invoices
CREATE TABLE invoices (
  invoice_id INT AUTO_INCREMENT,
  event_id INT,
  invoice_date DATE NOT NULL,
  invoice_amount DECIMAL(10, 2) NOT NULL,
  invoice_status VARCHAR(50) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (invoice_id),
  FOREIGN KEY (event_id) REFERENCES events(event_id) ON DELETE CASCADE
);
```

```sql
-- sample_data.sql

-- Insert sample data into clients table
INSERT INTO clients (first_name, last_name, email, phone_number, address)
VALUES
  ('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St'),
  ('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210', '456 Elm St'),
  ('Bob', 'Johnson', 'bob.johnson@example.com', '555-123-4567', '789 Oak St');

-- Insert sample data into events table
INSERT INTO events (client_id, event_date, event_time, event_type, event_location, num_guests)
VALUES
  (1, '2024-09-20', '18:00:00', 'Wedding', 'The Grand Ballroom', 200),
  (2, '2024-10-15', '19:00:00', 'Birthday Party', 'The Park Hotel', 50),
  (3, '2024-11-20', '20:00:00', 'Corporate Event', 'The Convention Center', 100);

-- Insert sample data into musicians table
INSERT INTO musicians (first_name, last_name, instrument, rate)
VALUES
  ('Michael', 'Brown', 'Violin', 100.00),
  ('Emily', 'Chen', 'Cello', 120.00),
  ('David', 'Lee', 'Piano', 150.00);

-- Insert sample data into event_musicians table
INSERT INTO event_musicians (event_id, musician_id)
VALUES
  (1, 1),
  (1, 2),
  (2, 3),
  (3, 1),
  (3, 2);

-- Insert sample data into payments table
INSERT INTO payments (event_id, payment_date, payment_amount, payment_method)
VALUES
  (1, '2024-08-15', 500.00, 'Credit Card'),
  (2, '2024-09-01', 200.00, 'Cash'),
  (3, '2024-10-01', 1000.00, 'Check');

-- Insert sample data into invoices table
INSERT INTO invoices (event_id, invoice_date, invoice_amount, invoice_status)
VALUES
  (1, '2024-09-01', 2000.00, 'Pending'),
  (2, '2024-10-01', 500.00, 'Paid'),
  (3, '2024-11-01', 3000.00, 'Pending');
```
