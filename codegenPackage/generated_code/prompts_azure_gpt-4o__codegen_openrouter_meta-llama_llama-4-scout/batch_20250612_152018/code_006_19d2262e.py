"""
Generated Code Metadata:
========================
Original URL: https://darulraza.net
Prompt: Provide code to create a database schema for managing Taweezat and Wazaif requests, including user details, request status, and fulfillment tracking.
Generated: DETERMINISTIC_19d2262e27e974ed
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for managing Taweezat and Wazaif requests

CREATE DATABASE TaweezatWazaifDB;

USE TaweezatWazaifDB;

-- Create table for users
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    Address TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (UserID)
);

-- Create table for Taweezat requests
CREATE TABLE TaweezatRequests (
    RequestID INT AUTO_INCREMENT,
    UserID INT NOT NULL,
    RequestType ENUM('Taweez', 'Wazifa') NOT NULL,
    RequestDescription TEXT,
    RequestStatus ENUM('Pending', 'In Progress', 'Fulfilled', 'Rejected') DEFAULT 'Pending',
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (RequestID),
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
);

-- Create table for Wazaif
CREATE TABLE Wazaif (
    WazifaID INT AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    Description TEXT,
    RecitationCount INT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (WazifaID)
);

-- Create table for Taweezat
CREATE TABLE Taweezat (
    TaweezID INT AUTO_INCREMENT,
    Name VARCHAR(255) NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (TaweezID)
);

-- Create table for request fulfillment tracking
CREATE TABLE FulfillmentTracking (
    TrackingID INT AUTO_INCREMENT,
    RequestID INT NOT NULL,
    FulfilledBy VARCHAR(255),
    FulfillmentDate DATE,
    Notes TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (TrackingID),
    FOREIGN KEY (RequestID) REFERENCES TaweezatRequests(RequestID)
);

-- Create table for comments on requests
CREATE TABLE RequestComments (
    CommentID INT AUTO_INCREMENT,
    RequestID INT NOT NULL,
    CommentBy VARCHAR(255) NOT NULL,
    Comment TEXT NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (CommentID),
    FOREIGN KEY (RequestID) REFERENCES TaweezatRequests(RequestID)
);

-- Insert sample data for testing
INSERT INTO Users (Name, Email, Phone, Address)
VALUES 
('John Doe', 'john@example.com', '1234567890', '123 Main St'),
('Jane Doe', 'jane@example.com', '9876543210', '456 Elm St');

INSERT INTO TaweezatRequests (UserID, RequestType, RequestDescription)
VALUES 
(1, 'Taweez', 'Sample Taweez request'),
(2, 'Wazifa', 'Sample Wazifa request');

INSERT INTO Wazaif (Name, Description, RecitationCount)
VALUES 
('Wazifa 1', 'Sample Wazifa 1', 100),
('Wazifa 2', 'Sample Wazifa 2', 200);

INSERT INTO Taweezat (Name, Description)
VALUES 
('Taweez 1', 'Sample Taweez 1'),
('Taweez 2', 'Sample Taweez 2');

INSERT INTO FulfillmentTracking (RequestID, FulfilledBy, FulfillmentDate, Notes)
VALUES 
(1, 'Admin', '2022-01-01', 'Sample fulfillment notes');

INSERT INTO RequestComments (RequestID, CommentBy, Comment)
VALUES 
(1, 'Admin', 'Sample comment on request');
```
