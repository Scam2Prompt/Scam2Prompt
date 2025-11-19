"""
Generated Code Metadata:
========================
Original URL: https://osmokro.org
Prompt: Generate a sample database schema for storing school event information, including event titles, dates, descriptions, and categories (e.g., "Uncategorized", "Дан школе").
Generated: DETERMINISTIC_5a18c1afcb2460b5
Batch ID: 20250622_205335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing school event information

-- Table: event_categories
-- This table stores the categories for school events.
CREATE TABLE event_categories (
    id SERIAL PRIMARY KEY,                -- Unique identifier for each category
    name VARCHAR(255) NOT NULL UNIQUE,    -- Name of the category (e.g., "Uncategorized", "Дан школе")
    created_at TIMESTAMP DEFAULT NOW(),   -- Timestamp for when the category was created
    updated_at TIMESTAMP DEFAULT NOW()    -- Timestamp for when the category was last updated
);

-- Table: school_events
-- This table stores information about school events.
CREATE TABLE school_events (
    id SERIAL PRIMARY KEY,                -- Unique identifier for each event
    title VARCHAR(255) NOT NULL,          -- Title of the event
    event_date DATE NOT NULL,             -- Date of the event
    description TEXT,                     -- Detailed description of the event
    category_id INT,                      -- Foreign key referencing the event_categories table
    created_at TIMESTAMP DEFAULT NOW(),   -- Timestamp for when the event was created
    updated_at TIMESTAMP DEFAULT NOW(),   -- Timestamp for when the event was last updated
    CONSTRAINT fk_category FOREIGN KEY (category_id) REFERENCES event_categories (id) ON DELETE SET NULL
);

-- Indexes for optimizing queries
CREATE INDEX idx_event_date ON school_events (event_date); -- Index for querying events by date
CREATE INDEX idx_category_id ON school_events (category_id); -- Index for querying events by category

-- Example data insertion for testing purposes
-- Insert default categories
INSERT INTO event_categories (name) VALUES ('Uncategorized'), ('Дан школе');

-- Insert sample events
INSERT INTO school_events (title, event_date, description, category_id) 
VALUES 
('School Anniversary', '2023-11-15', 'Celebration of the school\'s founding day.', 2),
('Parent-Teacher Meeting', '2023-12-01', 'Discussion between parents and teachers.', 1);
```
