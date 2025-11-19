"""
Generated Code Metadata:
========================
Original URL: https://fenceguys4u.com
Prompt: Create a database schema for storing customer inquiries, project details, and feedback, tailored to the services offered by "The Fence Guys" (fences, decks, pergolas).
Generated: DETERMINISTIC_a4cbee7caf2a7c9b
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for The Fence Guys

CREATE DATABASE TheFenceGuys;

USE TheFenceGuys;

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    Address VARCHAR(255),
    City VARCHAR(100),
    State VARCHAR(100),
    PostalCode VARCHAR(20),
    PRIMARY KEY (CustomerID)
);

-- Table to store inquiry types (e.g., fences, decks, pergolas)
CREATE TABLE InquiryTypes (
    InquiryTypeID INT AUTO_INCREMENT,
    InquiryType VARCHAR(100) NOT NULL,
    Description TEXT,
    PRIMARY KEY (InquiryTypeID)
);

-- Table to store customer inquiries
CREATE TABLE Inquiries (
    InquiryID INT AUTO_INCREMENT,
    CustomerID INT NOT NULL,
    InquiryTypeID INT NOT NULL,
    InquiryDate DATE NOT NULL,
    Description TEXT,
    Status VARCHAR(50) NOT NULL DEFAULT 'New',
    PRIMARY KEY (InquiryID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (InquiryTypeID) REFERENCES InquiryTypes(InquiryTypeID)
);

-- Table to store project details
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT,
    InquiryID INT NOT NULL,
    ProjectDate DATE NOT NULL,
    ProjectType VARCHAR(100) NOT NULL,
    Description TEXT,
    Status VARCHAR(50) NOT NULL DEFAULT 'Not Started',
    PRIMARY KEY (ProjectID),
    FOREIGN KEY (InquiryID) REFERENCES Inquiries(InquiryID)
);

-- Table to store project feedback
CREATE TABLE Feedback (
    FeedbackID INT AUTO_INCREMENT,
    ProjectID INT NOT NULL,
    Rating TINYINT NOT NULL CHECK (Rating BETWEEN 1 AND 5),
    Comment TEXT,
    FeedbackDate DATE NOT NULL,
    PRIMARY KEY (FeedbackID),
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID)
);

-- Insert sample data for inquiry types
INSERT INTO InquiryTypes (InquiryType, Description)
VALUES 
('Fence Installation', 'Installation of new fences'),
('Deck Installation', 'Installation of new decks'),
('Pergola Installation', 'Installation of new pergolas'),
('Fence Repair', 'Repair of existing fences'),
('Deck Repair', 'Repair of existing decks'),
('Pergola Repair', 'Repair of existing pergolas');

-- Create views for easier data retrieval
CREATE VIEW CustomerInquiries AS
SELECT 
    c.CustomerID, 
    c.FirstName, 
    c.LastName, 
    i.InquiryID, 
    it.InquiryType, 
    i.InquiryDate, 
    i.Status
FROM 
    Customers c
JOIN 
    Inquiries i ON c.CustomerID = i.CustomerID
JOIN 
    InquiryTypes it ON i.InquiryTypeID = it.InquiryTypeID;

CREATE VIEW ProjectFeedback AS
SELECT 
    p.ProjectID, 
    p.ProjectType, 
    f.FeedbackID, 
    f.Rating, 
    f.Comment, 
    f.FeedbackDate
FROM 
    Projects p
JOIN 
    Feedback f ON p.ProjectID = f.ProjectID;
```
