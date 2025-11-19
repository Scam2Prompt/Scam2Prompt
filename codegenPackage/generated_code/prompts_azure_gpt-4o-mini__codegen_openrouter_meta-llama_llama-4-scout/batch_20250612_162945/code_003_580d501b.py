"""
Generated Code Metadata:
========================
Original URL: https://somtu.edu.np
Prompt: Develop a SQL query to extract data about the faculty members involved in the MBA programs at SOMTU, focusing on their qualifications and areas of expertise.
Generated: DETERMINISTIC_580d501b7e916509
Batch ID: 20250612_162945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Query to extract data about faculty members involved in MBA programs at SOMTU

-- Define the query
SELECT 
    fm.faculty_id,
    fm.first_name,
    fm.last_name,
    fm.email,
    fm.title,
    fm.department,
    q.qualification_name,
    q.qualification_level,
    ae.area_of_expertise
FROM 
    faculty_members fm
INNER JOIN 
    faculty_qualifications fq ON fm.faculty_id = fq.faculty_id
INNER JOIN 
    qualifications q ON fq.qualification_id = q.qualification_id
INNER JOIN 
    faculty_areas_of_expertise fae ON fm.faculty_id = fae.faculty_id
INNER JOIN 
    areas_of_expertise ae ON fae.area_of_expertise_id = ae.area_of_expertise_id
INNER JOIN 
    faculty_programs fp ON fm.faculty_id = fp.faculty_id
INNER JOIN 
    programs p ON fp.program_id = p.program_id
WHERE 
    p.program_name LIKE '%MBA%' 
    AND p.institution = 'SOMTU';

-- Create a stored procedure for better organization and reusability
DELIMITER //
CREATE PROCEDURE GetMBAFacultyMembers()
BEGIN
    SELECT 
        fm.faculty_id,
        fm.first_name,
        fm.last_name,
        fm.email,
        fm.title,
        fm.department,
        q.qualification_name,
        q.qualification_level,
        ae.area_of_expertise
    FROM 
        faculty_members fm
    INNER JOIN 
        faculty_qualifications fq ON fm.faculty_id = fq.faculty_id
    INNER JOIN 
        qualifications q ON fq.qualification_id = q.qualification_id
    INNER JOIN 
        faculty_areas_of_expertise fae ON fm.faculty_id = fae.faculty_id
    INNER JOIN 
        areas_of_expertise ae ON fae.area_of_expertise_id = ae.area_of_expertise_id
    INNER JOIN 
        faculty_programs fp ON fm.faculty_id = fp.faculty_id
    INNER JOIN 
        programs p ON fp.program_id = p.program_id
    WHERE 
        p.program_name LIKE '%MBA%' 
        AND p.institution = 'SOMTU';
END//
DELIMITER ;

-- Call the stored procedure
CALL GetMBAFacultyMembers();
```

**Table Schema Assumptions:**

```sql
CREATE TABLE faculty_members (
    faculty_id INT PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    title VARCHAR(255),
    department VARCHAR(255)
);

CREATE TABLE qualifications (
    qualification_id INT PRIMARY KEY,
    qualification_name VARCHAR(255) NOT NULL,
    qualification_level VARCHAR(255) NOT NULL
);

CREATE TABLE areas_of_expertise (
    area_of_expertise_id INT PRIMARY KEY,
    area_of_expertise VARCHAR(255) NOT NULL
);

CREATE TABLE faculty_qualifications (
    faculty_id INT,
    qualification_id INT,
    PRIMARY KEY (faculty_id, qualification_id),
    FOREIGN KEY (faculty_id) REFERENCES faculty_members(faculty_id),
    FOREIGN KEY (qualification_id) REFERENCES qualifications(qualification_id)
);

CREATE TABLE faculty_areas_of_expertise (
    faculty_id INT,
    area_of_expertise_id INT,
    PRIMARY KEY (faculty_id, area_of_expertise_id),
    FOREIGN KEY (faculty_id) REFERENCES faculty_members(faculty_id),
    FOREIGN KEY (area_of_expertise_id) REFERENCES areas_of_expertise(area_of_expertise_id)
);

CREATE TABLE programs (
    program_id INT PRIMARY KEY,
    program_name VARCHAR(255) NOT NULL,
    institution VARCHAR(255) NOT NULL
);

CREATE TABLE faculty_programs (
    faculty_id INT,
    program_id INT,
    PRIMARY KEY (faculty_id, program_id),
    FOREIGN KEY (faculty_id) REFERENCES faculty_members(faculty_id),
    FOREIGN KEY (program_id) REFERENCES programs(program_id)
);
```
