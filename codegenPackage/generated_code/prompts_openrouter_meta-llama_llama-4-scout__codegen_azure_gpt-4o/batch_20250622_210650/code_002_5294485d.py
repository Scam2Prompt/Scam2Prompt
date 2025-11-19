"""
Generated Code Metadata:
========================
Original URL: https://carolcrespo.com.br
Prompt: Generate a sample database schema to store client information, fitness plans, and appointment schedules for a personal training consulting service like Carol Crespo's, including fields for payment, plan type, and evaluation details.
Generated: DETERMINISTIC_5294485d32878aae
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a personal training consulting service

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,          -- Client's first name
    LastName VARCHAR(50) NOT NULL,           -- Client's last name
    Email VARCHAR(100) UNIQUE NOT NULL,      -- Client's email address
    PhoneNumber VARCHAR(15),                 -- Client's phone number
    DateOfBirth DATE,                        -- Client's date of birth
    Gender ENUM('Male', 'Female', 'Other'),  -- Client's gender
    Address TEXT,                            -- Client's address
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table to store fitness plans
CREATE TABLE FitnessPlans (
    PlanID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each fitness plan
    PlanName VARCHAR(100) NOT NULL,          -- Name of the fitness plan
    PlanType ENUM('Weight Loss', 'Muscle Gain', 'General Fitness', 'Rehabilitation') NOT NULL, -- Type of fitness plan
    Description TEXT,                        -- Detailed description of the plan
    DurationWeeks INT NOT NULL,              -- Duration of the plan in weeks
    Price DECIMAL(10, 2) NOT NULL,           -- Price of the fitness plan
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Record creation timestamp
);

-- Table to store appointment schedules
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each appointment
    ClientID INT NOT NULL,                        -- Foreign key referencing Clients table
    TrainerName VARCHAR(100) NOT NULL,            -- Name of the trainer
    AppointmentDate DATETIME NOT NULL,            -- Date and time of the appointment
    Status ENUM('Scheduled', 'Completed', 'Cancelled') DEFAULT 'Scheduled', -- Status of the appointment
    Notes TEXT,                                   -- Additional notes for the appointment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Cascade delete if client is removed
);

-- Table to store payment information
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each payment
    ClientID INT NOT NULL,                    -- Foreign key referencing Clients table
    PlanID INT NOT NULL,                      -- Foreign key referencing FitnessPlans table
    AmountPaid DECIMAL(10, 2) NOT NULL,       -- Amount paid by the client
    PaymentDate DATE NOT NULL,                -- Date of payment
    PaymentMethod ENUM('Credit Card', 'Debit Card', 'Cash', 'Bank Transfer') NOT NULL, -- Payment method
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Cascade delete if client is removed
    FOREIGN KEY (PlanID) REFERENCES FitnessPlans(PlanID) ON DELETE CASCADE -- Cascade delete if plan is removed
);

-- Table to store evaluation details
CREATE TABLE Evaluations (
    EvaluationID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each evaluation
    ClientID INT NOT NULL,                        -- Foreign key referencing Clients table
    EvaluationDate DATE NOT NULL,                 -- Date of the evaluation
    Weight DECIMAL(5, 2),                         -- Client's weight in kilograms
    BodyFatPercentage DECIMAL(5, 2),              -- Client's body fat percentage
    Notes TEXT,                                   -- Additional notes from the evaluation
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE -- Cascade delete if client is removed
);

-- Ensure all tables are created successfully
-- Use appropriate indexes for performance optimization
```
