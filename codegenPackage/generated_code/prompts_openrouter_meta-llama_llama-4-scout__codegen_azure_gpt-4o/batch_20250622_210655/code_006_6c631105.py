"""
Generated Code Metadata:
========================
Original URL: https://byamed.net
Prompt: Design a database schema for a high-end web design and development agency, incorporating data models for client projects, services, and portfolios, similar to the ones managed by Amed Abraham.
Generated: DETERMINISTIC_6c631105f2c23e4d
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a high-end web design and development agency

-- Table to store information about clients
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    Name VARCHAR(255) NOT NULL,              -- Full name of the client
    Email VARCHAR(255) NOT NULL UNIQUE,      -- Email address of the client
    PhoneNumber VARCHAR(20),                 -- Contact phone number
    CompanyName VARCHAR(255),                -- Name of the client's company
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the client was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store information about services offered by the agency
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service
    Name VARCHAR(255) NOT NULL,               -- Name of the service
    Description TEXT,                         -- Detailed description of the service
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the service was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store information about client projects
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project
    ClientID INT NOT NULL,                    -- Foreign key referencing Clients table
    Name VARCHAR(255) NOT NULL,               -- Name of the project
    Description TEXT,                         -- Detailed description of the project
    StartDate DATE NOT NULL,                  -- Start date of the project
    EndDate DATE,                             -- End date of the project (nullable for ongoing projects)
    Status ENUM('Pending', 'In Progress', 'Completed') NOT NULL, -- Current status of the project
    Budget DECIMAL(10, 2),                    -- Budget allocated for the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the project was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store information about the agency's portfolio
CREATE TABLE Portfolio (
    PortfolioID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each portfolio entry
    ProjectID INT NOT NULL,                     -- Foreign key referencing Projects table
    Title VARCHAR(255) NOT NULL,                -- Title of the portfolio entry
    Description TEXT,                           -- Detailed description of the portfolio entry
    ImageURL VARCHAR(2083),                     -- URL to an image showcasing the portfolio entry
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the portfolio entry was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store many-to-many relationships between projects and services
CREATE TABLE ProjectServices (
    ProjectID INT NOT NULL,                    -- Foreign key referencing Projects table
    ServiceID INT NOT NULL,                    -- Foreign key referencing Services table
    PRIMARY KEY (ProjectID, ServiceID),        -- Composite primary key
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Indexes for optimizing queries
CREATE INDEX idx_client_email ON Clients(Email); -- Index for quick lookup by email
CREATE INDEX idx_project_status ON Projects(Status); -- Index for filtering projects by status
CREATE INDEX idx_service_name ON Services(Name); -- Index for searching services by name
```
