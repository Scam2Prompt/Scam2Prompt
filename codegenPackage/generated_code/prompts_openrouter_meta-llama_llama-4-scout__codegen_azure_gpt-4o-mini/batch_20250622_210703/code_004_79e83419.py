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

-- Create a table to store client details
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,           -- Client's first name
    LastName VARCHAR(50) NOT NULL,            -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,       -- Client's email address (must be unique)
    PhoneNumber VARCHAR(15),                   -- Client's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the client was added
);

-- Create a table to store service types
CREATE TABLE ServiceTypes (
    ServiceTypeID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each service type
    ServiceName VARCHAR(100) NOT NULL,            -- Name of the service (e.g., transport, ceremony)
    Description TEXT,                              -- Description of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP  -- Timestamp for when the service type was added
);

-- Create a table to store payment methods
CREATE TABLE PaymentMethods (
    PaymentMethodID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each payment method
    MethodName VARCHAR(50) NOT NULL,                -- Name of the payment method (e.g., credit card, cash)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP     -- Timestamp for when the payment method was added
);

-- Create a table to store funeral services
CREATE TABLE FuneralServices (
    ServiceID INT PRIMARY KEY AUTO_INCREMENT,        -- Unique identifier for each service
    ClientID INT NOT NULL,                           -- Foreign key referencing Clients
    ServiceTypeID INT NOT NULL,                      -- Foreign key referencing ServiceTypes
    PaymentMethodID INT NOT NULL,                    -- Foreign key referencing PaymentMethods
    ServiceDate DATE NOT NULL,                       -- Date of the service
    TotalAmount DECIMAL(10, 2) NOT NULL,            -- Total amount for the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp for when the service was added
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (ServiceTypeID) REFERENCES ServiceTypes(ServiceTypeID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (PaymentMethodID) REFERENCES PaymentMethods(PaymentMethodID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes can be added for performance optimization if necessary
CREATE INDEX idx_client_email ON Clients(Email);
CREATE INDEX idx_service_date ON FuneralServices(ServiceDate);
```
