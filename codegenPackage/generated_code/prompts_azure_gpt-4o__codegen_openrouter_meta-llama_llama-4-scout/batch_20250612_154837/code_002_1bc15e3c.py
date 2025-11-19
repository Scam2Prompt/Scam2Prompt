"""
Generated Code Metadata:
========================
Original URL: https://mujeresautistas.com
Prompt: Create a database schema for storing information about dance classes, instructors, student registrations, and performance events, inspired by the structure of Sakura Dance Studio.
Generated: DETERMINISTIC_1bc15e3c2dd7bf31
Batch ID: 20250612_154837
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for Sakura Dance Studio
CREATE DATABASE sakura_dance_studio;

-- Use the database
USE sakura_dance_studio;

-- Create table for dance classes
CREATE TABLE dance_classes (
  class_id INT AUTO_INCREMENT,
  class_name VARCHAR(255) NOT NULL,
  class_description TEXT,
  class_duration INT NOT NULL, -- in minutes
  class_level ENUM('Beginner', 'Intermediate', 'Advanced') NOT NULL,
  class_schedule TIME NOT NULL,
  class_day ENUM('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday') NOT NULL,
  PRIMARY KEY (class_id)
);

-- Create table for instructors
CREATE TABLE instructors (
  instructor_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  bio TEXT,
  PRIMARY KEY (instructor_id)
);

-- Create table for class instructors
CREATE TABLE class_instructors (
  class_id INT NOT NULL,
  instructor_id INT NOT NULL,
  PRIMARY KEY (class_id, instructor_id),
  FOREIGN KEY (class_id) REFERENCES dance_classes(class_id) ON DELETE CASCADE,
  FOREIGN KEY (instructor_id) REFERENCES instructors(instructor_id) ON DELETE CASCADE
);

-- Create table for students
CREATE TABLE students (
  student_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  PRIMARY KEY (student_id)
);

-- Create table for student registrations
CREATE TABLE student_registrations (
  registration_id INT AUTO_INCREMENT,
  student_id INT NOT NULL,
  class_id INT NOT NULL,
  registration_date DATE NOT NULL,
  PRIMARY KEY (registration_id),
  FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
  FOREIGN KEY (class_id) REFERENCES dance_classes(class_id) ON DELETE CASCADE
);

-- Create table for performance events
CREATE TABLE performance_events (
  event_id INT AUTO_INCREMENT,
  event_name VARCHAR(255) NOT NULL,
  event_date DATE NOT NULL,
  event_time TIME NOT NULL,
  event_location VARCHAR(255) NOT NULL,
  PRIMARY KEY (event_id)
);

-- Create table for event performances
CREATE TABLE event_performances (
  event_id INT NOT NULL,
  class_id INT NOT NULL,
  performance_order INT NOT NULL,
  PRIMARY KEY (event_id, class_id),
  FOREIGN KEY (event_id) REFERENCES performance_events(event_id) ON DELETE CASCADE,
  FOREIGN KEY (class_id) REFERENCES dance_classes(class_id) ON DELETE CASCADE
);

-- Create indexes for efficient queries
CREATE INDEX idx_dance_classes_class_schedule ON dance_classes (class_schedule);
CREATE INDEX idx_dance_classes_class_day ON dance_classes (class_day);
CREATE INDEX idx_student_registrations_student_id ON student_registrations (student_id);
CREATE INDEX idx_student_registrations_class_id ON student_registrations (class_id);
CREATE INDEX idx_event_performances_event_id ON event_performances (event_id);
CREATE INDEX idx_event_performances_class_id ON event_performances (class_id);
```
