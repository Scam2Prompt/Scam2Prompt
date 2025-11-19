"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stars-ksa.com
Prompt: Design a database schema for managing customer inquiries and service requests for a cleaning company, inspired by the contact methods used by Star Cleaning Services.
Generated: DETERMINISTIC_5211ce42a09ac979
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing customer inquiries and service requests for a cleaning company

-- Table to store customer information
CREATE TABLE Customers (
    CustomerID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,            -- Customer's first name
    LastName VARCHAR(50) NOT NULL,             -- Customer's last name
    Email VARCHAR(100) NOT NULL UNIQUE,        -- Customer's email address
    PhoneNumber VARCHAR(15),                   -- Customer's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of account creation
);

-- Table to store customer inquiries
CREATE TABLE CustomerInquiries (
    InquiryID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each inquiry
    CustomerID INT NOT NULL,                   -- Foreign key referencing Customers table
    InquiryType VARCHAR(50) NOT NULL,          -- Type of inquiry (e.g., "Service Request", "General Question")
    Message TEXT NOT NULL,                     -- Inquiry message from the customer
    Status VARCHAR(20) DEFAULT 'Pending',      -- Status of the inquiry (e.g., "Pending", "Resolved")
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of inquiry creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of latest update
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE
);

-- Table to store service requests
CREATE TABLE ServiceRequests (
    RequestID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each service request
    CustomerID INT NOT NULL,                   -- Foreign key referencing Customers table
    ServiceType VARCHAR(50) NOT NULL,          -- Type of service requested (e.g., "Residential Cleaning", "Commercial Cleaning")
    ScheduledDate DATE NOT NULL,               -- Scheduled date for the service
    Status VARCHAR(20) DEFAULT 'Scheduled',    -- Status of the request (e.g., "Scheduled", "Completed", "Canceled")
    Notes TEXT,                                -- Additional notes or instructions for the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of service request creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of latest update
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE
);

-- Index to optimize searches for inquiries and requests by customer
CREATE INDEX idx_customer_inquiries ON CustomerInquiries (CustomerID);
CREATE INDEX idx_customer_requests ON ServiceRequests (CustomerID);

-- Table to log communication history between the company and customers
CREATE TABLE CommunicationLogs (
    CommunicationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each communication log
    CustomerID INT NOT NULL,                        -- Foreign key referencing Customers table
    CommunicationMethod VARCHAR(50) NOT NULL,       -- Method of communication (e.g., "Email", "Phone", "SMS")
    Message TEXT NOT NULL,                          -- Content of the communication
    SentAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,     -- Timestamp of when the communication was sent
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE
);

-- Table to store metadata about the services offered by the company
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,        -- Name of the service (e.g., "Residential Cleaning")
    Description TEXT,                         -- Description of the service
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the service
    Duration INT NOT NULL,                    -- Estimated duration of the service in minutes
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of service creation
);

-- Table to associate service requests with specific services
CREATE TABLE ServiceRequestDetails (
    DetailID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each detail entry
    RequestID INT NOT NULL,                    -- Foreign key referencing ServiceRequests table
    ServiceID INT NOT NULL,                    -- Foreign key referencing Services table
    Quantity INT DEFAULT 1,                    -- Quantity of the service requested
    TotalCost DECIMAL(10, 2) NOT NULL,         -- Total cost for the requested service
    FOREIGN KEY (RequestID) REFERENCES ServiceRequests(RequestID) ON DELETE CASCADE,
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE
);
```
