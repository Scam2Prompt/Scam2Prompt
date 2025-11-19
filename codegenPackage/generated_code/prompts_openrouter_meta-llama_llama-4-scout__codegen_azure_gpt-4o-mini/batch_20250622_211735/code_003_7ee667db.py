"""
Generated Code Metadata:
========================
Original URL: https://momspg.com
Prompt: "Design a database schema for storing information about PG properties, tenants, and rent payments, inspired by Moms PG's features."
Generated: DETERMINISTIC_7ee667db818cbe9d
Batch ID: 20250622_211735
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about PG properties, tenants, and rent payments

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS RentPayments;
DROP TABLE IF EXISTS Tenants;
DROP TABLE IF EXISTS Properties;

-- Table to store information about PG properties
CREATE TABLE Properties (
    PropertyID SERIAL PRIMARY KEY, -- Unique identifier for each property
    PropertyName VARCHAR(255) NOT NULL, -- Name of the property
    Address VARCHAR(255) NOT NULL, -- Address of the property
    City VARCHAR(100) NOT NULL, -- City where the property is located
    State VARCHAR(100) NOT NULL, -- State where the property is located
    ZipCode VARCHAR(10) NOT NULL, -- Zip code of the property location
    OwnerName VARCHAR(255) NOT NULL, -- Name of the property owner
    ContactNumber VARCHAR(15), -- Contact number of the property owner
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the property was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Table to store information about tenants
CREATE TABLE Tenants (
    TenantID SERIAL PRIMARY KEY, -- Unique identifier for each tenant
    FullName VARCHAR(255) NOT NULL, -- Full name of the tenant
    Email VARCHAR(255) UNIQUE NOT NULL, -- Email address of the tenant
    PhoneNumber VARCHAR(15), -- Phone number of the tenant
    PropertyID INT NOT NULL, -- Foreign key referencing the property
    MoveInDate DATE NOT NULL, -- Date when the tenant moved in
    MoveOutDate DATE, -- Date when the tenant moved out (nullable)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the tenant was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of the last update
    FOREIGN KEY (PropertyID) REFERENCES Properties(PropertyID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store information about rent payments
CREATE TABLE RentPayments (
    PaymentID SERIAL PRIMARY KEY, -- Unique identifier for each payment
    TenantID INT NOT NULL, -- Foreign key referencing the tenant
    PaymentDate DATE NOT NULL, -- Date when the payment was made
    Amount DECIMAL(10, 2) NOT NULL, -- Amount paid
    PaymentMethod VARCHAR(50), -- Method of payment (e.g., cash, bank transfer)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the payment was recorded
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of the last update
    FOREIGN KEY (TenantID) REFERENCES Tenants(TenantID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for faster querying
CREATE INDEX idx_property_name ON Properties(PropertyName);
CREATE INDEX idx_tenant_email ON Tenants(Email);
CREATE INDEX idx_payment_date ON RentPayments(PaymentDate);
```
