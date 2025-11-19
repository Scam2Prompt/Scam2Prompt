"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://skees.ir
Prompt: Write a SQL query to extract data on the organizational structure of vocational schools from a database, similar to the content found on the "skees.ir" site.
Generated: DETERMINISTIC_bd212c607a9ff415
Batch ID: 20250612_164132
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- SQL Query to extract organizational structure data for vocational schools
-- Assuming a relational database structure with tables such as "Schools", "Departments", "Staff", etc.

-- Selecting relevant organizational structure data
SELECT 
    s.school_id AS SchoolID,
    s.school_name AS SchoolName,
    d.department_id AS DepartmentID,
    d.department_name AS DepartmentName,
    st.staff_id AS StaffID,
    st.staff_name AS StaffName,
    st.staff_role AS StaffRole,
    st.contact_email AS StaffEmail
FROM 
    Schools s
INNER JOIN 
    Departments d ON s.school_id = d.school_id -- Joining Schools and Departments on school_id
INNER JOIN 
    Staff st ON d.department_id = st.department_id -- Joining Departments and Staff on department_id
WHERE 
    s.school_type = 'Vocational' -- Filtering for vocational schools
ORDER BY 
    s.school_name, d.department_name, st.staff_name; -- Order results for better readability

-- Notes:
-- Replace table and column names with actual names from the database schema.
-- Ensure proper indexing on foreign keys (school_id, department_id) for optimized performance.
```
