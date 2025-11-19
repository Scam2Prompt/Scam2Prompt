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
-- Database Schema for Fuel Injector Cleaning Services

-- Table to store client details
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,      -- Client's email address
    PhoneNumber VARCHAR(15),                 -- Client's phone number
    Address TEXT                             -- Client's address
);

-- Table to store vehicle types
CREATE TABLE VehicleTypes (
    VehicleTypeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each vehicle type
    Make VARCHAR(50) NOT NULL,                    -- Vehicle manufacturer (e.g., Toyota, Ford)
    Model VARCHAR(50) NOT NULL,                   -- Vehicle model (e.g., Corolla, Mustang)
    Year INT NOT NULL                             -- Year of manufacture
);

-- Table to store service history
CREATE TABLE ServiceHistory (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service record
    ClientID INT NOT NULL,                    -- Foreign key referencing Clients table
    VehicleTypeID INT NOT NULL,               -- Foreign key referencing VehicleTypes table
    ServiceDate DATE NOT NULL,                -- Date of the service
    ServiceDetails TEXT NOT NULL,             -- Description of the service performed
    Cost DECIMAL(10, 2) NOT NULL,             -- Cost of the service
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE,
    FOREIGN KEY (VehicleTypeID) REFERENCES VehicleTypes(VehicleTypeID) ON DELETE CASCADE
);

-- Indexes for faster lookups
CREATE INDEX idx_client_email ON Clients(Email);
CREATE INDEX idx_vehicle_make_model ON VehicleTypes(Make, Model);
CREATE INDEX idx_service_date ON ServiceHistory(ServiceDate);

-- Suggested programming language for implementation: Python
-- Python is suitable for this use case due to its rich ecosystem of libraries for database interaction (e.g., SQLAlchemy, psycopg2).
```
