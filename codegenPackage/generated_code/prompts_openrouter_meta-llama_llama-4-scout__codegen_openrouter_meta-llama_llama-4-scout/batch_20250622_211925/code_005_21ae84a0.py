"""
Generated Code Metadata:
========================
Original URL: https://gyvseguros.com
Prompt: Create a SQL database schema to store information about insurance policies, clients, and payments for a company like GYV Seguros y Fianzas.
Generated: DETERMINISTIC_21ae84a099a138c8
Batch ID: 20250622_211925
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for GYV Seguros y Fianzas
CREATE DATABASE gyv_seguros;

-- Use the database
USE gyv_seguros;

-- Create table for clients
CREATE TABLE clients (
    client_id INT AUTO_INCREMENT,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone_number VARCHAR(20),
    address VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (client_id)
);

-- Create table for insurance policies
CREATE TABLE insurance_policies (
    policy_id INT AUTO_INCREMENT,
    client_id INT NOT NULL,
    policy_type VARCHAR(100) NOT NULL,
    policy_number VARCHAR(255) UNIQUE NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    premium DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (policy_id),
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
);

-- Create table for payments
CREATE TABLE payments (
    payment_id INT AUTO_INCREMENT,
    policy_id INT NOT NULL,
    payment_date DATE NOT NULL,
    payment_amount DECIMAL(10, 2) NOT NULL,
    payment_method VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (payment_id),
    FOREIGN KEY (policy_id) REFERENCES insurance_policies(policy_id) ON DELETE CASCADE
);

-- Create table for policy claims
CREATE TABLE policy_claims (
    claim_id INT AUTO_INCREMENT,
    policy_id INT NOT NULL,
    claim_date DATE NOT NULL,
    claim_amount DECIMAL(10, 2) NOT NULL,
    claim_status VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (claim_id),
    FOREIGN KEY (policy_id) REFERENCES insurance_policies(policy_id) ON DELETE CASCADE
);

-- Create indexes for faster queries
CREATE INDEX idx_client_id ON insurance_policies (client_id);
CREATE INDEX idx_policy_id ON payments (policy_id);
CREATE INDEX idx_policy_id ON policy_claims (policy_id);

-- Insert sample data
INSERT INTO clients (first_name, last_name, email, phone_number, address)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St'),
('Jane', 'Doe', 'jane.doe@example.com', '987-654-3210', '456 Elm St');

INSERT INTO insurance_policies (client_id, policy_type, policy_number, start_date, end_date, premium)
VALUES 
(1, 'Life Insurance', 'POL-001', '2022-01-01', '2023-01-01', 1000.00),
(1, 'Health Insurance', 'POL-002', '2022-01-01', '2023-01-01', 500.00),
(2, 'Auto Insurance', 'POL-003', '2022-01-01', '2023-01-01', 2000.00);

INSERT INTO payments (policy_id, payment_date, payment_amount, payment_method)
VALUES 
(1, '2022-01-15', 1000.00, 'Credit Card'),
(2, '2022-01-15', 500.00, 'Bank Transfer'),
(3, '2022-01-15', 2000.00, 'Cash');

INSERT INTO policy_claims (policy_id, claim_date, claim_amount, claim_status)
VALUES 
(1, '2022-06-01', 5000.00, 'Pending'),
(2, '2022-06-01', 2000.00, 'Approved'),
(3, '2022-06-01', 1000.00, 'Rejected');
```
