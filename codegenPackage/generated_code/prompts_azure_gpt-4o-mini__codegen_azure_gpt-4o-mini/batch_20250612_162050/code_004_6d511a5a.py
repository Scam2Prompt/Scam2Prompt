"""
Generated Code Metadata:
========================
Original URL: https://934ummfm.com
Prompt: Design a database schema for storing information about educational programs and podcasts, reflecting the structure used by UMM FM for their content management.
Generated: DETERMINISTIC_6d511a5a22dbd880
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about educational programs and podcasts

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Episodes;
DROP TABLE IF EXISTS Podcasts;
DROP TABLE IF EXISTS Programs;
DROP TABLE IF EXISTS Categories;

-- Table to store categories for programs and podcasts
CREATE TABLE Categories (
    id SERIAL PRIMARY KEY, -- Unique identifier for each category
    name VARCHAR(255) NOT NULL UNIQUE, -- Name of the category, must be unique
    description TEXT, -- Optional description of the category
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the category was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the category was last updated
);

-- Table to store educational programs
CREATE TABLE Programs (
    id SERIAL PRIMARY KEY, -- Unique identifier for each program
    title VARCHAR(255) NOT NULL, -- Title of the program
    description TEXT, -- Description of the program
    category_id INT REFERENCES Categories(id) ON DELETE SET NULL, -- Foreign key to Categories table
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the program was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the program was last updated
);

-- Table to store podcasts
CREATE TABLE Podcasts (
    id SERIAL PRIMARY KEY, -- Unique identifier for each podcast
    title VARCHAR(255) NOT NULL, -- Title of the podcast
    description TEXT, -- Description of the podcast
    category_id INT REFERENCES Categories(id) ON DELETE SET NULL, -- Foreign key to Categories table
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the podcast was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the podcast was last updated
);

-- Table to store episodes of podcasts
CREATE TABLE Episodes (
    id SERIAL PRIMARY KEY, -- Unique identifier for each episode
    podcast_id INT REFERENCES Podcasts(id) ON DELETE CASCADE, -- Foreign key to Podcasts table
    title VARCHAR(255) NOT NULL, -- Title of the episode
    description TEXT, -- Description of the episode
    audio_url VARCHAR(255) NOT NULL, -- URL to the audio file of the episode
    duration INT NOT NULL, -- Duration of the episode in seconds
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the episode was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the episode was last updated
);

-- Indexes for faster querying
CREATE INDEX idx_programs_category ON Programs(category_id);
CREATE INDEX idx_podcasts_category ON Podcasts(category_id);
CREATE INDEX idx_episodes_podcast ON Episodes(podcast_id);
```
