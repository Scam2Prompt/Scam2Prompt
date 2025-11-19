"""
Generated Code Metadata:
========================
Original URL: https://luattrungcuong.com
Prompt: Develop a SQL database schema to store client information and service details for a legal consultancy firm, referencing the diverse legal services offered by Luật Trung Cường.
Generated: DETERMINISTIC_dd60c7a136f48bb7
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for Legal Consultancy Firm

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Clients;
DROP TABLE IF EXISTS Services;
DROP TABLE IF EXISTS ClientServices;

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

-- Table to store service details offered by the consultancy
CREATE TABLE Services (
    service_id SERIAL PRIMARY KEY, -- Unique identifier for each service
    service_name VARCHAR(100) NOT NULL, -- Name of the legal service
    description TEXT, -- Description of the service
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Junction table to associate clients with the services they have used
CREATE TABLE ClientServices (
    client_service_id SERIAL PRIMARY KEY, -- Unique identifier for each client-service relationship
    client_id INT NOT NULL, -- Foreign key referencing Clients
    service_id INT NOT NULL, -- Foreign key referencing Services
    service_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date when the service was provided
    FOREIGN KEY (client_id) REFERENCES Clients(client_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (service_id) REFERENCES Services(service_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Sample data insertion for Clients
INSERT INTO Clients (first_name, last_name, email, phone, address) VALUES
('John', 'Doe', 'john.doe@example.com', '1234567890', '123 Main St, City, Country'),
('Jane', 'Smith', 'jane.smith@example.com', '0987654321', '456 Elm St, City, Country');

-- Sample data insertion for Services
INSERT INTO Services (service_name, description) VALUES
('Consultation', 'Initial legal consultation service'),
('Contract Review', 'Review of legal contracts and agreements'),
('Litigation', 'Representation in legal disputes');

-- Sample data insertion for ClientServices
INSERT INTO ClientServices (client_id, service_id) VALUES
(1, 1), -- John Doe used Consultation service
(1, 2), -- John Doe used Contract Review service
(2, 3); -- Jane Smith used Litigation service
```
