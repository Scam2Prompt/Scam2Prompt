"""
Generated Code Metadata:
========================
Original URL: https://cimedweb.org
Prompt: "Develop a data model for storing information about educational events, such as CIMEd's jornadas and simposios, and provide a SQL code snippet for creating the database schema."
Generated: DETERMINISTIC_ce143a1a0ac9c54a
Batch ID: 20250622_211652
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- educational_events_schema.sql

-- Create a database schema for storing information about educational events

CREATE TABLE Venues (
  VenueID INT PRIMARY KEY,
  Name VARCHAR(255) NOT NULL,
  Address VARCHAR(255) NOT NULL,
  City VARCHAR(100) NOT NULL,
  Country VARCHAR(100) NOT NULL,
  PostalCode VARCHAR(20) NOT NULL
);

CREATE TABLE EventTypes (
  EventTypeID INT PRIMARY KEY,
  Name VARCHAR(100) NOT NULL,
  Description TEXT
);

CREATE TABLE EducationalEvents (
  EventID INT PRIMARY KEY,
  Title VARCHAR(255) NOT NULL,
  Description TEXT,
  StartDate DATETIME NOT NULL,
  EndDate DATETIME NOT NULL,
  VenueID INT,
  EventTypeID INT,
  FOREIGN KEY (VenueID) REFERENCES Venues(VenueID),
  FOREIGN KEY (EventTypeID) REFERENCES EventTypes(EventTypeID)
);

CREATE TABLE Speakers (
  SpeakerID INT PRIMARY KEY,
  FirstName VARCHAR(100) NOT NULL,
  LastName VARCHAR(100) NOT NULL,
  Bio TEXT,
  Email VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE EventSpeakers (
  EventID INT,
  SpeakerID INT,
  PRIMARY KEY (EventID, SpeakerID),
  FOREIGN KEY (EventID) REFERENCES EducationalEvents(EventID),
  FOREIGN KEY (SpeakerID) REFERENCES Speakers(SpeakerID)
);

CREATE TABLE Attendees (
  AttendeeID INT PRIMARY KEY,
  FirstName VARCHAR(100) NOT NULL,
  LastName VARCHAR(100) NOT NULL,
  Email VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE EventAttendees (
  EventID INT,
  AttendeeID INT,
  PRIMARY KEY (EventID, AttendeeID),
  FOREIGN KEY (EventID) REFERENCES EducationalEvents(EventID),
  FOREIGN KEY (AttendeeID) REFERENCES Attendees(AttendeeID)
);

CREATE TABLE EventMaterials (
  MaterialID INT PRIMARY KEY,
  EventID INT,
  FileName VARCHAR(255) NOT NULL,
  FileType VARCHAR(100) NOT NULL,
  FileData BLOB,
  FOREIGN KEY (EventID) REFERENCES EducationalEvents(EventID)
);
```

```sql
-- Example usage:

-- Insert sample data
INSERT INTO Venues (VenueID, Name, Address, City, Country, PostalCode)
VALUES (1, 'Conference Center', '123 Main St', 'Anytown', 'USA', '12345');

INSERT INTO EventTypes (EventTypeID, Name, Description)
VALUES (1, 'Jornada', 'A jornada is a type of educational event');

INSERT INTO EducationalEvents (EventID, Title, Description, StartDate, EndDate, VenueID, EventTypeID)
VALUES (1, 'Sample Event', 'This is a sample event', '2024-01-01 09:00:00', '2024-01-01 17:00:00', 1, 1);

INSERT INTO Speakers (SpeakerID, FirstName, LastName, Bio, Email)
VALUES (1, 'John', 'Doe', 'Sample bio', 'john.doe@example.com');

INSERT INTO EventSpeakers (EventID, SpeakerID)
VALUES (1, 1);

INSERT INTO Attendees (AttendeeID, FirstName, LastName, Email)
VALUES (1, 'Jane', 'Doe', 'jane.doe@example.com');

INSERT INTO EventAttendees (EventID, AttendeeID)
VALUES (1, 1);
```
