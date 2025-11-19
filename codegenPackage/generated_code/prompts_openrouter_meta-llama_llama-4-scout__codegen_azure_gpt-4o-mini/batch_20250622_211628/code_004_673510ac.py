"""
Generated Code Metadata:
========================
Original URL: https://lzero.us
Prompt: Design a database schema for storing information about sports coaches, trainers, and athletes, inspired by the team of dedicated coaches at L-Zero, including details about their experience, qualifications, and services offered.
Generated: DETERMINISTIC_673510ac56ff88ad
Batch ID: 20250622_211628
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about sports coaches, trainers, and athletes

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Athletes;
DROP TABLE IF EXISTS Coaches;
DROP TABLE IF EXISTS Trainers;
DROP TABLE IF EXISTS Services;

-- Table to store information about athletes
CREATE TABLE Athletes (
    athlete_id SERIAL PRIMARY KEY,          -- Unique identifier for each athlete
    first_name VARCHAR(50) NOT NULL,       -- Athlete's first name
    last_name VARCHAR(50) NOT NULL,        -- Athlete's last name
    date_of_birth DATE NOT NULL,            -- Athlete's date of birth
    sport VARCHAR(50) NOT NULL,             -- Sport the athlete participates in
    experience_years INT DEFAULT 0,        -- Years of experience in the sport
    coach_id INT,                           -- Foreign key referencing the coach
    FOREIGN KEY (coach_id) REFERENCES Coaches(coach_id) ON DELETE SET NULL
);

-- Table to store information about coaches
CREATE TABLE Coaches (
    coach_id SERIAL PRIMARY KEY,            -- Unique identifier for each coach
    first_name VARCHAR(50) NOT NULL,       -- Coach's first name
    last_name VARCHAR(50) NOT NULL,        -- Coach's last name
    qualifications TEXT,                    -- Qualifications of the coach
    experience_years INT NOT NULL,         -- Years of coaching experience
    services_offered TEXT,                  -- Services offered by the coach
    contact_info VARCHAR(100)               -- Contact information for the coach
);

-- Table to store information about trainers
CREATE TABLE Trainers (
    trainer_id SERIAL PRIMARY KEY,          -- Unique identifier for each trainer
    first_name VARCHAR(50) NOT NULL,       -- Trainer's first name
    last_name VARCHAR(50) NOT NULL,        -- Trainer's last name
    certifications TEXT,                    -- Certifications held by the trainer
    experience_years INT NOT NULL,         -- Years of training experience
    services_offered TEXT,                  -- Services offered by the trainer
    contact_info VARCHAR(100)               -- Contact information for the trainer
);

-- Table to store services offered by coaches and trainers
CREATE TABLE Services (
    service_id SERIAL PRIMARY KEY,          -- Unique identifier for each service
    service_name VARCHAR(100) NOT NULL,    -- Name of the service
    description TEXT,                       -- Description of the service
    coach_id INT,                           -- Foreign key referencing the coach
    trainer_id INT,                         -- Foreign key referencing the trainer
    FOREIGN KEY (coach_id) REFERENCES Coaches(coach_id) ON DELETE CASCADE,
    FOREIGN KEY (trainer_id) REFERENCES Trainers(trainer_id) ON DELETE CASCADE
);

-- Indexes for faster querying
CREATE INDEX idx_athlete_coach ON Athletes(coach_id);
CREATE INDEX idx_coach_services ON Services(coach_id);
CREATE INDEX idx_trainer_services ON Services(trainer_id);
```
