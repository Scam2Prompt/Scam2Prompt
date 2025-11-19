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
-- Sample Database Schema for Managing Client Information, Event Details, and Payment Records for an Orchestra Service

-- Drop existing tables if they exist (for development purposes)
DROP TABLE IF EXISTS Payments;
DROP TABLE IF EXISTS Events;
DROP TABLE IF EXISTS Clients;

-- Table to store client information
CREATE TABLE Clients (
    client_id SERIAL PRIMARY KEY, -- Unique identifier for each client
    first_name VARCHAR(50) NOT NULL, -- Client's first name
    last_name VARCHAR(50) NOT NULL, -- Client's last name
    email VARCHAR(100) UNIQUE NOT NULL, -- Client's email address
    phone_number VARCHAR(15), -- Client's phone number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store event details
CREATE TABLE Events (
    event_id SERIAL PRIMARY KEY, -- Unique identifier for each event
    event_name VARCHAR(100) NOT NULL, -- Name of the event
    event_date TIMESTAMP NOT NULL, -- Date and time of the event
    venue VARCHAR(100) NOT NULL, -- Venue of the event
    ticket_price DECIMAL(10, 2) NOT NULL, -- Price of the ticket
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store payment records
CREATE TABLE Payments (
    payment_id SERIAL PRIMARY KEY, -- Unique identifier for each payment
    client_id INT NOT NULL, -- Foreign key referencing Clients table
    event_id INT NOT NULL, -- Foreign key referencing Events table
    amount DECIMAL(10, 2) NOT NULL, -- Amount paid
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of payment
    payment_method VARCHAR(50) NOT NULL, -- Method of payment (e.g., Credit Card, PayPal)
    FOREIGN KEY (client_id) REFERENCES Clients(client_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (event_id) REFERENCES Events(event_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_client_email ON Clients(email);
CREATE INDEX idx_event_date ON Events(event_date);
CREATE INDEX idx_payment_client ON Payments(client_id);
CREATE INDEX idx_payment_event ON Payments(event_id);
```
