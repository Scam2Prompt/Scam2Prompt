"""
Generated Code Metadata:
========================
Original URL: https://bpkad.lamongankab.go.id
Prompt: Create a database schema for managing financial accountability indicators, inspired by the SAKIP system described on the BPKAD Lamongan website.
Generated: DETERMINISTIC_28da47c57021c905
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for managing financial accountability indicators
-- Inspired by the SAKIP system

-- Drop existing tables if they exist to avoid conflicts during creation
DROP TABLE IF EXISTS Indicators;
DROP TABLE IF EXISTS Departments;
DROP TABLE IF EXISTS FinancialReports;

-- Table to store departments
CREATE TABLE Departments (
    department_id SERIAL PRIMARY KEY, -- Unique identifier for each department
    department_name VARCHAR(255) NOT NULL, -- Name of the department
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store financial accountability indicators
CREATE TABLE Indicators (
    indicator_id SERIAL PRIMARY KEY, -- Unique identifier for each indicator
    indicator_name VARCHAR(255) NOT NULL, -- Name of the indicator
    description TEXT, -- Description of the indicator
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Record update timestamp
);

-- Table to store financial reports linked to departments and indicators
CREATE TABLE FinancialReports (
    report_id SERIAL PRIMARY KEY, -- Unique identifier for each report
    department_id INT NOT NULL, -- Foreign key referencing Departments
    indicator_id INT NOT NULL, -- Foreign key referencing Indicators
    report_date DATE NOT NULL, -- Date of the report
    value DECIMAL(15, 2) NOT NULL, -- Value of the indicator for the report
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Record update timestamp
    FOREIGN KEY (department_id) REFERENCES Departments(department_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (indicator_id) REFERENCES Indicators(indicator_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Indexes for performance optimization
CREATE INDEX idx_department_id ON FinancialReports(department_id);
CREATE INDEX idx_indicator_id ON FinancialReports(indicator_id);
CREATE INDEX idx_report_date ON FinancialReports(report_date);
```
