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
-- Database schema for storing information about upcoming events, previous events, and event galleries
-- This schema is designed for a ministry organization like SIM

-- Table to store information about events
CREATE TABLE Events (
    EventID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each event
    Name VARCHAR(255) NOT NULL,             -- Name of the event
    Description TEXT,                       -- Detailed description of the event
    StartDate DATE NOT NULL,                -- Start date of the event
    EndDate DATE,                           -- End date of the event (nullable for single-day events)
    Location VARCHAR(255),                  -- Location of the event
    IsUpcoming BOOLEAN NOT NULL,            -- Flag to indicate if the event is upcoming (true) or previous (false)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the event was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the event was last updated
);

-- Table to store event galleries (images associated with events)
CREATE TABLE EventGalleries (
    GalleryID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each gallery entry
    EventID INT NOT NULL,                     -- Foreign key referencing the Events table
    ImageURL VARCHAR(2083) NOT NULL,          -- URL of the image
    Caption VARCHAR(255),                     -- Optional caption for the image
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the gallery entry was created
    FOREIGN KEY (EventID) REFERENCES Events(EventID) ON DELETE CASCADE -- Ensure gallery entries are deleted if the event is deleted
);

-- Table to store additional metadata or tags for events
CREATE TABLE EventTags (
    TagID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each tag
    EventID INT NOT NULL,                 -- Foreign key referencing the Events table
    TagName VARCHAR(100) NOT NULL,        -- Name of the tag
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the tag was created
    FOREIGN KEY (EventID) REFERENCES Events(EventID) ON DELETE CASCADE -- Ensure tags are deleted if the event is deleted
);

-- Indexes for optimizing queries
CREATE INDEX idx_event_start_date ON Events (StartDate); -- Index for querying events by start date
CREATE INDEX idx_event_is_upcoming ON Events (IsUpcoming); -- Index for querying upcoming or previous events
CREATE INDEX idx_gallery_event_id ON EventGalleries (EventID); -- Index for querying galleries by event ID
CREATE INDEX idx_tag_event_id ON EventTags (EventID); -- Index for querying tags by event ID
```
