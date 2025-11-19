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
-- Create database schema for personal training consulting service

CREATE DATABASE PersonalTrainingService;

USE PersonalTrainingService;

-- Create table for clients
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    Address VARCHAR(255),
    City VARCHAR(100),
    State VARCHAR(100),
    ZipCode VARCHAR(10),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ClientID)
);

-- Create table for fitness plans
CREATE TABLE FitnessPlans (
    PlanID INT AUTO_INCREMENT,
    PlanType VARCHAR(100) NOT NULL,
    Description TEXT,
    Duration INT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (PlanID)
);

-- Create table for appointments
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT,
    ClientID INT NOT NULL,
    PlanID INT,
    AppointmentDate DATE NOT NULL,
    StartTime TIME NOT NULL,
    EndTime TIME NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (AppointmentID),
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID),
    FOREIGN KEY (PlanID) REFERENCES FitnessPlans(PlanID)
);

-- Create table for payments
CREATE TABLE Payments (
    PaymentID INT AUTO_INCREMENT,
    AppointmentID INT NOT NULL,
    PaymentDate DATE NOT NULL,
    Amount DECIMAL(10, 2) NOT NULL,
    PaymentMethod VARCHAR(100) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (PaymentID),
    FOREIGN KEY (AppointmentID) REFERENCES Appointments(AppointmentID)
);

-- Create table for evaluations
CREATE TABLE Evaluations (
    EvaluationID INT AUTO_INCREMENT,
    ClientID INT NOT NULL,
    EvaluationDate DATE NOT NULL,
    Progress TEXT,
    Goals TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (EvaluationID),
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID)
);

-- Create table for client plans
CREATE TABLE ClientPlans (
    ClientPlanID INT AUTO_INCREMENT,
    ClientID INT NOT NULL,
    PlanID INT NOT NULL,
    StartDate DATE NOT NULL,
    EndDate DATE,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ClientPlanID),
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID),
    FOREIGN KEY (PlanID) REFERENCES FitnessPlans(PlanID)
);

-- Example data insertion
INSERT INTO Clients (FirstName, LastName, Email, Phone, Address, City, State, ZipCode)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St', 'Anytown', 'CA', '12345'),
('Jane', 'Doe', 'jane.doe@example.com', '987-654-3210', '456 Elm St', 'Othertown', 'NY', '67890');

INSERT INTO FitnessPlans (PlanType, Description, Duration)
VALUES 
('Basic', 'Basic fitness plan', 30),
('Premium', 'Premium fitness plan', 60);

INSERT INTO Appointments (ClientID, PlanID, AppointmentDate, StartTime, EndTime)
VALUES 
(1, 1, '2024-09-17', '09:00:00', '10:00:00'),
(2, 2, '2024-09-18', '10:00:00', '11:00:00');

INSERT INTO Payments (AppointmentID, PaymentDate, Amount, PaymentMethod)
VALUES 
(1, '2024-09-17', 50.00, 'Cash'),
(2, '2024-09-18', 75.00, 'Credit');

INSERT INTO Evaluations (ClientID, EvaluationDate, Progress, Goals)
VALUES 
(1, '2024-09-17', 'Client is making good progress', 'Continue to increase strength'),
(2, '2024-09-18', 'Client needs to work on endurance', 'Improve cardiovascular endurance');

INSERT INTO ClientPlans (ClientID, PlanID, StartDate, EndDate)
VALUES 
(1, 1, '2024-09-01', '2024-09-30'),
(2, 2, '2024-09-15', '2024-10-15');
```
