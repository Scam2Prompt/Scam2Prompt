"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.olgon.net
Prompt: Develop a database schema for tracking suppliers, service providers, cooperatives, and farmers, leveraging ICT as mentioned in Olgon Prime Resources Ltd.'s processes.
Generated: DETERMINISTIC_76623723570720bc
Batch ID: 20250612_151534
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Tracking Suppliers, Service Providers, Cooperatives, and Farmers
-- This schema is designed to leverage ICT for efficient tracking and management.

-- Table: Users
-- General table to store user details (suppliers, service providers, cooperatives, and farmers)
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,           -- Unique identifier for each user
    user_type VARCHAR(50) NOT NULL,       -- Type of user (e.g., 'Supplier', 'Service Provider', 'Cooperative', 'Farmer')
    name VARCHAR(255) NOT NULL,           -- Name of the user
    email VARCHAR(255) UNIQUE NOT NULL,   -- Email of the user (must be unique)
    phone VARCHAR(20),                    -- Phone number of the user
    address TEXT,                         -- Address of the user
    registered_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Registration date
    is_active BOOLEAN DEFAULT TRUE        -- Status of the user (active/inactive)
);

-- Table: Suppliers
-- Specific details for suppliers
CREATE TABLE Suppliers (
    supplier_id SERIAL PRIMARY KEY,       -- Unique identifier for the supplier
    user_id INT NOT NULL,                 -- Reference to Users table
    company_name VARCHAR(255),            -- Name of the company
    product_type VARCHAR(255),            -- Type of products supplied
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Ensures data integrity
);

-- Table: ServiceProviders
-- Specific details for service providers
CREATE TABLE ServiceProviders (
    service_provider_id SERIAL PRIMARY KEY, -- Unique identifier for the service provider
    user_id INT NOT NULL,                    -- Reference to Users table
    service_type VARCHAR(255),               -- Type of services offered
    availability_schedule TEXT,              -- Availability schedule of the provider
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Ensures data integrity
);

-- Table: Cooperatives
-- Specific details for cooperatives
CREATE TABLE Cooperatives (
    cooperative_id SERIAL PRIMARY KEY,     -- Unique identifier for the cooperative
    user_id INT NOT NULL,                  -- Reference to Users table
    cooperative_name VARCHAR(255),         -- Name of the cooperative
    total_members INT DEFAULT 0,           -- Total number of members in the cooperative
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Ensures data integrity
);

-- Table: Farmers
-- Specific details for farmers
CREATE TABLE Farmers (
    farmer_id SERIAL PRIMARY KEY,          -- Unique identifier for the farmer
    user_id INT NOT NULL,                  -- Reference to Users table
    farm_size DECIMAL(10,2),               -- Size of the farm (e.g., in acres or hectares)
    crop_type VARCHAR(255),                -- Type of crops grown
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Ensures data integrity
);

-- Table: Transactions
-- To log transactions between various entities
CREATE TABLE Transactions (
    transaction_id SERIAL PRIMARY KEY,     -- Unique identifier for the transaction
    sender_id INT NOT NULL,                -- Sender's user_id
    receiver_id INT NOT NULL,              -- Receiver's user_id
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of the transaction
    transaction_amount DECIMAL(10,2) NOT NULL, -- Amount involved in the transaction
    description TEXT,                      -- Description of the transaction
    FOREIGN KEY (sender_id) REFERENCES Users(user_id) ON DELETE SET NULL, -- Reference to sender
    FOREIGN KEY (receiver_id) REFERENCES Users(user_id) ON DELETE SET NULL -- Reference to receiver
);

-- Table: ICTLogs
-- Logs for ICT interactions to track and record activities
CREATE TABLE ICTLogs (
    log_id SERIAL PRIMARY KEY,             -- Unique identifier for the log entry
    user_id INT NOT NULL,                  -- Reference to Users table
    action VARCHAR(255) NOT NULL,          -- Action performed (e.g., 'Login', 'Transaction')
    log_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Time of the action
    details TEXT,                          -- Additional details about the action
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Ensures data integrity
);

-- Indexes for optimization
CREATE INDEX idx_users_user_type ON Users(user_type); -- Index for user_type queries
CREATE INDEX idx_transactions_date ON Transactions(transaction_date); -- Index for transaction date queries

-- End of Schema
```
