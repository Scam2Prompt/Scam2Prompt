"""
Generated Code Metadata:
========================
Original URL: https://www.limpiezadetuboscostablanca.net
Prompt: Create a database schema for storing information about plumbing service calls, including fields for service type (e.g., asbestos removal, pipe rehabilitation), customer details, and technician assignments, inspired by Limpieza de Tubos Costablanca.
Generated: DETERMINISTIC_c6fee5a1d532c625
Batch ID: 20250612_154909
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about plumbing service calls

CREATE TABLE Customers (
    customer_id SERIAL PRIMARY KEY, -- Unique identifier for each customer
    first_name VARCHAR(50) NOT NULL, -- Customer's first name
    last_name VARCHAR(50) NOT NULL, -- Customer's last name
    phone_number VARCHAR(15) NOT NULL, -- Customer's phone number
    email VARCHAR(100), -- Customer's email address
    address TEXT NOT NULL, -- Customer's address
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

CREATE TABLE ServiceTypes (
    service_type_id SERIAL PRIMARY KEY, -- Unique identifier for each service type
    service_name VARCHAR(100) NOT NULL, -- Name of the service (e.g., asbestos removal)
    description TEXT, -- Description of the service
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

CREATE TABLE Technicians (
    technician_id SERIAL PRIMARY KEY, -- Unique identifier for each technician
    first_name VARCHAR(50) NOT NULL, -- Technician's first name
    last_name VARCHAR(50) NOT NULL, -- Technician's last name
    phone_number VARCHAR(15) NOT NULL, -- Technician's phone number
    email VARCHAR(100), -- Technician's email address
    hire_date DATE NOT NULL, -- Date the technician was hired
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

CREATE TABLE ServiceCalls (
    service_call_id SERIAL PRIMARY KEY, -- Unique identifier for each service call
    customer_id INT NOT NULL, -- Foreign key referencing Customers
    service_type_id INT NOT NULL, -- Foreign key referencing ServiceTypes
    technician_id INT, -- Foreign key referencing Technicians (nullable)
    service_date TIMESTAMP NOT NULL, -- Date and time of the service call
    status VARCHAR(20) NOT NULL DEFAULT 'Pending', -- Status of the service call (e.g., Pending, Completed)
    notes TEXT, -- Additional notes about the service call
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (service_type_id) REFERENCES ServiceTypes(service_type_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (technician_id) REFERENCES Technicians(technician_id) ON DELETE SET NULL -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_service_calls_customer ON ServiceCalls(customer_id);
CREATE INDEX idx_service_calls_service_type ON ServiceCalls(service_type_id);
CREATE INDEX idx_service_calls_technician ON ServiceCalls(technician_id);
```
