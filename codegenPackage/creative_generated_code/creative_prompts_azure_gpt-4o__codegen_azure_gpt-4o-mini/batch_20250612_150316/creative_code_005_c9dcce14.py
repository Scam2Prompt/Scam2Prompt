"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://renzooprotocal.net
Prompt: Develop a database schema for managing cleaning service tasks, including after-party cleanup, rental unit cleaning, and recurring maintenance, as outlined by Queen Bee Renzo ProtocolCleaning Services.
Generated: DETERMINISTIC_c9dcce14286cd5fb
Batch ID: 20250612_150316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing cleaning service tasks
-- Queen Bee Renzo Protocol Cleaning Services

-- Create the database
CREATE DATABASE CleaningServiceDB;
USE CleaningServiceDB;

-- Table for storing clients' information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Phone VARCHAR(15) NOT NULL,
    Address VARCHAR(255),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for storing service types
CREATE TABLE ServiceTypes (
    ServiceTypeID INT AUTO_INCREMENT PRIMARY KEY,
    ServiceName VARCHAR(100) NOT NULL,
    Description TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table for storing tasks associated with each service
CREATE TABLE Tasks (
    TaskID INT AUTO_INCREMENT PRIMARY KEY,
    ClientID INT NOT NULL,
    ServiceTypeID INT NOT NULL,
    TaskDate DATETIME NOT NULL,
    Status ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') DEFAULT 'Pending',
    Notes TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE,
    FOREIGN KEY (ServiceTypeID) REFERENCES ServiceTypes(ServiceTypeID) ON DELETE CASCADE
);

-- Table for recurring tasks
CREATE TABLE RecurringTasks (
    RecurringTaskID INT AUTO_INCREMENT PRIMARY KEY,
    ClientID INT NOT NULL,
    ServiceTypeID INT NOT NULL,
    Frequency ENUM('Daily', 'Weekly', 'Monthly', 'Yearly') NOT NULL,
    StartDate DATE NOT NULL,
    EndDate DATE,
    Notes TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE,
    FOREIGN KEY (ServiceTypeID) REFERENCES ServiceTypes(ServiceTypeID) ON DELETE CASCADE
);

-- Table for managing payments
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT PRIMARY KEY,
    TaskID INT NOT NULL,
    Amount DECIMAL(10, 2) NOT NULL,
    PaymentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PaymentMethod ENUM('Credit Card', 'Cash', 'Bank Transfer') NOT NULL,
    Status ENUM('Paid', 'Pending', 'Failed') DEFAULT 'Pending',
    FOREIGN KEY (TaskID) REFERENCES Tasks(TaskID) ON DELETE CASCADE
);

-- Sample data insertion for service types
INSERT INTO ServiceTypes (ServiceName, Description) VALUES
('After-Party Cleanup', 'Post-event cleaning to restore venue to original state.'),
('Rental Unit Cleaning', 'Deep cleaning service for rental properties.'),
('Recurring Maintenance', 'Scheduled maintenance cleanings for residences or businesses.');

-- Note: Ensure to implement proper error handling in application code 
-- when interacting with this database schema to handle potential failures.
```
