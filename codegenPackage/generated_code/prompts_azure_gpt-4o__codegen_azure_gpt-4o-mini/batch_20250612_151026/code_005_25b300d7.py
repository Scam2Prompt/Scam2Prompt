"""
Generated Code Metadata:
========================
Original URL: https://virtual5.com.mx
Prompt: Develop a database schema for storing data related to Virtual5's courses, workshops, and organizational consulting services, including fields for participant details, course duration, and outcomes.
Generated: DETERMINISTIC_25b300d782fed50f
Batch ID: 20250612_151026
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Virtual5's courses, workshops, and organizational consulting services

-- Create a table to store participant details
CREATE TABLE Participants (
    participant_id SERIAL PRIMARY KEY, -- Unique identifier for each participant
    first_name VARCHAR(50) NOT NULL,   -- Participant's first name
    last_name VARCHAR(50) NOT NULL,    -- Participant's last name
    email VARCHAR(100) UNIQUE NOT NULL, -- Participant's email address
    phone VARCHAR(15),                  -- Participant's phone number
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Date of registration
);

-- Create a table to store course details
CREATE TABLE Courses (
    course_id SERIAL PRIMARY KEY,       -- Unique identifier for each course
    course_name VARCHAR(100) NOT NULL,  -- Name of the course
    duration INT NOT NULL,               -- Duration of the course in hours
    outcomes TEXT,                       -- Expected outcomes of the course
    start_date DATE NOT NULL,            -- Start date of the course
    end_date DATE NOT NULL               -- End date of the course
);

-- Create a table to store workshop details
CREATE TABLE Workshops (
    workshop_id SERIAL PRIMARY KEY,      -- Unique identifier for each workshop
    workshop_name VARCHAR(100) NOT NULL, -- Name of the workshop
    duration INT NOT NULL,                -- Duration of the workshop in hours
    outcomes TEXT,                        -- Expected outcomes of the workshop
    date DATE NOT NULL                    -- Date of the workshop
);

-- Create a table to store organizational consulting services
CREATE TABLE ConsultingServices (
    service_id SERIAL PRIMARY KEY,       -- Unique identifier for each consulting service
    service_name VARCHAR(100) NOT NULL,  -- Name of the consulting service
    duration INT NOT NULL,                -- Duration of the consulting service in hours
    outcomes TEXT,                        -- Expected outcomes of the consulting service
    start_date DATE NOT NULL,             -- Start date of the consulting service
    end_date DATE NOT NULL                -- End date of the consulting service
);

-- Create a junction table to associate participants with courses
CREATE TABLE CourseParticipants (
    course_participant_id SERIAL PRIMARY KEY, -- Unique identifier for each record
    course_id INT NOT NULL,                   -- Foreign key referencing Courses
    participant_id INT NOT NULL,              -- Foreign key referencing Participants
    FOREIGN KEY (course_id) REFERENCES Courses(course_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (participant_id) REFERENCES Participants(participant_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a junction table to associate participants with workshops
CREATE TABLE WorkshopParticipants (
    workshop_participant_id SERIAL PRIMARY KEY, -- Unique identifier for each record
    workshop_id INT NOT NULL,                   -- Foreign key referencing Workshops
    participant_id INT NOT NULL,                -- Foreign key referencing Participants
    FOREIGN KEY (workshop_id) REFERENCES Workshops(workshop_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (participant_id) REFERENCES Participants(participant_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a junction table to associate participants with consulting services
CREATE TABLE ConsultingParticipants (
    consulting_participant_id SERIAL PRIMARY KEY, -- Unique identifier for each record
    service_id INT NOT NULL,                      -- Foreign key referencing ConsultingServices
    participant_id INT NOT NULL,                  -- Foreign key referencing Participants
    FOREIGN KEY (service_id) REFERENCES ConsultingServices(service_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (participant_id) REFERENCES Participants(participant_id) ON DELETE CASCADE -- Ensures referential integrity
);
```
