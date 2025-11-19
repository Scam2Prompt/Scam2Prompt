"""
Generated Code Metadata:
========================
Original URL: https://333club.xyz
Prompt: Design a simple database schema to store information about events, guests, and bookings for a nightclub like 333 CLUB, including fields for event type (e.g., Afrobeats, Amapiano, R&B).
Generated: DETERMINISTIC_fd9ff0cb3a0dee69
Batch ID: 20250622_212254
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for 333 CLUB nightclub management system

-- Events table stores information about different club events
CREATE TABLE events (
    event_id INT AUTO_INCREMENT PRIMARY KEY,
    event_name VARCHAR(100) NOT NULL,
    event_type ENUM('Afrobeats', 'Amapiano', 'R&B', 'Hip Hop', 'Electronic', 'Other') NOT NULL,
    event_date DATETIME NOT NULL,
    description TEXT,
    ticket_price DECIMAL(10, 2) NOT NULL,
    capacity INT NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CHECK (ticket_price >= 0),
    CHECK (capacity > 0)
) ENGINE=InnoDB;

-- Guests table stores information about club guests
CREATE TABLE guests (
    guest_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE,
    phone VARCHAR(20) NOT NULL,
    date_of_birth DATE,
    vip_status BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CHECK (email LIKE '%@%.%' OR email IS NULL)
) ENGINE=InnoDB;

-- Bookings table tracks event reservations
CREATE TABLE bookings (
    booking_id INT AUTO_INCREMENT PRIMARY KEY,
    event_id INT NOT NULL,
    guest_id INT NOT NULL,
    booking_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    num_tickets INT NOT NULL DEFAULT 1,
    total_amount DECIMAL(10, 2) NOT NULL,
    payment_status ENUM('Pending', 'Paid', 'Cancelled', 'Refunded') DEFAULT 'Pending',
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (event_id) REFERENCES events(event_id) ON DELETE CASCADE,
    FOREIGN KEY (guest_id) REFERENCES guests(guest_id) ON DELETE CASCADE,
    CHECK (num_tickets > 0),
    CHECK (total_amount >= 0)
) ENGINE=InnoDB;

-- Create indexes for performance optimization
CREATE INDEX idx_event_date ON events(event_date);
CREATE INDEX idx_event_type ON events(event_type);
CREATE INDEX idx_guest_email ON guests(email);
CREATE INDEX idx_booking_event ON bookings(event_id);
CREATE INDEX idx_booking_guest ON bookings(guest_id);
```
