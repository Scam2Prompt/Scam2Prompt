"""
Generated Code Metadata:
========================
Original URL: https://www.igeog.uerj.br
Prompt: Develop a database schema to store information about the IGEOG selection processes, including candidate lists, results, and timelines for various "Editais."
Generated: DETERMINISTIC_75feafd5a596b796
Batch ID: 20250612_154423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for IGEOG selection processes
CREATE DATABASE igeog_selection;

-- Use the database
USE igeog_selection;

-- Create table for Editais
CREATE TABLE editais (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  start_date DATE NOT NULL,
  end_date DATE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for candidate lists
CREATE TABLE candidate_lists (
  id INT AUTO_INCREMENT,
  edital_id INT NOT NULL,
  candidate_name VARCHAR(255) NOT NULL,
  candidate_email VARCHAR(255) UNIQUE NOT NULL,
  application_date DATE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (edital_id) REFERENCES editais(id) ON DELETE CASCADE
);

-- Create table for selection results
CREATE TABLE selection_results (
  id INT AUTO_INCREMENT,
  edital_id INT NOT NULL,
  candidate_list_id INT,
  result VARCHAR(50) NOT NULL CHECK (result IN ('approved', 'rejected', 'interview')),
  interview_date DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (edital_id) REFERENCES editais(id) ON DELETE CASCADE,
  FOREIGN KEY (candidate_list_id) REFERENCES candidate_lists(id) ON DELETE SET NULL
);

-- Create table for timelines
CREATE TABLE timelines (
  id INT AUTO_INCREMENT,
  edital_id INT NOT NULL,
  stage VARCHAR(100) NOT NULL,
  start_date DATE NOT NULL,
  end_date DATE NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (edital_id) REFERENCES editais(id) ON DELETE CASCADE
);

-- Create indexes for foreign keys
CREATE INDEX idx_candidate_lists_edital_id ON candidate_lists (edital_id);
CREATE INDEX idx_selection_results_edital_id ON selection_results (edital_id);
CREATE INDEX idx_selection_results_candidate_list_id ON selection_results (candidate_list_id);
CREATE INDEX idx_timelines_edital_id ON timelines (edital_id);

-- Example insert statements
INSERT INTO editais (name, description, start_date, end_date)
VALUES ('Edital 2024', 'Selection process for 2024', '2024-01-01', '2024-12-31');

INSERT INTO candidate_lists (edital_id, candidate_name, candidate_email, application_date)
VALUES (1, 'John Doe', 'john@example.com', '2024-02-01');

INSERT INTO selection_results (edital_id, candidate_list_id, result, interview_date)
VALUES (1, 1, 'approved', '2024-03-01');

INSERT INTO timelines (edital_id, stage, start_date, end_date, description)
VALUES (1, 'Application', '2024-01-01', '2024-02-28', 'Application period');
```
