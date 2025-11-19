"""
Generated Code Metadata:
========================
Original URL: https://fuelinjectorservices.com.au
Prompt: Design a database schema to store information about fuel injector cleaning services, including client details, vehicle types, and service history, and suggest a suitable programming language for implementation.
Generated: DETERMINISTIC_04646993978d9571
Batch ID: 20250622_205301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for fuel injector cleaning services

-- Table to store client details
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,           -- Client's first name
    LastName VARCHAR(50) NOT NULL,            -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Client's email address
    Phone VARCHAR(15),                         -- Client's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the client was added
);

-- Table to store vehicle types
CREATE TABLE VehicleTypes (
    VehicleTypeID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each vehicle type
    Make VARCHAR(50) NOT NULL,                    -- Vehicle make (e.g., Toyota, Ford)
    Model VARCHAR(50) NOT NULL,                   -- Vehicle model (e.g., Camry, F-150)
    Year INT CHECK (Year > 1885 AND Year <= YEAR(CURRENT_DATE)), -- Vehicle year
    ClientID INT,                                  -- Foreign key to link to Clients
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store service history
CREATE TABLE ServiceHistory (
    ServiceID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each service record
    ClientID INT NOT NULL,                         -- Foreign key to link to Clients
    VehicleTypeID INT NOT NULL,                    -- Foreign key to link to VehicleTypes
    ServiceDate DATE NOT NULL,                     -- Date of the service
    ServiceDescription TEXT NOT NULL,              -- Description of the service performed
    Cost DECIMAL(10, 2) NOT NULL,                 -- Cost of the service
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (VehicleTypeID) REFERENCES VehicleTypes(VehicleTypeID) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_client_email ON Clients(Email);
CREATE INDEX idx_vehicle_make_model ON VehicleTypes(Make, Model);
CREATE INDEX idx_service_date ON ServiceHistory(ServiceDate);
```

### Suggested Programming Language for Implementation
- **Python**: A versatile language with strong support for database interaction through libraries like SQLAlchemy or Django ORM, making it suitable for building applications that manage this database schema.
