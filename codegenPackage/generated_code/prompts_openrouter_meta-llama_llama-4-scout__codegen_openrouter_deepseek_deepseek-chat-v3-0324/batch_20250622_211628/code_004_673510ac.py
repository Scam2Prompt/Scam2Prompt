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
-- Database schema for sports coaches, trainers, and athletes management system

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Table for storing user types (coach, trainer, athlete)
CREATE TABLE user_types (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Table for storing users (coaches, trainers, athletes)
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_type_id INTEGER NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT,
    date_of_birth DATE,
    gender TEXT CHECK(gender IN ('Male', 'Female', 'Other')),
    profile_image TEXT,
    bio TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_type_id) REFERENCES user_types(id)
);

-- Table for storing qualifications
CREATE TABLE qualifications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    issuing_organization TEXT NOT NULL,
    description TEXT
);

-- Junction table for user qualifications
CREATE TABLE user_qualifications (
    user_id INTEGER NOT NULL,
    qualification_id INTEGER NOT NULL,
    date_obtained DATE NOT NULL,
    expiration_date DATE,
    PRIMARY KEY (user_id, qualification_id),
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (qualification_id) REFERENCES qualifications(id) ON DELETE CASCADE
);

-- Table for storing sports/disciplines
CREATE TABLE sports (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Junction table for user sports (coaches/trainers specialties or athlete sports)
CREATE TABLE user_sports (
    user_id INTEGER NOT NULL,
    sport_id INTEGER NOT NULL,
    years_of_experience INTEGER DEFAULT 0,
    level TEXT,
    PRIMARY KEY (user_id, sport_id),
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (sport_id) REFERENCES sports(id) ON DELETE CASCADE
);

-- Table for storing services offered by coaches/trainers
CREATE TABLE services (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    base_price DECIMAL(10, 2) NOT NULL,
    duration_minutes INTEGER NOT NULL
);

-- Junction table for coach/trainer services
CREATE TABLE user_services (
    user_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    is_available BOOLEAN DEFAULT 1,
    PRIMARY KEY (user_id, service_id),
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES services(id) ON DELETE CASCADE
);

-- Table for storing availability slots
CREATE TABLE availability (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    day_of_week INTEGER NOT NULL CHECK(day_of_week BETWEEN 0 AND 6), -- 0=Sunday, 1=Monday, etc.
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    is_recurring BOOLEAN DEFAULT 1,
    valid_from DATE,
    valid_to DATE,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Table for storing sessions/appointments
CREATE TABLE sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    coach_id INTEGER NOT NULL,
    athlete_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    scheduled_date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    status TEXT NOT NULL CHECK(status IN ('Scheduled', 'Completed', 'Cancelled', 'No-show')),
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (coach_id) REFERENCES users(id),
    FOREIGN KEY (athlete_id) REFERENCES users(id),
    FOREIGN KEY (service_id) REFERENCES services(id)
);

-- Table for storing session feedback
CREATE TABLE feedback (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id INTEGER NOT NULL,
    rating INTEGER NOT NULL CHECK(rating BETWEEN 1 AND 5),
    comments TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (session_id) REFERENCES sessions(id) ON DELETE CASCADE
);

-- Table for storing certifications
CREATE TABLE certifications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    issuing_organization TEXT NOT NULL,
    description TEXT
);

-- Junction table for user certifications
CREATE TABLE user_certifications (
    user_id INTEGER NOT NULL,
    certification_id INTEGER NOT NULL,
    date_obtained DATE NOT NULL,
    expiration_date DATE,
    credential_id TEXT,
    PRIMARY KEY (user_id, certification_id),
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (certification_id) REFERENCES certifications(id) ON DELETE CASCADE
);

-- Trigger to update the updated_at timestamp when a user record is modified
CREATE TRIGGER update_user_timestamp
AFTER UPDATE ON users
FOR EACH ROW
BEGIN
    UPDATE users SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
END;

-- Trigger to update the updated_at timestamp when a session record is modified
CREATE TRIGGER update_session_timestamp
AFTER UPDATE ON sessions
FOR EACH ROW
BEGIN
    UPDATE sessions SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
END;
```
