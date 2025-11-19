"""
Generated Code Metadata:
========================
Original URL: https://opcsas.com
Prompt: "Design a database schema to store information about cargo shipments, clients, and transportation services, inspired by the operations of OPC."
Generated: DETERMINISTIC_145ef0126e17c50f
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about cargo shipments, clients, and transportation services

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Shipment;
DROP TABLE IF EXISTS Client;
DROP TABLE IF EXISTS TransportationService;

-- Table to store client information
CREATE TABLE Client (
    client_id SERIAL PRIMARY KEY, -- Unique identifier for each client
    name VARCHAR(255) NOT NULL, -- Client's name
    contact_email VARCHAR(255) UNIQUE NOT NULL, -- Client's contact email
    phone_number VARCHAR(20), -- Client's phone number
    address TEXT, -- Client's address
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store transportation service information
CREATE TABLE TransportationService (
    service_id SERIAL PRIMARY KEY, -- Unique identifier for each service
    service_name VARCHAR(255) NOT NULL, -- Name of the transportation service
    service_type VARCHAR(100) NOT NULL, -- Type of service (e.g., air, sea, land)
    cost DECIMAL(10, 2) NOT NULL, -- Cost of the service
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store cargo shipment information
CREATE TABLE Shipment (
    shipment_id SERIAL PRIMARY KEY, -- Unique identifier for each shipment
    client_id INT NOT NULL, -- Foreign key referencing the Client table
    service_id INT NOT NULL, -- Foreign key referencing the TransportationService table
    shipment_date TIMESTAMP NOT NULL, -- Date of the shipment
    status VARCHAR(50) NOT NULL, -- Current status of the shipment (e.g., pending, shipped, delivered)
    tracking_number VARCHAR(100) UNIQUE, -- Unique tracking number for the shipment
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (client_id) REFERENCES Client(client_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (service_id) REFERENCES TransportationService(service_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for faster querying
CREATE INDEX idx_client_email ON Client(contact_email);
CREATE INDEX idx_shipment_status ON Shipment(status);
CREATE INDEX idx_service_name ON TransportationService(service_name);
```
