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
-- schema.sql

-- Create a database for school events
CREATE DATABASE school_events;

-- Use the school_events database
USE school_events;

-- Create a table for event categories
CREATE TABLE event_categories (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  UNIQUE KEY (name)
);

-- Create a table for school events
CREATE TABLE events (
  id INT AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  date DATE NOT NULL,
  description TEXT,
  category_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (category_id) REFERENCES event_categories(id) ON DELETE SET NULL
);

-- Insert default event categories
INSERT INTO event_categories (name, description) VALUES
  ('Uncategorized', 'Events without a specific category'),
  ('Дан школе', 'Events related to the school');

-- Example event insertion
INSERT INTO events (title, date, description, category_id) VALUES
  ('School Dance', '2024-09-20', 'A fun night for students and teachers', 1),
  ('Open House', '2024-10-15', 'Meet the teachers and learn about our school', 2);

-- Create a view for events with category information
CREATE VIEW events_with_categories AS
SELECT 
  e.id,
  e.title,
  e.date,
  e.description,
  ec.name AS category_name
FROM events e
LEFT JOIN event_categories ec ON e.category_id = ec.id;
```
