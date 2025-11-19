"""
Generated Code Metadata:
========================
Original URL: https://ecbc.online
Prompt: Design a MySQL database schema to store information about ECBC Radio's programs, hosts, and playlists, and provide a sample query to retrieve the program schedule for a specific day of the week.
Generated: DETERMINISTIC_c3bf2a5330a77c5f
Batch ID: 20250622_211335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema
CREATE DATABASE ecbc_radio;

-- Use database schema
USE ecbc_radio;

-- Create table for programs
CREATE TABLE programs (
  program_id INT AUTO_INCREMENT,
  program_name VARCHAR(255) NOT NULL,
  program_description TEXT,
  day_of_week ENUM('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday') NOT NULL,
  start_time TIME NOT NULL,
  end_time TIME NOT NULL,
  PRIMARY KEY (program_id)
);

-- Create table for hosts
CREATE TABLE hosts (
  host_id INT AUTO_INCREMENT,
  host_name VARCHAR(255) NOT NULL,
  host_bio TEXT,
  PRIMARY KEY (host_id)
);

-- Create table for program hosts
CREATE TABLE program_hosts (
  program_id INT NOT NULL,
  host_id INT NOT NULL,
  PRIMARY KEY (program_id, host_id),
  FOREIGN KEY (program_id) REFERENCES programs(program_id) ON DELETE CASCADE,
  FOREIGN KEY (host_id) REFERENCES hosts(host_id) ON DELETE CASCADE
);

-- Create table for playlists
CREATE TABLE playlists (
  playlist_id INT AUTO_INCREMENT,
  program_id INT NOT NULL,
  song_title VARCHAR(255) NOT NULL,
  artist_name VARCHAR(255) NOT NULL,
  play_time TIME NOT NULL,
  PRIMARY KEY (playlist_id),
  FOREIGN KEY (program_id) REFERENCES programs(program_id) ON DELETE CASCADE
);

-- Insert sample data
INSERT INTO programs (program_name, program_description, day_of_week, start_time, end_time)
VALUES 
('Morning Show', 'The morning show with the latest news and updates', 'Monday', '06:00:00', '10:00:00'),
('Afternoon Drive', 'The afternoon drive with your favorite music', 'Monday', '16:00:00', '20:00:00');

INSERT INTO hosts (host_name, host_bio)
VALUES 
('John Doe', 'John is a well-known radio host with years of experience'),
('Jane Smith', 'Jane is a talented radio host with a passion for music');

INSERT INTO program_hosts (program_id, host_id)
VALUES 
(1, 1),
(2, 2);

INSERT INTO playlists (program_id, song_title, artist_name, play_time)
VALUES 
(1, 'Song 1', 'Artist 1', '06:30:00'),
(1, 'Song 2', 'Artist 2', '07:00:00'),
(2, 'Song 3', 'Artist 3', '16:30:00');

-- Sample query to retrieve program schedule for a specific day of the week
SELECT 
  p.program_name, 
  p.start_time, 
  p.end_time, 
  h.host_name
FROM 
  programs p
  LEFT JOIN program_hosts ph ON p.program_id = ph.program_id
  LEFT JOIN hosts h ON ph.host_id = h.host_id
WHERE 
  p.day_of_week = 'Monday'
ORDER BY 
  p.start_time;
```
