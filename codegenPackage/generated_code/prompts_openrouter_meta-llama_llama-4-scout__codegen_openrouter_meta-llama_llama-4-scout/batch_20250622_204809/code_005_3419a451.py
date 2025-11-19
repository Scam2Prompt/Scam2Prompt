"""
Generated Code Metadata:
========================
Original URL: https://springsinternational.org
Prompt: Create a SQL query to extract data on volunteer participation in neighborhood saturation projects like Mission 2030 Houston.
Generated: DETERMINISTIC_3419a45159492bd3
Batch ID: 20250622_204809
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Mission2030_Houston_Volunteer_Participation.sql

-- Create a stored procedure to extract volunteer participation data
DELIMITER $$

CREATE PROCEDURE GetVolunteerParticipationData()
BEGIN
    -- Select relevant columns from the volunteer and project tables
    SELECT 
        vp.project_id,
        p.project_name,
        vp.volunteer_id,
        v.volunteer_name,
        vp.participation_date,
        vp.hours_contributed
    FROM 
        Volunteer_Participation vp
    INNER JOIN 
        Volunteers v ON vp.volunteer_id = v.volunteer_id
    INNER JOIN 
        Projects p ON vp.project_id = p.project_id
    ORDER BY 
        vp.participation_date DESC;
END$$

DELIMITER ;

-- Create a function to get total volunteer hours for a project
DELIMITER $$

CREATE FUNCTION GetTotalVolunteerHoursForProject(project_id INT)
RETURNS INT
BEGIN
    DECLARE total_hours INT;
    
    SELECT 
        SUM(hours_contributed) 
    INTO 
        total_hours
    FROM 
        Volunteer_Participation
    WHERE 
        project_id = project_id;
    
    RETURN IFNULL(total_hours, 0);
END$$

DELIMITER ;

-- Example usage:
CALL GetVolunteerParticipationData();

-- Get total volunteer hours for a specific project
SELECT 
    GetTotalVolunteerHoursForProject(1) AS total_volunteer_hours;

-- Create table schema for reference
CREATE TABLE IF NOT EXISTS Projects (
    project_id INT AUTO_INCREMENT,
    project_name VARCHAR(255) NOT NULL,
    project_description TEXT,
    PRIMARY KEY (project_id)
);

CREATE TABLE IF NOT EXISTS Volunteers (
    volunteer_id INT AUTO_INCREMENT,
    volunteer_name VARCHAR(255) NOT NULL,
    volunteer_email VARCHAR(255) UNIQUE NOT NULL,
    PRIMARY KEY (volunteer_id)
);

CREATE TABLE IF NOT EXISTS Volunteer_Participation (
    participation_id INT AUTO_INCREMENT,
    project_id INT NOT NULL,
    volunteer_id INT NOT NULL,
    participation_date DATE NOT NULL,
    hours_contributed DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (participation_id),
    FOREIGN KEY (project_id) REFERENCES Projects(project_id),
    FOREIGN KEY (volunteer_id) REFERENCES Volunteers(volunteer_id)
);

-- Insert sample data
INSERT INTO Projects (project_name) 
VALUES 
('Mission2030 Houston'),
('Neighborhood Clean-Up'),
('Community Event');

INSERT INTO Volunteers (volunteer_name, volunteer_email) 
VALUES 
('John Doe', 'john.doe@example.com'),
('Jane Smith', 'jane.smith@example.com'),
('Bob Johnson', 'bob.johnson@example.com');

INSERT INTO Volunteer_Participation (project_id, volunteer_id, participation_date, hours_contributed) 
VALUES 
(1, 1, '2022-01-01', 5.00),
(1, 2, '2022-01-01', 3.00),
(2, 3, '2022-02-01', 4.00);
```
