"""
Generated Code Metadata:
========================
Original URL: https://www.premierpointing.com.au
Prompt: Create a database schema for managing client reviews and project details, including fields for mortar type, tuckpointing details, and remedial techniques, inspired by Premier Pointing's services.
Generated: DETERMINISTIC_7a1403ddafc763ba
Batch ID: 20250612_145249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing client reviews and project details
CREATE DATABASE PremierPointing;

USE PremierPointing;

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Phone VARCHAR(15),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table to store project details
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY,
    ClientID INT NOT NULL,
    ProjectName VARCHAR(100) NOT NULL,
    MortarType VARCHAR(50) NOT NULL,
    TuckpointingDetails TEXT,
    RemedialTechniques TEXT,
    StartDate DATE,
    EndDate DATE,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE
);

-- Table to store client reviews
CREATE TABLE Reviews (
    ReviewID INT AUTO_INCREMENT PRIMARY KEY,
    ProjectID INT NOT NULL,
    Rating INT CHECK (Rating BETWEEN 1 AND 5),
    Comments TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE
);

-- Indexes for performance optimization
CREATE INDEX idx_client_email ON Clients(Email);
CREATE INDEX idx_project_client ON Projects(ClientID);
CREATE INDEX idx_review_project ON Reviews(ProjectID);
```
