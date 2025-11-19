"""
Generated Code Metadata:
========================
Original URL: https://cmpinnacle.com
Prompt: "Design a database schema to store information about construction projects, including project details, timelines, and client information, for a company like C&M Pinnacle."
Generated: DETERMINISTIC_39da393309f0e508
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for C&M Pinnacle construction projects
CREATE DATABASE cm_pinnacle;

-- Use the cm_pinnacle database
USE cm_pinnacle;

-- Create a table to store client information
CREATE TABLE clients (
  client_id INT AUTO_INCREMENT,
  company_name VARCHAR(255) NOT NULL,
  contact_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  address VARCHAR(255) NOT NULL,
  PRIMARY KEY (client_id)
);

-- Create a table to store project details
CREATE TABLE projects (
  project_id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  project_name VARCHAR(255) NOT NULL,
  project_description TEXT,
  start_date DATE NOT NULL,
  end_date DATE,
  status ENUM('planned', 'in_progress', 'completed', 'cancelled') NOT NULL DEFAULT 'planned',
  PRIMARY KEY (project_id),
  FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
);

-- Create a table to store project timelines
CREATE TABLE project_timelines (
  timeline_id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  milestone_name VARCHAR(255) NOT NULL,
  milestone_date DATE NOT NULL,
  status ENUM('planned', 'completed') NOT NULL DEFAULT 'planned',
  PRIMARY KEY (timeline_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Create a table to store project team members
CREATE TABLE team_members (
  team_member_id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  employee_name VARCHAR(255) NOT NULL,
  role VARCHAR(255) NOT NULL,
  PRIMARY KEY (team_member_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Create a table to store project expenses
CREATE TABLE project_expenses (
  expense_id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  expense_date DATE NOT NULL,
  expense_category VARCHAR(255) NOT NULL,
  expense_amount DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (expense_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Create a stored procedure to insert a new project
DELIMITER //
CREATE PROCEDURE insert_project(
  IN p_client_id INT,
  IN p_project_name VARCHAR(255),
  IN p_project_description TEXT,
  IN p_start_date DATE,
  IN p_end_date DATE
)
BEGIN
  INSERT INTO projects (client_id, project_name, project_description, start_date, end_date)
  VALUES (p_client_id, p_project_name, p_project_description, p_start_date, p_end_date);
END//
DELIMITER ;

-- Create a stored procedure to update a project's status
DELIMITER //
CREATE PROCEDURE update_project_status(
  IN p_project_id INT,
  IN p_status ENUM('planned', 'in_progress', 'completed', 'cancelled')
)
BEGIN
  UPDATE projects
  SET status = p_status
  WHERE project_id = p_project_id;
END//
DELIMITER ;

-- Example usage:
INSERT INTO clients (company_name, contact_name, email, phone_number, address)
VALUES ('Example Client', 'John Doe', 'john.doe@example.com', '123-456-7890', '123 Main St');

SET @client_id = LAST_INSERT_ID();

INSERT INTO projects (client_id, project_name, project_description, start_date, end_date)
VALUES (@client_id, 'Example Project', 'This is an example project', '2022-01-01', '2022-12-31');

SET @project_id = LAST_INSERT_ID();

INSERT INTO project_timelines (project_id, milestone_name, milestone_date)
VALUES (@project_id, 'Project Kickoff', '2022-01-01');

INSERT INTO team_members (project_id, employee_name, role)
VALUES (@project_id, 'Jane Smith', 'Project Manager');

INSERT INTO project_expenses (project_id, expense_date, expense_category, expense_amount)
VALUES (@project_id, '2022-01-15', 'Materials', 1000.00);

CALL insert_project(@client_id, 'New Project', 'This is a new project', '2023-01-01', '2023-12-31');

CALL update_project_status(@project_id, 'in_progress');
```
