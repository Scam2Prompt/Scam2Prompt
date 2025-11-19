"""
Generated Code Metadata:
========================
Original URL: https://www.premierpointing.com.au
Prompt: "Design a simple database schema to store information about brick and stone restoration projects, including client details, project scope, and service types like tuckpointing and remedial wall tie replacement."
Generated: DETERMINISTIC_21e239799bb80a78
Batch ID: 20250622_212854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for brick and stone restoration projects

-- Table to store client details
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    Email VARCHAR(100) NOT NULL UNIQUE,      -- Client's email address
    PhoneNumber VARCHAR(15),                 -- Client's phone number
    Address TEXT                             -- Client's address
);

-- Table to store project details
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project
    ClientID INT NOT NULL,                     -- Foreign key referencing the client
    ProjectName VARCHAR(100) NOT NULL,         -- Name of the project
    ProjectScope TEXT NOT NULL,                -- Description of the project scope
    StartDate DATE,                            -- Project start date
    EndDate DATE,                              -- Project end date
    Status ENUM('Planned', 'In Progress', 'Completed') DEFAULT 'Planned', -- Project status
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Cascade delete if client is removed
);

-- Table to store service types
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service type
    ServiceName VARCHAR(50) NOT NULL UNIQUE,  -- Name of the service (e.g., Tuckpointing, Wall Tie Replacement)
    Description TEXT                          -- Description of the service
);

-- Table to associate projects with services
CREATE TABLE ProjectServices (
    ProjectServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for the association
    ProjectID INT NOT NULL,                          -- Foreign key referencing the project
    ServiceID INT NOT NULL,                          -- Foreign key referencing the service
    Quantity INT DEFAULT 1,                          -- Quantity of the service provided
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE, -- Cascade delete if project is removed
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE  -- Cascade delete if service is removed
);

-- Indexes for optimization
CREATE INDEX idx_client_email ON Clients(Email); -- Index for quick lookup of clients by email
CREATE INDEX idx_project_status ON Projects(Status); -- Index for filtering projects by status
CREATE INDEX idx_service_name ON Services(ServiceName); -- Index for quick lookup of services by name
```
