"""
Generated Code Metadata:
========================
Original URL: https://equilibri-bio.la-guarida.com.ar
Prompt: "Generate a sample database schema to store information about therapy sessions, including treatment types, therapist schedules, and client bookings, inspired by the services provided by Equilibri-Bio."
Generated: DETERMINISTIC_25c91c5b37dc72eb
Batch ID: 20250622_212318
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for therapy sessions, treatment types, therapist schedules, and client bookings

-- Table to store information about treatment types
CREATE TABLE TreatmentTypes (
    TreatmentID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each treatment type
    Name VARCHAR(100) NOT NULL,                 -- Name of the treatment (e.g., "Cognitive Behavioral Therapy")
    Description TEXT,                           -- Detailed description of the treatment
    DurationMinutes INT NOT NULL,              -- Duration of the treatment in minutes
    Price DECIMAL(10, 2) NOT NULL,              -- Price of the treatment
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the record was last updated
);

-- Table to store information about therapists
CREATE TABLE Therapists (
    TherapistID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each therapist
    FirstName VARCHAR(50) NOT NULL,             -- First name of the therapist
    LastName VARCHAR(50) NOT NULL,              -- Last name of the therapist
    Email VARCHAR(100) UNIQUE NOT NULL,         -- Email address of the therapist
    PhoneNumber VARCHAR(15),                    -- Contact phone number
    Specialization VARCHAR(100),                -- Therapist's area of specialization
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the record was last updated
);

-- Table to store therapist schedules
CREATE TABLE TherapistSchedules (
    ScheduleID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each schedule entry
    TherapistID INT NOT NULL,                   -- Foreign key referencing Therapists table
    DayOfWeek ENUM('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday') NOT NULL, -- Day of the week
    StartTime TIME NOT NULL,                    -- Start time of the schedule
    EndTime TIME NOT NULL,                      -- End time of the schedule
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the record was last updated
    FOREIGN KEY (TherapistID) REFERENCES Therapists(TherapistID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table to store client information
CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each client
    FirstName VARCHAR(50) NOT NULL,             -- First name of the client
    LastName VARCHAR(50) NOT NULL,              -- Last name of the client
    Email VARCHAR(100) UNIQUE NOT NULL,         -- Email address of the client
    PhoneNumber VARCHAR(15),                    -- Contact phone number
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the record was last updated
);

-- Table to store client bookings
CREATE TABLE ClientBookings (
    BookingID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each booking
    ClientID INT NOT NULL,                      -- Foreign key referencing Clients table
    TherapistID INT NOT NULL,                   -- Foreign key referencing Therapists table
    TreatmentID INT NOT NULL,                   -- Foreign key referencing TreatmentTypes table
    BookingDate DATE NOT NULL,                  -- Date of the booking
    StartTime TIME NOT NULL,                    -- Start time of the session
    EndTime TIME NOT NULL,                      -- End time of the session
    Status ENUM('Pending', 'Confirmed', 'Cancelled') DEFAULT 'Pending', -- Status of the booking
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the record was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the record was last updated
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (TherapistID) REFERENCES Therapists(TherapistID) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (TreatmentID) REFERENCES TreatmentTypes(TreatmentID) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for optimizing queries
CREATE INDEX idx_therapist_schedule ON TherapistSchedules (TherapistID, DayOfWeek);
CREATE INDEX idx_client_booking ON ClientBookings (ClientID, BookingDate);
```
