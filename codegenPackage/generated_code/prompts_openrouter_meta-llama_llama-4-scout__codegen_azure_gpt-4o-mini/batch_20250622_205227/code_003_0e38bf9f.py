"""
Generated Code Metadata:
========================
Original URL: https://www.sharethomecare.com.au
Prompt: "Design a database schema to store information about NDIS services, including supported independent living, assistance with travel and transport, and community participation activities."
Generated: DETERMINISTIC_0e38bf9fc20e36d9
Batch ID: 20250622_205227
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about NDIS services

-- Create a table to store information about NDIS services
CREATE TABLE NDIS_Services (
    service_id SERIAL PRIMARY KEY, -- Unique identifier for each service
    service_name VARCHAR(255) NOT NULL, -- Name of the service
    service_description TEXT, -- Description of the service
    service_type VARCHAR(50) NOT NULL CHECK (service_type IN ('Independent Living', 'Travel and Transport', 'Community Participation')), -- Type of service
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the service was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the service was last updated
);

-- Create a table to store information about clients
CREATE TABLE Clients (
    client_id SERIAL PRIMARY KEY, -- Unique identifier for each client
    client_name VARCHAR(255) NOT NULL, -- Name of the client
    date_of_birth DATE NOT NULL, -- Date of birth of the client
    contact_number VARCHAR(15), -- Contact number of the client
    email VARCHAR(255), -- Email address of the client
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the client was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the client was last updated
);

-- Create a table to link clients to the services they are receiving
CREATE TABLE Client_Services (
    client_service_id SERIAL PRIMARY KEY, -- Unique identifier for each client-service relationship
    client_id INT NOT NULL, -- Foreign key referencing Clients
    service_id INT NOT NULL, -- Foreign key referencing NDIS_Services
    start_date DATE NOT NULL, -- Start date of the service for the client
    end_date DATE, -- End date of the service for the client (nullable)
    status VARCHAR(50) NOT NULL CHECK (status IN ('Active', 'Inactive')), -- Status of the service for the client
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the client-service relationship was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the client-service relationship was last updated
    FOREIGN KEY (client_id) REFERENCES Clients(client_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (service_id) REFERENCES NDIS_Services(service_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create an index on the service type for faster queries
CREATE INDEX idx_service_type ON NDIS_Services(service_type);

-- Create an index on the client name for faster queries
CREATE INDEX idx_client_name ON Clients(client_name);
```
