"""
Generated Code Metadata:
========================
Original URL: https://stars-ksa.com
Prompt: Design a database schema for managing customer inquiries and service requests for a cleaning company, inspired by the contact methods used by Star Cleaning Services.
Generated: DETERMINISTIC_5211ce42a09ac979
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for cleaning company
CREATE DATABASE CleaningCompany;

-- Use the database
USE CleaningCompany;

-- Create table for customers
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
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (CustomerID)
);

-- Create table for service types
CREATE TABLE ServiceTypes (
    ServiceTypeID INT AUTO_INCREMENT,
    ServiceType VARCHAR(100) NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ServiceTypeID)
);

-- Create table for service requests
CREATE TABLE ServiceRequests (
    ServiceRequestID INT AUTO_INCREMENT,
    CustomerID INT NOT NULL,
    ServiceTypeID INT NOT NULL,
    RequestDate DATE NOT NULL,
    RequestTime TIME NOT NULL,
    Description TEXT,
    Status ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') DEFAULT 'Pending',
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ServiceRequestID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (ServiceTypeID) REFERENCES ServiceTypes(ServiceTypeID)
);

-- Create table for inquiries
CREATE TABLE Inquiries (
    InquiryID INT AUTO_INCREMENT,
    CustomerID INT NOT NULL,
    InquiryDate DATE NOT NULL,
    InquiryTime TIME NOT NULL,
    Description TEXT,
    Response TEXT,
    Status ENUM('Pending', 'Responded', 'Follow-up') DEFAULT 'Pending',
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (InquiryID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

-- Create table for service providers
CREATE TABLE ServiceProviders (
    ServiceProviderID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ServiceProviderID)
);

-- Create table for service request assignments
CREATE TABLE ServiceRequestAssignments (
    ServiceRequestAssignmentID INT AUTO_INCREMENT,
    ServiceRequestID INT NOT NULL,
    ServiceProviderID INT NOT NULL,
    AssignedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (ServiceRequestAssignmentID),
    FOREIGN KEY (ServiceRequestID) REFERENCES ServiceRequests(ServiceRequestID),
    FOREIGN KEY (ServiceProviderID) REFERENCES ServiceProviders(ServiceProviderID)
);

-- Create indexes for foreign keys
CREATE INDEX idx_ServiceRequests_CustomerID ON ServiceRequests (CustomerID);
CREATE INDEX idx_ServiceRequests_ServiceTypeID ON ServiceRequests (ServiceTypeID);
CREATE INDEX idx_Inquiries_CustomerID ON Inquiries (CustomerID);
CREATE INDEX idx_ServiceRequestAssignments_ServiceRequestID ON ServiceRequestAssignments (ServiceRequestID);
CREATE INDEX idx_ServiceRequestAssignments_ServiceProviderID ON ServiceRequestAssignments (ServiceProviderID);
```

```sql
-- sample_data.sql

-- Insert sample data into customers table
INSERT INTO Customers (FirstName, LastName, Email, Phone, Address, City, State, PostalCode)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St', 'Anytown', 'CA', '12345'),
('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210', '456 Elm St', 'Othertown', 'NY', '67890');

-- Insert sample data into service types table
INSERT INTO ServiceTypes (ServiceType, Description)
VALUES 
('House Cleaning', 'General house cleaning services'),
('Office Cleaning', 'Office cleaning services'),
('Special Event Cleaning', 'Cleaning services for special events');

-- Insert sample data into service requests table
INSERT INTO ServiceRequests (CustomerID, ServiceTypeID, RequestDate, RequestTime, Description)
VALUES 
(1, 1, '2024-09-16', '09:00:00', 'Need house cleaned for party'),
(2, 2, '2024-09-17', '10:00:00', 'Need office cleaned');

-- Insert sample data into inquiries table
INSERT INTO Inquiries (CustomerID, InquiryDate, InquiryTime, Description)
VALUES 
(1, '2024-09-15', '12:00:00', 'What are your cleaning services?'),
(2, '2024-09-16', '14:00:00', 'Do you offer eco-friendly cleaning?');

-- Insert sample data into service providers table
INSERT INTO ServiceProviders (FirstName, LastName, Email, Phone)
VALUES 
('Bob', 'Johnson', 'bob.johnson@example.com', '555-123-4567'),
('Alice', 'Williams', 'alice.williams@example.com', '555-987-6543');

-- Insert sample data into service request assignments table
INSERT INTO ServiceRequestAssignments (ServiceRequestID, ServiceProviderID)
VALUES 
(1, 1),
(2, 2);
```
