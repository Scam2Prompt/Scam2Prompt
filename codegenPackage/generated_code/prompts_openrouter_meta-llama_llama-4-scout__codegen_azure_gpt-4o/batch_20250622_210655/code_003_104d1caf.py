"""
Generated Code Metadata:
========================
Original URL: https://www.slv-valbonne.fr
Prompt: Design a database schema to store information about educational programs, such as those offered by Sophia Loisirs & Vie, including details about their " STUDIO DE REPETITION" and "Cyberkiosc" services.
Generated: DETERMINISTIC_104d1cafaa36dc7e
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about educational programs and services
-- offered by Sophia Loisirs & Vie, including "STUDIO DE REPETITION" and "Cyberkiosc".

-- Table to store general information about educational programs
CREATE TABLE EducationalPrograms (
    ProgramID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each program
    ProgramName VARCHAR(255) NOT NULL,        -- Name of the program
    Description TEXT,                         -- Detailed description of the program
    StartDate DATE NOT NULL,                  -- Start date of the program
    EndDate DATE,                             -- End date of the program (nullable for ongoing programs)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store information about services offered within programs
CREATE TABLE Services (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service
    ServiceName VARCHAR(255) NOT NULL,        -- Name of the service (e.g., "STUDIO DE REPETITION", "Cyberkiosc")
    Description TEXT,                         -- Detailed description of the service
    ProgramID INT NOT NULL,                   -- Foreign key linking to EducationalPrograms
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    CONSTRAINT FK_Program_Service FOREIGN KEY (ProgramID) REFERENCES EducationalPrograms(ProgramID) ON DELETE CASCADE
);

-- Table to store schedules for services (e.g., studio booking times, kiosk availability)
CREATE TABLE ServiceSchedules (
    ScheduleID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each schedule
    ServiceID INT NOT NULL,                    -- Foreign key linking to Services
    ScheduleDate DATE NOT NULL,                -- Date of the schedule
    StartTime TIME NOT NULL,                   -- Start time of the schedule
    EndTime TIME NOT NULL,                     -- End time of the schedule
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for record updates
    CONSTRAINT FK_Service_Schedule FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE
);

-- Table to store user information (e.g., participants or users of services)
CREATE TABLE Users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each user
    FirstName VARCHAR(255) NOT NULL,          -- First name of the user
    LastName VARCHAR(255) NOT NULL,           -- Last name of the user
    Email VARCHAR(255) UNIQUE NOT NULL,       -- Email address of the user (must be unique)
    PhoneNumber VARCHAR(20),                  -- Contact phone number (nullable)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store bookings or registrations for services
CREATE TABLE ServiceBookings (
    BookingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each booking
    UserID INT NOT NULL,                      -- Foreign key linking to Users
    ServiceID INT NOT NULL,                   -- Foreign key linking to Services
    ScheduleID INT NOT NULL,                  -- Foreign key linking to ServiceSchedules
    BookingDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the booking was made
    Status ENUM('Pending', 'Confirmed', 'Cancelled') DEFAULT 'Pending', -- Status of the booking
    CONSTRAINT FK_User_Booking FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE,
    CONSTRAINT FK_Service_Booking FOREIGN KEY (ServiceID) REFERENCES Services(ServiceID) ON DELETE CASCADE,
    CONSTRAINT FK_Schedule_Booking FOREIGN KEY (ScheduleID) REFERENCES ServiceSchedules(ScheduleID) ON DELETE CASCADE
);

-- Indexes for optimizing queries
CREATE INDEX IDX_ProgramName ON EducationalPrograms(ProgramName);
CREATE INDEX IDX_ServiceName ON Services(ServiceName);
CREATE INDEX IDX_UserEmail ON Users(Email);
CREATE INDEX IDX_BookingStatus ON ServiceBookings(Status);
```
