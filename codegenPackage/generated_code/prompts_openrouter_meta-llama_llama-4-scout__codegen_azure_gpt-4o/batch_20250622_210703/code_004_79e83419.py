"""
Generated Code Metadata:
========================
Original URL: https://www.adour-pompes-funebres.fr
Prompt: "Design a simple database schema to store information about funeral services, including client details, service types (e.g., transport, ceremony), and payment methods."
Generated: DETERMINISTIC_79e834198f23b179
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about funeral services

-- Table to store client details
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    PhoneNumber VARCHAR(15),                 -- Client's phone number
    Email VARCHAR(100),                      -- Client's email address
    Address TEXT,                            -- Client's physical address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Table to store service types
CREATE TABLE ServiceTypes (
    ServiceTypeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service type
    ServiceName VARCHAR(100) NOT NULL,            -- Name of the service (e.g., transport, ceremony)
    Description TEXT,                             -- Description of the service
    Price DECIMAL(10, 2) NOT NULL,                -- Price of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Table to store payment methods
CREATE TABLE PaymentMethods (
    PaymentMethodID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each payment method
    MethodName VARCHAR(50) NOT NULL,                -- Name of the payment method (e.g., credit card, cash)
    Description TEXT,                               -- Description of the payment method
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP   -- Timestamp for record creation
);

-- Table to store funeral service bookings
CREATE TABLE FuneralServices (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each funeral service
    ClientID INT NOT NULL,                          -- Foreign key referencing Clients table
    ServiceTypeID INT NOT NULL,                     -- Foreign key referencing ServiceTypes table
    PaymentMethodID INT NOT NULL,                   -- Foreign key referencing PaymentMethods table
    ServiceDate DATE NOT NULL,                      -- Date of the funeral service
    Notes TEXT,                                     -- Additional notes about the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for record creation
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE,
    FOREIGN KEY (ServiceTypeID) REFERENCES ServiceTypes(ServiceTypeID) ON DELETE CASCADE,
    FOREIGN KEY (PaymentMethodID) REFERENCES PaymentMethods(PaymentMethodID) ON DELETE CASCADE
);

-- Indexes for optimizing queries
CREATE INDEX idx_client_id ON FuneralServices(ClientID);
CREATE INDEX idx_service_type_id ON FuneralServices(ServiceTypeID);
CREATE INDEX idx_payment_method_id ON FuneralServices(PaymentMethodID);
```
