"""
Generated Code Metadata:
========================
Original URL: https://conferencesglobal.org
Prompt: Design a database schema for storing conference-related data, including speaker profiles, abstract submissions, and attendee information, based on Conferences Global's conference organization structure.
Generated: DETERMINISTIC_caa2645a5e1d854e
Batch ID: 20250622_211826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing conference-related data

-- Create a table for storing conference information
CREATE TABLE Conferences (
    conference_id SERIAL PRIMARY KEY, -- Unique identifier for each conference
    name VARCHAR(255) NOT NULL, -- Name of the conference
    start_date DATE NOT NULL, -- Start date of the conference
    end_date DATE NOT NULL, -- End date of the conference
    location VARCHAR(255) NOT NULL, -- Location of the conference
    description TEXT, -- Description of the conference
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the conference was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Create a table for storing speaker profiles
CREATE TABLE Speakers (
    speaker_id SERIAL PRIMARY KEY, -- Unique identifier for each speaker
    conference_id INT NOT NULL, -- Foreign key referencing the conference
    name VARCHAR(255) NOT NULL, -- Name of the speaker
    bio TEXT, -- Biography of the speaker
    email VARCHAR(255) UNIQUE NOT NULL, -- Email of the speaker
    profile_picture_url VARCHAR(255), -- URL to the speaker's profile picture
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the speaker profile was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of the last update
    FOREIGN KEY (conference_id) REFERENCES Conferences(conference_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table for storing abstract submissions
CREATE TABLE Abstracts (
    abstract_id SERIAL PRIMARY KEY, -- Unique identifier for each abstract
    conference_id INT NOT NULL, -- Foreign key referencing the conference
    speaker_id INT NOT NULL, -- Foreign key referencing the speaker
    title VARCHAR(255) NOT NULL, -- Title of the abstract
    content TEXT NOT NULL, -- Content of the abstract
    submission_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date when the abstract was submitted
    status VARCHAR(50) DEFAULT 'Pending', -- Status of the abstract (e.g., Pending, Accepted, Rejected)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the abstract was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of the last update
    FOREIGN KEY (conference_id) REFERENCES Conferences(conference_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (speaker_id) REFERENCES Speakers(speaker_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create a table for storing attendee information
CREATE TABLE Attendees (
    attendee_id SERIAL PRIMARY KEY, -- Unique identifier for each attendee
    conference_id INT NOT NULL, -- Foreign key referencing the conference
    name VARCHAR(255) NOT NULL, -- Name of the attendee
    email VARCHAR(255) UNIQUE NOT NULL, -- Email of the attendee
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date when the attendee registered
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the attendee record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of the last update
    FOREIGN KEY (conference_id) REFERENCES Conferences(conference_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Create an index on the email fields for faster lookups
CREATE INDEX idx_speaker_email ON Speakers(email);
CREATE INDEX idx_attendee_email ON Attendees(email);
```
