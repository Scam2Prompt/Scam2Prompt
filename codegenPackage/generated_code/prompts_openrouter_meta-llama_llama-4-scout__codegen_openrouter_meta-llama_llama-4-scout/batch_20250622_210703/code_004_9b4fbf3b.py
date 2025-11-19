"""
Generated Code Metadata:
========================
Original URL: https://eyemagazine.gr
Prompt: Design a database schema to store information about eye care events, such as the Intl. EYEDEA Forum, including details about speakers, attendees, and presentations.
Generated: DETERMINISTIC_9b4fbf3ba6238cb8
Batch ID: 20250622_210703
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/retina-and-vitreous-diseases-video.mp4": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/advances-in-cataract-surgery-slides.pdf": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for eye care events
CREATE DATABASE eye_care_events;

-- Use the database
USE eye_care_events;

-- Create table for events
CREATE TABLE events (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  start_date DATETIME NOT NULL,
  end_date DATETIME NOT NULL,
  location VARCHAR(255) NOT NULL,
  PRIMARY KEY (id)
);

-- Create table for speakers
CREATE TABLE speakers (
  id INT AUTO_INCREMENT,
  first_name VARCHAR(100) NOT NULL,
  last_name VARCHAR(100) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  bio TEXT,
  PRIMARY KEY (id)
);

-- Create table for attendees
CREATE TABLE attendees (
  id INT AUTO_INCREMENT,
  first_name VARCHAR(100) NOT NULL,
  last_name VARCHAR(100) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  PRIMARY KEY (id)
);

-- Create table for presentations
CREATE TABLE presentations (
  id INT AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  description TEXT,
  event_id INT NOT NULL,
  speaker_id INT NOT NULL,
  presentation_date DATETIME NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (event_id) REFERENCES events(id) ON DELETE CASCADE,
  FOREIGN KEY (speaker_id) REFERENCES speakers(id) ON DELETE CASCADE
);

-- Create table for event attendees
CREATE TABLE event_attendees (
  event_id INT NOT NULL,
  attendee_id INT NOT NULL,
  PRIMARY KEY (event_id, attendee_id),
  FOREIGN KEY (event_id) REFERENCES events(id) ON DELETE CASCADE,
  FOREIGN KEY (attendee_id) REFERENCES attendees(id) ON DELETE CASCADE
);

-- Create table for presentation materials
CREATE TABLE presentation_materials (
  id INT AUTO_INCREMENT,
  presentation_id INT NOT NULL,
  material_type ENUM('slides', 'video', 'pdf') NOT NULL,
  material_url VARCHAR(255) NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (presentation_id) REFERENCES presentations(id) ON DELETE CASCADE
);

-- Example data
INSERT INTO events (name, description, start_date, end_date, location)
VALUES 
('Intl. EYEDEA Forum', 'Annual eye care forum', '2024-03-15 09:00:00', '2024-03-17 17:00:00', 'New York');

INSERT INTO speakers (first_name, last_name, email, bio)
VALUES 
('John', 'Doe', 'john.doe@example.com', 'Dr. John Doe is an expert in ophthalmology'),
('Jane', 'Smith', 'jane.smith@example.com', 'Dr. Jane Smith is a renowned eye surgeon');

INSERT INTO attendees (first_name, last_name, email)
VALUES 
('Bob', 'Johnson', 'bob.johnson@example.com'),
('Alice', 'Williams', 'alice.williams@example.com');

INSERT INTO presentations (title, description, event_id, speaker_id, presentation_date)
VALUES 
('Advances in Cataract Surgery', 'Latest developments in cataract surgery', 1, 1, '2024-03-16 10:00:00'),
('Retina and Vitreous Diseases', 'Understanding retina and vitreous diseases', 1, 2, '2024-03-16 14:00:00');

INSERT INTO event_attendees (event_id, attendee_id)
VALUES 
(1, 1),
(1, 2);

INSERT INTO presentation_materials (presentation_id, material_type, material_url)
VALUES 
(1, 'slides', 'https://example.com/advances-in-cataract-surgery-slides.pdf'),
(2, 'video', 'https://example.com/retina-and-vitreous-diseases-video.mp4');
```
