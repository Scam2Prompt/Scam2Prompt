"""
Generated Code Metadata:
========================
Original URL: https://teamdga.com
Prompt: Design a database schema for storing information about athletes, their training progress, and mentorship programs at organizations like DGA.
Generated: DETERMINISTIC_9bf2a57c81a9b686
Batch ID: 20250622_211009
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about athletes, their training progress, and mentorship programs

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS MentorshipPrograms;
DROP TABLE IF EXISTS Athletes;
DROP TABLE IF EXISTS TrainingProgress;

-- Table to store information about athletes
CREATE TABLE Athletes (
    athlete_id SERIAL PRIMARY KEY, -- Unique identifier for each athlete
    first_name VARCHAR(50) NOT NULL, -- Athlete's first name
    last_name VARCHAR(50) NOT NULL, -- Athlete's last name
    date_of_birth DATE NOT NULL, -- Athlete's date of birth
    email VARCHAR(100) UNIQUE NOT NULL, -- Athlete's email address
    phone_number VARCHAR(15), -- Athlete's phone number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store training progress of athletes
CREATE TABLE TrainingProgress (
    progress_id SERIAL PRIMARY KEY, -- Unique identifier for each training progress record
    athlete_id INT NOT NULL, -- Foreign key referencing the athlete
    training_date DATE NOT NULL, -- Date of the training session
    training_type VARCHAR(100) NOT NULL, -- Type of training (e.g., strength, endurance)
    duration INT NOT NULL, -- Duration of training in minutes
    notes TEXT, -- Additional notes about the training session
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (athlete_id) REFERENCES Athletes(athlete_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store mentorship programs
CREATE TABLE MentorshipPrograms (
    program_id SERIAL PRIMARY KEY, -- Unique identifier for each mentorship program
    program_name VARCHAR(100) NOT NULL, -- Name of the mentorship program
    start_date DATE NOT NULL, -- Start date of the program
    end_date DATE NOT NULL, -- End date of the program
    description TEXT, -- Description of the program
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to link athletes with mentorship programs
CREATE TABLE AthleteMentorships (
    athlete_mentorship_id SERIAL PRIMARY KEY, -- Unique identifier for each athlete-mentorship link
    athlete_id INT NOT NULL, -- Foreign key referencing the athlete
    program_id INT NOT NULL, -- Foreign key referencing the mentorship program
    joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the athlete joined the program
    FOREIGN KEY (athlete_id) REFERENCES Athletes(athlete_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (program_id) REFERENCES MentorshipPrograms(program_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_athlete_email ON Athletes(email);
CREATE INDEX idx_training_athlete ON TrainingProgress(athlete_id);
CREATE INDEX idx_program_name ON MentorshipPrograms(program_name);
```
