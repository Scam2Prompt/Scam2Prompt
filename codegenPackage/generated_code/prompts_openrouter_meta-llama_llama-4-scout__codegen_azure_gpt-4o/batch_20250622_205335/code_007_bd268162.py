"""
Generated Code Metadata:
========================
Original URL: https://osmokro.org
Prompt: Generate a database schema for storing school events with titles, dates, and descriptions.
Generated: DETERMINISTIC_bd268162ba82cb23
Batch ID: 20250622_205335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing school events

-- Create a table to store school events
CREATE TABLE SchoolEvents (
    EventID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each event
    Title VARCHAR(255) NOT NULL,            -- Title of the event (required)
    EventDate DATE NOT NULL,                -- Date of the event (required)
    Description TEXT,                       -- Detailed description of the event (optional)
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the event was created
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the event was last updated
);

-- Add an index on EventDate for faster queries related to dates
CREATE INDEX idx_event_date ON SchoolEvents(EventDate);

-- Example of inserting data into the table
-- INSERT INTO SchoolEvents (Title, EventDate, Description)
-- VALUES ('Science Fair', '2023-11-15', 'Annual science fair showcasing student projects.');

-- Example of querying data
-- SELECT * FROM SchoolEvents WHERE EventDate = '2023-11-15';

-- Example of updating an event
-- UPDATE SchoolEvents SET Title = 'Updated Science Fair' WHERE EventID = 1;

-- Example of deleting an event
-- DELETE FROM SchoolEvents WHERE EventID = 1;
```
