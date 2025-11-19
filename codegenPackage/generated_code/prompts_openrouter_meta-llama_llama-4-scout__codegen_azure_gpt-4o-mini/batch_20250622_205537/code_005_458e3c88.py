"""
Generated Code Metadata:
========================
Original URL: https://majeli-avocat.com
Prompt: Design a basic database schema to store information about clients, cases, and appointments for a law firm like Majeli Avocat, and suggest a suitable programming language for implementation.
Generated: DETERMINISTIC_458e3c885158b79d
Batch ID: 20250622_205537
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for a Law Firm

-- Table to store client information
CREATE TABLE Clients (
    client_id SERIAL PRIMARY KEY, -- Unique identifier for each client
    first_name VARCHAR(50) NOT NULL, -- Client's first name
    last_name VARCHAR(50) NOT NULL, -- Client's last name
    email VARCHAR(100) UNIQUE NOT NULL, -- Client's email address
    phone VARCHAR(15), -- Client's phone number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table to store case information
CREATE TABLE Cases (
    case_id SERIAL PRIMARY KEY, -- Unique identifier for each case
    client_id INT NOT NULL, -- Foreign key referencing Clients
    case_number VARCHAR(50) UNIQUE NOT NULL, -- Unique case number
    case_type VARCHAR(50) NOT NULL, -- Type of case (e.g., Criminal, Civil)
    status VARCHAR(20) NOT NULL, -- Current status of the case (e.g., Open, Closed)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (client_id) REFERENCES Clients(client_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store appointment information
CREATE TABLE Appointments (
    appointment_id SERIAL PRIMARY KEY, -- Unique identifier for each appointment
    case_id INT NOT NULL, -- Foreign key referencing Cases
    appointment_date TIMESTAMP NOT NULL, -- Date and time of the appointment
    location VARCHAR(100), -- Location of the appointment
    notes TEXT, -- Additional notes for the appointment
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (case_id) REFERENCES Cases(case_id) ON DELETE CASCADE -- Ensures referential integrity
);
```

### Suggested Programming Language for Implementation
- **Python**: A versatile language with strong support for database interaction through libraries like SQLAlchemy or Django ORM, making it suitable for building applications that manage client, case, and appointment data efficiently.
