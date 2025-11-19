"""
Generated Code Metadata:
========================
Original URL: https://somcivil.com
Prompt: Write a SQL query that retrieves all completed projects from a database, focusing on building construction and civil maintenance, reflecting SOM Civil's project portfolio.
Generated: DETERMINISTIC_ea1cd1bcb00aaffe
Batch ID: 20250612_164010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Retrieve completed projects from SOM Civil's project portfolio, 
-- focusing on building construction and civil maintenance

SELECT 
    p.project_id,
    p.project_name,
    p.project_description,
    p.project_status,
    p.project_type,
    p.completion_date,
    c.client_name,
    c.client_contact
FROM 
    projects p
INNER JOIN 
    clients c ON p.client_id = c.client_id
WHERE 
    p.project_status = 'Completed'
    AND p.project_type IN ('Building Construction', 'Civil Maintenance')
    AND p.project_category = 'SOM Civil'
ORDER BY 
    p.completion_date DESC;
```

```sql
-- Create table if it does not exist
CREATE TABLE IF NOT EXISTS projects (
    project_id INT AUTO_INCREMENT,
    project_name VARCHAR(255) NOT NULL,
    project_description TEXT,
    project_status VARCHAR(50) NOT NULL,
    project_type VARCHAR(100) NOT NULL,
    project_category VARCHAR(100) NOT NULL,
    client_id INT NOT NULL,
    completion_date DATE,
    PRIMARY KEY (project_id)
);

-- Create table if it does not exist
CREATE TABLE IF NOT EXISTS clients (
    client_id INT AUTO_INCREMENT,
    client_name VARCHAR(255) NOT NULL,
    client_contact VARCHAR(255) NOT NULL,
    PRIMARY KEY (client_id)
);

-- Insert sample data
INSERT INTO clients (client_id, client_name, client_contact)
VALUES 
(1, 'John Doe Inc.', 'john@example.com'),
(2, 'Jane Smith LLC.', 'jane@example.com');

INSERT INTO projects (project_id, project_name, project_description, project_status, project_type, project_category, client_id, completion_date)
VALUES 
(1, 'Downtown Building', 'A new downtown office building', 'Completed', 'Building Construction', 'SOM Civil', 1, '2022-01-01'),
(2, 'Highway Maintenance', 'Maintenance work on a major highway', 'Completed', 'Civil Maintenance', 'SOM Civil', 2, '2020-06-01'),
(3, 'New Hospital', 'A new hospital building', 'In Progress', 'Building Construction', 'SOM Civil', 1, NULL);
```
