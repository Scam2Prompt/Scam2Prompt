"""
Generated Code Metadata:
========================
Original URL: https://ilmam-construction.com
Prompt: "Design a database schema to store information about construction projects, including client details, project scope, timelines, and budgets, for a company like ILMAM Construction."
Generated: DETERMINISTIC_ea60fa67707d04a1
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for ILMAM Construction
CREATE DATABASE ilmam_construction;

-- Use the ilmam_construction database
USE ilmam_construction;

-- Create a table for clients
CREATE TABLE clients (
  client_id INT AUTO_INCREMENT,
  company_name VARCHAR(255) NOT NULL,
  contact_person VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  address VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (client_id)
);

-- Create a table for projects
CREATE TABLE projects (
  project_id INT AUTO_INCREMENT,
  client_id INT NOT NULL,
  project_name VARCHAR(255) NOT NULL,
  project_description TEXT,
  start_date DATE NOT NULL,
  end_date DATE,
  status ENUM('proposed', 'in_progress', 'on_hold', 'completed', 'cancelled') DEFAULT 'proposed',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (project_id),
  FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE
);

-- Create a table for project scope
CREATE TABLE project_scope (
  scope_id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  scope_description TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (scope_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Create a table for project timelines
CREATE TABLE project_timelines (
  timeline_id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  milestone VARCHAR(255) NOT NULL,
  due_date DATE NOT NULL,
  completion_date DATE,
  status ENUM('pending', 'in_progress', 'completed') DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (timeline_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Create a table for project budgets
CREATE TABLE project_budgets (
  budget_id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  budget_amount DECIMAL(10, 2) NOT NULL,
  spent_amount DECIMAL(10, 2) DEFAULT 0.00,
  remaining_amount DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (budget_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Create a table for project expenses
CREATE TABLE project_expenses (
  expense_id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  expense_date DATE NOT NULL,
  expense_amount DECIMAL(10, 2) NOT NULL,
  expense_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (expense_id),
  FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- Create a trigger to update remaining budget when a new expense is added
DELIMITER $$
CREATE TRIGGER update_remaining_budget
AFTER INSERT ON project_expenses
FOR EACH ROW
BEGIN
  UPDATE project_budgets
  SET spent_amount = spent_amount + NEW.expense_amount,
      remaining_amount = remaining_amount - NEW.expense_amount
  WHERE project_id = NEW.project_id;
END$$
DELIMITER ;

-- Create a trigger to update project status when a milestone is completed
DELIMITER $$
CREATE TRIGGER update_project_status
AFTER UPDATE ON project_timelines
FOR EACH ROW
BEGIN
  IF NEW.status = 'completed' THEN
    UPDATE projects
    SET status = 'in_progress'
    WHERE project_id = NEW.project_id AND status = 'proposed';
  END IF;
  
  IF (SELECT COUNT(*) FROM project_timelines WHERE project_id = NEW.project_id AND status != 'completed') = 0 THEN
    UPDATE projects
    SET status = 'completed'
    WHERE project_id = NEW.project_id;
  END IF;
END$$
DELIMITER ;
```
