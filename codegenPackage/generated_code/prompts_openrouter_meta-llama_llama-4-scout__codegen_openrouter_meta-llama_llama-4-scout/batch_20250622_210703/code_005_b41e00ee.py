"""
Generated Code Metadata:
========================
Original URL: https://grupoinmobiliariocrecer.com.co
Prompt: Design a database schema for storing information about properties, clients, and transactions for a real estate company like Grupo Crecer.
Generated: DETERMINISTIC_b41e00ee634ba77e
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database
CREATE DATABASE real_estate;

-- Use database
USE real_estate;

-- Create table for properties
CREATE TABLE properties (
  id INT AUTO_INCREMENT,
  address VARCHAR(255) NOT NULL,
  city VARCHAR(100) NOT NULL,
  state VARCHAR(100) NOT NULL,
  zip_code VARCHAR(20) NOT NULL,
  property_type ENUM('residential', 'commercial') NOT NULL,
  price DECIMAL(10, 2) NOT NULL,
  square_footage INT NOT NULL,
  num_bedrooms INT,
  num_bathrooms INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for clients
CREATE TABLE clients (
  id INT AUTO_INCREMENT,
  first_name VARCHAR(100) NOT NULL,
  last_name VARCHAR(100) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for transactions
CREATE TABLE transactions (
  id INT AUTO_INCREMENT,
  property_id INT NOT NULL,
  client_id INT NOT NULL,
  transaction_date DATE NOT NULL,
  transaction_type ENUM('sale', 'rental') NOT NULL,
  amount DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (property_id) REFERENCES properties(id) ON DELETE CASCADE,
  FOREIGN KEY (client_id) REFERENCES clients(id) ON DELETE CASCADE
);

-- Create table for agents
CREATE TABLE agents (
  id INT AUTO_INCREMENT,
  first_name VARCHAR(100) NOT NULL,
  last_name VARCHAR(100) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for property agents
CREATE TABLE property_agents (
  property_id INT NOT NULL,
  agent_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (property_id, agent_id),
  FOREIGN KEY (property_id) REFERENCES properties(id) ON DELETE CASCADE,
  FOREIGN KEY (agent_id) REFERENCES agents(id) ON DELETE CASCADE
);

-- Create indexes
CREATE INDEX idx_properties_address ON properties (address);
CREATE INDEX idx_clients_email ON clients (email);
CREATE INDEX idx_transactions_property_id ON transactions (property_id);
CREATE INDEX idx_transactions_client_id ON transactions (client_id);
```

```sql
-- data.sql

-- Insert sample data into properties table
INSERT INTO properties (address, city, state, zip_code, property_type, price, square_footage, num_bedrooms, num_bathrooms)
VALUES
  ('123 Main St', 'Anytown', 'CA', '12345', 'residential', 500000.00, 2000, 3, 2),
  ('456 Elm St', 'Othertown', 'NY', '67890', 'residential', 750000.00, 3000, 4, 3),
  ('789 Oak St', 'Anytown', 'CA', '12345', 'commercial', 1000000.00, 5000, NULL, NULL);

-- Insert sample data into clients table
INSERT INTO clients (first_name, last_name, email, phone_number)
VALUES
  ('John', 'Doe', 'john.doe@example.com', '555-1234'),
  ('Jane', 'Smith', 'jane.smith@example.com', '555-5678'),
  ('Bob', 'Johnson', 'bob.johnson@example.com', '555-9012');

-- Insert sample data into transactions table
INSERT INTO transactions (property_id, client_id, transaction_date, transaction_type, amount)
VALUES
  (1, 1, '2022-01-01', 'sale', 500000.00),
  (2, 2, '2022-06-01', 'rental', 2000.00),
  (3, 3, '2022-12-01', 'sale', 1000000.00);

-- Insert sample data into agents table
INSERT INTO agents (first_name, last_name, email, phone_number)
VALUES
  ('Alice', 'Brown', 'alice.brown@example.com', '555-1111'),
  ('Mike', 'Davis', 'mike.davis@example.com', '555-2222'),
  ('Emily', 'Chen', 'emily.chen@example.com', '555-3333');

-- Insert sample data into property_agents table
INSERT INTO property_agents (property_id, agent_id)
VALUES
  (1, 1),
  (1, 2),
  (2, 3),
  (3, 1);
```
