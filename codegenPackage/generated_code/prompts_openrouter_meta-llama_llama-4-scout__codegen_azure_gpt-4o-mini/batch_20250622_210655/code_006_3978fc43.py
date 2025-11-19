"""
Generated Code Metadata:
========================
Original URL: https://sun-almamlaka.com
Prompt: "Design a simple database schema for managing home maintenance services including insulation, cleaning, and water leakage detection."
Generated: DETERMINISTIC_3978fc4356ccc97c
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing home maintenance services

-- Create a table for storing service types
CREATE TABLE ServiceTypes (
    ServiceTypeID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each service type
    ServiceName VARCHAR(100) NOT NULL,            -- Name of the service (e.g., Insulation, Cleaning)
    Description TEXT,                              -- Description of the service
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the service type was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table for storing customers
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,     -- Unique identifier for each customer
    FirstName VARCHAR(50) NOT NULL,               -- Customer's first name
    LastName VARCHAR(50) NOT NULL,                 -- Customer's last name
    Email VARCHAR(100) UNIQUE NOT NULL,            -- Customer's email address (must be unique)
    Phone VARCHAR(15),                             -- Customer's phone number
    Address VARCHAR(255),                          -- Customer's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the customer was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table for storing service appointments
CREATE TABLE Appointments (
    AppointmentID INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each appointment
    CustomerID INT NOT NULL,                        -- Foreign key referencing Customers
    ServiceTypeID INT NOT NULL,                     -- Foreign key referencing ServiceTypes
    AppointmentDate DATETIME NOT NULL,              -- Date and time of the appointment
    Status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled', -- Status of the appointment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the appointment was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (ServiceTypeID) REFERENCES ServiceTypes(ServiceTypeID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table for storing service feedback
CREATE TABLE Feedback (
    FeedbackID INT PRIMARY KEY AUTO_INCREMENT,      -- Unique identifier for each feedback entry
    AppointmentID INT NOT NULL,                     -- Foreign key referencing Appointments
    Rating INT CHECK (Rating BETWEEN 1 AND 5),      -- Rating given by the customer (1 to 5)
    Comments TEXT,                                   -- Additional comments from the customer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the feedback was submitted
    FOREIGN KEY (AppointmentID) REFERENCES Appointments(AppointmentID) ON DELETE CASCADE -- Ensure referential integrity
);
```
