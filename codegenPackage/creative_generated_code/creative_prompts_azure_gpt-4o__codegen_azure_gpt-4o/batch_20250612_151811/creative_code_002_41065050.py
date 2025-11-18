"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hubexperts.ch
Prompt: Generate code to create a database schema for storing client information, service details (e.g., company creation, auditing), and deadlines, based on the offerings of Hub Experts.
Generated: DETERMINISTIC_410650504a9d6ec0
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL Script to create a database schema for storing client information, service details, and deadlines.
-- This schema is designed to be efficient, normalized, and production-ready.

-- Create 'clients' table to store client information.
CREATE TABLE clients (
    client_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    name VARCHAR(255) NOT NULL, -- Full name of the client
    email VARCHAR(255) NOT NULL UNIQUE, -- Unique email address of the client
    phone_number VARCHAR(20), -- Contact number of the client
    address TEXT, -- Address details of the client
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the record was last updated
);

-- Create 'services' table to store service details.
CREATE TABLE services (
    service_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service
    name VARCHAR(255) NOT NULL, -- Name of the service (e.g., Company Creation, Auditing)
    description TEXT NOT NULL, -- Detailed description of the service
    price DECIMAL(10, 2) NOT NULL, -- Price of the service
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the record was last updated
);

-- Create 'deadlines' table to store deadlines related to services for clients.
CREATE TABLE deadlines (
    deadline_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each deadline
    client_id INT NOT NULL, -- Foreign key referencing the 'clients' table
    service_id INT NOT NULL, -- Foreign key referencing the 'services' table
    deadline_date DATE NOT NULL, -- Date of the deadline
    status ENUM('Pending', 'Completed', 'Overdue') DEFAULT 'Pending', -- Status of the deadline
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the record was last updated
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE, -- Cascade delete ensures integrity
    FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE CASCADE -- Cascade delete ensures integrity
);

-- Additional indices for improved query performance.
CREATE INDEX idx_client_email ON clients(email); -- Index on 'email' for faster lookups
CREATE INDEX idx_service_name ON services(name); -- Index on 'name' for faster lookups
CREATE INDEX idx_deadline_date ON deadlines(deadline_date); -- Index on 'deadline_date' for faster filtering
```
