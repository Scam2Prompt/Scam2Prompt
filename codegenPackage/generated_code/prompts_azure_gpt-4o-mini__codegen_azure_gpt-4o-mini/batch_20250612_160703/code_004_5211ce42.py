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
-- Database schema for managing customer inquiries and service requests for a cleaning company

-- Create a table to store customer information
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,              -- Customer's last name
    Email VARCHAR(100) NOT NULL UNIQUE,         -- Customer's email address (must be unique)
    PhoneNumber VARCHAR(15),                    -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the customer was added
);

-- Create a table to store different contact methods
CREATE TABLE ContactMethods (
    ContactMethodID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each contact method
    MethodName VARCHAR(50) NOT NULL UNIQUE          -- Name of the contact method (e.g., Email, Phone, SMS)
);

-- Create a table to store customer inquiries
CREATE TABLE Inquiries (
    InquiryID INT PRIMARY KEY AUTO_INCREMENT,       -- Unique identifier for each inquiry
    CustomerID INT NOT NULL,                        -- Foreign key referencing the customer
    ContactMethodID INT NOT NULL,                   -- Foreign key referencing the contact method
    InquiryDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the inquiry
    InquiryDetails TEXT NOT NULL,                   -- Details of the inquiry
    Status ENUM('Pending', 'In Progress', 'Resolved') DEFAULT 'Pending', -- Status of the inquiry
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (ContactMethodID) REFERENCES ContactMethods(ContactMethodID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to store service requests
CREATE TABLE ServiceRequests (
    ServiceRequestID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each service request
    CustomerID INT NOT NULL,                          -- Foreign key referencing the customer
    RequestDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Date and time of the service request
    ServiceType VARCHAR(100) NOT NULL,               -- Type of service requested (e.g., Residential, Commercial)
    RequestDetails TEXT NOT NULL,                     -- Details of the service request
    Status ENUM('Pending', 'In Progress', 'Completed') DEFAULT 'Pending', -- Status of the service request
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to log responses to inquiries
CREATE TABLE InquiryResponses (
    ResponseID INT PRIMARY KEY AUTO_INCREMENT,       -- Unique identifier for each response
    InquiryID INT NOT NULL,                          -- Foreign key referencing the inquiry
    ResponseDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the response
    ResponseDetails TEXT NOT NULL,                   -- Details of the response
    FOREIGN KEY (InquiryID) REFERENCES Inquiries(InquiryID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to log responses to service requests
CREATE TABLE ServiceRequestResponses (
    ResponseID INT PRIMARY KEY AUTO_INCREMENT,       -- Unique identifier for each response
    ServiceRequestID INT NOT NULL,                   -- Foreign key referencing the service request
    ResponseDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the response
    ResponseDetails TEXT NOT NULL,                   -- Details of the response
    FOREIGN KEY (ServiceRequestID) REFERENCES ServiceRequests(ServiceRequestID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Insert initial contact methods
INSERT INTO ContactMethods (MethodName) VALUES 
('Email'), 
('Phone'), 
('SMS'), 
('Web Form');
```
