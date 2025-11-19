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
-- Sample database schema for storing school event information

-- Create a table for event categories
CREATE TABLE event_categories (
    id SERIAL PRIMARY KEY, -- Unique identifier for each category
    name VARCHAR(255) NOT NULL UNIQUE, -- Name of the category, must be unique
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the category was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the category was last updated
);

-- Create a table for events
CREATE TABLE events (
    id SERIAL PRIMARY KEY, -- Unique identifier for each event
    title VARCHAR(255) NOT NULL, -- Title of the event
    event_date DATE NOT NULL, -- Date of the event
    description TEXT, -- Description of the event
    category_id INT, -- Foreign key referencing the event category
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the event was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the event was last updated
    FOREIGN KEY (category_id) REFERENCES event_categories(id) ON DELETE SET NULL -- Ensures referential integrity; sets category_id to NULL if the category is deleted
);

-- Insert default categories into the event_categories table
INSERT INTO event_categories (name) VALUES
('Uncategorized'),
('Дан школе');

-- Example of how to insert a new event
-- INSERT INTO events (title, event_date, description, category_id) VALUES
-- ('School Science Fair', '2023-05-15', 'An annual event showcasing student projects.', 1);
```
