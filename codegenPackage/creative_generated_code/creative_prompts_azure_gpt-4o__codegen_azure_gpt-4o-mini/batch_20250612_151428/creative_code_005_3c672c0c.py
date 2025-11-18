"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anima.art.br
Prompt: Write a SQL query to store and retrieve information about Ânima's art courses, including course names like "história em quadrinhos" and "pintura em tela."
Generated: DETERMINISTIC_3c672c0c847b8577
Batch ID: 20250612_151428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Create a table to store information about Anima's art courses
CREATE TABLE ArtCourses (
    CourseID INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each course
    CourseName VARCHAR(255) NOT NULL,         -- Name of the course
    Description TEXT,                          -- Description of the course
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Insert sample data into the ArtCourses table
INSERT INTO ArtCourses (CourseName, Description) VALUES
('história em quadrinhos', 'Um curso sobre a arte e a narrativa das histórias em quadrinhos.'),
('pintura em tela', 'Um curso que ensina técnicas de pintura em tela.');

-- Retrieve all courses from the ArtCourses table
SELECT 
    CourseID, 
    CourseName, 
    Description, 
    CreatedAt, 
    UpdatedAt 
FROM 
    ArtCourses;

-- Error handling can be performed in the application layer where this SQL is executed.
-- Ensure that the application checks for errors after executing these statements.
```
