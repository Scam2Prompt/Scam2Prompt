"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mluce-ginza.net
Prompt: Design a database schema for storing client information, appointment details, and service records for an art makeup salon, focusing on scalability and security.
Generated: DETERMINISTIC_f81004e042056219
Batch ID: 20250612_163406
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Art Makeup Salon

-- Create a table to store client information
CREATE TABLE Clients (
    client_id SERIAL PRIMARY KEY, -- Unique identifier for each client
    first_name VARCHAR(50) NOT NULL, -- Client's first name
    last_name VARCHAR(50) NOT NULL, -- Client's last name
    email VARCHAR(100) UNIQUE NOT NULL, -- Client's email (unique)
    phone VARCHAR(15), -- Client's phone number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table to store appointment details
CREATE TABLE Appointments (
    appointment_id SERIAL PRIMARY KEY, -- Unique identifier for each appointment
    client_id INT NOT NULL, -- Reference to the client
    appointment_date TIMESTAMP NOT NULL, -- Date and time of the appointment
    service_id INT NOT NULL, -- Reference to the service provided
    status VARCHAR(20) DEFAULT 'scheduled', -- Status of the appointment (scheduled, completed, canceled)
    notes TEXT, -- Additional notes for the appointment
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (client_id) REFERENCES Clients(client_id) ON DELETE CASCADE, -- Foreign key constraint
    FOREIGN KEY (service_id) REFERENCES Services(service_id) ON DELETE CASCADE -- Foreign key constraint
);

-- Create a table to store service records
CREATE TABLE Services (
    service_id SERIAL PRIMARY KEY, -- Unique identifier for each service
    service_name VARCHAR(100) NOT NULL, -- Name of the service
    price DECIMAL(10, 2) NOT NULL, -- Price of the service
    duration INT NOT NULL, -- Duration of the service in minutes
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Create a table to log service records associated with appointments
CREATE TABLE ServiceRecords (
    record_id SERIAL PRIMARY KEY, -- Unique identifier for each service record
    appointment_id INT NOT NULL, -- Reference to the appointment
    service_id INT NOT NULL, -- Reference to the service provided
    performed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- When the service was performed
    feedback TEXT, -- Client feedback about the service
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (appointment_id) REFERENCES Appointments(appointment_id) ON DELETE CASCADE, -- Foreign key constraint
    FOREIGN KEY (service_id) REFERENCES Services(service_id) ON DELETE CASCADE -- Foreign key constraint
);

-- Indexes to improve query performance
CREATE INDEX idx_clients_email ON Clients(email);
CREATE INDEX idx_appointments_date ON Appointments(appointment_date);
CREATE INDEX idx_services_name ON Services(service_name);
```
