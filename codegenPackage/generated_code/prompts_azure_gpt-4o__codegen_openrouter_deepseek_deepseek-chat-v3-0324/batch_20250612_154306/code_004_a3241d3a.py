"""
Generated Code Metadata:
========================
Original URL: https://vimsa.com.br
Prompt: Write a SQL query to store and retrieve data about Vimsa bus routes, schedules, and recharge points in a relational database.
Generated: DETERMINISTIC_a3241d3aff512040
Batch ID: 20250612_154306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Vimsa bus management system

-- Create database
CREATE DATABASE IF NOT EXISTS vimsa_bus_system;
USE vimsa_bus_system;

-- Create tables with proper constraints and indexes

-- Bus routes table
CREATE TABLE IF NOT EXISTS routes (
    route_id INT AUTO_INCREMENT PRIMARY KEY,
    route_name VARCHAR(100) NOT NULL,
    origin VARCHAR(100) NOT NULL,
    destination VARCHAR(100) NOT NULL,
    distance_km DECIMAL(6,2) NOT NULL,
    estimated_duration_min INT NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT chk_distance CHECK (distance_km > 0),
    CONSTRAINT chk_duration CHECK (estimated_duration_min > 0)
);

-- Bus stops table
CREATE TABLE IF NOT EXISTS stops (
    stop_id INT AUTO_INCREMENT PRIMARY KEY,
    stop_name VARCHAR(100) NOT NULL,
    location POINT NOT NULL,
    address TEXT,
    is_recharge_point BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    SPATIAL INDEX(location)
);

-- Route stops mapping table
CREATE TABLE IF NOT EXISTS route_stops (
    route_id INT NOT NULL,
    stop_id INT NOT NULL,
    stop_sequence INT NOT NULL,
    distance_from_prev_km DECIMAL(6,2) NOT NULL,
    estimated_time_from_prev_min INT NOT NULL,
    PRIMARY KEY (route_id, stop_id),
    FOREIGN KEY (route_id) REFERENCES routes(route_id) ON DELETE CASCADE,
    FOREIGN KEY (stop_id) REFERENCES stops(stop_id) ON DELETE CASCADE,
    CONSTRAINT chk_sequence CHECK (stop_sequence > 0),
    CONSTRAINT chk_route_distance CHECK (distance_from_prev_km >= 0),
    CONSTRAINT chk_route_time CHECK (estimated_time_from_prev_min >= 0)
);

-- Bus schedule table
CREATE TABLE IF NOT EXISTS schedules (
    schedule_id INT AUTO_INCREMENT PRIMARY KEY,
    route_id INT NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    frequency_min INT,
    operating_days SET('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday') NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (route_id) REFERENCES routes(route_id) ON DELETE CASCADE,
    CONSTRAINT chk_frequency CHECK (frequency_min > 0 OR frequency_min IS NULL),
    CONSTRAINT chk_time CHECK (start_time < end_time)
);

-- Recharge points table (specialized stops)
CREATE TABLE IF NOT EXISTS recharge_points (
    stop_id INT PRIMARY KEY,
    recharge_type ENUM('Fast', 'Standard') NOT NULL,
    available_slots INT NOT NULL,
    operating_hours_start TIME NOT NULL,
    operating_hours_end TIME NOT NULL,
    FOREIGN KEY (stop_id) REFERENCES stops(stop_id) ON DELETE CASCADE,
    CONSTRAINT chk_slots CHECK (available_slots > 0),
    CONSTRAINT chk_recharge_hours CHECK (operating_hours_start < operating_hours_end)
);

-- Sample queries for data retrieval

-- Get all active routes with their schedules
SELECT 
    r.route_id, 
    r.route_name, 
    r.origin, 
    r.destination,
    s.schedule_id,
    s.start_time,
    s.end_time,
    s.frequency_min,
    s.operating_days
FROM 
    routes r
JOIN 
    schedules s ON r.route_id = s.route_id
WHERE 
    r.is_active = TRUE 
    AND s.is_active = TRUE
ORDER BY 
    r.route_name, s.start_time;

-- Get all stops for a specific route in sequence
SELECT 
    rs.stop_sequence,
    s.stop_id,
    s.stop_name,
    s.is_recharge_point,
    rs.distance_from_prev_km,
    rs.estimated_time_from_prev_min
FROM 
    route_stops rs
JOIN 
    stops s ON rs.stop_id = s.stop_id
WHERE 
    rs.route_id = 1  -- Parameterize this in application
ORDER BY 
    rs.stop_sequence;

-- Find nearby recharge points within 5km radius of a given point
SELECT 
    s.stop_id,
    s.stop_name,
    ST_Distance_Sphere(s.location, POINT(12.9716, 77.5946)) / 1000 AS distance_km,  -- Example coordinates
    rp.recharge_type,
    rp.available_slots,
    rp.operating_hours_start,
    rp.operating_hours_end
FROM 
    stops s
JOIN 
    recharge_points rp ON s.stop_id = rp.stop_id
WHERE 
    ST_Distance_Sphere(s.location, POINT(12.9716, 77.5946)) <= 5000  -- 5km radius
    AND TIME(NOW()) BETWEEN rp.operating_hours_start AND rp.operating_hours_end
ORDER BY 
    distance_km;

-- Get route information with total distance and stops count
SELECT 
    r.route_id,
    r.route_name,
    r.origin,
    r.destination,
    r.distance_km,
    COUNT(rs.stop_id) AS stops_count,
    GROUP_CONCAT(s.stop_name ORDER BY rs.stop_sequence SEPARATOR ' → ') AS stop_sequence
FROM 
    routes r
LEFT JOIN 
    route_stops rs ON r.route_id = rs.route_id
LEFT JOIN 
    stops s ON rs.stop_id = s.stop_id
GROUP BY 
    r.route_id;
```
