"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://laotaigroup.com
Prompt: Develop a database schema for managing real estate assets and rental services, inspired by the operations of Lao Tai Trading - Investment Group.
Generated: DETERMINISTIC_1be63a220719483b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing real estate assets and rental services
-- This schema is designed to handle properties, tenants, leases, and transactions.

-- Table to manage information about properties
CREATE TABLE Properties (
    property_id SERIAL PRIMARY KEY,               -- Unique identifier for each property
    name VARCHAR(255) NOT NULL,                  -- Name/Title of the property
    type VARCHAR(100) NOT NULL,                  -- Type of property (e.g., Residential, Commercial)
    address TEXT NOT NULL,                       -- Full address of the property
    city VARCHAR(100) NOT NULL,                  -- City where the property is located
    country VARCHAR(100) NOT NULL,               -- Country where the property is located
    price DECIMAL(15,2) NOT NULL,                -- Value or price of the property
    status VARCHAR(50) NOT NULL DEFAULT 'Available', -- Current status (e.g., Available, Rented, Maintenance)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to manage information about tenants
CREATE TABLE Tenants (
    tenant_id SERIAL PRIMARY KEY,                -- Unique identifier for each tenant
    first_name VARCHAR(100) NOT NULL,            -- Tenant's first name
    last_name VARCHAR(100) NOT NULL,             -- Tenant's last name
    email VARCHAR(255) UNIQUE NOT NULL,          -- Email address of the tenant
    phone VARCHAR(15),                           -- Phone number of the tenant
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to manage rental leases
CREATE TABLE Leases (
    lease_id SERIAL PRIMARY KEY,                 -- Unique identifier for each lease
    property_id INT NOT NULL,                    -- Foreign key referencing Properties table
    tenant_id INT NOT NULL,                      -- Foreign key referencing Tenants table
    start_date DATE NOT NULL,                    -- Start date of the lease
    end_date DATE NOT NULL,                      -- End date of the lease
    monthly_rent DECIMAL(10,2) NOT NULL,         -- Monthly rent amount
    status VARCHAR(50) NOT NULL DEFAULT 'Active', -- Status of the lease (e.g., Active, Terminated)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of last update
    CONSTRAINT fk_property FOREIGN KEY (property_id) REFERENCES Properties(property_id) ON DELETE CASCADE,
    CONSTRAINT fk_tenant FOREIGN KEY (tenant_id) REFERENCES Tenants(tenant_id) ON DELETE CASCADE
);

-- Table to manage payment transactions
CREATE TABLE Transactions (
    transaction_id SERIAL PRIMARY KEY,           -- Unique identifier for each transaction
    lease_id INT NOT NULL,                       -- Foreign key referencing Leases table
    payment_date DATE NOT NULL,                  -- Date when the payment was made
    amount DECIMAL(10,2) NOT NULL,               -- Payment amount
    payment_method VARCHAR(50) NOT NULL,         -- Payment method (e.g., Credit Card, Bank Transfer)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of record creation
    CONSTRAINT fk_lease FOREIGN KEY (lease_id) REFERENCES Leases(lease_id) ON DELETE CASCADE
);

-- Indexes for fast querying
CREATE INDEX idx_properties_status ON Properties(status); -- Index for querying properties by status
CREATE INDEX idx_leases_status ON Leases(status);         -- Index for querying leases by status
CREATE INDEX idx_transactions_payment_date ON Transactions(payment_date); -- Index for querying transactions by payment date

-- Views for reporting purposes
CREATE VIEW ActiveLeases AS
SELECT 
    l.lease_id, 
    p.name AS property_name,
    CONCAT(t.first_name, ' ', t.last_name) AS tenant_name,
    l.start_date, 
    l.end_date, 
    l.monthly_rent
FROM Leases l
JOIN Properties p ON l.property_id = p.property_id
JOIN Tenants t ON l.tenant_id = t.tenant_id
WHERE l.status = 'Active';

CREATE VIEW PaymentSummary AS
SELECT 
    lease_id, 
    SUM(amount) AS total_paid,
    COUNT(transaction_id) AS payment_count
FROM Transactions
GROUP BY lease_id;
```
