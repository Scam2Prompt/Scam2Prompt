"""
Generated Code Metadata:
========================
Original URL: https://inmobiliariacapri.com.co
Prompt: "Design a database schema to store information about properties, clients, and transactions for a real estate company like Inmobiliaria Capri."
Generated: DETERMINISTIC_9e9c02fe067c6bf5
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a real estate company

-- Drop existing tables if they exist (for development purposes)
DROP TABLE IF EXISTS Transactions;
DROP TABLE IF EXISTS Properties;
DROP TABLE IF EXISTS Clients;

-- Table to store client information
CREATE TABLE Clients (
    client_id SERIAL PRIMARY KEY, -- Unique identifier for each client
    first_name VARCHAR(50) NOT NULL, -- Client's first name
    last_name VARCHAR(50) NOT NULL, -- Client's last name
    email VARCHAR(100) UNIQUE NOT NULL, -- Client's email address
    phone VARCHAR(15), -- Client's phone number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store property information
CREATE TABLE Properties (
    property_id SERIAL PRIMARY KEY, -- Unique identifier for each property
    address VARCHAR(255) NOT NULL, -- Property address
    city VARCHAR(100) NOT NULL, -- City where the property is located
    state VARCHAR(100) NOT NULL, -- State where the property is located
    zip_code VARCHAR(10) NOT NULL, -- Zip code of the property
    price DECIMAL(10, 2) NOT NULL, -- Price of the property
    property_type VARCHAR(50) NOT NULL, -- Type of property (e.g., house, apartment)
    status VARCHAR(20) NOT NULL CHECK (status IN ('available', 'sold', 'pending')), -- Status of the property
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store transaction information
CREATE TABLE Transactions (
    transaction_id SERIAL PRIMARY KEY, -- Unique identifier for each transaction
    client_id INT NOT NULL, -- Foreign key referencing Clients
    property_id INT NOT NULL, -- Foreign key referencing Properties
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of the transaction
    transaction_amount DECIMAL(10, 2) NOT NULL, -- Amount of the transaction
    status VARCHAR(20) NOT NULL CHECK (status IN ('completed', 'pending', 'canceled')), -- Status of the transaction
    FOREIGN KEY (client_id) REFERENCES Clients(client_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (property_id) REFERENCES Properties(property_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_client_email ON Clients(email);
CREATE INDEX idx_property_address ON Properties(address);
CREATE INDEX idx_transaction_date ON Transactions(transaction_date);
```
