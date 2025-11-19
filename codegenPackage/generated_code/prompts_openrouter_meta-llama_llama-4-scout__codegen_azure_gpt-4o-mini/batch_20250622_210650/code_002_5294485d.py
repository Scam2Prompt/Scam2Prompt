"""
Generated Code Metadata:
========================
Original URL: https://carolcrespo.com.br
Prompt: Generate a sample database schema to store client information, fitness plans, and appointment schedules for a personal training consulting service like Carol Crespo's, including fields for payment, plan type, and evaluation details.
Generated: DETERMINISTIC_5294485d32878aae
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Sample database schema for a personal training consulting service

-- Table to store client information
CREATE TABLE Clients (
    client_id SERIAL PRIMARY KEY, -- Unique identifier for each client
    first_name VARCHAR(50) NOT NULL, -- Client's first name
    last_name VARCHAR(50) NOT NULL, -- Client's last name
    email VARCHAR(100) UNIQUE NOT NULL, -- Client's email address
    phone VARCHAR(15), -- Client's phone number
    date_of_birth DATE, -- Client's date of birth
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store fitness plans
CREATE TABLE FitnessPlans (
    plan_id SERIAL PRIMARY KEY, -- Unique identifier for each fitness plan
    client_id INT NOT NULL, -- Foreign key referencing Clients table
    plan_type VARCHAR(50) NOT NULL, -- Type of fitness plan (e.g., weight loss, muscle gain)
    description TEXT, -- Description of the fitness plan
    start_date DATE NOT NULL, -- Start date of the fitness plan
    end_date DATE, -- End date of the fitness plan (nullable)
    evaluation_details TEXT, -- Details of evaluations or assessments
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (client_id) REFERENCES Clients(client_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store appointment schedules
CREATE TABLE Appointments (
    appointment_id SERIAL PRIMARY KEY, -- Unique identifier for each appointment
    client_id INT NOT NULL, -- Foreign key referencing Clients table
    appointment_date TIMESTAMP NOT NULL, -- Date and time of the appointment
    duration INT NOT NULL, -- Duration of the appointment in minutes
    payment_status VARCHAR(20) NOT NULL CHECK (payment_status IN ('Paid', 'Pending', 'Cancelled')), -- Payment status
    notes TEXT, -- Additional notes for the appointment
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (client_id) REFERENCES Clients(client_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_client_email ON Clients(email);
CREATE INDEX idx_plan_client ON FitnessPlans(client_id);
CREATE INDEX idx_appointment_client ON Appointments(client_id);
```
