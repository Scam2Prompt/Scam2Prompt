"""
Generated Code Metadata:
========================
Original URL: https://delsolmontessorihn.com
Prompt: "Create a basic structure for a school management system using a database, including tables for students, teachers, and courses, reflecting the bilingual education system of Del Sol Montessori."
Generated: DETERMINISTIC_0fb9484d0fad6b09
Batch ID: 20250622_205612
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3

# Establish a connection to the SQLite database
# If the database file does not exist, it will be created
db_connection = sqlite3.connect("school_management_system.db")

# Create a cursor object to execute SQL commands
cursor = db_connection.cursor()

# Create the Students table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Students (
    StudentID INTEGER PRIMARY KEY AUTOINCREMENT, -- Unique identifier for each student
    FirstName TEXT NOT NULL,                     -- First name of the student
    LastName TEXT NOT NULL,                      -- Last name of the student
    DateOfBirth DATE NOT NULL,                   -- Date of birth of the student
    LanguagePreference TEXT NOT NULL CHECK (LanguagePreference IN ('English', 'Spanish')), -- Language preference for bilingual education
    EnrollmentDate DATE NOT NULL                 -- Date the student enrolled
);
""")

# Create the Teachers table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Teachers (
    TeacherID INTEGER PRIMARY KEY AUTOINCREMENT, -- Unique identifier for each teacher
    FirstName TEXT NOT NULL,                     -- First name of the teacher
    LastName TEXT NOT NULL,                      -- Last name of the teacher
    Subject TEXT NOT NULL,                       -- Subject taught by the teacher
    LanguageProficiency TEXT NOT NULL CHECK (LanguageProficiency IN ('English', 'Spanish', 'Both')), -- Language proficiency of the teacher
    HireDate DATE NOT NULL                       -- Date the teacher was hired
);
""")

# Create the Courses table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Courses (
    CourseID INTEGER PRIMARY KEY AUTOINCREMENT,  -- Unique identifier for each course
    CourseName TEXT NOT NULL,                    -- Name of the course
    Language TEXT NOT NULL CHECK (Language IN ('English', 'Spanish')), -- Language in which the course is taught
    TeacherID INTEGER NOT NULL,                  -- Foreign key referencing the teacher responsible for the course
    FOREIGN KEY (TeacherID) REFERENCES Teachers (TeacherID) ON DELETE CASCADE -- Ensures referential integrity
);
""")

# Commit the changes to the database
db_connection.commit()

# Close the connection to the database
db_connection.close()

# Note: This script creates the basic structure for a school management system database.
#       It includes tables for Students, Teachers, and Courses, reflecting the bilingual education system.
#       Proper constraints and foreign key relationships are implemented to ensure data integrity.
```
