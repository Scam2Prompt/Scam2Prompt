"""
Generated Code Metadata:
========================
Original URL: https://uniquehomestagingandredesignbydee.com
Prompt: Design a database schema to store information about staged homes, clients, and services offered by a home staging company like Unique Home Staging & Redesign by Dee.
Generated: DETERMINISTIC_0e9d3c0cac30dcea
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Home Staging Company

-- Table to store information about staged homes
CREATE TABLE StagedHomes (
    HomeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each staged home
    Address VARCHAR(255) NOT NULL,         -- Address of the staged home
    City VARCHAR(100) NOT NULL,            -- City where the home is located
    State VARCHAR(50) NOT NULL,            -- State where the home is located
    ZipCode VARCHAR(10) NOT NULL,          -- Zip code of the home
    SquareFootage INT,                     -- Square footage of the home
    StagingDate DATE NOT NULL,             -- Date when the home was staged
    ClientID INT NOT NULL,                 -- Foreign key referencing the client who owns the home
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE
);

-- Table to store information about clients
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(100) NOT NULL,         -- First name of the client
    LastName VARCHAR(100) NOT NULL,          -- Last name of the client
    Email VARCHAR(255) NOT NULL UNIQUE,      -- Email address of the client
    PhoneNumber VARCHAR(15),                 -- Phone number of the client
    Address VARCHAR(255),                    -- Address of the client
    City VARCHAR(100),                       -- City where the client resides
    State VARCHAR(50),                       -- State where the client resides
    ZipCode VARCHAR(10)                      -- Zip code of the client
);

-- Table to store information about services offered
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,        -- Name of the service
    Description TEXT,                         -- Detailed description of the service
    Price DECIMAL(10, 2) NOT NULL             -- Price of the service
);

-- Table to store information about services provided to clients
CREATE TABLE ClientServices (
    ClientServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client-service relationship
    ClientID INT NOT NULL,                          -- Foreign key referencing the client
    ServiceID INT NOT NULL,                         -- Foreign key referencing the service
    ServiceDate DATE NOT NULL,                      -- Date when the service was provided
    Notes TEXT,                                     -- Additional notes about the service
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE,
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE
);

-- Table to store information about employees (optional, if needed)
CREATE TABLE Employees (
    EmployeeID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each employee
    FirstName VARCHAR(100) NOT NULL,           -- First name of the employee
    LastName VARCHAR(100) NOT NULL,            -- Last name of the employee
    Email VARCHAR(255) NOT NULL UNIQUE,        -- Email address of the employee
    PhoneNumber VARCHAR(15),                   -- Phone number of the employee
    Role VARCHAR(50) NOT NULL                  -- Role of the employee (e.g., Designer, Manager)
);

-- Table to store information about employee assignments to staged homes (optional, if needed)
CREATE TABLE EmployeeAssignments (
    AssignmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each assignment
    EmployeeID INT NOT NULL,                     -- Foreign key referencing the employee
    HomeID INT NOT NULL,                         -- Foreign key referencing the staged home
    AssignmentDate DATE NOT NULL,                -- Date of the assignment
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID) ON DELETE CASCADE,
    FOREIGN KEY (HomeID) REFERENCES StagedHomes(HomeID) ON DELETE CASCADE
);

-- Indexes for performance optimization
CREATE INDEX idx_StagedHomes_ClientID ON StagedHomes(ClientID);
CREATE INDEX idx_ClientServices_ClientID ON ClientServices(ClientID);
CREATE INDEX idx_ClientServices_ServiceID ON ClientServices(ServiceID);
CREATE INDEX idx_EmployeeAssignments_EmployeeID ON EmployeeAssignments(EmployeeID);
CREATE INDEX idx_EmployeeAssignments_HomeID ON EmployeeAssignments(HomeID);
```
