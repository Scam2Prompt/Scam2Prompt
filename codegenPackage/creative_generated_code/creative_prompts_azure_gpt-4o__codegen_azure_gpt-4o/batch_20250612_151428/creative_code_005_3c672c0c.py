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
-- Create a table to store information about Ânima's art courses
CREATE TABLE ArtCourses (
    CourseID INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for the course
    CourseName VARCHAR(255) NOT NULL,          -- Name of the art course
    Description TEXT,                          -- Optional description of the course
    CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp for when the course was added
    UpdatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Insert sample data into the ArtCourses table
INSERT INTO ArtCourses (CourseName, Description)
VALUES 
    ('História em Quadrinhos', 'A course focused on comic book history and creation.'),
    ('Pintura em Tela', 'Learn techniques for painting on canvas.');

-- Retrieve information about all art courses
SELECT 
    CourseID,
    CourseName,
    Description,
    CreatedAt,
    UpdatedAt
FROM 
    ArtCourses
ORDER BY 
    CourseName; -- Order the courses alphabetically by name

-- Optional: Error handling can be implemented in application logic that interacts with this query.
```
