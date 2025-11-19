"""
Generated Code Metadata:
========================
Original URL: https://openmindsinstituto.com.br
Prompt: Generate code to structure a database for managing courses and study groups in speech-language pathology, including fields for course type (EAD or presencial), topics (e.g., orofacial motricity), and participant registration.
Generated: DETERMINISTIC_8ce8fb238dca7a5a
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for managing courses and study groups in speech-language pathology
CREATE DATABASE speech_language_pathology;

-- Use the created database
USE speech_language_pathology;

-- Create a table for course types
CREATE TABLE course_types (
  id INT AUTO_INCREMENT,
  type VARCHAR(10) NOT NULL CHECK (type IN ('EAD', 'presencial')),
  description VARCHAR(255),
  PRIMARY KEY (id)
);

-- Create a table for topics
CREATE TABLE topics (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  PRIMARY KEY (id)
);

-- Create a table for courses
CREATE TABLE courses (
  id INT AUTO_INCREMENT,
  course_type_id INT NOT NULL,
  topic_id INT NOT NULL,
  title VARCHAR(255) NOT NULL,
  start_date DATE NOT NULL,
  end_date DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (course_type_id) REFERENCES course_types(id),
  FOREIGN KEY (topic_id) REFERENCES topics(id)
);

-- Create a table for participants
CREATE TABLE participants (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone VARCHAR(20),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for course participants
CREATE TABLE course_participants (
  course_id INT NOT NULL,
  participant_id INT NOT NULL,
  registration_date DATE NOT NULL,
  PRIMARY KEY (course_id, participant_id),
  FOREIGN KEY (course_id) REFERENCES courses(id),
  FOREIGN KEY (participant_id) REFERENCES participants(id)
);

-- Create a table for study groups
CREATE TABLE study_groups (
  id INT AUTO_INCREMENT,
  course_id INT NOT NULL,
  group_name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (course_id) REFERENCES courses(id)
);

-- Create a table for study group participants
CREATE TABLE study_group_participants (
  study_group_id INT NOT NULL,
  participant_id INT NOT NULL,
  PRIMARY KEY (study_group_id, participant_id),
  FOREIGN KEY (study_group_id) REFERENCES study_groups(id),
  FOREIGN KEY (participant_id) REFERENCES participants(id)
);

-- Insert some sample data
INSERT INTO course_types (type, description) 
VALUES 
('EAD', 'Online course'),
('presencial', 'In-person course');

INSERT INTO topics (name, description) 
VALUES 
('Orofacial Motricity', 'Study of the muscles of the face and mouth'),
('Language Development', 'Study of language development in children');

INSERT INTO courses (course_type_id, topic_id, title, start_date, end_date) 
VALUES 
(1, 1, 'EAD Orofacial Motricity', '2024-01-01', '2024-06-30'),
(2, 2, 'Presencial Language Development', '2024-03-01', '2024-08-31');

INSERT INTO participants (name, email, phone) 
VALUES 
('John Doe', 'john@example.com', '1234567890'),
('Jane Doe', 'jane@example.com', '9876543210');

INSERT INTO course_participants (course_id, participant_id, registration_date) 
VALUES 
(1, 1, '2024-01-15'),
(1, 2, '2024-02-01'),
(2, 1, '2024-03-15');

INSERT INTO study_groups (course_id, group_name, description) 
VALUES 
(1, 'Group 1', 'Discussion group for EAD Orofacial Motricity'),
(2, 'Group 2', 'Discussion group for Presencial Language Development');

INSERT INTO study_group_participants (study_group_id, participant_id) 
VALUES 
(1, 1),
(1, 2),
(2, 1);
```
