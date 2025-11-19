"""
Generated Code Metadata:
========================
Original URL: https://whitepinesinn.com
Prompt: Design a database schema to store information about cabins, guests, and reservations at White Pines Lodge, including relationships between entities.
Generated: DETERMINISTIC_ef2d5244c90e88fa
Batch ID: 20250622_204559
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for White Pines Lodge
CREATE DATABASE white_pines_lodge;

-- Use the database
USE white_pines_lodge;

-- Create table for cabins
CREATE TABLE cabins (
  cabin_id INT AUTO_INCREMENT,
  cabin_number INT NOT NULL,
  max_occupancy INT NOT NULL,
  rate DECIMAL(10, 2) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (cabin_id)
);

-- Create table for guests
CREATE TABLE guests (
  guest_id INT AUTO_INCREMENT,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  email VARCHAR(100) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  address VARCHAR(200),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (guest_id)
);

-- Create table for reservations
CREATE TABLE reservations (
  reservation_id INT AUTO_INCREMENT,
  cabin_id INT NOT NULL,
  guest_id INT NOT NULL,
  arrival_date DATE NOT NULL,
  departure_date DATE NOT NULL,
  total_cost DECIMAL(10, 2) NOT NULL,
  status ENUM('pending', 'confirmed', 'cancelled', 'checked_out') DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (reservation_id),
  FOREIGN KEY (cabin_id) REFERENCES cabins(cabin_id) ON DELETE CASCADE,
  FOREIGN KEY (guest_id) REFERENCES guests(guest_id) ON DELETE CASCADE
);

-- Create table for payments
CREATE TABLE payments (
  payment_id INT AUTO_INCREMENT,
  reservation_id INT NOT NULL,
  payment_date DATE NOT NULL,
  payment_amount DECIMAL(10, 2) NOT NULL,
  payment_method ENUM('cash', 'credit_card', 'debit_card') NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (payment_id),
  FOREIGN KEY (reservation_id) REFERENCES reservations(reservation_id) ON DELETE CASCADE
);

-- Create indexes for foreign keys
CREATE INDEX idx_reservations_cabin_id ON reservations (cabin_id);
CREATE INDEX idx_reservations_guest_id ON reservations (guest_id);
CREATE INDEX idx_payments_reservation_id ON payments (reservation_id);
```

```sql
-- sample_data.sql

-- Insert sample data into cabins table
INSERT INTO cabins (cabin_number, max_occupancy, rate, description)
VALUES
  (1, 4, 150.00, 'Cozy cabin with fireplace'),
  (2, 6, 250.00, 'Spacious cabin with lake view'),
  (3, 2, 100.00, 'Simple cabin with basic amenities');

-- Insert sample data into guests table
INSERT INTO guests (first_name, last_name, email, phone_number, address)
VALUES
  ('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St'),
  ('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210', '456 Elm St'),
  ('Bob', 'Johnson', 'bob.johnson@example.com', '555-123-4567', '789 Oak St');

-- Insert sample data into reservations table
INSERT INTO reservations (cabin_id, guest_id, arrival_date, departure_date, total_cost)
VALUES
  (1, 1, '2024-09-01', '2024-09-03', 300.00),
  (2, 2, '2024-09-15', '2024-09-17', 500.00),
  (3, 3, '2024-09-20', '2024-09-22', 200.00);

-- Insert sample data into payments table
INSERT INTO payments (reservation_id, payment_date, payment_amount, payment_method)
VALUES
  (1, '2024-08-25', 300.00, 'credit_card'),
  (2, '2024-09-01', 250.00, 'cash'),
  (3, '2024-09-10', 200.00, 'debit_card');
```
