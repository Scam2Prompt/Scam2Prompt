"""
Generated Code Metadata:
========================
Original URL: https://azagros.com
Prompt: Create a database schema to store information about grain and fruit production, field mapping, and visit logs, ensuring compatibility with both web and mobile platforms as described on Azagros.
Generated: DETERMINISTIC_47a4a68bb43146a7
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about grain and fruit production, field mapping, and visit logs

-- Create a table to store information about different crops
CREATE TABLE crops (
    crop_id SERIAL PRIMARY KEY, -- Unique identifier for each crop
    name VARCHAR(100) NOT NULL, -- Name of the crop
    type VARCHAR(50) NOT NULL, -- Type of crop (e.g., grain, fruit)
    description TEXT, -- Description of the crop
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the crop was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Create a table to store information about fields
CREATE TABLE fields (
    field_id SERIAL PRIMARY KEY, -- Unique identifier for each field
    name VARCHAR(100) NOT NULL, -- Name of the field
    location GEOGRAPHY(Point, 4326) NOT NULL, -- Geographic location of the field (latitude, longitude)
    size DECIMAL(10, 2) NOT NULL, -- Size of the field in acres
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the field was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Create a table to map crops to fields
CREATE TABLE crop_field_mapping (
    mapping_id SERIAL PRIMARY KEY, -- Unique identifier for each mapping
    crop_id INT NOT NULL REFERENCES crops(crop_id) ON DELETE CASCADE, -- Foreign key referencing crops
    field_id INT NOT NULL REFERENCES fields(field_id) ON DELETE CASCADE, -- Foreign key referencing fields
    planting_date DATE NOT NULL, -- Date when the crop was planted
    harvest_date DATE, -- Date when the crop was harvested
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the mapping was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Create a table to log visits to the fields
CREATE TABLE visit_logs (
    visit_id SERIAL PRIMARY KEY, -- Unique identifier for each visit log
    field_id INT NOT NULL REFERENCES fields(field_id) ON DELETE CASCADE, -- Foreign key referencing fields
    visit_date TIMESTAMP NOT NULL, -- Date and time of the visit
    visitor_name VARCHAR(100) NOT NULL, -- Name of the visitor
    notes TEXT, -- Additional notes about the visit
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the visit log was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Create indexes for faster querying
CREATE INDEX idx_crop_name ON crops(name);
CREATE INDEX idx_field_name ON fields(name);
CREATE INDEX idx_visit_date ON visit_logs(visit_date);
```
