"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hyperswap.tech
Prompt: Design a database schema for storing information about paving projects and customer reviews, based on the structure used by Bedford Paving Company.
Generated: DETERMINISTIC_cec7e318c75bc2fe
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing information about paving projects and customer reviews

-- Drop existing tables if they exist (for demo purposes only)
DROP TABLE IF EXISTS CustomerReviews;
DROP TABLE IF EXISTS PavingProjects;
DROP TABLE IF EXISTS Customers;

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each customer
    Name VARCHAR(100) NOT NULL,                -- Customer's name
    Email VARCHAR(100) UNIQUE NOT NULL,        -- Customer's email (must be unique)
    Phone VARCHAR(15) NOT NULL,                -- Customer's contact number
    Address VARCHAR(255),                       -- Optional address field
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table to store paving project information
CREATE TABLE PavingProjects (
    ProjectID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each paving project
    CustomerID INT NOT NULL,                    -- Reference to the customer who owns the project
    ProjectDescription TEXT NOT NULL,           -- Description of the paving project
    ProjectCost DECIMAL(10, 2) NOT NULL,       -- Cost of the paving project
    ProjectStartDate DATE NOT NULL,             -- Start date of the project
    ProjectEndDate DATE,                        -- End date of the project (nullable)
    Status ENUM('Pending', 'In Progress', 'Completed') NOT NULL DEFAULT 'Pending', -- Status of the project
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Foreign key constraint
);

-- Table to store customer reviews for paving projects
CREATE TABLE CustomerReviews (
    ReviewID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each review
    ProjectID INT NOT NULL,                      -- Reference to the associated paving project
    CustomerID INT NOT NULL,                     -- Reference to the customer who submitted the review
    Rating INT CHECK (Rating >= 1 AND Rating <= 5), -- Rating from 1 to 5
    ReviewText TEXT,                             -- Review text provided by the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (ProjectID) REFERENCES PavingProjects(ProjectID) ON DELETE CASCADE, -- Foreign key constraint
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Foreign key constraint
);

-- Sample Queries to insert and retrieve data
-- NOTE: These are sample queries that would normally be run in your application logic.

-- To insert a new customer
INSERT INTO Customers (Name, Email, Phone, Address) 
VALUES ('John Doe', 'john@example.com', '555-1234', '123 Main St');

-- To insert a new paving project for a customer
INSERT INTO PavingProjects (CustomerID, ProjectDescription, ProjectCost, ProjectStartDate)
VALUES (1, 'Driveway repaving', 2000.00, '2023-10-01');

-- To insert a new customer review for a paving project
INSERT INTO CustomerReviews (ProjectID, CustomerID, Rating, ReviewText)
VALUES (1, 1, 5, 'Excellent service and quality work!');

-- To retrieve all paving projects along with their customer reviews
SELECT P.ProjectID, C.Name, P.ProjectDescription, P.ProjectCost, P.Status, R.Rating, R.ReviewText
FROM PavingProjects P
JOIN Customers C ON P.CustomerID = C.CustomerID
LEFT JOIN CustomerReviews R ON P.ProjectID = R.ProjectID;
```
