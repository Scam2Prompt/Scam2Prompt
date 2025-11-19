"""
Generated Code Metadata:
========================
Original URL: https://www.picturedbyd.com
Prompt: Generate a SQL database schema to manage photography bookings, client information, and image delivery for a business like Pictured by Dhaval.
Generated: DETERMINISTIC_0b670d8102ec13b6
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for Photography Bookings

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS ImageDelivery;
DROP TABLE IF EXISTS Bookings;
DROP TABLE IF EXISTS Clients;

-- Table to store client information
CREATE TABLE Clients (
    client_id SERIAL PRIMARY KEY, -- Unique identifier for each client
    first_name VARCHAR(50) NOT NULL, -- Client's first name
    last_name VARCHAR(50) NOT NULL, -- Client's last name
    email VARCHAR(100) UNIQUE NOT NULL, -- Client's email address
    phone VARCHAR(15), -- Client's phone number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store booking information
CREATE TABLE Bookings (
    booking_id SERIAL PRIMARY KEY, -- Unique identifier for each booking
    client_id INT NOT NULL, -- Foreign key referencing Clients table
    booking_date DATE NOT NULL, -- Date of the booking
    session_type VARCHAR(100) NOT NULL, -- Type of photography session (e.g., wedding, portrait)
    status VARCHAR(20) DEFAULT 'Pending', -- Status of the booking (e.g., Pending, Confirmed, Completed)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (client_id) REFERENCES Clients(client_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store image delivery information
CREATE TABLE ImageDelivery (
    delivery_id SERIAL PRIMARY KEY, -- Unique identifier for each image delivery
    booking_id INT NOT NULL, -- Foreign key referencing Bookings table
    delivery_date DATE NOT NULL, -- Date when images are delivered
    delivery_method VARCHAR(50) NOT NULL, -- Method of delivery (e.g., Digital, Print)
    delivery_status VARCHAR(20) DEFAULT 'Pending', -- Status of the delivery (e.g., Pending, Delivered)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (booking_id) REFERENCES Bookings(booking_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_client_email ON Clients(email);
CREATE INDEX idx_booking_date ON Bookings(booking_date);
CREATE INDEX idx_delivery_date ON ImageDelivery(delivery_date);
```
