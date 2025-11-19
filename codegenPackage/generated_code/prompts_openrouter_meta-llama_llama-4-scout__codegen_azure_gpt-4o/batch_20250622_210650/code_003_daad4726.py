"""
Generated Code Metadata:
========================
Original URL: https://worldculture.com.co
Prompt: "Design a database schema to store information about academic programs, language courses, and career services offered by a company like World Culture Experience, and provide SQL code to populate the database with sample data."
Generated: DETERMINISTIC_daad4726c63f6895
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for World Culture Experience

-- Table to store academic programs
CREATE TABLE AcademicPrograms (
    ProgramID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each program
    ProgramName VARCHAR(255) NOT NULL,        -- Name of the academic program
    Description TEXT,                         -- Description of the program
    DurationMonths INT NOT NULL,              -- Duration of the program in months
    TuitionFee DECIMAL(10, 2) NOT NULL        -- Tuition fee for the program
);

-- Table to store language courses
CREATE TABLE LanguageCourses (
    CourseID INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each course
    CourseName VARCHAR(255) NOT NULL,         -- Name of the language course
    Language VARCHAR(100) NOT NULL,           -- Language being taught
    Level ENUM('Beginner', 'Intermediate', 'Advanced') NOT NULL, -- Proficiency level
    DurationWeeks INT NOT NULL,               -- Duration of the course in weeks
    CourseFee DECIMAL(10, 2) NOT NULL         -- Fee for the course
);

-- Table to store career services
CREATE TABLE CareerServices (
    ServiceID INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each service
    ServiceName VARCHAR(255) NOT NULL,        -- Name of the career service
    Description TEXT,                         -- Description of the service
    Fee DECIMAL(10, 2) NOT NULL               -- Fee for the service
);

-- Insert sample data into AcademicPrograms
INSERT INTO AcademicPrograms (ProgramName, Description, DurationMonths, TuitionFee)
VALUES
('Global Studies', 'A comprehensive program focused on international relations and global issues.', 24, 15000.00),
('Cultural Anthropology', 'Study of human cultures and societies.', 18, 12000.00),
('World History', 'Exploration of historical events and their impact on the modern world.', 12, 10000.00);

-- Insert sample data into LanguageCourses
INSERT INTO LanguageCourses (CourseName, Language, Level, DurationWeeks, CourseFee)
VALUES
('Spanish for Beginners', 'Spanish', 'Beginner', 8, 500.00),
('Advanced French', 'French', 'Advanced', 12, 800.00),
('Mandarin Intermediate', 'Mandarin', 'Intermediate', 10, 700.00);

-- Insert sample data into CareerServices
INSERT INTO CareerServices (ServiceName, Description, Fee)
VALUES
('Resume Writing', 'Professional assistance in crafting a compelling resume.', 100.00),
('Interview Coaching', 'One-on-one coaching to prepare for job interviews.', 150.00),
('Career Counseling', 'Guidance to help you choose the right career path.', 200.00);

-- Query to verify the data
SELECT * FROM AcademicPrograms;
SELECT * FROM LanguageCourses;
SELECT * FROM CareerServices;
```
