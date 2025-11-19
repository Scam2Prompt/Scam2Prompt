"""
Generated Code Metadata:
========================
Original URL: https://www.martingodwinequine.com
Prompt: Design a database schema for managing client information and appointment scheduling for an equine care service, taking cues from the organizational structure of Martin Godwin Equine Services.
Generated: DETERMINISTIC_d5ab1b53594d67ff
Batch ID: 20250612_163952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing client information and appointment scheduling
-- for an equine care service, inspired by Martin Godwin Equine Services.

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Appointments;
DROP TABLE IF EXISTS Clients;
DROP TABLE IF EXISTS Horses;
DROP TABLE IF EXISTS Services;
DROP TABLE IF EXISTS Staff;

-- Table to store client information
CREATE TABLE Clients (
    client_id SERIAL PRIMARY KEY, -- Unique identifier for each client
    first_name VARCHAR(50) NOT NULL, -- Client's first name
    last_name VARCHAR(50) NOT NULL, -- Client's last name
    email VARCHAR(100) UNIQUE NOT NULL, -- Client's email address
    phone VARCHAR(15), -- Client's phone number
    address TEXT, -- Client's address
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store horse information
CREATE TABLE Horses (
    horse_id SERIAL PRIMARY KEY, -- Unique identifier for each horse
    client_id INT NOT NULL, -- Foreign key referencing Clients
    name VARCHAR(50) NOT NULL, -- Horse's name
    breed VARCHAR(50), -- Horse's breed
    age INT, -- Horse's age
    medical_history TEXT, -- Horse's medical history
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (client_id) REFERENCES Clients(client_id) ON DELETE CASCADE -- Ensures horses are deleted if the client is deleted
);

-- Table to store services offered
CREATE TABLE Services (
    service_id SERIAL PRIMARY KEY, -- Unique identifier for each service
    service_name VARCHAR(100) NOT NULL, -- Name of the service
    description TEXT, -- Description of the service
    price DECIMAL(10, 2) NOT NULL, -- Price of the service
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store staff information
CREATE TABLE Staff (
    staff_id SERIAL PRIMARY KEY, -- Unique identifier for each staff member
    first_name VARCHAR(50) NOT NULL, -- Staff member's first name
    last_name VARCHAR(50) NOT NULL, -- Staff member's last name
    role VARCHAR(50) NOT NULL, -- Role of the staff member (e.g., veterinarian, groomer)
    email VARCHAR(100) UNIQUE NOT NULL, -- Staff member's email address
    phone VARCHAR(15), -- Staff member's phone number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store appointment information
CREATE TABLE Appointments (
    appointment_id SERIAL PRIMARY KEY, -- Unique identifier for each appointment
    horse_id INT NOT NULL, -- Foreign key referencing Horses
    service_id INT NOT NULL, -- Foreign key referencing Services
    staff_id INT NOT NULL, -- Foreign key referencing Staff
    appointment_date TIMESTAMP NOT NULL, -- Date and time of the appointment
    notes TEXT, -- Additional notes for the appointment
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (horse_id) REFERENCES Horses(horse_id) ON DELETE CASCADE, -- Ensures appointments are deleted if the horse is deleted
    FOREIGN KEY (service_id) REFERENCES Services(service_id) ON DELETE CASCADE, -- Ensures appointments are deleted if the service is deleted
    FOREIGN KEY (staff_id) REFERENCES Staff(staff_id) ON DELETE CASCADE -- Ensures appointments are deleted if the staff member is deleted
);

-- Indexes for optimizing queries
CREATE INDEX idx_client_email ON Clients(email);
CREATE INDEX idx_horse_name ON Horses(name);
CREATE INDEX idx_service_name ON Services(service_name);
CREATE INDEX idx_staff_email ON Staff(email);
CREATE INDEX idx_appointment_date ON Appointments(appointment_date);
```
