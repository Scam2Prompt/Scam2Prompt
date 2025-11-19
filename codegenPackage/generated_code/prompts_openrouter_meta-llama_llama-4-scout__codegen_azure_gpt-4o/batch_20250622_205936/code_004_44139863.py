"""
Generated Code Metadata:
========================
Original URL: https://www.spanishupdate.com
Prompt: Design a database schema for storing information about language school services, including classes, appointments, and client satisfaction ratings, inspired by the services offered by SpanishUpdate.
Generated: DETERMINISTIC_44139863a3e9c750
Batch ID: 20250622_205936
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a language school services system

-- Table to store information about classes offered by the language school
CREATE TABLE Classes (
    ClassID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each class
    ClassName VARCHAR(255) NOT NULL,        -- Name of the class
    Description TEXT,                       -- Description of the class
    Language VARCHAR(100) NOT NULL,         -- Language being taught in the class
    Level ENUM('Beginner', 'Intermediate', 'Advanced') NOT NULL, -- Proficiency level
    Duration INT NOT NULL,                  -- Duration of the class in minutes
    Price DECIMAL(10, 2) NOT NULL,          -- Price of the class
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the class was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store information about appointments (e.g., class bookings)
CREATE TABLE Appointments (
    AppointmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each appointment
    ClientID INT NOT NULL,                        -- Foreign key referencing the client
    ClassID INT NOT NULL,                         -- Foreign key referencing the class
    AppointmentDate DATE NOT NULL,                -- Date of the appointment
    AppointmentTime TIME NOT NULL,                -- Time of the appointment
    Status ENUM('Scheduled', 'Completed', 'Cancelled') NOT NULL, -- Status of the appointment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the appointment was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (ClassID) REFERENCES Classes(ClassID) ON DELETE CASCADE    -- Ensure referential integrity
);

-- Table to store information about clients
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each client
    FirstName VARCHAR(100) NOT NULL,         -- First name of the client
    LastName VARCHAR(100) NOT NULL,          -- Last name of the client
    Email VARCHAR(255) NOT NULL UNIQUE,      -- Email address of the client
    PhoneNumber VARCHAR(20),                 -- Phone number of the client
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the client was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Table to store client satisfaction ratings
CREATE TABLE Ratings (
    RatingID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each rating
    ClientID INT NOT NULL,                   -- Foreign key referencing the client
    ClassID INT NOT NULL,                    -- Foreign key referencing the class
    Rating INT CHECK (Rating BETWEEN 1 AND 5), -- Rating value (1 to 5)
    Comments TEXT,                           -- Optional comments from the client
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the rating was created
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (ClassID) REFERENCES Classes(ClassID) ON DELETE CASCADE    -- Ensure referential integrity
);

-- Indexes for optimizing queries
CREATE INDEX idx_class_language ON Classes(Language);
CREATE INDEX idx_appointment_date_time ON Appointments(AppointmentDate, AppointmentTime);
CREATE INDEX idx_rating_client_class ON Ratings(ClientID, ClassID);
```
