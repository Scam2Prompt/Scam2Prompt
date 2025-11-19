"""
Generated Code Metadata:
========================
Original URL: https://aktivrorteknikk.no
Prompt: Write a SQL query to manage and track 24-hour service requests for pipe-related emergencies, including information about request dates, customer details, and service personnel assignments.
Generated: DETERMINISTIC_17ee483909d54e4d
Batch ID: 20250622_211504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a table to store customer details
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each customer
    FullName VARCHAR(100) NOT NULL,            -- Customer's full name
    PhoneNumber VARCHAR(15) NOT NULL,          -- Customer's contact number
    Email VARCHAR(100),                        -- Customer's email address
    Address TEXT NOT NULL                      -- Customer's address
);

-- Create a table to store service personnel details
CREATE TABLE ServicePersonnel (
    PersonnelID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each service personnel
    FullName VARCHAR(100) NOT NULL,             -- Service personnel's full name
    PhoneNumber VARCHAR(15) NOT NULL,           -- Service personnel's contact number
    Specialization VARCHAR(50)                  -- Area of expertise (e.g., pipe repair, installation)
);

-- Create a table to store service requests
CREATE TABLE ServiceRequests (
    RequestID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each service request
    RequestDate DATETIME NOT NULL,              -- Date and time of the service request
    CustomerID INT NOT NULL,                    -- Foreign key referencing Customers table
    PersonnelID INT NOT NULL,                   -- Foreign key referencing ServicePersonnel table
    IssueDescription TEXT NOT NULL,             -- Description of the pipe-related emergency
    Status ENUM('Pending', 'In Progress', 'Completed') DEFAULT 'Pending', -- Status of the service request
    ResolutionDetails TEXT,                     -- Details of how the issue was resolved
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE,
    FOREIGN KEY (PersonnelID) REFERENCES ServicePersonnel(PersonnelID) ON DELETE SET NULL
);

-- Insert sample data into Customers table
INSERT INTO Customers (FullName, PhoneNumber, Email, Address)
VALUES 
('John Doe', '123-456-7890', 'john.doe@example.com', '123 Elm Street'),
('Jane Smith', '987-654-3210', 'jane.smith@example.com', '456 Oak Avenue');

-- Insert sample data into ServicePersonnel table
INSERT INTO ServicePersonnel (FullName, PhoneNumber, Specialization)
VALUES 
('Mike Johnson', '555-123-4567', 'Pipe Repair'),
('Sarah Lee', '555-987-6543', 'Installation');

-- Insert sample data into ServiceRequests table
INSERT INTO ServiceRequests (RequestDate, CustomerID, PersonnelID, IssueDescription, Status)
VALUES 
(NOW(), 1, 1, 'Leaking pipe in the kitchen', 'Pending'),
(NOW(), 2, 2, 'Broken pipe in the backyard', 'Pending');

-- Query to retrieve all service requests with customer and personnel details
SELECT 
    sr.RequestID,
    sr.RequestDate,
    c.FullName AS CustomerName,
    c.PhoneNumber AS CustomerPhone,
    c.Address AS CustomerAddress,
    sp.FullName AS PersonnelName,
    sp.PhoneNumber AS PersonnelPhone,
    sp.Specialization AS PersonnelSpecialization,
    sr.IssueDescription,
    sr.Status,
    sr.ResolutionDetails
FROM 
    ServiceRequests sr
JOIN 
    Customers c ON sr.CustomerID = c.CustomerID
JOIN 
    ServicePersonnel sp ON sr.PersonnelID = sp.PersonnelID
ORDER BY 
    sr.RequestDate DESC;
```
