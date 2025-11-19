"""
Generated Code Metadata:
========================
Original URL: https://bitcoinxcash.com
Prompt: Design a database schema to store event-related data, including event details, attendee information, and vendor contracts, for an event planning company in Japan.
Generated: DETERMINISTIC_9617666ac1f3fc60
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the event planning company
CREATE DATABASE EventPlanning;

-- Use the EventPlanning database
USE EventPlanning;

-- Create a table to store event details
CREATE TABLE Events (
    EventID INT AUTO_INCREMENT,
    EventName VARCHAR(255) NOT NULL,
    EventDate DATE NOT NULL,
    EventTime TIME NOT NULL,
    EventLocation VARCHAR(255) NOT NULL,
    EventType VARCHAR(100) NOT NULL,
    EventDescription TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (EventID)
);

-- Create a table to store attendee information
CREATE TABLE Attendees (
    AttendeeID INT AUTO_INCREMENT,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (AttendeeID)
);

-- Create a table to store event attendee relationships
CREATE TABLE EventAttendees (
    EventID INT NOT NULL,
    AttendeeID INT NOT NULL,
    TicketType VARCHAR(100) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (EventID, AttendeeID),
    FOREIGN KEY (EventID) REFERENCES Events(EventID) ON DELETE CASCADE,
    FOREIGN KEY (AttendeeID) REFERENCES Attendees(AttendeeID) ON DELETE CASCADE
);

-- Create a table to store vendor information
CREATE TABLE Vendors (
    VendorID INT AUTO_INCREMENT,
    VendorName VARCHAR(255) NOT NULL,
    VendorType VARCHAR(100) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    Phone VARCHAR(20),
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (VendorID)
);

-- Create a table to store vendor contracts
CREATE TABLE VendorContracts (
    ContractID INT AUTO_INCREMENT,
    EventID INT NOT NULL,
    VendorID INT NOT NULL,
    ContractDate DATE NOT NULL,
    ContractAmount DECIMAL(10, 2) NOT NULL,
    ContractDetails TEXT,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (ContractID),
    FOREIGN KEY (EventID) REFERENCES Events(EventID) ON DELETE CASCADE,
    FOREIGN KEY (VendorID) REFERENCES Vendors(VendorID) ON DELETE CASCADE
);

-- Create a table to store event vendors
CREATE TABLE EventVendors (
    EventID INT NOT NULL,
    VendorID INT NOT NULL,
    VendorService VARCHAR(100) NOT NULL,
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (EventID, VendorID),
    FOREIGN KEY (EventID) REFERENCES Events(EventID) ON DELETE CASCADE,
    FOREIGN KEY (VendorID) REFERENCES Vendors(VendorID) ON DELETE CASCADE
);

-- Create indexes on foreign key columns
CREATE INDEX idx_EventAttendees_EventID ON EventAttendees(EventID);
CREATE INDEX idx_EventAttendees_AttendeeID ON EventAttendees(AttendeeID);
CREATE INDEX idx_VendorContracts_EventID ON VendorContracts(EventID);
CREATE INDEX idx_VendorContracts_VendorID ON VendorContracts(VendorID);
CREATE INDEX idx_EventVendors_EventID ON EventVendors(EventID);
CREATE INDEX idx_EventVendors_VendorID ON EventVendors(VendorID);

-- Insert sample data
INSERT INTO Events (EventName, EventDate, EventTime, EventLocation, EventType, EventDescription)
VALUES 
('Wedding Reception', '2024-09-20', '14:00:00', 'Tokyo', 'Wedding', 'Reception for 100 guests'),
('Conference', '2024-10-15', '09:00:00', 'Osaka', 'Conference', '3-day conference for 500 attendees');

INSERT INTO Attendees (FirstName, LastName, Email, Phone)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890'),
('Jane', 'Smith', 'jane.smith@example.com', '098-765-4321');

INSERT INTO EventAttendees (EventID, AttendeeID, TicketType)
VALUES 
(1, 1, 'VIP'),
(1, 2, 'Standard'),
(2, 1, 'Speaker');

INSERT INTO Vendors (VendorName, VendorType, Email, Phone)
VALUES 
('Catering Inc.', 'Catering', 'catering@example.com', '111-222-3333'),
('Audio Visual Co.', 'AV', 'av@example.com', '444-555-6666');

INSERT INTO VendorContracts (EventID, VendorID, ContractDate, ContractAmount, ContractDetails)
VALUES 
(1, 1, '2024-08-01', 5000.00, 'Catering for 100 guests'),
(1, 2, '2024-08-15', 2000.00, 'AV equipment rental');

INSERT INTO EventVendors (EventID, VendorID, VendorService)
VALUES 
(1, 1, 'Food and Beverage'),
(1, 2, 'Sound and Lighting');
```
