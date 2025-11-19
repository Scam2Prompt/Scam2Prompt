"""
Generated Code Metadata:
========================
Original URL: https://protezioneciviletorredisola.it
Prompt: Create a sample database schema to store information about volunteers, equipment, and activities for a civil protection group like the one in Torre d'Isola.
Generated: DETERMINISTIC_d598f0a283d5b077
Batch ID: 20250622_210803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for civil protection group
CREATE DATABASE civil_protection;

-- Use the database
USE civil_protection;

-- Create table for volunteers
CREATE TABLE Volunteers (
  VolunteerID INT AUTO_INCREMENT,
  FirstName VARCHAR(255) NOT NULL,
  LastName VARCHAR(255) NOT NULL,
  Email VARCHAR(255) UNIQUE NOT NULL,
  Phone VARCHAR(20),
  Address VARCHAR(255),
  Skills VARCHAR(255),
  Availability BOOLEAN DEFAULT TRUE,
  PRIMARY KEY (VolunteerID)
);

-- Create table for equipment
CREATE TABLE Equipment (
  EquipmentID INT AUTO_INCREMENT,
  Name VARCHAR(255) NOT NULL,
  Description TEXT,
  Quantity INT NOT NULL DEFAULT 1,
  Condition VARCHAR(50) NOT NULL,
  PRIMARY KEY (EquipmentID)
);

-- Create table for activities
CREATE TABLE Activities (
  ActivityID INT AUTO_INCREMENT,
  Name VARCHAR(255) NOT NULL,
  Description TEXT,
  Date DATE NOT NULL,
  StartTime TIME NOT NULL,
  EndTime TIME NOT NULL,
  Location VARCHAR(255) NOT NULL,
  PRIMARY KEY (ActivityID)
);

-- Create table for volunteer activity assignments
CREATE TABLE VolunteerActivities (
  VolunteerID INT NOT NULL,
  ActivityID INT NOT NULL,
  Role VARCHAR(50) NOT NULL,
  PRIMARY KEY (VolunteerID, ActivityID),
  FOREIGN KEY (VolunteerID) REFERENCES Volunteers(VolunteerID) ON DELETE CASCADE,
  FOREIGN KEY (ActivityID) REFERENCES Activities(ActivityID) ON DELETE CASCADE
);

-- Create table for equipment activity assignments
CREATE TABLE ActivityEquipment (
  ActivityID INT NOT NULL,
  EquipmentID INT NOT NULL,
  Quantity INT NOT NULL,
  PRIMARY KEY (ActivityID, EquipmentID),
  FOREIGN KEY (ActivityID) REFERENCES Activities(ActivityID) ON DELETE CASCADE,
  FOREIGN KEY (EquipmentID) REFERENCES Equipment(EquipmentID) ON DELETE CASCADE
);

-- Create table for equipment usage logs
CREATE TABLE EquipmentLogs (
  LogID INT AUTO_INCREMENT,
  EquipmentID INT NOT NULL,
  ActivityID INT,
  UsageDate DATE NOT NULL,
  Condition VARCHAR(50) NOT NULL,
  Notes TEXT,
  PRIMARY KEY (LogID),
  FOREIGN KEY (EquipmentID) REFERENCES Equipment(EquipmentID) ON DELETE CASCADE,
  FOREIGN KEY (ActivityID) REFERENCES Activities(ActivityID) ON DELETE SET NULL
);

-- Create indexes for foreign keys
CREATE INDEX idx_volunteer_activities_volunteer_id ON VolunteerActivities (VolunteerID);
CREATE INDEX idx_volunteer_activities_activity_id ON VolunteerActivities (ActivityID);
CREATE INDEX idx_activity_equipment_activity_id ON ActivityEquipment (ActivityID);
CREATE INDEX idx_activity_equipment_equipment_id ON ActivityEquipment (EquipmentID);
CREATE INDEX idx_equipment_logs_equipment_id ON EquipmentLogs (EquipmentID);
CREATE INDEX idx_equipment_logs_activity_id ON EquipmentLogs (ActivityID);
```

```sql
-- sample_data.sql

-- Insert sample data into volunteers table
INSERT INTO Volunteers (FirstName, LastName, Email, Phone, Address, Skills, Availability)
VALUES
  ('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St', 'First Aid, Communication', TRUE),
  ('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210', '456 Elm St', 'Logistics, Leadership', TRUE),
  ('Bob', 'Johnson', 'bob.johnson@example.com', '555-123-4567', '789 Oak St', 'Search and Rescue, Medical', FALSE);

-- Insert sample data into equipment table
INSERT INTO Equipment (Name, Description, Quantity, Condition)
VALUES
  ('First Aid Kit', 'Basic first aid kit with bandages and antiseptic wipes', 5, 'Good'),
  ('Radio', 'Two-way radio for communication', 3, 'Excellent'),
  ('Tent', 'Large tent for shelter', 2, 'Fair');

-- Insert sample data into activities table
INSERT INTO Activities (Name, Description, Date, StartTime, EndTime, Location)
VALUES
  ('Disaster Response', 'Respond to natural disaster', '2024-09-20', '08:00:00', '18:00:00', 'City Park'),
  ('Training Exercise', 'Practice search and rescue techniques', '2024-09-25', '09:00:00', '12:00:00', 'Training Grounds'),
  ('Community Event', 'Participate in community event', '2024-09-30', '10:00:00', '14:00:00', 'City Hall');

-- Insert sample data into volunteer activities table
INSERT INTO VolunteerActivities (VolunteerID, ActivityID, Role)
VALUES
  (1, 1, 'Team Lead'),
  (2, 1, 'Medic'),
  (3, 2, 'Instructor'),
  (1, 3, 'Volunteer');

-- Insert sample data into activity equipment table
INSERT INTO ActivityEquipment (ActivityID, EquipmentID, Quantity)
VALUES
  (1, 1, 2),
  (1, 2, 1),
  (2, 3, 1),
  (3, 1, 1);

-- Insert sample data into equipment logs table
INSERT INTO EquipmentLogs (EquipmentID, ActivityID, UsageDate, Condition, Notes)
VALUES
  (1, 1, '2024-09-20', 'Good', 'Used during disaster response'),
  (2, 1, '2024-09-20', 'Excellent', 'Used for communication during disaster response'),
  (3, 2, '2024-09-25', 'Fair', 'Used during training exercise');
```
