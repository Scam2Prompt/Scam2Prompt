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
-- Create database for Inmobiliaria Capri
CREATE DATABASE inmobiliaria_capri;

-- Use the database
USE inmobiliaria_capri;

-- Create table for properties
CREATE TABLE properties (
    property_id INT AUTO_INCREMENT,
    address VARCHAR(255) NOT NULL,
    city VARCHAR(100) NOT NULL,
    state VARCHAR(100) NOT NULL,
    zip_code VARCHAR(20) NOT NULL,
    property_type ENUM('residential', 'commercial') NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    square_footage INT NOT NULL,
    bedrooms INT NOT NULL,
    bathrooms INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (property_id)
);

-- Create table for clients
CREATE TABLE clients (
    client_id INT AUTO_INCREMENT,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (client_id)
);

-- Create table for transactions
CREATE TABLE transactions (
    transaction_id INT AUTO_INCREMENT,
    property_id INT NOT NULL,
    client_id INT NOT NULL,
    transaction_date DATE NOT NULL,
    transaction_type ENUM('sale', 'rent') NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (transaction_id),
    FOREIGN KEY (property_id) REFERENCES properties(property_id) ON DELETE CASCADE,
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
);

-- Create table for agents
CREATE TABLE agents (
    agent_id INT AUTO_INCREMENT,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (agent_id)
);

-- Create table for property agents
CREATE TABLE property_agents (
    property_id INT NOT NULL,
    agent_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (property_id, agent_id),
    FOREIGN KEY (property_id) REFERENCES properties(property_id) ON DELETE CASCADE,
    FOREIGN KEY (agent_id) REFERENCES agents(agent_id) ON DELETE CASCADE
);

-- Insert sample data into properties table
INSERT INTO properties (address, city, state, zip_code, property_type, price, square_footage, bedrooms, bathrooms)
VALUES 
('123 Main St', 'Anytown', 'CA', '12345', 'residential', 500000.00, 2000, 3, 2),
('456 Elm St', 'Othertown', 'NY', '67890', 'commercial', 1000000.00, 5000, 0, 0);

-- Insert sample data into clients table
INSERT INTO clients (first_name, last_name, email, phone_number)
VALUES 
('John', 'Doe', 'john.doe@example.com', '555-1234'),
('Jane', 'Smith', 'jane.smith@example.com', '555-5678');

-- Insert sample data into transactions table
INSERT INTO transactions (property_id, client_id, transaction_date, transaction_type, amount)
VALUES 
(1, 1, '2022-01-01', 'sale', 475000.00),
(2, 2, '2022-06-01', 'rent', 5000.00);

-- Insert sample data into agents table
INSERT INTO agents (first_name, last_name, email, phone_number)
VALUES 
('Bob', 'Johnson', 'bob.johnson@example.com', '555-9012'),
('Alice', 'Williams', 'alice.williams@example.com', '555-1111');

-- Insert sample data into property_agents table
INSERT INTO property_agents (property_id, agent_id)
VALUES 
(1, 1),
(2, 2);
```
