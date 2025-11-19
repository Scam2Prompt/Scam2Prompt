"""
Generated Code Metadata:
========================
Original URL: https://strk.site
Prompt: "Create a SQL database schema to manage client projects, services, and costs for a Kazan-based renovation company like STRK."
Generated: DETERMINISTIC_7ba53145056b03c9
Batch ID: 20250622_205204
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL Database Schema for managing client projects, services, and costs
-- This schema is designed for a renovation company based in Kazan.

-- Create a table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FullName VARCHAR(255) NOT NULL,          -- Full name of the client
    PhoneNumber VARCHAR(15),                 -- Contact phone number
    Email VARCHAR(255),                      -- Contact email address
    Address TEXT,                            -- Address of the client
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Create a table to store project information
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project
    ClientID INT NOT NULL,                    -- Foreign key referencing Clients table
    ProjectName VARCHAR(255) NOT NULL,        -- Name of the project
    StartDate DATE NOT NULL,                  -- Start date of the project
    EndDate DATE,                             -- End date of the project (nullable for ongoing projects)
    Status ENUM('Planned', 'In Progress', 'Completed', 'Cancelled') NOT NULL, -- Status of the project
    TotalCost DECIMAL(10, 2),                 -- Total cost of the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Cascade delete if client is removed
);

-- Create a table to store services offered by the company
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service
    ServiceName VARCHAR(255) NOT NULL,        -- Name of the service
    Description TEXT,                         -- Description of the service
    UnitCost DECIMAL(10, 2) NOT NULL,         -- Cost per unit of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Create a table to store project-specific services
CREATE TABLE ProjectServices (
    ProjectServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project-service record
    ProjectID INT NOT NULL,                          -- Foreign key referencing Projects table
    ServiceID INT NOT NULL,                          -- Foreign key referencing Services table
    Quantity INT NOT NULL,                           -- Quantity of the service used in the project
    TotalCost DECIMAL(10, 2) GENERATED ALWAYS AS (Quantity * UnitCost) STORED, -- Calculated total cost
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp for record creation
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE, -- Cascade delete if project is removed
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE  -- Cascade delete if service is removed
);

-- Create a table to store payment information
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each payment
    ProjectID INT NOT NULL,                   -- Foreign key referencing Projects table
    PaymentDate DATE NOT NULL,                -- Date of the payment
    Amount DECIMAL(10, 2) NOT NULL,           -- Amount paid
    PaymentMethod ENUM('Cash', 'Card', 'Bank Transfer') NOT NULL, -- Payment method
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Cascade delete if project is removed
);

-- Indexes for optimizing queries
CREATE INDEX idx_client_fullname ON Clients(FullName);
CREATE INDEX idx_project_status ON Projects(Status);
CREATE INDEX idx_service_name ON Services(ServiceName);
CREATE INDEX idx_payment_date ON Payments(PaymentDate);

-- End of schema definition
```
