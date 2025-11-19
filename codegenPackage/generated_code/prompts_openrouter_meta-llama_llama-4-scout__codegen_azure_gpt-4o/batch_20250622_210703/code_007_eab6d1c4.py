"""
Generated Code Metadata:
========================
Original URL: https://citygardenmexico.com.mx
Prompt: "Design a database schema to store information about gardening projects, clients, and services offered by City Garden Mexico."
Generated: DETERMINISTIC_eab6d1c4d29078e7
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for City Garden Mexico

-- Table to store information about clients
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,      -- Client's email address
    PhoneNumber VARCHAR(15),                 -- Client's phone number
    Address TEXT,                            -- Client's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the client was added
);

-- Table to store information about gardening projects
CREATE TABLE GardeningProjects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project
    ClientID INT NOT NULL,                    -- Foreign key referencing the client
    ProjectName VARCHAR(100) NOT NULL,        -- Name of the gardening project
    StartDate DATE NOT NULL,                  -- Start date of the project
    EndDate DATE,                             -- End date of the project (nullable for ongoing projects)
    Budget DECIMAL(10, 2),                    -- Budget allocated for the project
    Status ENUM('Planned', 'In Progress', 'Completed') DEFAULT 'Planned', -- Status of the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the project was added
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Cascade delete if client is removed
);

-- Table to store information about services offered
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,        -- Name of the service
    Description TEXT,                         -- Description of the service
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the service was added
);

-- Table to store the relationship between projects and services
CREATE TABLE ProjectServices (
    ProjectServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each record
    ProjectID INT NOT NULL,                          -- Foreign key referencing the gardening project
    ServiceID INT NOT NULL,                          -- Foreign key referencing the service
    Quantity INT DEFAULT 1,                          -- Quantity of the service used in the project
    TotalCost DECIMAL(10, 2) GENERATED ALWAYS AS (Quantity * (SELECT Price FROM Services WHERE Services.ServiceID = ServiceID)) STORED, -- Total cost for the service in the project
    FOREIGN KEY (ProjectID) REFERENCES GardeningProjects(ProjectID) ON DELETE CASCADE, -- Cascade delete if project is removed
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE -- Cascade delete if service is removed
);

-- Indexes for optimizing queries
CREATE INDEX idx_client_email ON Clients(Email); -- Index for quick lookup by email
CREATE INDEX idx_project_status ON GardeningProjects(Status); -- Index for filtering projects by status
CREATE INDEX idx_service_name ON Services(ServiceName); -- Index for quick lookup by service name
```
