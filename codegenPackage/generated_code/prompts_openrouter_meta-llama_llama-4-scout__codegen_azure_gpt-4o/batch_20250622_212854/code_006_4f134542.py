"""
Generated Code Metadata:
========================
Original URL: https://mmgroupnepal.com
Prompt: Create a simple database schema to store information about MM Group's clients, products, and services.
Generated: DETERMINISTIC_4f134542e52bd5c6
Batch ID: 20250622_212854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for MM Group's clients, products, and services

-- Create a table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,      -- Client's email address (must be unique)
    PhoneNumber VARCHAR(15),                 -- Client's phone number
    Address TEXT,                            -- Client's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the client record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table to store product information
CREATE TABLE Products (
    ProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    Name VARCHAR(100) NOT NULL,               -- Name of the product
    Description TEXT,                         -- Description of the product
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the product
    Stock INT NOT NULL,                       -- Quantity of the product in stock
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the product record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table to store service information
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service
    Name VARCHAR(100) NOT NULL,               -- Name of the service
    Description TEXT,                         -- Description of the service
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the service
    Duration INT NOT NULL,                    -- Duration of the service in minutes
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the service record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create a table to store client-product relationships (e.g., purchases)
CREATE TABLE ClientProducts (
    ClientProductID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each record
    ClientID INT NOT NULL,                          -- Foreign key referencing Clients table
    ProductID INT NOT NULL,                         -- Foreign key referencing Products table
    Quantity INT NOT NULL,                          -- Quantity of the product purchased
    PurchaseDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of the purchase
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Cascade delete if client is removed
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE -- Cascade delete if product is removed
);

-- Create a table to store client-service relationships (e.g., bookings)
CREATE TABLE ClientServices (
    ClientServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each record
    ClientID INT NOT NULL,                          -- Foreign key referencing Clients table
    ServiceID INT NOT NULL,                         -- Foreign key referencing Services table
    AppointmentDate TIMESTAMP NOT NULL,             -- Date and time of the service appointment
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Cascade delete if client is removed
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE -- Cascade delete if service is removed
);

-- Ensure the database is optimized for production use
-- Add indexes for faster lookups
CREATE INDEX idx_clients_email ON Clients(Email);
CREATE INDEX idx_products_name ON Products(Name);
CREATE INDEX idx_services_name ON Services(Name);
CREATE INDEX idx_clientproducts_clientid ON ClientProducts(ClientID);
CREATE INDEX idx_clientservices_clientid ON ClientServices(ClientID);
```
