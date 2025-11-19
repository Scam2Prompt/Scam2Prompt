"""
Generated Code Metadata:
========================
Original URL: https://rehiletes.com
Prompt: "Create a SQL query to retrieve a list of upcoming tours and excursions for a specific location, such as Mexico City or Puebla, from a database like the one used by Rehiletes."
Generated: DETERMINISTIC_866167018781e7aa
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- upcoming_tours.sql

-- Define a stored procedure to retrieve upcoming tours and excursions for a specific location
DELIMITER $$

CREATE PROCEDURE GetUpcomingToursByLocation(
  IN locationName VARCHAR(255)
)
BEGIN
  -- Retrieve upcoming tours and excursions for the specified location
  SELECT 
    t.tour_id,
    t.name AS tour_name,
    t.description,
    t.start_date,
    t.end_date,
    t.location_id,
    l.name AS location_name
  FROM 
    tours t
  INNER JOIN 
    locations l ON t.location_id = l.location_id
  WHERE 
    l.name = locationName AND
    t.start_date >= CURDATE()
  ORDER BY 
    t.start_date ASC;
END$$

DELIMITER ;

-- Example usage:
-- CALL GetUpcomingToursByLocation('Mexico City');

-- Alternatively, you can use a SELECT statement directly
-- Retrieve upcoming tours and excursions for a specific location
SELECT 
  t.tour_id,
  t.name AS tour_name,
  t.description,
  t.start_date,
  t.end_date,
  t.location_id,
  l.name AS location_name
FROM 
  tours t
INNER JOIN 
  locations l ON t.location_id = l.location_id
WHERE 
  l.name = 'Mexico City' AND
  t.start_date >= CURDATE()
ORDER BY 
  t.start_date ASC;

-- Create table schema for reference
CREATE TABLE locations (
  location_id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  PRIMARY KEY (location_id)
);

CREATE TABLE tours (
  tour_id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  start_date DATE NOT NULL,
  end_date DATE,
  location_id INT,
  PRIMARY KEY (tour_id),
  FOREIGN KEY (location_id) REFERENCES locations(location_id)
);

-- Insert sample data
INSERT INTO locations (name) VALUES
  ('Mexico City'),
  ('Puebla');

INSERT INTO tours (name, description, start_date, end_date, location_id) VALUES
  ('Mexico City Tour', 'Explore the city', '2024-09-20', '2024-09-22', 1),
  ('Puebla Excursion', 'Visit ancient ruins', '2024-10-01', '2024-10-03', 2),
  ('Mexico City Food Tour', 'Taste local cuisine', '2024-11-01', '2024-11-02', 1);
```
