"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cart3.pages.dev
Prompt: Develop a sample database schema for managing client information, appointment scheduling, and service offerings in a legal and accounting firm, based on the practice areas of Carthew Chau & Co.
Generated: DETERMINISTIC_f74cd68ea025f227
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Carthew Chau & Co. Legal and Accounting Firm

-- Create the database
CREATE DATABASE CarthewChauCo;

-- Use the created database
USE CarthewChauCo;

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,      -- Client's email address
    PhoneNumber VARCHAR(15) NOT NULL,        -- Client's phone number
    Address VARCHAR(255),                     -- Client's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store service offerings
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,        -- Name of the service
    Description TEXT,                         -- Description of the service
    PracticeArea VARCHAR(50) NOT NULL,        -- Relevant practice area (e.g., Legal, Accounting)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to manage appointments
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each appointment
    ClientID INT NOT NULL,                       -- Foreign key referencing Clients table
    ServiceID INT NOT NULL,                      -- Foreign key referencing Services table
    AppointmentDate DATETIME NOT NULL,           -- Date and time of the appointment
    Status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled', -- Status of the appointment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store payment records
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each payment
    AppointmentID INT NOT NULL,                -- Foreign key referencing Appointments table
    Amount DECIMAL(10, 2) NOT NULL,           -- Amount of the payment
    PaymentDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time of the payment
    PaymentMethod ENUM('Credit Card', 'Cash', 'Bank Transfer') NOT NULL, -- Method of payment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (AppointmentID) REFERENCES Appointments(AppointmentID) ON DELETE CASCADE -- Ensure referential integrity
);
```
