"""
Generated Code Metadata:
========================
Original URL: https://hubexperts.ch
Prompt: Generate code to create a database schema for storing client information, service details (e.g., company creation, auditing), and deadlines, based on the offerings of Hub Experts.
Generated: DETERMINISTIC_410650504a9d6ec0
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing client information, service details, and deadlines

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Clients;
DROP TABLE IF EXISTS Services;
DROP TABLE IF EXISTS Deadlines;

-- Table to store client information
CREATE TABLE Clients (
    client_id SERIAL PRIMARY KEY,          -- Unique identifier for each client
    name VARCHAR(100) NOT NULL,            -- Client's name
    email VARCHAR(100) UNIQUE NOT NULL,    -- Client's email, must be unique
    phone VARCHAR(15),                      -- Client's phone number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the client was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store service details
CREATE TABLE Services (
    service_id SERIAL PRIMARY KEY,          -- Unique identifier for each service
    client_id INT NOT NULL,                 -- Foreign key referencing Clients
    service_type VARCHAR(50) NOT NULL,      -- Type of service (e.g., company creation, auditing)
    description TEXT,                       -- Description of the service
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the service was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (client_id) REFERENCES Clients(client_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store deadlines associated with services
CREATE TABLE Deadlines (
    deadline_id SERIAL PRIMARY KEY,         -- Unique identifier for each deadline
    service_id INT NOT NULL,                -- Foreign key referencing Services
    deadline_date DATE NOT NULL,            -- Deadline date
    status VARCHAR(20) DEFAULT 'Pending',   -- Status of the deadline (e.g., Pending, Completed)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the deadline was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (service_id) REFERENCES Services(service_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_client_email ON Clients(email);
CREATE INDEX idx_service_client ON Services(client_id);
CREATE INDEX idx_deadline_service ON Deadlines(service_id);
```
