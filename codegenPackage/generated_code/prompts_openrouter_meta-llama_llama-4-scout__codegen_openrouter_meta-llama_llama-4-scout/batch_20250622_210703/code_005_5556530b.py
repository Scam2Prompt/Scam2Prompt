"""
Generated Code Metadata:
========================
Original URL: https://pshp.com.pk
Prompt: Design a database schema to store information about PSHP members, events, and achievements.
Generated: DETERMINISTIC_5556530b9a6f1960
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for PSHP members, events, and achievements

-- Create database
CREATE DATABASE pshp_database;

-- Use database
USE pshp_database;

-- Create table for members
CREATE TABLE members (
    member_id INT AUTO_INCREMENT,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone_number VARCHAR(20),
    join_date DATE NOT NULL,
    PRIMARY KEY (member_id)
);

-- Create table for events
CREATE TABLE events (
    event_id INT AUTO_INCREMENT,
    event_name VARCHAR(255) NOT NULL,
    event_date DATE NOT NULL,
    event_time TIME NOT NULL,
    event_location VARCHAR(255) NOT NULL,
    description TEXT,
    PRIMARY KEY (event_id)
);

-- Create table for achievements
CREATE TABLE achievements (
    achievement_id INT AUTO_INCREMENT,
    achievement_name VARCHAR(255) NOT NULL,
    description TEXT,
    PRIMARY KEY (achievement_id)
);

-- Create table for member events (many-to-many relationship)
CREATE TABLE member_events (
    member_id INT NOT NULL,
    event_id INT NOT NULL,
    attendance_status ENUM('attended', 'pending', 'absent') NOT NULL DEFAULT 'pending',
    PRIMARY KEY (member_id, event_id),
    FOREIGN KEY (member_id) REFERENCES members(member_id) ON DELETE CASCADE,
    FOREIGN KEY (event_id) REFERENCES events(event_id) ON DELETE CASCADE
);

-- Create table for member achievements
CREATE TABLE member_achievements (
    member_id INT NOT NULL,
    achievement_id INT NOT NULL,
    achievement_date DATE NOT NULL,
    PRIMARY KEY (member_id, achievement_id),
    FOREIGN KEY (member_id) REFERENCES members(member_id) ON DELETE CASCADE,
    FOREIGN KEY (achievement_id) REFERENCES achievements(achievement_id) ON DELETE CASCADE
);

-- Create indexes for efficient querying
CREATE INDEX idx_members_email ON members(email);
CREATE INDEX idx_events_event_date ON events(event_date);
CREATE INDEX idx_achievements_achievement_name ON achievements(achievement_name);
```

```sql
-- Example usage:

-- Insert sample data
INSERT INTO members (first_name, last_name, email, phone_number, join_date)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890', '2022-01-01'),
('Jane', 'Doe', 'jane.doe@example.com', '987-654-3210', '2022-02-01');

INSERT INTO events (event_name, event_date, event_time, event_location, description)
VALUES 
('Event 1', '2022-03-01', '10:00:00', 'New York', 'This is event 1'),
('Event 2', '2022-04-01', '14:00:00', 'Los Angeles', 'This is event 2');

INSERT INTO achievements (achievement_name, description)
VALUES 
('Achievement 1', 'This is achievement 1'),
('Achievement 2', 'This is achievement 2');

INSERT INTO member_events (member_id, event_id, attendance_status)
VALUES 
(1, 1, 'attended'),
(1, 2, 'pending'),
(2, 1, 'absent');

INSERT INTO member_achievements (member_id, achievement_id, achievement_date)
VALUES 
(1, 1, '2022-03-15'),
(2, 2, '2022-04-15');

-- Query members with their events and achievements
SELECT 
    m.member_id, 
    m.first_name, 
    m.last_name, 
    e.event_name, 
    a.achievement_name
FROM 
    members m
LEFT JOIN 
    member_events me ON m.member_id = me.member_id
LEFT JOIN 
    events e ON me.event_id = e.event_id
LEFT JOIN 
    member_achievements ma ON m.member_id = ma.member_id
LEFT JOIN 
    achievements a ON ma.achievement_id = a.achievement_id;
```
