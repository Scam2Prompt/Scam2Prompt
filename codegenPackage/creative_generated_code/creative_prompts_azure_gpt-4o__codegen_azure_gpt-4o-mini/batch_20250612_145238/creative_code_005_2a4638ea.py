"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://playland.co.ke
Prompt: Design a database schema to store information about Playland Kenya’s activities, pricing, and operating hours, ensuring it includes fields for activity names, costs, and time slots.
Generated: DETERMINISTIC_2a4638ea75565392
Batch ID: 20250612_145238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for Playland Kenya activities
CREATE DATABASE playland_kenya;

USE playland_kenya;

-- Table to store information about activities
CREATE TABLE activities (
    activity_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each activity
    name VARCHAR(255) NOT NULL, -- Name of the activity
    cost DECIMAL(10, 2) NOT NULL, -- Cost of the activity, with 2 decimal places
    description TEXT, -- Description of the activity
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the activity was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of when the activity was last updated
);

-- Table to store time slots for each activity
CREATE TABLE time_slots (
    time_slot_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each time slot
    activity_id INT NOT NULL, -- Foreign key referencing activities
    start_time TIME NOT NULL, -- Start time of the activity
    end_time TIME NOT NULL, -- End time of the activity
    CONSTRAINT fk_activity
        FOREIGN KEY (activity_id) 
        REFERENCES activities(activity_id)
        ON DELETE CASCADE, -- Delete time slots if the corresponding activity is deleted
    UNIQUE (activity_id, start_time) -- Ensure no overlapping time slots for the same activity
);

-- Table to store operating hours for the facility
CREATE TABLE operating_hours (
    day_of_week ENUM('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday') PRIMARY KEY, -- Day of the week
    open_time TIME NOT NULL, -- Opening time of the facility
    close_time TIME NOT NULL -- Closing time of the facility
);

-- Sample data for activities
INSERT INTO activities (name, cost, description) VALUES
('Bouncing Castle', 500.00, 'A fun bouncing activity for kids.'),
('Mini Golf', 1000.00, 'A miniature golf experience for all ages.'),
('Trampoline Park', 800.00, 'Jump and play in the trampoline area.');

-- Sample data for time slots
INSERT INTO time_slots (activity_id, start_time, end_time) VALUES
(1, '10:00:00', '12:00:00'),
(1, '13:00:00', '15:00:00'),
(2, '09:00:00', '11:00:00'),
(3, '11:00:00', '14:00:00');

-- Sample data for operating hours
INSERT INTO operating_hours (day_of_week, open_time, close_time) VALUES
('Monday', '09:00:00', '18:00:00'),
('Tuesday', '09:00:00', '18:00:00'),
('Wednesday', '09:00:00', '18:00:00'),
('Thursday', '09:00:00', '18:00:00'),
('Friday', '09:00:00', '20:00:00'),
('Saturday', '10:00:00', '20:00:00'),
('Sunday', '10:00:00', '18:00:00');
```
