"""
Generated Code Metadata:
========================
Original URL: https://araform.org
Prompt: "Write a SQL query to extract a list of all available courses in specific categories (e.g., 'Operatore Socio Sanitario', 'Tecnico Meccatronico') from a database structured like the one presumed for araform.org."
Generated: DETERMINISTIC_7f732cd7b59c9bdd
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- SQL query to extract courses in specific categories from a presumed araform.org-like database
SELECT 
    c.course_id,
    c.course_name,
    c.description,
    c.duration,
    c.price,
    cat.category_name,
    loc.location_name
FROM 
    courses c
JOIN 
    categories cat ON c.category_id = cat.category_id
LEFT JOIN 
    locations loc ON c.location_id = loc.location_id
WHERE 
    cat.category_name IN ('Operatore Socio Sanitario', 'Tecnico Meccatronico')
    AND c.is_active = 1  -- Assuming this flag indicates available courses
ORDER BY 
    cat.category_name, c.course_name;
```
