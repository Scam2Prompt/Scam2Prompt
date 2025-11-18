"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://skifoundation.org
Prompt: Recommend a database schema design for managing SKI Foundation's "Magang Pekerja Profesional" program, including tables for participants, mentors, and internship projects.
Generated: DETERMINISTIC_55e01cf17f1eb462
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing SKI Foundation's "Magang Pekerja Profesional" program

-- Create a table for participants
CREATE TABLE Participants (
    participant_id SERIAL PRIMARY KEY, -- Unique identifier for each participant
    first_name VARCHAR(50) NOT NULL,   -- First name of the participant
    last_name VARCHAR(50) NOT NULL,    -- Last name of the participant
    email VARCHAR(100) UNIQUE NOT NULL, -- Email address of the participant
    phone VARCHAR(20),                  -- Phone number of the participant
    date_of_birth DATE NOT NULL,        -- Date of birth of the participant
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the participant is added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the participant is updated
);

-- Create a table for mentors
CREATE TABLE Mentors (
    mentor_id SERIAL PRIMARY KEY,       -- Unique identifier for each mentor
    first_name VARCHAR(50) NOT NULL,   -- First name of the mentor
    last_name VARCHAR(50) NOT NULL,    -- Last name of the mentor
    email VARCHAR(100) UNIQUE NOT NULL, -- Email address of the mentor
    phone VARCHAR(20),                  -- Phone number of the mentor
    expertise VARCHAR(100),             -- Area of expertise of the mentor
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the mentor is added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the mentor is updated
);

-- Create a table for internship projects
CREATE TABLE InternshipProjects (
    project_id SERIAL PRIMARY KEY,      -- Unique identifier for each project
    title VARCHAR(100) NOT NULL,        -- Title of the internship project
    description TEXT NOT NULL,          -- Description of the internship project
    start_date DATE NOT NULL,           -- Start date of the project
    end_date DATE NOT NULL,             -- End date of the project
    mentor_id INT REFERENCES Mentors(mentor_id) ON DELETE SET NULL, -- Reference to mentor
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the project is added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the project is updated
);

-- Create a table for participant internships
CREATE TABLE ParticipantInternships (
    internship_id SERIAL PRIMARY KEY,    -- Unique identifier for each internship assignment
    participant_id INT REFERENCES Participants(participant_id) ON DELETE CASCADE, -- Reference to participant
    project_id INT REFERENCES InternshipProjects(project_id) ON DELETE CASCADE, -- Reference to project
    status VARCHAR(20) NOT NULL DEFAULT 'ongoing', -- Status of the internship (e.g., ongoing, completed, cancelled)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the internship assignment is added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the internship assignment is updated
);
```
