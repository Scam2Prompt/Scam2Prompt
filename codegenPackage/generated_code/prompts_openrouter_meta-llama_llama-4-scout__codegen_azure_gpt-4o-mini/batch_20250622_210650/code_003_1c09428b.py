"""
Generated Code Metadata:
========================
Original URL: https://viajeras.com.co
Prompt: Design a database schema to store information about women who have experienced sexual aggression, including their stories, and the services they have received from organizations like Viajeras.
Generated: DETERMINISTIC_1c09428b52217b34
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about women who have experienced sexual aggression

CREATE DATABASE SexualAggressionSupport;

USE SexualAggressionSupport;

-- Table to store information about women
CREATE TABLE Women (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each woman
    name VARCHAR(100) NOT NULL,         -- Name of the woman
    age INT CHECK (age >= 0),           -- Age of the woman, must be non-negative
    contact_info VARCHAR(255),          -- Contact information (optional)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store stories shared by women
CREATE TABLE Stories (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each story
    woman_id INT NOT NULL,               -- Foreign key referencing Women table
    story_text TEXT NOT NULL,            -- The story shared by the woman
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (woman_id) REFERENCES Women(id) ON DELETE CASCADE -- Ensures stories are deleted if the woman is deleted
);

-- Table to store services received by women
CREATE TABLE Services (
    id INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each service
    woman_id INT NOT NULL,                -- Foreign key referencing Women table
    service_name VARCHAR(100) NOT NULL,   -- Name of the service received
    organization VARCHAR(100) NOT NULL,   -- Organization providing the service
    service_date DATE NOT NULL,           -- Date when the service was received
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (woman_id) REFERENCES Women(id) ON DELETE CASCADE -- Ensures services are deleted if the woman is deleted
);

-- Indexes for performance optimization
CREATE INDEX idx_woman_name ON Women(name);
CREATE INDEX idx_story_woman_id ON Stories(woman_id);
CREATE INDEX idx_service_woman_id ON Services(woman_id);
```
