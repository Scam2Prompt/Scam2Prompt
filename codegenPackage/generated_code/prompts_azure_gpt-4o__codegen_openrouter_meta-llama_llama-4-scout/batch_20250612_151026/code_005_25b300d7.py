"""
Generated Code Metadata:
========================
Original URL: https://virtual5.com.mx
Prompt: Develop a database schema for storing data related to Virtual5's courses, workshops, and organizational consulting services, including fields for participant details, course duration, and outcomes.
Generated: DETERMINISTIC_25b300d782fed50f
Batch ID: 20250612_151026
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create a database for Virtual5's services
CREATE DATABASE virtual5_services;

-- Use the virtual5_services database
USE virtual5_services;

-- Create a table for courses
CREATE TABLE courses (
  id INT AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  description TEXT,
  duration_hours INT,
  start_date DATE,
  end_date DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for workshops
CREATE TABLE workshops (
  id INT AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  description TEXT,
  duration_hours INT,
  start_date DATE,
  end_date DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for organizational consulting services
CREATE TABLE consulting_services (
  id INT AUTO_INCREMENT,
  service_type VARCHAR(255) NOT NULL,
  description TEXT,
  duration_hours INT,
  start_date DATE,
  end_date DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for participants
CREATE TABLE participants (
  id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a many-to-many relationship table for course participants
CREATE TABLE course_participants (
  course_id INT,
  participant_id INT,
  outcome VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (course_id, participant_id),
  FOREIGN KEY (course_id) REFERENCES courses(id) ON DELETE CASCADE,
  FOREIGN KEY (participant_id) REFERENCES participants(id) ON DELETE CASCADE
);

-- Create a many-to-many relationship table for workshop participants
CREATE TABLE workshop_participants (
  workshop_id INT,
  participant_id INT,
  outcome VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (workshop_id, participant_id),
  FOREIGN KEY (workshop_id) REFERENCES workshops(id) ON DELETE CASCADE,
  FOREIGN KEY (participant_id) REFERENCES participants(id) ON DELETE CASCADE
);

-- Create a many-to-many relationship table for consulting service participants
CREATE TABLE consulting_service_participants (
  consulting_service_id INT,
  participant_id INT,
  outcome VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (consulting_service_id, participant_id),
  FOREIGN KEY (consulting_service_id) REFERENCES consulting_services(id) ON DELETE CASCADE,
  FOREIGN KEY (participant_id) REFERENCES participants(id) ON DELETE CASCADE
);

-- Create indexes for faster queries
CREATE INDEX idx_courses_title ON courses(title);
CREATE INDEX idx_workshops_title ON workshops(title);
CREATE INDEX idx_consulting_services_service_type ON consulting_services(service_type);
CREATE INDEX idx_participants_email ON participants(email);
```

```sql
-- example_data.sql

-- Insert example data into the database
INSERT INTO courses (title, description, duration_hours, start_date, end_date)
VALUES
  ('Introduction to Python', 'Learn the basics of Python programming', 12, '2022-01-01', '2022-01-03'),
  ('Advanced JavaScript', 'Take your JavaScript skills to the next level', 16, '2022-02-01', '2022-02-04');

INSERT INTO workshops (title, description, duration_hours, start_date, end_date)
VALUES
  ('Agile Methodologies', 'Learn about Agile development methodologies', 8, '2022-03-01', '2022-03-02'),
  ('DevOps Fundamentals', 'Understand the basics of DevOps', 12, '2022-04-01', '2022-04-03');

INSERT INTO consulting_services (service_type, description, duration_hours, start_date, end_date)
VALUES
  ('IT Consulting', 'Get expert advice on IT strategy and implementation', 20, '2022-05-01', '2022-05-15'),
  ('Digital Transformation', 'Transform your business with our digital expertise', 40, '2022-06-01', '2022-07-15');

INSERT INTO participants (first_name, last_name, email, phone_number)
VALUES
  ('John', 'Doe', 'john.doe@example.com', '123-456-7890'),
  ('Jane', 'Smith', 'jane.smith@example.com', '987-654-3210');

INSERT INTO course_participants (course_id, participant_id, outcome)
VALUES
  (1, 1, 'Completed'),
  (1, 2, 'Completed'),
  (2, 1, 'In Progress');

INSERT INTO workshop_participants (workshop_id, participant_id, outcome)
VALUES
  (1, 1, 'Completed'),
  (2, 2, 'Completed');

INSERT INTO consulting_service_participants (consulting_service_id, participant_id, outcome)
VALUES
  (1, 1, 'Completed'),
  (2, 2, 'In Progress');
```
