"""
Generated Code Metadata:
========================
Original URL: https://pconsultsa.com
Prompt: Design a simple database schema to store information about clients, projects, and outcomes for a consulting firm like PConsultsa.
Generated: DETERMINISTIC_164e27c73f1e33f9
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the consulting firm
CREATE DATABASE PConsultsaDB;

-- Use the created database
USE PConsultsaDB;

-- Create a table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT,
    ClientName VARCHAR(255) NOT NULL,
    ClientEmail VARCHAR(255) UNIQUE NOT NULL,
    ClientPhone VARCHAR(20),
    ClientAddress VARCHAR(255),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ClientID)
);

-- Create a table to store project information
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT,
    ClientID INT NOT NULL,
    ProjectName VARCHAR(255) NOT NULL,
    ProjectDescription TEXT,
    ProjectStartDate DATE,
    ProjectEndDate DATE,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ProjectID),
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE
);

-- Create a table to store outcome information
CREATE TABLE Outcomes (
    OutcomeID INT AUTO_INCREMENT,
    ProjectID INT NOT NULL,
    OutcomeDescription TEXT NOT NULL,
    OutcomeDate DATE NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (OutcomeID),
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE
);

-- Create a table to store users for authentication (optional)
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT,
    Username VARCHAR(255) UNIQUE NOT NULL,
    PasswordHash VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Role ENUM('admin', 'consultant') NOT NULL DEFAULT 'consultant',
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (UserID)
);

-- Example insert statements
INSERT INTO Clients (ClientName, ClientEmail, ClientPhone, ClientAddress)
VALUES 
('John Doe Inc.', 'john.doe@example.com', '123-456-7890', '123 Main St'),
('Jane Smith LLC.', 'jane.smith@example.com', '987-654-3210', '456 Elm St');

INSERT INTO Projects (ClientID, ProjectName, ProjectDescription, ProjectStartDate, ProjectEndDate)
VALUES 
(1, 'Marketing Strategy', 'Develop a marketing strategy for John Doe Inc.', '2022-01-01', '2022-06-30'),
(1, 'Rebranding', 'Rebrand John Doe Inc.', '2022-07-01', '2022-12-31'),
(2, 'IT Consulting', 'Provide IT consulting services for Jane Smith LLC.', '2022-01-01', '2022-03-31');

INSERT INTO Outcomes (ProjectID, OutcomeDescription, OutcomeDate)
VALUES 
(1, 'Completed market research', '2022-02-15'),
(1, 'Developed marketing strategy document', '2022-04-01'),
(2, 'Designed new logo', '2022-08-01'),
(3, 'Conducted IT audit', '2022-01-15');
```
