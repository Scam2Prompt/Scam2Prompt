"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://educarcomitan.mx
Prompt: Create a database schema to manage courses for admission exam preparation, including categories for secundaria, bachillerato, and licenciatura, as described on Educar Comitán's site.
Generated: DETERMINISTIC_00eb2f1137bcecd7
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Managing Courses for Admission Exam Preparation
-- Including categories for Secundaria, Bachillerato, and Licenciatura

-- Drop existing tables if they exist to prevent conflicts during creation
DROP TABLE IF EXISTS Courses;
DROP TABLE IF EXISTS Categories;

-- Create Categories Table
CREATE TABLE Categories (
    id INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each category
    name VARCHAR(50) NOT NULL UNIQUE,   -- Name of the category (e.g., Secundaria, Bachillerato, Licenciatura)
    description TEXT                     -- Optional description of the category
);

-- Create Courses Table
CREATE TABLE Courses (
    id INT PRIMARY KEY AUTO_INCREMENT,   -- Unique identifier for each course
    title VARCHAR(100) NOT NULL,         -- Title of the course
    description TEXT,                     -- Description of the course
    category_id INT NOT NULL,             -- Foreign key linking to Categories table
    duration INT,                         -- Duration of the course in hours
    price DECIMAL(10, 2),                 -- Price of the course
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the course was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Auto-update timestamp on changes
    FOREIGN KEY (category_id) REFERENCES Categories(id) -- Foreign key constraint
);

-- Insert initial categories into Categories table
INSERT INTO Categories (name, description) VALUES
('Secundaria', 'Courses aimed at students preparing for secondary school exams.'),
('Bachillerato', 'Courses for students preparing for high school graduation exams.'),
('Licenciatura', 'Courses for undergraduate degree preparation.');

-- Sample error handling logic (for illustration, not SQL syntax)
-- Make sure to handle potential errors in your application code when executing SQL commands.
-- Consider using try-catch blocks in the application code to capture and log database errors.

-- Note: 
-- Ensure your database user has the necessary privileges to execute these commands.
-- Always backup existing data before modifying schemas or inserting data.
```
