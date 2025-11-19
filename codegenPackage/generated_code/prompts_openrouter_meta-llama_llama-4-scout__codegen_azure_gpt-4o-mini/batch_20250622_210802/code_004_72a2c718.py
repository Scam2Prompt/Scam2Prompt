"""
Generated Code Metadata:
========================
Original URL: https://cooperativacooprometa.com
Prompt: Design a basic database schema for storing client information, credits, and educational programs for a cooperative like Cooprometa.
Generated: DETERMINISTIC_72a2c718827b14fb
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Cooprometa

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Clients;
DROP TABLE IF EXISTS Credits;
DROP TABLE IF EXISTS EducationalPrograms;

-- Table to store client information
CREATE TABLE Clients (
    client_id SERIAL PRIMARY KEY, -- Unique identifier for each client
    first_name VARCHAR(50) NOT NULL, -- Client's first name
    last_name VARCHAR(50) NOT NULL, -- Client's last name
    email VARCHAR(100) UNIQUE NOT NULL, -- Client's email address, must be unique
    phone_number VARCHAR(15), -- Client's phone number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store credits associated with clients
CREATE TABLE Credits (
    credit_id SERIAL PRIMARY KEY, -- Unique identifier for each credit
    client_id INT NOT NULL, -- Foreign key referencing Clients table
    amount DECIMAL(10, 2) NOT NULL, -- Amount of credit
    issued_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when credit was issued
    FOREIGN KEY (client_id) REFERENCES Clients(client_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store educational programs
CREATE TABLE EducationalPrograms (
    program_id SERIAL PRIMARY KEY, -- Unique identifier for each program
    program_name VARCHAR(100) NOT NULL, -- Name of the educational program
    description TEXT, -- Description of the program
    start_date DATE NOT NULL, -- Start date of the program
    end_date DATE NOT NULL, -- End date of the program
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to associate clients with educational programs
CREATE TABLE ClientPrograms (
    client_program_id SERIAL PRIMARY KEY, -- Unique identifier for each client-program association
    client_id INT NOT NULL, -- Foreign key referencing Clients table
    program_id INT NOT NULL, -- Foreign key referencing EducationalPrograms table
    enrollment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the client enrolled in the program
    FOREIGN KEY (client_id) REFERENCES Clients(client_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (program_id) REFERENCES EducationalPrograms(program_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_client_email ON Clients(email);
CREATE INDEX idx_program_name ON EducationalPrograms(program_name);
```
