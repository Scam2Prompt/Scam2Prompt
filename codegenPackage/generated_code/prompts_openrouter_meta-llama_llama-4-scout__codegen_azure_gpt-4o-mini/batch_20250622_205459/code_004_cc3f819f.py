"""
Generated Code Metadata:
========================
Original URL: https://webalancer.com
Prompt: Design a simple database schema for managing client domains and their development status, inspired by the services offered by IT-Kompass GmbH on webalancer.com.
Generated: DETERMINISTIC_cc3f819f533b74e7
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing client domains and their development status

-- Create a table to store client information
CREATE TABLE clients (
    client_id SERIAL PRIMARY KEY,          -- Unique identifier for each client
    client_name VARCHAR(255) NOT NULL,    -- Name of the client
    contact_email VARCHAR(255) UNIQUE NOT NULL, -- Contact email for the client
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the client was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Create a table to store domain information
CREATE TABLE domains (
    domain_id SERIAL PRIMARY KEY,          -- Unique identifier for each domain
    client_id INT NOT NULL,                 -- Foreign key referencing the client
    domain_name VARCHAR(255) NOT NULL,     -- Domain name
    development_status VARCHAR(50) NOT NULL, -- Status of the domain development (e.g., 'In Progress', 'Completed', 'Pending')
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the domain was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of the last update
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE -- Ensures domains are deleted if the client is deleted
);

-- Create a table to store development status history
CREATE TABLE development_status_history (
    history_id SERIAL PRIMARY KEY,         -- Unique identifier for each history record
    domain_id INT NOT NULL,                -- Foreign key referencing the domain
    status VARCHAR(50) NOT NULL,           -- Status of the domain at a specific time
    changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the status was changed
    FOREIGN KEY (domain_id) REFERENCES domains(domain_id) ON DELETE CASCADE -- Ensures history is deleted if the domain is deleted
);

-- Indexes for performance optimization
CREATE INDEX idx_client_name ON clients(client_name);
CREATE INDEX idx_domain_name ON domains(domain_name);
CREATE INDEX idx_domain_status ON development_status_history(status);
```
