"""
Generated Code Metadata:
========================
Original URL: https://gstouristcentre.gr
Prompt: "Write a SQL query to retrieve information about tourist destinations in Corfu, including their descriptions and activities offered, from a database schema similar to what might be used by GS Tourist Centre."
Generated: DETERMINISTIC_3eea5732deec9c1d
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Retrieve information about tourist destinations in Corfu
-- =====================================================================

-- Define the database schema
-- For this example, let's assume we have the following tables:
--   - destinations (id, name, description, location)
--   - activities (id, name, description, destination_id)
--   - locations (id, name, region)

-- Query to retrieve tourist destinations in Corfu
SELECT 
    d.id AS destination_id,
    d.name AS destination_name,
    d.description AS destination_description,
    l.name AS location_name,
    a.id AS activity_id,
    a.name AS activity_name,
    a.description AS activity_description
FROM 
    destinations d
INNER JOIN 
    locations l ON d.location = l.id
LEFT JOIN 
    activities a ON d.id = a.destination_id
WHERE 
    l.region = 'Corfu'
ORDER BY 
    d.id, a.id;

-- Alternatively, if you want to retrieve a list of activities for each destination
-- =====================================================================

-- Query to retrieve tourist destinations in Corfu with a list of activities
SELECT 
    d.id AS destination_id,
    d.name AS destination_name,
    d.description AS destination_description,
    l.name AS location_name,
    JSON_AGG(JSON_BUILD_OBJECT('activity_id', a.id, 'activity_name', a.name, 'activity_description', a.description)) AS activities
FROM 
    destinations d
INNER JOIN 
    locations l ON d.location = l.id
LEFT JOIN 
    activities a ON d.id = a.destination_id
WHERE 
    l.region = 'Corfu'
GROUP BY 
    d.id, d.name, d.description, l.name
ORDER BY 
    d.id;
```

```sql
-- Create database schema for reference
-- =====================================================================
CREATE TABLE locations (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    region VARCHAR(255) NOT NULL
);

CREATE TABLE destinations (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    location INTEGER NOT NULL,
    FOREIGN KEY (location) REFERENCES locations(id)
);

CREATE TABLE activities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    destination_id INTEGER NOT NULL,
    FOREIGN KEY (destination_id) REFERENCES destinations(id)
);

-- Insert sample data
-- =====================================================================
INSERT INTO locations (name, region) 
VALUES 
('Corfu Town', 'Corfu'),
('Paleokastritsa', 'Corfu');

INSERT INTO destinations (name, description, location) 
VALUES 
('Corfu Town Sightseeing', 'Explore the historic town', 1),
('Paleokastritsa Beach', 'Relax on the beautiful beach', 2);

INSERT INTO activities (name, description, destination_id) 
VALUES 
('Old Fortress Visit', 'Visit the historic fortress', 1),
('Beach Volleyball', 'Play volleyball on the beach', 2),
('Town Walking Tour', 'Explore the town on foot', 1);
```
