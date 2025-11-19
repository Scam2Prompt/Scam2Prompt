"""
Generated Code Metadata:
========================
Original URL: https://global-sconsulting.com
Prompt: "Design a database schema for a real estate brokerage platform in Senegal, including tables for properties, clients, and transactions."
Generated: DETERMINISTIC_ae976d62dee0de8a
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a real estate brokerage platform in Senegal

-- Create a table for properties
CREATE TABLE properties (
    property_id SERIAL PRIMARY KEY, -- Unique identifier for each property
    title VARCHAR(255) NOT NULL, -- Title of the property
    description TEXT, -- Detailed description of the property
    price DECIMAL(15, 2) NOT NULL, -- Price of the property
    location VARCHAR(255) NOT NULL, -- Location of the property
    property_type VARCHAR(100) NOT NULL, -- Type of property (e.g., house, apartment, land)
    status VARCHAR(50) NOT NULL CHECK (status IN ('available', 'sold', 'rented')), -- Status of the property
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the property was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the property was last updated
);

-- Create a table for clients
CREATE TABLE clients (
    client_id SERIAL PRIMARY KEY, -- Unique identifier for each client
    first_name VARCHAR(100) NOT NULL, -- Client's first name
    last_name VARCHAR(100) NOT NULL, -- Client's last name
    email VARCHAR(255) UNIQUE NOT NULL, -- Client's email address
    phone_number VARCHAR(20), -- Client's phone number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the client was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the client was last updated
);

-- Create a table for transactions
CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY, -- Unique identifier for each transaction
    property_id INT NOT NULL, -- Foreign key referencing the property involved in the transaction
    client_id INT NOT NULL, -- Foreign key referencing the client involved in the transaction
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of the transaction
    transaction_type VARCHAR(50) NOT NULL CHECK (transaction_type IN ('buy', 'rent')), -- Type of transaction
    amount DECIMAL(15, 2) NOT NULL, -- Amount involved in the transaction
    FOREIGN KEY (property_id) REFERENCES properties(property_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_property_status ON properties(status);
CREATE INDEX idx_client_email ON clients(email);
CREATE INDEX idx_transaction_date ON transactions(transaction_date);
```
