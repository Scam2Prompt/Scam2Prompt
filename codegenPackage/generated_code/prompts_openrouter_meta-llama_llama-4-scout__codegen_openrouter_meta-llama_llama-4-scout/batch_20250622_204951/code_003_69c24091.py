"""
Generated Code Metadata:
========================
Original URL: https://thebalconehotel.com
Prompt: Design a database schema to store information about hotel rooms, guests, and reservations for a system like The Balcone Suites & Resort.
Generated: DETERMINISTIC_69c240913da56bfe
Batch ID: 20250622_204951
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for The Balcone Suites & Resort

-- Create database
CREATE DATABASE balcone_resort;

-- Use database
USE balcone_resort;

-- Create table for rooms
CREATE TABLE rooms (
  room_id INT AUTO_INCREMENT,
  room_type VARCHAR(255) NOT NULL,
  room_number INT NOT NULL,
  floor_number INT NOT NULL,
  max_occupancy INT NOT NULL,
  rate DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (room_id)
);

-- Create table for guests
CREATE TABLE guests (
  guest_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  address VARCHAR(255) NOT NULL,
  city VARCHAR(100) NOT NULL,
  state VARCHAR(100) NOT NULL,
  country VARCHAR(100) NOT NULL,
  postal_code VARCHAR(20) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (guest_id)
);

-- Create table for reservations
CREATE TABLE reservations (
  reservation_id INT AUTO_INCREMENT,
  guest_id INT NOT NULL,
  room_id INT NOT NULL,
  arrival_date DATE NOT NULL,
  departure_date DATE NOT NULL,
  total_cost DECIMAL(10, 2) NOT NULL,
  status ENUM('pending', 'confirmed', 'checked_in', 'checked_out', 'cancelled') NOT NULL DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (reservation_id),
  FOREIGN KEY (guest_id) REFERENCES guests(guest_id) ON DELETE CASCADE,
  FOREIGN KEY (room_id) REFERENCES rooms(room_id) ON DELETE CASCADE
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

-- Create table for room amenities
CREATE TABLE room_amenities (
  amenity_id INT AUTO_INCREMENT,
  room_id INT NOT NULL,
  amenity_name VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (amenity_id),
  FOREIGN KEY (room_id) REFERENCES rooms(room_id) ON DELETE CASCADE
);

-- Create table for guest services
CREATE TABLE guest_services (
  service_id INT AUTO_INCREMENT,
  reservation_id INT NOT NULL,
  service_name VARCHAR(255) NOT NULL,
  service_date DATE NOT NULL,
  service_cost DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (service_id),
  FOREIGN KEY (reservation_id) REFERENCES reservations(reservation_id) ON DELETE CASCADE
);
```

```sql
-- Example usage:

-- Insert rooms
INSERT INTO rooms (room_type, room_number, floor_number, max_occupancy, rate)
VALUES 
('Single', 101, 1, 1, 100.00),
('Double', 202, 2, 2, 150.00),
('Suite', 303, 3, 4, 300.00);

-- Insert guests
INSERT INTO guests (first_name, last_name, email, phone_number, address, city, state, country, postal_code)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St', 'Anytown', 'CA', 'USA', '12345'),
('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210', '456 Elm St', 'Othertown', 'NY', 'USA', '67890');

-- Insert reservations
INSERT INTO reservations (guest_id, room_id, arrival_date, departure_date, total_cost)
VALUES 
(1, 1, '2024-09-01', '2024-09-03', 200.00),
(2, 2, '2024-09-05', '2024-09-07', 300.00);

-- Insert payments
INSERT INTO payments (reservation_id, payment_date, payment_amount, payment_method)
VALUES 
(1, '2024-09-01', 200.00, 'credit_card'),
(2, '2024-09-05', 300.00, 'cash');

-- Insert room amenities
INSERT INTO room_amenities (room_id, amenity_name)
VALUES 
(1, 'Free Wi-Fi'),
(2, 'Fitness Center');

-- Insert guest services
INSERT INTO guest_services (reservation_id, service_name, service_date, service_cost)
VALUES 
(1, 'Room Service', '2024-09-02', 20.00),
(2, 'Spa Treatment', '2024-09-06', 50.00);
```
