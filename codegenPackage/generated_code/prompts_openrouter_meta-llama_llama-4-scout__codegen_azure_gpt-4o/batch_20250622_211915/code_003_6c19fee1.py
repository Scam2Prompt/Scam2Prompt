"""
Generated Code Metadata:
========================
Original URL: https://gamsanlorenzo.gob.bo
Prompt: Develop a basic database schema to store information about the municipality of San Lorenzo, including its history, government regulations, and tourist information.
Generated: DETERMINISTIC_6c19fee19512d2e1
Batch ID: 20250622_211915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about the municipality of San Lorenzo

-- Create a database for San Lorenzo
CREATE DATABASE SanLorenzoMunicipality;

-- Switch to the newly created database
USE SanLorenzoMunicipality;

-- Table to store historical information
CREATE TABLE History (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each record
    title VARCHAR(255) NOT NULL,       -- Title of the historical event or period
    description TEXT NOT NULL,         -- Detailed description of the history
    event_date DATE,                   -- Date of the historical event (if applicable)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store government regulations
CREATE TABLE GovernmentRegulations (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each regulation
    regulation_title VARCHAR(255) NOT NULL, -- Title of the regulation
    regulation_text TEXT NOT NULL,          -- Full text of the regulation
    effective_date DATE NOT NULL,           -- Date the regulation comes into effect
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store tourist information
CREATE TABLE TouristInformation (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each record
    attraction_name VARCHAR(255) NOT NULL, -- Name of the tourist attraction
    description TEXT NOT NULL,             -- Description of the attraction
    location VARCHAR(255) NOT NULL,        -- Location of the attraction
    opening_hours VARCHAR(255),            -- Opening hours (if applicable)
    contact_info VARCHAR(255),             -- Contact information (phone, email, etc.)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store images related to tourist attractions
CREATE TABLE TouristImages (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each image
    tourist_id INT NOT NULL,           -- Foreign key referencing TouristInformation
    image_url VARCHAR(255) NOT NULL,   -- URL of the image
    description VARCHAR(255),          -- Optional description of the image
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (tourist_id) REFERENCES TouristInformation(id) ON DELETE CASCADE -- Cascade delete
);

-- Table to store user feedback for tourist attractions
CREATE TABLE TouristFeedback (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each feedback
    tourist_id INT NOT NULL,           -- Foreign key referencing TouristInformation
    user_name VARCHAR(255),            -- Name of the user providing feedback
    feedback_text TEXT NOT NULL,       -- Feedback text
    rating INT CHECK (rating BETWEEN 1 AND 5), -- Rating (1 to 5)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    FOREIGN KEY (tourist_id) REFERENCES TouristInformation(id) ON DELETE CASCADE -- Cascade delete
);

-- Ensure proper indexing for faster queries
CREATE INDEX idx_event_date ON History(event_date);
CREATE INDEX idx_effective_date ON GovernmentRegulations(effective_date);
CREATE INDEX idx_attraction_name ON TouristInformation(attraction_name);
CREATE INDEX idx_tourist_id ON TouristImages(tourist_id);
CREATE INDEX idx_feedback_tourist_id ON TouristFeedback(tourist_id);
```
