"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bandadorada.com
Prompt: Outline a database schema for storing information about music events, clients, and services, similar to the structure used by Orquesta Dorada for managing their bookings.
Generated: DETERMINISTIC_21a1799f44631b28
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing music events, clients, and services

CREATE TABLE Clients (
    client_id INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each client
    first_name VARCHAR(50) NOT NULL,           -- Client's first name
    last_name VARCHAR(50) NOT NULL,            -- Client's last name
    email VARCHAR(100) UNIQUE NOT NULL,        -- Client's email address, must be unique
    phone VARCHAR(15),                          -- Client's phone number, optional
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

CREATE TABLE Services (
    service_id INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each service
    service_name VARCHAR(100) NOT NULL,         -- Name of the service
    description TEXT,                            -- Description of the service
    price DECIMAL(10, 2) NOT NULL,              -- Price of the service
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

CREATE TABLE Events (
    event_id INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each event
    client_id INT NOT NULL,                      -- Foreign key reference to Clients table
    service_id INT NOT NULL,                     -- Foreign key reference to Services table
    event_date DATETIME NOT NULL,                -- Date and time of the event
    location VARCHAR(255) NOT NULL,              -- Location of the event
    notes TEXT,                                   -- Additional notes for the event
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Record update timestamp
    FOREIGN KEY (client_id) REFERENCES Clients(client_id) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (service_id) REFERENCES Services(service_id) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_client_email ON Clients(email);
CREATE INDEX idx_service_name ON Services(service_name);
CREATE INDEX idx_event_date ON Events(event_date);
```
