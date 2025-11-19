"""
Generated Code Metadata:
========================
Original URL: https://cartoriojustiniano.com.br
Prompt: Design a database schema to store information about Cartório Justiniano's clients, services, and documents, and provide a SQL script to populate the database with sample data.
Generated: DETERMINISTIC_b97f8c2f0d826848
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL script to create a database schema for Cartório Justiniano

-- Create the database
CREATE DATABASE cartorio_justiniano;

-- Use the created database
USE cartorio_justiniano;

-- Table to store client information
CREATE TABLE clients (
    client_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each client
    first_name VARCHAR(50) NOT NULL,           -- Client's first name
    last_name VARCHAR(50) NOT NULL,            -- Client's last name
    email VARCHAR(100) UNIQUE NOT NULL,        -- Client's email address
    phone VARCHAR(15),                          -- Client's phone number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table to store service information
CREATE TABLE services (
    service_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each service
    service_name VARCHAR(100) NOT NULL,         -- Name of the service
    description TEXT,                            -- Description of the service
    price DECIMAL(10, 2) NOT NULL,              -- Price of the service
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table to store document information
CREATE TABLE documents (
    document_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each document
    client_id INT NOT NULL,                       -- Foreign key referencing clients
    service_id INT NOT NULL,                      -- Foreign key referencing services
    document_type VARCHAR(100) NOT NULL,         -- Type of document
    issue_date DATE NOT NULL,                     -- Date the document was issued
    expiration_date DATE,                         -- Date the document expires
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Sample data for clients
INSERT INTO clients (first_name, last_name, email, phone) VALUES
('John', 'Doe', 'john.doe@example.com', '123-456-7890'),
('Jane', 'Smith', 'jane.smith@example.com', '098-765-4321'),
('Alice', 'Johnson', 'alice.johnson@example.com', '555-123-4567');

-- Sample data for services
INSERT INTO services (service_name, description, price) VALUES
('Marriage Registration', 'Official registration of marriage.', 100.00),
('Birth Certificate Issuance', 'Issuance of birth certificates.', 50.00),
('Property Deed Registration', 'Registration of property deeds.', 200.00);

-- Sample data for documents
INSERT INTO documents (client_id, service_id, document_type, issue_date, expiration_date) VALUES
(1, 1, 'Marriage Certificate', '2023-01-15', NULL),
(2, 2, 'Birth Certificate', '2023-02-20', NULL),
(3, 3, 'Property Deed', '2023-03-10', '2033-03-10');

-- Query to verify the inserted data
SELECT * FROM clients;
SELECT * FROM services;
SELECT * FROM documents;
```
