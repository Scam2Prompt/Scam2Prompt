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
-- Database schema for school event management system
CREATE TABLE event_categories (
    category_id SERIAL PRIMARY KEY,
    category_name VARCHAR(50) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE events (
    event_id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    start_datetime TIMESTAMP NOT NULL,
    end_datetime TIMESTAMP NOT NULL,
    location VARCHAR(100),
    category_id INTEGER REFERENCES event_categories(category_id),
    is_published BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT valid_datetime CHECK (end_datetime > start_datetime)
);

-- Insert default categories
INSERT INTO event_categories (category_name, description) VALUES 
('Uncategorized', 'Events without specific category'),
('School Event', 'Official school-wide events'),
('Sports', 'Athletic competitions and games'),
('Arts', 'Music, theater, and visual arts events'),
('Academic', 'Academic competitions and ceremonies'),
('Community', 'Events involving local community'),
('Дан школе', 'Special events honoring the school');

-- Create indexes for better performance
CREATE INDEX idx_events_date ON events (start_datetime);
CREATE INDEX idx_events_category ON events (category_id);
```
