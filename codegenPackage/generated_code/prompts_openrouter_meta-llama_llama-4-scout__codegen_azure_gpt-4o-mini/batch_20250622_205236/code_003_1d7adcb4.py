"""
Generated Code Metadata:
========================
Original URL: https://alshehhi.net
Prompt: Design a database schema for a web application that manages client projects and services, like the ones offered by Alshehhi.Net.
Generated: DETERMINISTIC_1d7adcb48c1546cd
Batch ID: 20250622_205236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing client projects and services

-- Create a table to store client information
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each client
    Name VARCHAR(255) NOT NULL,               -- Name of the client
    Email VARCHAR(255) UNIQUE NOT NULL,       -- Email address of the client
    Phone VARCHAR(20),                         -- Phone number of the client
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the client was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of the last update
);

-- Create a table to store project information
CREATE TABLE Projects (
    ProjectID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each project
    ClientID INT NOT NULL,                     -- Foreign key referencing Clients
    ProjectName VARCHAR(255) NOT NULL,        -- Name of the project
    Description TEXT,                          -- Description of the project
    StartDate DATE,                           -- Start date of the project
    EndDate DATE,                             -- End date of the project
    Status ENUM('Pending', 'In Progress', 'Completed', 'On Hold') DEFAULT 'Pending',  -- Current status of the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the project was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of the last update
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Create a table to store services offered
CREATE TABLE Services (
    ServiceID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each service
    ServiceName VARCHAR(255) NOT NULL,        -- Name of the service
    Description TEXT,                          -- Description of the service
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the service was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of the last update
);

-- Create a table to link projects with services
CREATE TABLE ProjectServices (
    ProjectServiceID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each project-service link
    ProjectID INT NOT NULL,                           -- Foreign key referencing Projects
    ServiceID INT NOT NULL,                           -- Foreign key referencing Services
    Quantity INT DEFAULT 1,                          -- Quantity of the service for the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Timestamp of when the link was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of the last update
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE   -- Ensure referential integrity
);

-- Create a table to store invoices related to projects
CREATE TABLE Invoices (
    InvoiceID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each invoice
    ProjectID INT NOT NULL,                    -- Foreign key referencing Projects
    Amount DECIMAL(10, 2) NOT NULL,           -- Total amount of the invoice
    InvoiceDate DATE NOT NULL,                 -- Date of the invoice
    DueDate DATE NOT NULL,                     -- Due date for the invoice
    Status ENUM('Paid', 'Unpaid', 'Overdue') DEFAULT 'Unpaid',  -- Current status of the invoice
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the invoice was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of the last update
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE  -- Ensure referential integrity
);
```
