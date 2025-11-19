"""
Generated Code Metadata:
========================
Original URL: https://fenceguys4u.com
Prompt: "Design a database schema to store information about customers, projects, and services offered by a fence, deck, and pergola installation company, including fields for customer satisfaction ratings and project completion dates."
Generated: DETERMINISTIC_ebc45a33555c8a23
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a fence, deck, and pergola installation company

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,             -- Customer's last name
    Email VARCHAR(100) NOT NULL UNIQUE,        -- Customer's email address
    PhoneNumber VARCHAR(15),                   -- Customer's phone number
    Address TEXT,                              -- Customer's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the customer record was created
);

-- Table to store project information
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each project
    CustomerID INT NOT NULL,                   -- Foreign key linking to the Customers table
    ProjectType ENUM('Fence', 'Deck', 'Pergola') NOT NULL, -- Type of project
    StartDate DATE NOT NULL,                   -- Project start date
    CompletionDate DATE,                       -- Project completion date
    SatisfactionRating INT CHECK (SatisfactionRating BETWEEN 1 AND 5), -- Customer satisfaction rating (1-5)
    TotalCost DECIMAL(10, 2) NOT NULL,         -- Total cost of the project
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the project record was created
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store services offered by the company
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,         -- Name of the service
    Description TEXT,                          -- Description of the service
    BasePrice DECIMAL(10, 2) NOT NULL,         -- Base price for the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the service record was created
);

-- Table to link projects and services (many-to-many relationship)
CREATE TABLE ProjectServices (
    ProjectServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each record
    ProjectID INT NOT NULL,                          -- Foreign key linking to the Projects table
    ServiceID INT NOT NULL,                          -- Foreign key linking to the Services table
    Quantity INT NOT NULL CHECK (Quantity > 0),      -- Quantity of the service used in the project
    TotalPrice DECIMAL(10, 2) NOT NULL,              -- Total price for the service in the project
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Indexes for optimizing queries
CREATE INDEX idx_customer_email ON Customers(Email); -- Index for quick lookup by email
CREATE INDEX idx_project_customer ON Projects(CustomerID); -- Index for quick lookup by customer ID
CREATE INDEX idx_project_type ON Projects(ProjectType); -- Index for quick lookup by project type
CREATE INDEX idx_service_name ON Services(ServiceName); -- Index for quick lookup by service name
```
