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
-- Database Schema for PG Properties, Tenants, and Rent Payments

-- Table to store information about PG properties
CREATE TABLE PGProperties (
    PropertyID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each property
    Name VARCHAR(255) NOT NULL,                -- Name of the PG property
    Address TEXT NOT NULL,                     -- Address of the PG property
    City VARCHAR(100) NOT NULL,                -- City where the PG is located
    State VARCHAR(100) NOT NULL,               -- State where the PG is located
    ZipCode VARCHAR(10) NOT NULL,              -- Zip code of the PG location
    TotalRooms INT NOT NULL,                   -- Total number of rooms in the PG
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the property was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store information about tenants
CREATE TABLE Tenants (
    TenantID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each tenant
    FirstName VARCHAR(100) NOT NULL,           -- First name of the tenant
    LastName VARCHAR(100) NOT NULL,            -- Last name of the tenant
    Email VARCHAR(255) UNIQUE NOT NULL,        -- Email address of the tenant
    PhoneNumber VARCHAR(15) NOT NULL,          -- Contact number of the tenant
    PropertyID INT NOT NULL,                   -- Foreign key linking to PGProperties
    RoomNumber INT NOT NULL,                   -- Room number assigned to the tenant
    MoveInDate DATE NOT NULL,                  -- Date when the tenant moved in
    MoveOutDate DATE DEFAULT NULL,             -- Date when the tenant moved out (if applicable)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the tenant was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (PropertyID) REFERENCES PGProperties(PropertyID) ON DELETE CASCADE -- Cascade delete if property is removed
);

-- Table to store information about rent payments
CREATE TABLE RentPayments (
    PaymentID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each payment
    TenantID INT NOT NULL,                     -- Foreign key linking to Tenants
    PropertyID INT NOT NULL,                   -- Foreign key linking to PGProperties
    PaymentDate DATE NOT NULL,                 -- Date of the payment
    Amount DECIMAL(10, 2) NOT NULL,            -- Amount paid
    PaymentMethod VARCHAR(50) NOT NULL,        -- Method of payment (e.g., Cash, Card, Online)
    PaymentStatus ENUM('Pending', 'Completed', 'Failed') NOT NULL DEFAULT 'Pending', -- Status of the payment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the payment record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (TenantID) REFERENCES Tenants(TenantID) ON DELETE CASCADE, -- Cascade delete if tenant is removed
    FOREIGN KEY (PropertyID) REFERENCES PGProperties(PropertyID) ON DELETE CASCADE -- Cascade delete if property is removed
);

-- Indexes for optimizing queries
CREATE INDEX idx_pg_city ON PGProperties (City);
CREATE INDEX idx_tenant_email ON Tenants (Email);
CREATE INDEX idx_payment_date ON RentPayments (PaymentDate);
```
