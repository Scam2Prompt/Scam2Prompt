"""
Generated Code Metadata:
========================
Original URL: https://blastfair.com
Prompt: "Design a database schema for an architectural firm that offers various services like consulting, project management, and architectural solutions."
Generated: DETERMINISTIC_c821bd8b45ca73de
Batch ID: 20250622_210122
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an architectural firm

-- Create a table to store information about services offered by the firm
CREATE TABLE Services (
    ServiceID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,         -- Name of the service
    Description TEXT,                           -- Description of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the service was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Create a table to store information about clients
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each client
    ClientName VARCHAR(100) NOT NULL,           -- Name of the client
    ContactEmail VARCHAR(100) UNIQUE NOT NULL,  -- Email address of the client
    PhoneNumber VARCHAR(15),                     -- Phone number of the client
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the client was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Create a table to store projects undertaken by the firm
CREATE TABLE Projects (
    ProjectID INT PRIMARY KEY AUTO_INCREMENT,    -- Unique identifier for each project
    ClientID INT NOT NULL,                       -- Foreign key referencing Clients
    ServiceID INT NOT NULL,                      -- Foreign key referencing Services
    ProjectName VARCHAR(100) NOT NULL,          -- Name of the project
    StartDate DATE NOT NULL,                     -- Start date of the project
    EndDate DATE,                                -- End date of the project (nullable)
    Status ENUM('Pending', 'In Progress', 'Completed', 'On Hold') NOT NULL DEFAULT 'Pending',  -- Current status of the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the project was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of last update
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Create a table to store project team members
CREATE TABLE TeamMembers (
    TeamMemberID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each team member
    ProjectID INT NOT NULL,                       -- Foreign key referencing Projects
    MemberName VARCHAR(100) NOT NULL,            -- Name of the team member
    Role VARCHAR(50) NOT NULL,                    -- Role of the team member in the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the team member was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of last update
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Create a table to store invoices for projects
CREATE TABLE Invoices (
    InvoiceID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each invoice
    ProjectID INT NOT NULL,                       -- Foreign key referencing Projects
    Amount DECIMAL(10, 2) NOT NULL,              -- Amount of the invoice
    InvoiceDate DATE NOT NULL,                    -- Date of the invoice
    DueDate DATE NOT NULL,                        -- Due date for payment
    Status ENUM('Paid', 'Unpaid', 'Overdue') NOT NULL DEFAULT 'Unpaid',  -- Payment status of the invoice
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the invoice was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of last update
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE  -- Ensure referential integrity
);
```
