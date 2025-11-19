"""
Generated Code Metadata:
========================
Original URL: https://cle.com
Prompt: Design a database schema to store information about CLE conferences, including speaker names, topics, and locations, based on the data available on the CLE International website.
Generated: DETERMINISTIC_31407738e1fb82d3
Batch ID: 20250622_205228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for CLE conferences

-- Create a database
CREATE DATABASE cle_conferences;

-- Use the database
USE cle_conferences;

-- Create a table for speakers
CREATE TABLE speakers (
  id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  bio TEXT,
  PRIMARY KEY (id)
);

-- Create a table for topics
CREATE TABLE topics (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  PRIMARY KEY (id)
);

-- Create a table for locations
CREATE TABLE locations (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  address VARCHAR(255) NOT NULL,
  city VARCHAR(100) NOT NULL,
  country VARCHAR(100) NOT NULL,
  PRIMARY KEY (id)
);

-- Create a table for conferences
CREATE TABLE conferences (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  start_date DATE NOT NULL,
  end_date DATE NOT NULL,
  location_id INT,
  PRIMARY KEY (id),
  FOREIGN KEY (location_id) REFERENCES locations(id)
);

-- Create a table for conference speakers
CREATE TABLE conference_speakers (
  conference_id INT NOT NULL,
  speaker_id INT NOT NULL,
  PRIMARY KEY (conference_id, speaker_id),
  FOREIGN KEY (conference_id) REFERENCES conferences(id),
  FOREIGN KEY (speaker_id) REFERENCES speakers(id)
);

-- Create a table for conference topics
CREATE TABLE conference_topics (
  conference_id INT NOT NULL,
  topic_id INT NOT NULL,
  PRIMARY KEY (conference_id, topic_id),
  FOREIGN KEY (conference_id) REFERENCES conferences(id),
  FOREIGN KEY (topic_id) REFERENCES topics(id)
);

-- Example data
INSERT INTO speakers (first_name, last_name, bio)
VALUES 
('John', 'Doe', 'Software engineer with 10 years of experience'),
('Jane', 'Smith', 'Data scientist with 5 years of experience');

INSERT INTO topics (name, description)
VALUES 
('Artificial Intelligence', 'AI and machine learning topics'),
('Cybersecurity', 'Security topics');

INSERT INTO locations (name, address, city, country)
VALUES 
('Hotel A', '123 Main St', 'New York', 'USA'),
('Hotel B', '456 Park Ave', 'London', 'UK');

INSERT INTO conferences (name, start_date, end_date, location_id)
VALUES 
('CLE 2024', '2024-01-01', '2024-01-03', 1),
('CLE 2025', '2025-06-01', '2025-06-03', 2);

INSERT INTO conference_speakers (conference_id, speaker_id)
VALUES 
(1, 1),
(1, 2),
(2, 1);

INSERT INTO conference_topics (conference_id, topic_id)
VALUES 
(1, 1),
(1, 2),
(2, 1);
```
