"""
Generated Code Metadata:
========================
Original URL: https://albatrosspa.cl
Prompt: "Design a database schema for a construction project management system, incorporating features like project tracking, team collaboration, and client communication, similar to Albatros SPA's approach to project management."
Generated: DETERMINISTIC_3aa5a495f2b19d9e
Batch ID: 20250622_211510
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a Construction Project Management System

-- Table to store information about clients
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    Address TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table to store information about projects
CREATE TABLE Projects (
    ProjectID INT PRIMARY KEY AUTO_INCREMENT,
    ClientID INT NOT NULL,
    ProjectName VARCHAR(255) NOT NULL,
    StartDate DATE NOT NULL,
    EndDate DATE,
    Status ENUM('Planning', 'In Progress', 'Completed', 'On Hold') NOT NULL,
    Budget DECIMAL(10, 2),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE
);

-- Table to store information about team members
CREATE TABLE TeamMembers (
    MemberID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Role VARCHAR(100),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Table to associate team members with projects
CREATE TABLE ProjectTeam (
    ProjectID INT NOT NULL,
    MemberID INT NOT NULL,
    PRIMARY KEY (ProjectID, MemberID),
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE,
    FOREIGN KEY (MemberID) REFERENCES TeamMembers(MemberID) ON DELETE CASCADE
);

-- Table to store tasks related to projects
CREATE TABLE Tasks (
    TaskID INT PRIMARY KEY AUTO_INCREMENT,
    ProjectID INT NOT NULL,
    AssignedTo INT,
    TaskName VARCHAR(255) NOT NULL,
    Description TEXT,
    Status ENUM('Not Started', 'In Progress', 'Completed', 'Blocked') NOT NULL,
    DueDate DATE,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE,
    FOREIGN KEY (AssignedTo) REFERENCES TeamMembers(MemberID) ON DELETE SET NULL
);

-- Table to store communication logs between clients and team members
CREATE TABLE Communications (
    CommunicationID INT PRIMARY KEY AUTO_INCREMENT,
    ProjectID INT NOT NULL,
    SenderID INT NOT NULL,
    ReceiverID INT NOT NULL,
    Message TEXT NOT NULL,
    SentAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE,
    FOREIGN KEY (SenderID) REFERENCES TeamMembers(MemberID) ON DELETE CASCADE,
    FOREIGN KEY (ReceiverID) REFERENCES TeamMembers(MemberID) ON DELETE CASCADE
);

-- Table to store project milestones
CREATE TABLE Milestones (
    MilestoneID INT PRIMARY KEY AUTO_INCREMENT,
    ProjectID INT NOT NULL,
    MilestoneName VARCHAR(255) NOT NULL,
    DueDate DATE NOT NULL,
    Status ENUM('Pending', 'Achieved', 'Delayed') NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE
);
```
