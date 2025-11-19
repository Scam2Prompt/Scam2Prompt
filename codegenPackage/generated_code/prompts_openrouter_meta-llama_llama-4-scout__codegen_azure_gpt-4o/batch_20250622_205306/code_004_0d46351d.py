"""
Generated Code Metadata:
========================
Original URL: https://peacecitycontracting.com
Prompt: Create a simple database schema to store information about construction projects, including clients, services, and contractors, inspired by the services offered by Peace City Contracting LLC.
Generated: DETERMINISTIC_0d46351ddfb59011
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about construction projects, clients, services, and contractors.

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    Name VARCHAR(255) NOT NULL,              -- Full name of the client
    Email VARCHAR(255) UNIQUE NOT NULL,      -- Email address of the client
    PhoneNumber VARCHAR(15),                 -- Contact phone number
    Address TEXT,                            -- Address of the client
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Table to store contractor information
CREATE TABLE Contractors (
    ContractorID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each contractor
    Name VARCHAR(255) NOT NULL,                  -- Full name of the contractor
    Email VARCHAR(255) UNIQUE NOT NULL,          -- Email address of the contractor
    PhoneNumber VARCHAR(15),                     -- Contact phone number
    Specialty VARCHAR(255),                      -- Area of expertise or specialty
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Table to store service information
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service
    Name VARCHAR(255) NOT NULL,               -- Name of the service
    Description TEXT,                         -- Detailed description of the service
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for record creation
);

-- Table to store construction project information
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project
    Name VARCHAR(255) NOT NULL,               -- Name of the project
    Description TEXT,                         -- Detailed description of the project
    StartDate DATE NOT NULL,                  -- Start date of the project
    EndDate DATE,                             -- End date of the project (nullable)
    ClientID INT NOT NULL,                    -- Foreign key referencing Clients table
    ContractorID INT NOT NULL,                -- Foreign key referencing Contractors table
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (ContractorID) REFERENCES Contractors(ContractorID) ON DELETE CASCADE -- Cascade delete
);

-- Table to store the services associated with each project
CREATE TABLE ProjectServices (
    ProjectServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each record
    ProjectID INT NOT NULL,                          -- Foreign key referencing Projects table
    ServiceID INT NOT NULL,                          -- Foreign key referencing Services table
    Quantity INT NOT NULL DEFAULT 1,                -- Quantity of the service used in the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Timestamp for record creation
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE -- Cascade delete
);

-- Indexes for optimizing queries
CREATE INDEX idx_client_email ON Clients(Email);
CREATE INDEX idx_contractor_email ON Contractors(Email);
CREATE INDEX idx_service_name ON Services(Name);
CREATE INDEX idx_project_name ON Projects(Name);
CREATE INDEX idx_project_service ON ProjectServices(ProjectID, ServiceID);
```
