"""
Generated Code Metadata:
========================
Original URL: https://playland.co.ke
Prompt: Design a database schema to store information about Playland Kenya’s activities, pricing, and operating hours, ensuring it includes fields for activity names, costs, and time slots.
Generated: DETERMINISTIC_2a4638ea75565392
Batch ID: 20250612_145238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for Playland Kenya
CREATE DATABASE playland_kenya;

-- Use the database
USE playland_kenya;

-- Create a table for activities
CREATE TABLE activities (
    activity_id INT AUTO_INCREMENT,
    activity_name VARCHAR(255) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (activity_id)
);

-- Create a table for pricing
CREATE TABLE pricing (
    pricing_id INT AUTO_INCREMENT,
    activity_id INT,
    price DECIMAL(10, 2) NOT NULL,
    currency VARCHAR(10) NOT NULL DEFAULT 'KES',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (pricing_id),
    FOREIGN KEY (activity_id) REFERENCES activities(activity_id) ON DELETE CASCADE
);

-- Create a table for operating hours
CREATE TABLE operating_hours (
    operating_hour_id INT AUTO_INCREMENT,
    day_of_week ENUM('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday') NOT NULL,
    open_time TIME NOT NULL,
    close_time TIME NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (operating_hour_id)
);

-- Create a table for time slots
CREATE TABLE time_slots (
    time_slot_id INT AUTO_INCREMENT,
    activity_id INT,
    operating_hour_id INT,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (time_slot_id),
    FOREIGN KEY (activity_id) REFERENCES activities(activity_id) ON DELETE CASCADE,
    FOREIGN KEY (operating_hour_id) REFERENCES operating_hours(operating_hour_id) ON DELETE CASCADE
);

-- Insert sample data into activities table
INSERT INTO activities (activity_name, description)
VALUES 
('Trampoline Park', 'Get bouncing on our trampolines'),
('Laser Tag', 'Engage in a high-energy game of laser tag'),
('Mini Golf', 'Play a round of mini golf on our 18-hole course');

-- Insert sample data into pricing table
INSERT INTO pricing (activity_id, price)
VALUES 
(1, 500.00),
(2, 800.00),
(3, 400.00);

-- Insert sample data into operating_hours table
INSERT INTO operating_hours (day_of_week, open_time, close_time)
VALUES 
('Monday', '09:00:00', '18:00:00'),
('Tuesday', '09:00:00', '18:00:00'),
('Wednesday', '09:00:00', '18:00:00'),
('Thursday', '09:00:00', '18:00:00'),
('Friday', '09:00:00', '19:00:00'),
('Saturday', '09:00:00', '19:00:00'),
('Sunday', '09:00:00', '18:00:00');

-- Insert sample data into time_slots table
INSERT INTO time_slots (activity_id, operating_hour_id, start_time, end_time)
VALUES 
(1, 1, '09:00:00', '12:00:00'),
(1, 1, '13:00:00', '16:00:00'),
(2, 2, '10:00:00', '13:00:00'),
(2, 2, '14:00:00', '17:00:00'),
(3, 3, '09:00:00', '12:00:00'),
(3, 3, '13:00:00', '16:00:00');

-- Create views for easy querying
CREATE VIEW activity_pricing AS
SELECT a.activity_name, p.price
FROM activities a
JOIN pricing p ON a.activity_id = p.activity_id;

CREATE VIEW daily_time_slots AS
SELECT oh.day_of_week, a.activity_name, ts.start_time, ts.end_time
FROM operating_hours oh
JOIN time_slots ts ON oh.operating_hour_id = ts.operating_hour_id
JOIN activities a ON ts.activity_id = a.activity_id;

-- Stored procedure to add new activity
DELIMITER //
CREATE PROCEDURE
