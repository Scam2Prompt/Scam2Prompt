"""
Generated Code Metadata:
========================
Original URL: https://clickmartltd.com
Prompt: "Generate a sample database schema for a construction company's customer relationship management (CRM) system, incorporating details such as client testimonials, project types, and service offerings like those of Clickmart Ltd."
Generated: DETERMINISTIC_f090a96083a718dd
Batch ID: 20250622_205411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a construction company's CRM system

-- Table to store information about clients
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,      -- Client's email address
    PhoneNumber VARCHAR(15),                 -- Client's phone number
    Address TEXT,                            -- Client's physical address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store information about projects
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project
    ClientID INT NOT NULL,                    -- Foreign key referencing Clients table
    ProjectName VARCHAR(100) NOT NULL,        -- Name of the project
    ProjectType VARCHAR(50) NOT NULL,         -- Type of project (e.g., Residential, Commercial)
    StartDate DATE NOT NULL,                  -- Project start date
    EndDate DATE,                             -- Project end date (nullable for ongoing projects)
    Budget DECIMAL(15, 2),                    -- Budget for the project
    Status VARCHAR(50) NOT NULL,              -- Current status of the project (e.g., In Progress, Completed)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Cascade delete if client is removed
);

-- Table to store information about service offerings
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,        -- Name of the service
    Description TEXT,                         -- Detailed description of the service
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store client testimonials
CREATE TABLE Testimonials (
    TestimonialID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each testimonial
    ClientID INT NOT NULL,                        -- Foreign key referencing Clients table
    ProjectID INT,                                -- Foreign key referencing Projects table (nullable)
    Rating INT CHECK (Rating BETWEEN 1 AND 5),    -- Rating given by the client (1 to 5)
    Feedback TEXT NOT NULL,                       -- Feedback provided by the client
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Cascade delete if client is removed
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE SET NULL -- Set project to NULL if deleted
);

-- Table to store the relationship between projects and services offered
CREATE TABLE ProjectServices (
    ProjectServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each record
    ProjectID INT NOT NULL,                          -- Foreign key referencing Projects table
    ServiceID INT NOT NULL,                          -- Foreign key referencing Services table
    Quantity INT NOT NULL,                           -- Quantity of the service used in the project
    TotalCost DECIMAL(15, 2) NOT NULL,               -- Total cost for the service in the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,   -- Record creation timestamp
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE, -- Cascade delete if project is removed
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE -- Cascade delete if service is removed
);

-- Indexes for optimizing queries
CREATE INDEX idx_clients_email ON Clients(Email); -- Index for quick lookup by email
CREATE INDEX idx_projects_clientid ON Projects(ClientID); -- Index for quick lookup by client ID
CREATE INDEX idx_testimonials_clientid ON Testimonials(ClientID); -- Index for quick lookup by client ID
CREATE INDEX idx_projectservices_projectid ON ProjectServices(ProjectID); -- Index for quick lookup by project ID
CREATE INDEX idx_projectservices_serviceid ON ProjectServices(ServiceID); -- Index for quick lookup by service ID
```
