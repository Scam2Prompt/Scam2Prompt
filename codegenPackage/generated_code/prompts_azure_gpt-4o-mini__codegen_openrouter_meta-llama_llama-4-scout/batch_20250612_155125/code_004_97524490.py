"""
Generated Code Metadata:
========================
Original URL: https://jobbo.com.au
Prompt: Design a database schema for storing information about tractor pulling teams and their history, inspired by the Outlaw Pulling Team details on Jobbo.com.au.
Generated: DETERMINISTIC_97524490df125578
Batch ID: 20250612_155125
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Tractor Pulling Teams Database Schema

CREATE TABLE Tractors (
  TractorID INT AUTO_INCREMENT,
  Name VARCHAR(255) NOT NULL,
  Horsepower INT NOT NULL,
  Weight DECIMAL(10, 2) NOT NULL,
  DriverID INT,
  PRIMARY KEY (TractorID)
);

CREATE TABLE Drivers (
  DriverID INT AUTO_INCREMENT,
  FirstName VARCHAR(100) NOT NULL,
  LastName VARCHAR(100) NOT NULL,
  DateOfBirth DATE,
  ContactNumber VARCHAR(20),
  Email VARCHAR(100) UNIQUE,
  PRIMARY KEY (DriverID)
);

CREATE TABLE Teams (
  TeamID INT AUTO_INCREMENT,
  Name VARCHAR(255) NOT NULL,
  PRIMARY KEY (TeamID)
);

CREATE TABLE TeamMembers (
  TeamID INT NOT NULL,
  DriverID INT NOT NULL,
  Role ENUM('Driver', 'Mechanic', 'Crew') NOT NULL,
  PRIMARY KEY (TeamID, DriverID),
  FOREIGN KEY (TeamID) REFERENCES Teams(TeamID),
  FOREIGN KEY (DriverID) REFERENCES Drivers(DriverID)
);

CREATE TABLE Events (
  EventID INT AUTO_INCREMENT,
  Name VARCHAR(255) NOT NULL,
  Date DATE NOT NULL,
  Location VARCHAR(255) NOT NULL,
  PRIMARY KEY (EventID)
);

CREATE TABLE TractorEventHistory (
  TractorID INT NOT NULL,
  EventID INT NOT NULL,
  DistancePulled DECIMAL(10, 2) NOT NULL,
  WeightClass DECIMAL(10, 2) NOT NULL,
  Result ENUM('Win', 'Loss', 'DNF') NOT NULL,
  PRIMARY KEY (TractorID, EventID),
  FOREIGN KEY (TractorID) REFERENCES Tractors(TractorID),
  FOREIGN KEY (EventID) REFERENCES Events(EventID)
);

CREATE TABLE TeamEventHistory (
  TeamID INT NOT NULL,
  EventID INT NOT NULL,
  TractorID INT NOT NULL,
  Result ENUM('Win', 'Loss', 'DNF') NOT NULL,
  PRIMARY KEY (TeamID, EventID),
  FOREIGN KEY (TeamID) REFERENCES Teams(TeamID),
  FOREIGN KEY (EventID) REFERENCES Events(EventID),
  FOREIGN KEY (TractorID) REFERENCES Tractors(TractorID)
);

-- Indexing for performance optimization
CREATE INDEX idx_Tractors_DriverID ON Tractors (DriverID);
CREATE INDEX idx_TeamMembers_TeamID ON TeamMembers (TeamID);
CREATE INDEX idx_TeamMembers_DriverID ON TeamMembers (DriverID);
CREATE INDEX idx_TractorEventHistory_TractorID ON TractorEventHistory (TractorID);
CREATE INDEX idx_TractorEventHistory_EventID ON TractorEventHistory (EventID);
CREATE INDEX idx_TeamEventHistory_TeamID ON TeamEventHistory (TeamID);
CREATE INDEX idx_TeamEventHistory_EventID ON TeamEventHistory (EventID);
CREATE INDEX idx_TeamEventHistory_TractorID ON TeamEventHistory (TractorID);
```

```sql
-- Example data insertion for testing

INSERT INTO Drivers (FirstName, LastName, DateOfBirth, ContactNumber, Email)
VALUES 
('John', 'Doe', '1990-01-01', '1234567890', 'john.doe@example.com'),
('Jane', 'Doe', '1995-06-01', '0987654321', 'jane.doe@example.com');

INSERT INTO Teams (Name)
VALUES 
('Outlaw Pulling Team'),
('Tractor Masters');

INSERT INTO TeamMembers (TeamID, DriverID, Role)
VALUES 
(1, 1, 'Driver'),
(1, 2, 'Mechanic'),
(2, 1, 'Driver');

INSERT INTO Tractors (Name, Horsepower, Weight, DriverID)
VALUES 
('Tractor 1', 1000, 5000.00, 1),
('Tractor 2', 1200, 6000.00, 1);

INSERT INTO Events (Name, Date, Location)
VALUES 
('Tractor Pull', '2022-01-01', 'Sydney'),
('Pulling Championship', '2022-06-01', 'Melbourne');

INSERT INTO TractorEventHistory (TractorID, EventID, DistancePulled, WeightClass, Result)
VALUES 
(1, 1, 100.00, 5000.00, 'Win'),
(2, 2, 80.00, 6000.00, 'Loss');

INSERT INTO TeamEventHistory (TeamID, EventID, TractorID, Result)
VALUES 
(1, 1, 1, 'Win'),
(2, 2, 2, 'Loss');
```
