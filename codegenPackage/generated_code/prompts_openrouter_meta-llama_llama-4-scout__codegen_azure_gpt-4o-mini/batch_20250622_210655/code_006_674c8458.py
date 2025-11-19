"""
Generated Code Metadata:
========================
Original URL: https://www.al-aanqua.com
Prompt: Design a database schema for storing information about art and cultural events in the Arab world, inspired by the website's content.
Generated: DETERMINISTIC_674c84584a6b2c73
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about art and cultural events in the Arab world

-- Create a table for storing information about events
CREATE TABLE Events (
    EventID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each event
    Title VARCHAR(255) NOT NULL,            -- Title of the event
    Description TEXT,                        -- Detailed description of the event
    EventDate DATETIME NOT NULL,            -- Date and time of the event
    Location VARCHAR(255) NOT NULL,         -- Location where the event is held
    OrganizerID INT,                         -- Foreign key referencing the organizer
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the event was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the event was last updated
    FOREIGN KEY (OrganizerID) REFERENCES Organizers(OrganizerID) -- Ensure referential integrity
);

-- Create a table for storing information about organizers
CREATE TABLE Organizers (
    OrganizerID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each organizer
    Name VARCHAR(255) NOT NULL,                 -- Name of the organizer
    ContactEmail VARCHAR(255),                   -- Contact email for the organizer
    PhoneNumber VARCHAR(20),                     -- Phone number for the organizer
    Website VARCHAR(255)                         -- Website of the organizer
);

-- Create a table for storing information about attendees
CREATE TABLE Attendees (
    AttendeeID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each attendee
    Name VARCHAR(255) NOT NULL,                -- Name of the attendee
    Email VARCHAR(255) NOT NULL UNIQUE,        -- Email of the attendee (must be unique)
    PhoneNumber VARCHAR(20),                   -- Phone number of the attendee
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the attendee was created
);

-- Create a table for storing registrations for events
CREATE TABLE EventRegistrations (
    RegistrationID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each registration
    EventID INT NOT NULL,                          -- Foreign key referencing the event
    AttendeeID INT NOT NULL,                       -- Foreign key referencing the attendee
    RegistrationDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the registration was made
    FOREIGN KEY (EventID) REFERENCES Events(EventID), -- Ensure referential integrity
    FOREIGN KEY (AttendeeID) REFERENCES Attendees(AttendeeID) -- Ensure referential integrity
);

-- Create a table for storing categories of events
CREATE TABLE EventCategories (
    CategoryID INT PRIMARY KEY AUTO_INCREMENT, -- Unique identifier for each category
    CategoryName VARCHAR(100) NOT NULL UNIQUE, -- Name of the category (must be unique)
    Description TEXT                            -- Description of the category
);

-- Create a junction table for many-to-many relationship between events and categories
CREATE TABLE EventCategoryMapping (
    EventID INT NOT NULL,                       -- Foreign key referencing the event
    CategoryID INT NOT NULL,                    -- Foreign key referencing the category
    PRIMARY KEY (EventID, CategoryID),         -- Composite primary key
    FOREIGN KEY (EventID) REFERENCES Events(EventID), -- Ensure referential integrity
    FOREIGN KEY (CategoryID) REFERENCES EventCategories(CategoryID) -- Ensure referential integrity
);

-- Create a table for storing feedback on events
CREATE TABLE EventFeedback (
    FeedbackID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each feedback entry
    EventID INT NOT NULL,                       -- Foreign key referencing the event
    AttendeeID INT NOT NULL,                    -- Foreign key referencing the attendee
    Rating INT CHECK (Rating BETWEEN 1 AND 5), -- Rating given by the attendee (1 to 5)
    Comments TEXT,                              -- Comments provided by the attendee
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the feedback was created
    FOREIGN KEY (EventID) REFERENCES Events(EventID), -- Ensure referential integrity
    FOREIGN KEY (AttendeeID) REFERENCES Attendees(AttendeeID) -- Ensure referential integrity
);
```
