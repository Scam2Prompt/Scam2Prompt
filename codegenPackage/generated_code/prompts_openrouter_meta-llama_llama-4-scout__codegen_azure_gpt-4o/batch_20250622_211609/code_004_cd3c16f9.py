"""
Generated Code Metadata:
========================
Original URL: https://fifthavenue.com.sg
Prompt: "Design a database schema to store client information, projects, and testimonials for an interior design firm like Fifth Avenue Interior."
Generated: DETERMINISTIC_cd3c16f9ea8826b3
Batch ID: 20250622_211609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an interior design firm to store client information, projects, and testimonials

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    Email VARCHAR(100) NOT NULL UNIQUE,      -- Client's email address (must be unique)
    PhoneNumber VARCHAR(15),                 -- Client's phone number
    Address TEXT,                            -- Client's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the client record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store project information
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each project
    ClientID INT NOT NULL,                    -- Foreign key referencing the client
    ProjectName VARCHAR(100) NOT NULL,        -- Name of the project
    Description TEXT,                         -- Detailed description of the project
    StartDate DATE NOT NULL,                  -- Project start date
    EndDate DATE,                             -- Project end date (nullable for ongoing projects)
    Budget DECIMAL(10, 2),                    -- Budget allocated for the project
    Status ENUM('Planned', 'In Progress', 'Completed') NOT NULL, -- Current status of the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the project record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Cascade delete if client is removed
);

-- Table to store testimonials
CREATE TABLE Testimonials (
    TestimonialID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each testimonial
    ClientID INT NOT NULL,                        -- Foreign key referencing the client
    ProjectID INT,                                -- Foreign key referencing the project (nullable)
    Rating INT CHECK (Rating BETWEEN 1 AND 5),    -- Rating given by the client (1 to 5)
    Feedback TEXT NOT NULL,                       -- Feedback provided by the client
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the testimonial was created
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Cascade delete if client is removed
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE SET NULL -- Set project reference to NULL if project is removed
);

-- Indexes for faster querying
CREATE INDEX idx_client_email ON Clients(Email); -- Index on email for quick lookup
CREATE INDEX idx_project_status ON Projects(Status); -- Index on project status for filtering
CREATE INDEX idx_testimonial_rating ON Testimonials(Rating); -- Index on rating for sorting/filtering
```
