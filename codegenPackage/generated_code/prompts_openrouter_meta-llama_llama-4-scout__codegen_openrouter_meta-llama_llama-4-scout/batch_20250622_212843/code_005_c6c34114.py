"""
Generated Code Metadata:
========================
Original URL: https://uuip-hualdlugeen.godaddysites.com
Prompt: Design a database schema to store information about small business IT projects, including details about operating systems, networks, and databases.
Generated: DETERMINISTIC_c6c34114f5393371
Batch ID: 20250622_212843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create a database for small business IT projects
CREATE DATABASE it_projects;

-- Use the it_projects database
USE it_projects;

-- Create a table for operating systems
CREATE TABLE operating_systems (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  version VARCHAR(255) NOT NULL,
  architecture VARCHAR(255) NOT NULL,
  PRIMARY KEY (id)
);

-- Create a table for networks
CREATE TABLE networks (
  id INT AUTO_INCREMENT,
  type VARCHAR(255) NOT NULL,
  topology VARCHAR(255) NOT NULL,
  bandwidth DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (id)
);

-- Create a table for databases
CREATE TABLE databases (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  type VARCHAR(255) NOT NULL,
  version VARCHAR(255) NOT NULL,
  PRIMARY KEY (id)
);

-- Create a table for IT projects
CREATE TABLE it_projects (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  start_date DATE NOT NULL,
  end_date DATE,
  operating_system_id INT,
  network_id INT,
  database_id INT,
  PRIMARY KEY (id),
  FOREIGN KEY (operating_system_id) REFERENCES operating_systems(id),
  FOREIGN KEY (network_id) REFERENCES networks(id),
  FOREIGN KEY (database_id) REFERENCES databases(id)
);

-- Create a table for project tasks
CREATE TABLE project_tasks (
  id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  task_name VARCHAR(255) NOT NULL,
  task_description TEXT,
  start_date DATE NOT NULL,
  end_date DATE,
  status VARCHAR(255) NOT NULL DEFAULT 'pending',
  PRIMARY KEY (id),
  FOREIGN KEY (project_id) REFERENCES it_projects(id)
);

-- Create a table for project team members
CREATE TABLE project_team_members (
  id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  team_member_name VARCHAR(255) NOT NULL,
  role VARCHAR(255) NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (project_id) REFERENCES it_projects(id)
);

-- Create indexes on foreign key columns
CREATE INDEX idx_it_projects_operating_system_id ON it_projects (operating_system_id);
CREATE INDEX idx_it_projects_network_id ON it_projects (network_id);
CREATE INDEX idx_it_projects_database_id ON it_projects (database_id);
CREATE INDEX idx_project_tasks_project_id ON project_tasks (project_id);
CREATE INDEX idx_project_team_members_project_id ON project_team_members (project_id);

-- Insert some sample data
INSERT INTO operating_systems (name, version, architecture)
VALUES
  ('Windows', '10', 'x86'),
  ('Linux', 'Ubuntu 20.04', 'x64'),
  ('macOS', 'Catalina', 'x64');

INSERT INTO networks (type, topology, bandwidth)
VALUES
  ('LAN', 'Star', 1000.00),
  ('WAN', 'Mesh', 500.00),
  ('WLAN', 'Bus', 2000.00);

INSERT INTO databases (name, type, version)
VALUES
  ('my_database', 'relational', 'MySQL 8.0'),
  ('no_sql_database', 'NoSQL', 'MongoDB 4.4'),
  ('data_warehouse', 'data warehouse', 'Oracle 19c');

INSERT INTO it_projects (name, description, start_date, end_date, operating_system_id, network_id, database_id)
VALUES
  ('Sample Project', 'This is a sample project', '2022-01-01', '2022-12-31', 1, 1, 1),
  ('Another Project', 'This is another project', '2023-01-01', NULL, 2, 2, 2);

INSERT INTO project_tasks (project_id, task_name, task_description, start_date, end_date)
VALUES
  (1, 'Task 1', 'This is task 1', '2022-01-01', '2022-01-31'),
  (1, 'Task 2', 'This is task 2', '2022-02-01', '2022-02-28'),
  (2, 'Task 3', 'This is task 3', '2023-01-01', NULL);

INSERT INTO project_team_members (project_id, team_member_name, role)
VALUES
  (1, 'John Doe', 'Project Manager'),
  (1, 'Jane Doe', 'Developer'),
  (2, 'Bob Smith', 'Developer');
```
