"""
Generated Code Metadata:
========================
Original URL: https://estetus.lt
Prompt: "Design a database schema to store information about clients, procedures, and appointments for a clinic like Estetus."
Generated: DETERMINISTIC_cf14bbe69aea5d53
Batch ID: 20250622_212748
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a clinic management system

-- Table to store client information
CREATE TABLE Clients (
    client_id SERIAL PRIMARY KEY, -- Unique identifier for each client
    first_name VARCHAR(50) NOT NULL, -- Client's first name
    last_name VARCHAR(50) NOT NULL, -- Client's last name
    date_of_birth DATE NOT NULL, -- Client's date of birth
    email VARCHAR(100) UNIQUE NOT NULL, -- Client's email address
    phone_number VARCHAR(15), -- Client's phone number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store procedure information
CREATE TABLE Procedures (
    procedure_id SERIAL PRIMARY KEY, -- Unique identifier for each procedure
    procedure_name VARCHAR(100) NOT NULL, -- Name of the procedure
    description TEXT, -- Description of the procedure
    duration_minutes INT NOT NULL, -- Duration of the procedure in minutes
    price DECIMAL(10, 2) NOT NULL, -- Price of the procedure
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store appointment information
CREATE TABLE Appointments (
    appointment_id SERIAL PRIMARY KEY, -- Unique identifier for each appointment
    client_id INT NOT NULL, -- Foreign key referencing Clients
    procedure_id INT NOT NULL, -- Foreign key referencing Procedures
    appointment_date TIMESTAMP NOT NULL, -- Date and time of the appointment
    status VARCHAR(20) DEFAULT 'Scheduled', -- Status of the appointment (Scheduled, Completed, Cancelled)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (client_id) REFERENCES Clients(client_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (procedure_id) REFERENCES Procedures(procedure_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for faster querying
CREATE INDEX idx_client_email ON Clients(email);
CREATE INDEX idx_procedure_name ON Procedures(procedure_name);
CREATE INDEX idx_appointment_date ON Appointments(appointment_date);
```
