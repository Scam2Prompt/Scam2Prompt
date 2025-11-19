"""
Generated Code Metadata:
========================
Original URL: https://mluce-ginza.net
Prompt: Generate a sample database schema for storing client information, treatment plans, and appointment schedules for a makeup salon with multiple services like M luce.
Generated: DETERMINISTIC_c486160f4f873434
Batch ID: 20250622_212850
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a makeup salon to store client information, treatment plans, and appointment schedules

-- Drop existing tables if they exist (for development purposes)
DROP TABLE IF EXISTS Appointments;
DROP TABLE IF EXISTS TreatmentPlans;
DROP TABLE IF EXISTS Clients;
DROP TABLE IF EXISTS Services;

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,      -- Client's email address (unique)
    PhoneNumber VARCHAR(15),                  -- Client's phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store services offered by the salon
CREATE TABLE Services (
    ServiceID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each service
    ServiceName VARCHAR(100) NOT NULL,        -- Name of the service
    Description TEXT,                          -- Description of the service
    Price DECIMAL(10, 2) NOT NULL,            -- Price of the service
    Duration INT NOT NULL                      -- Duration of the service in minutes
);

-- Table to store treatment plans for clients
CREATE TABLE TreatmentPlans (
    TreatmentPlanID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each treatment plan
    ClientID INT NOT NULL,                          -- Foreign key referencing Clients
    ServiceID INT NOT NULL,                         -- Foreign key referencing Services
    StartDate DATE NOT NULL,                        -- Start date of the treatment plan
    EndDate DATE NOT NULL,                          -- End date of the treatment plan
    Notes TEXT,                                    -- Additional notes for the treatment plan
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Table to store appointment schedules
CREATE TABLE Appointments (
    AppointmentID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each appointment
    ClientID INT NOT NULL,                          -- Foreign key referencing Clients
    ServiceID INT NOT NULL,                         -- Foreign key referencing Services
    AppointmentDate DATETIME NOT NULL,              -- Date and time of the appointment
    Status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled',  -- Status of the appointment
    Notes TEXT,                                    -- Additional notes for the appointment
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE  -- Ensure referential integrity
);

-- Sample data insertion (for testing purposes)
INSERT INTO Services (ServiceName, Description, Price, Duration) VALUES
('Makeup Application', 'Professional makeup application for events.', 100.00, 90),
('Facial Treatment', 'Relaxing facial treatment for skin rejuvenation.', 80.00, 60),
('Eyebrow Shaping', 'Shaping and styling of eyebrows.', 30.00, 30);

-- Note: Ensure to handle errors and exceptions in your application logic when interacting with this schema.
```
