"""
Generated Code Metadata:
========================
Original URL: https://afranaden.org
Prompt: Generate code to model a database schema for tracking humanitarian aid projects, including categories like "mosquito fogging campaigns," "monthly financial assistance," and "water well drilling," as outlined on the Gulf and Aden website.
Generated: DETERMINISTIC_d8ba76552b55d1c7
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- humanitarian_aid_schema.sql

-- Create a database schema for tracking humanitarian aid projects

-- Create a database
CREATE DATABASE humanitarian_aid;

-- Use the database
USE humanitarian_aid;

-- Create a table for project categories
CREATE TABLE project_categories (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for projects
CREATE TABLE projects (
  id INT AUTO_INCREMENT,
  category_id INT NOT NULL,
  title VARCHAR(255) NOT NULL,
  description TEXT,
  start_date DATE,
  end_date DATE,
  budget DECIMAL(10, 2),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (category_id) REFERENCES project_categories(id) ON DELETE CASCADE
);

-- Create a table for project locations
CREATE TABLE project_locations (
  id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  location VARCHAR(255) NOT NULL,
  latitude DECIMAL(10, 8),
  longitude DECIMAL(11, 8),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (project_id) REFERENCES projects(id) ON DELETE CASCADE
);

-- Create a table for project beneficiaries
CREATE TABLE project_beneficiaries (
  id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  name VARCHAR(255) NOT NULL,
  age INT,
  gender ENUM('male', 'female', 'other'),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (project_id) REFERENCES projects(id) ON DELETE CASCADE
);

-- Create a table for project expenses
CREATE TABLE project_expenses (
  id INT AUTO_INCREMENT,
  project_id INT NOT NULL,
  expense_date DATE NOT NULL,
  amount DECIMAL(10, 2) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (project_id) REFERENCES projects(id) ON DELETE CASCADE
);

-- Insert sample data
INSERT INTO project_categories (name, description)
VALUES
  ('Mosquito Fogging Campaigns', 'Mosquito fogging campaigns to prevent malaria and other diseases'),
  ('Monthly Financial Assistance', 'Monthly financial assistance to vulnerable populations'),
  ('Water Well Drilling', 'Drilling of water wells to provide access to clean water');

INSERT INTO projects (category_id, title, description, start_date, end_date, budget)
VALUES
  (1, 'Mosquito Fogging Campaign in Yemen', 'Mosquito fogging campaign in Yemen to prevent malaria', '2022-01-01', '2022-12-31', 100000.00),
  (2, 'Monthly Financial Assistance in Somalia', 'Monthly financial assistance to vulnerable populations in Somalia', '2022-01-01', '2022-12-31', 50000.00),
  (3, 'Water Well Drilling in Djibouti', 'Drilling of water wells in Djibouti to provide access to clean water', '2022-01-01', '2022-06-30', 200000.00);

INSERT INTO project_locations (project_id, location, latitude, longitude)
VALUES
  (1, 'Sana\'a, Yemen', 15.3694, 44.1907),
  (2, 'Mogadishu, Somalia', 7.0952, 46.9753),
  (3, 'Djibouti City, Djibouti', 11.5454, 43.1639);

INSERT INTO project_beneficiaries (project_id, name, age, gender)
VALUES
  (1, 'John Doe', 30, 'male'),
  (2, 'Jane Smith', 25, 'female'),
  (3, 'Ahmed Ali', 40, 'male');

INSERT INTO project_expenses (project_id, expense_date, amount, description)
VALUES
  (1, '2022-01-15', 5000.00, 'Mosquito fogging equipment'),
  (2, '2022-02-01', 1000.00, 'Financial assistance to beneficiaries'),
  (3, '2022-03-01', 50000.00, 'Water well drilling equipment');
```
