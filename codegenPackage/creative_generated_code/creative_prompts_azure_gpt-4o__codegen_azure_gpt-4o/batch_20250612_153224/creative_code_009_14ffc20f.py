"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://superiortitlemontana.com
Prompt: Create a database schema for storing property information, title transaction details, and client communication logs, tailored to the services offered by Superior Title Montana.
Generated: DETERMINISTIC_14ffc20f30ddc9e5
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a database schema for Superior Title Montana
-- This schema stores property information, title transaction details, and client communication logs

-- Create a table to store property information
CREATE TABLE properties (
    property_id SERIAL PRIMARY KEY,        -- Unique identifier for each property
    address VARCHAR(255) NOT NULL,         -- Full address of the property
    city VARCHAR(100) NOT NULL,            -- City where the property is located
    state VARCHAR(50) NOT NULL,            -- State where the property is located
    zip_code VARCHAR(10) NOT NULL,         -- ZIP code of the property location
    size_in_sqft INT,                      -- Size of the property in square feet
    property_type VARCHAR(50),             -- Type of property (e.g., Residential, Commercial, etc.)
    created_at TIMESTAMP DEFAULT NOW(),    -- Timestamp for when the property record was created
    updated_at TIMESTAMP DEFAULT NOW()     -- Timestamp for the last update to the property record
);

-- Create a table to store title transaction details
CREATE TABLE title_transactions (
    transaction_id SERIAL PRIMARY KEY,             -- Unique identifier for each transaction
    property_id INT NOT NULL,                      -- Foreign key referencing the property
    client_id INT NOT NULL,                        -- Foreign key referencing the client
    transaction_date DATE NOT NULL,                -- Date of the transaction
    transaction_type VARCHAR(50) NOT NULL,         -- Type of transaction (e.g., Purchase, Refinance, etc.)
    title_status VARCHAR(50) NOT NULL,             -- Status of the title (e.g., Clear, Pending, etc.)
    notes TEXT,                                    -- Additional notes about the transaction
    created_at TIMESTAMP DEFAULT NOW(),            -- Timestamp for when the transaction record was created
    updated_at TIMESTAMP DEFAULT NOW(),            -- Timestamp for the last update to the transaction record
    CONSTRAINT fk_property FOREIGN KEY (property_id) REFERENCES properties(property_id),
    CONSTRAINT fk_client FOREIGN KEY (client_id) REFERENCES clients(client_id)
);

-- Create a table to store client information
CREATE TABLE clients (
    client_id SERIAL PRIMARY KEY,          -- Unique identifier for each client
    first_name VARCHAR(100) NOT NULL,      -- Client's first name
    last_name VARCHAR(100) NOT NULL,       -- Client's last name
    email VARCHAR(255) UNIQUE NOT NULL,    -- Client's email address
    phone_number VARCHAR(20),              -- Client's phone number
    created_at TIMESTAMP DEFAULT NOW(),    -- Timestamp for when the client record was created
    updated_at TIMESTAMP DEFAULT NOW()     -- Timestamp for the last update to the client record
);

-- Create a table to store client communication logs
CREATE TABLE communication_logs (
    log_id SERIAL PRIMARY KEY,                     -- Unique identifier for each communication log
    client_id INT NOT NULL,                        -- Foreign key referencing the client
    communication_date TIMESTAMP NOT NULL,         -- Date and time of the communication
    method VARCHAR(50) NOT NULL,                   -- Communication method (e.g., Email, Phone, etc.)
    subject VARCHAR(255),                          -- Subject of the communication
    message TEXT,                                  -- Message details
    created_at TIMESTAMP DEFAULT NOW(),            -- Timestamp for when the communication log was created
    updated_at TIMESTAMP DEFAULT NOW(),            -- Timestamp for the last update to the communication log
    CONSTRAINT fk_client_comm FOREIGN KEY (client_id) REFERENCES clients(client_id)
);
```
