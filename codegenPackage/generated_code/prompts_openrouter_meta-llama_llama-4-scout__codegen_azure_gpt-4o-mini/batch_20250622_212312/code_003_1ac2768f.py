"""
Generated Code Metadata:
========================
Original URL: https://jhpsgaya.com
Prompt: Design a database schema for storing student information, academic subjects, and co-curricular activities for a school like JHPS Gaya.
Generated: DETERMINISTIC_1ac2768f9ca51940
Batch ID: 20250622_212312
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing student information, academic subjects, and co-curricular activities for JHPS Gaya

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Students;
DROP TABLE IF EXISTS Subjects;
DROP TABLE IF EXISTS Activities;
DROP TABLE IF EXISTS StudentSubjects;
DROP TABLE IF EXISTS StudentActivities;

-- Table to store student information
CREATE TABLE Students (
    student_id SERIAL PRIMARY KEY, -- Unique identifier for each student
    first_name VARCHAR(50) NOT NULL, -- Student's first name
    last_name VARCHAR(50) NOT NULL, -- Student's last name
    date_of_birth DATE NOT NULL, -- Student's date of birth
    enrollment_date DATE NOT NULL, -- Date when the student enrolled
    grade_level INT NOT NULL CHECK (grade_level BETWEEN 1 AND 12), -- Grade level of the student
    email VARCHAR(100) UNIQUE, -- Student's email address
    phone_number VARCHAR(15) -- Student's phone number
);

-- Table to store academic subjects
CREATE TABLE Subjects (
    subject_id SERIAL PRIMARY KEY, -- Unique identifier for each subject
    subject_name VARCHAR(100) NOT NULL UNIQUE, -- Name of the subject
    subject_code VARCHAR(10) NOT NULL UNIQUE -- Unique code for the subject
);

-- Table to store co-curricular activities
CREATE TABLE Activities (
    activity_id SERIAL PRIMARY KEY, -- Unique identifier for each activity
    activity_name VARCHAR(100) NOT NULL UNIQUE, -- Name of the activity
    description TEXT -- Description of the activity
);

-- Junction table to associate students with subjects
CREATE TABLE StudentSubjects (
    student_id INT NOT NULL, -- Foreign key referencing Students
    subject_id INT NOT NULL, -- Foreign key referencing Subjects
    PRIMARY KEY (student_id, subject_id), -- Composite primary key
    FOREIGN KEY (student_id) REFERENCES Students(student_id) ON DELETE CASCADE, -- Delete student records and associated subjects
    FOREIGN KEY (subject_id) REFERENCES Subjects(subject_id) ON DELETE CASCADE -- Delete subject records and associated students
);

-- Junction table to associate students with activities
CREATE TABLE StudentActivities (
    student_id INT NOT NULL, -- Foreign key referencing Students
    activity_id INT NOT NULL, -- Foreign key referencing Activities
    PRIMARY KEY (student_id, activity_id), -- Composite primary key
    FOREIGN KEY (student_id) REFERENCES Students(student_id) ON DELETE CASCADE, -- Delete student records and associated activities
    FOREIGN KEY (activity_id) REFERENCES Activities(activity_id) ON DELETE CASCADE -- Delete activity records and associated students
);

-- Sample data insertion (optional, for testing purposes)
-- INSERT INTO Students (first_name, last_name, date_of_birth, enrollment_date, grade_level, email, phone_number) VALUES
-- ('John', 'Doe', '2005-05-15', '2020-08-01', 10, 'john.doe@example.com', '1234567890');

-- INSERT INTO Subjects (subject_name, subject_code) VALUES
-- ('Mathematics', 'MATH101'),
-- ('Science', 'SCI101');

-- INSERT INTO Activities (activity_name, description) VALUES
-- ('Basketball', 'Team sport played on a court'),
-- ('Drama Club', 'Theatrical performances and acting workshops');
```
