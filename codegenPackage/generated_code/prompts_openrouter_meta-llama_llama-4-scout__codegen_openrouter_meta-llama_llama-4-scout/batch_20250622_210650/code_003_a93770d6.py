"""
Generated Code Metadata:
========================
Original URL: https://atvisaabogados.com
Prompt: "Design a simple database schema for storing client information, visa application types, and appointment schedules for an immigration law firm like AT Visa Abogados."
Generated: DETERMINISTIC_a93770d601c394d5
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for immigration law firm
CREATE DATABASE immigration_law_firm;

-- Use the database
USE immigration_law_firm;

-- Create table for clients
CREATE TABLE Clients (
  ClientID INT AUTO_INCREMENT,
  FirstName VARCHAR(255) NOT NULL,
  LastName VARCHAR(255) NOT NULL,
  Email VARCHAR(255) UNIQUE NOT NULL,
  Phone VARCHAR(20),
  Address VARCHAR(255),
  CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (ClientID)
);

-- Create table for visa application types
CREATE TABLE VisaApplicationTypes (
  ApplicationTypeID INT AUTO_INCREMENT,
  ApplicationType VARCHAR(255) NOT NULL,
  Description TEXT,
  CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (ApplicationTypeID)
);

-- Create table for appointment schedules
CREATE TABLE AppointmentSchedules (
  AppointmentID INT AUTO_INCREMENT,
  ClientID INT NOT NULL,
  ApplicationTypeID INT NOT NULL,
  AppointmentDate DATE NOT NULL,
  AppointmentTime TIME NOT NULL,
  Location VARCHAR(255) NOT NULL,
  Status VARCHAR(50) NOT NULL DEFAULT 'Scheduled',
  CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (AppointmentID),
  FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE,
  FOREIGN KEY (ApplicationTypeID) REFERENCES VisaApplicationTypes(ApplicationTypeID) ON DELETE CASCADE
);

-- Create table for appointment reminders
CREATE TABLE AppointmentReminders (
  ReminderID INT AUTO_INCREMENT,
  AppointmentID INT NOT NULL,
  ReminderDate DATE NOT NULL,
  ReminderTime TIME NOT NULL,
  Sent BOOLEAN NOT NULL DEFAULT FALSE,
  CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (ReminderID),
  FOREIGN KEY (AppointmentID) REFERENCES AppointmentSchedules(AppointmentID) ON DELETE CASCADE
);

-- Create table for client documents
CREATE TABLE ClientDocuments (
  DocumentID INT AUTO_INCREMENT,
  ClientID INT NOT NULL,
  DocumentType VARCHAR(255) NOT NULL,
  DocumentFile BLOB NOT NULL,
  UploadDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (DocumentID),
  FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE
);

-- Create indexes for faster queries
CREATE INDEX idx_ClientID ON AppointmentSchedules(ClientID);
CREATE INDEX idx_ApplicationTypeID ON AppointmentSchedules(ApplicationTypeID);
CREATE INDEX idx_AppointmentID ON AppointmentReminders(AppointmentID);
```

```sql
-- sample_data.sql

-- Insert sample data into Clients table
INSERT INTO Clients (FirstName, LastName, Email, Phone, Address)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St'),
('Jane', 'Doe', 'jane.doe@example.com', '987-654-3210', '456 Elm St');

-- Insert sample data into VisaApplicationTypes table
INSERT INTO VisaApplicationTypes (ApplicationType, Description)
VALUES 
('Work Visa', 'Application for work visa'),
('Student Visa', 'Application for student visa'),
('Tourist Visa', 'Application for tourist visa');

-- Insert sample data into AppointmentSchedules table
INSERT INTO AppointmentSchedules (ClientID, ApplicationTypeID, AppointmentDate, AppointmentTime, Location)
VALUES 
(1, 1, '2024-09-20', '10:00:00', 'New York'),
(2, 2, '2024-09-25', '11:00:00', 'Los Angeles');

-- Insert sample data into AppointmentReminders table
INSERT INTO AppointmentReminders (AppointmentID, ReminderDate, ReminderTime)
VALUES 
(1, '2024-09-19', '09:00:00'),
(2, '2024-09-24', '10:00:00');

-- Insert sample data into ClientDocuments table
INSERT INTO ClientDocuments (ClientID, DocumentType, DocumentFile)
VALUES 
(1, 'Passport', LOAD_FILE('path_to_passport.pdf')),
(2, 'ID Card', LOAD_FILE('path_to_id_card.pdf'));
```
