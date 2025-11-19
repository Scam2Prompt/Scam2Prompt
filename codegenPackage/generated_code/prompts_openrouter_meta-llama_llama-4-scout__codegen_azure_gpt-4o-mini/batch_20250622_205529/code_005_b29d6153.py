"""
Generated Code Metadata:
========================
Original URL: https://marchigue.cl
Prompt: Write a SQL query to design a database schema for storing information about tourist sites in Marchigüe, including details about the windmills, Hacienda Histórica de Marchigüe, and other attractions.
Generated: DETERMINISTIC_b29d61538c5064a3
Batch ID: 20250622_205529
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for storing information about tourist sites in Marchigüe

-- Drop the existing database if it exists (for development purposes)
DROP DATABASE IF EXISTS MarchigueTourism;

-- Create a new database for the tourist sites
CREATE DATABASE MarchigueTourism;

-- Use the newly created database
USE MarchigueTourism;

-- Table to store information about tourist sites
CREATE TABLE TouristSites (
    site_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each site
    name VARCHAR(255) NOT NULL,             -- Name of the tourist site
    description TEXT,                        -- Description of the tourist site
    location VARCHAR(255) NOT NULL,         -- Location of the tourist site
    site_type ENUM('Windmill', 'Hacienda', 'Attraction') NOT NULL, -- Type of the site
    opening_hours VARCHAR(100),              -- Opening hours of the site
    contact_info VARCHAR(100),               -- Contact information for the site
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for record creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for record updates
);

-- Table to store visitor reviews for each tourist site
CREATE TABLE Reviews (
    review_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each review
    site_id INT NOT NULL,                     -- Foreign key referencing the tourist site
    visitor_name VARCHAR(100) NOT NULL,       -- Name of the visitor
    rating INT CHECK (rating BETWEEN 1 AND 5), -- Rating given by the visitor (1 to 5)
    comment TEXT,                             -- Review comment
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for review creation
    FOREIGN KEY (site_id) REFERENCES TouristSites(site_id) ON DELETE CASCADE -- Foreign key constraint
);

-- Insert sample data for tourist sites
INSERT INTO TouristSites (name, description, location, site_type, opening_hours, contact_info)
VALUES 
('Windmill of Marchigüe', 'A historic windmill offering tours and scenic views.', 'Marchigüe, Chile', 'Windmill', '9 AM - 5 PM', 'info@windmillmarchigue.cl'),
('Hacienda Histórica de Marchigüe', 'A historical estate with rich cultural heritage.', 'Marchigüe, Chile', 'Hacienda', '10 AM - 6 PM', 'contact@haciendamarchigue.cl'),
('Marchigüe Nature Park', 'A beautiful park with hiking trails and picnic areas.', 'Marchigüe, Chile', 'Attraction', '8 AM - 8 PM', 'info@marchiguenaturepark.cl');

-- Sample query to retrieve all tourist sites
SELECT * FROM TouristSites;

-- Sample query to retrieve reviews for a specific tourist site
SELECT * FROM Reviews WHERE site_id = 1; -- Replace 1 with the desired site_id
```
