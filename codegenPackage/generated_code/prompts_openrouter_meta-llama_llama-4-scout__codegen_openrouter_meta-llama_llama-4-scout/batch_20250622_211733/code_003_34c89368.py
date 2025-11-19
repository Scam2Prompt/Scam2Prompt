"""
Generated Code Metadata:
========================
Original URL: https://tc-harsewinkel.de
Prompt: Design a database schema for storing information about tennis club members, their membership types, and contributions, and provide SQL code to create the schema.
Generated: DETERMINISTIC_34c8936850902a5e
Batch ID: 20250622_211733
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for tennis club management

-- Create database
CREATE DATABASE TennisClub;

-- Use database
USE TennisClub;

-- Create table for membership types
CREATE TABLE MembershipTypes (
    MembershipTypeID INT AUTO_INCREMENT,
    MembershipTypeName VARCHAR(255) NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (MembershipTypeID)
);

-- Create table for members
CREATE TABLE Members (
    MemberID INT AUTO_INCREMENT,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    Address VARCHAR(255),
    MembershipTypeID INT,
    JoinDate DATE,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (MemberID),
    FOREIGN KEY (MembershipTypeID) REFERENCES MembershipTypes(MembershipTypeID) ON DELETE SET NULL
);

-- Create table for contributions
CREATE TABLE Contributions (
    ContributionID INT AUTO_INCREMENT,
    MemberID INT,
    ContributionDate DATE NOT NULL,
    Amount DECIMAL(10, 2) NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ContributionID),
    FOREIGN KEY (MemberID) REFERENCES Members(MemberID) ON DELETE CASCADE
);

-- Create index on foreign key columns
CREATE INDEX idx_Members_MembershipTypeID ON Members (MembershipTypeID);
CREATE INDEX idx_Contributions_MemberID ON Contributions (MemberID);

-- Insert sample data for testing
INSERT INTO MembershipTypes (MembershipTypeName, Description)
VALUES 
('Full Member', 'Full access to club facilities'),
('Junior Member', 'Limited access to club facilities for juniors'),
('Social Member', 'Social events only');

INSERT INTO Members (FirstName, LastName, Email, Phone, Address, MembershipTypeID, JoinDate)
VALUES 
('John', 'Doe', 'john.doe@example.com', '1234567890', '123 Main St', 1, '2022-01-01'),
('Jane', 'Doe', 'jane.doe@example.com', '9876543210', '456 Elm St', 2, '2022-06-01'),
('Bob', 'Smith', 'bob.smith@example.com', '5551234567', '789 Oak St', 3, '2022-03-01');

INSERT INTO Contributions (MemberID, ContributionDate, Amount, Description)
VALUES 
(1, '2022-02-01', 100.00, 'Monthly dues'),
(1, '2022-03-01', 50.00, 'Event sponsorship'),
(2, '2022-07-01', 75.00, 'Monthly dues'),
(3, '2022-04-01', 200.00, 'Donation');
```
