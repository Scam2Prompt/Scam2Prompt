"""
Generated Code Metadata:
========================
Original URL: https://springsinternational.org
Prompt: Generate a sample database schema for storing information about upcoming events, previous events, and event galleries for a ministry organization like SIM.
Generated: DETERMINISTIC_f7a8e3148253167a
Batch ID: 20250622_204809
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about events and galleries for a ministry organization

CREATE DATABASE sim_events;

USE sim_events;

-- Table to store information about upcoming events
CREATE TABLE upcoming_events (
    event_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each event
    event_name VARCHAR(255) NOT NULL,        -- Name of the event
    event_date DATETIME NOT NULL,             -- Date and time of the event
    location VARCHAR(255) NOT NULL,           -- Location of the event
    description TEXT,                          -- Description of the event
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the event was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Table to store information about previous events
CREATE TABLE previous_events (
    event_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each event
    event_name VARCHAR(255) NOT NULL,        -- Name of the event
    event_date DATETIME NOT NULL,             -- Date and time of the event
    location VARCHAR(255) NOT NULL,           -- Location of the event
    description TEXT,                          -- Description of the event
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the event was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Table to store galleries associated with events
CREATE TABLE event_galleries (
    gallery_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each gallery
    event_id INT NOT NULL,                      -- Foreign key referencing the event
    image_url VARCHAR(255) NOT NULL,           -- URL of the image
    caption VARCHAR(255),                       -- Caption for the image
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the gallery entry was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of the last update
    FOREIGN KEY (event_id) REFERENCES upcoming_events(event_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_event_date_upcoming ON upcoming_events(event_date);
CREATE INDEX idx_event_date_previous ON previous_events(event_date);
CREATE INDEX idx_event_id_gallery ON event_galleries(event_id);
```
