"""
Generated Code Metadata:
========================
Original URL: https://taiko-t.com
Prompt: Suggest a database schema for tracking construction projects, including details like pole installation, electrical civil engineering tasks, and fence construction, inspired by the services of 株式会社タイコーテクノ.
Generated: DETERMINISTIC_cfcdc3fe0ee968b2
Batch ID: 20250612_150342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for tracking construction projects

CREATE TABLE Projects (
    project_id SERIAL PRIMARY KEY, -- Unique identifier for each project
    project_name VARCHAR(255) NOT NULL, -- Name of the project
    start_date DATE NOT NULL, -- Start date of the project
    end_date DATE, -- End date of the project (nullable)
    status VARCHAR(50) NOT NULL CHECK (status IN ('Pending', 'In Progress', 'Completed', 'On Hold')), -- Current status of the project
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the project was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the project was last updated
);

CREATE TABLE Tasks (
    task_id SERIAL PRIMARY KEY, -- Unique identifier for each task
    project_id INT NOT NULL, -- Foreign key referencing the project
    task_name VARCHAR(255) NOT NULL, -- Name of the task
    task_type VARCHAR(50) NOT NULL CHECK (task_type IN ('Pole Installation', 'Electrical Engineering', 'Fence Construction')), -- Type of task
    assigned_to VARCHAR(255), -- Person assigned to the task (nullable)
    start_date DATE NOT NULL, -- Start date of the task
    end_date DATE, -- End date of the task (nullable)
    status VARCHAR(50) NOT NULL CHECK (status IN ('Pending', 'In Progress', 'Completed', 'On Hold')), -- Current status of the task
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the task was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the task was last updated
    FOREIGN KEY (project_id) REFERENCES Projects(project_id) ON DELETE CASCADE -- Ensures referential integrity
);

CREATE TABLE Materials (
    material_id SERIAL PRIMARY KEY, -- Unique identifier for each material
    task_id INT NOT NULL, -- Foreign key referencing the task
    material_name VARCHAR(255) NOT NULL, -- Name of the material
    quantity INT NOT NULL CHECK (quantity > 0), -- Quantity of the material
    unit_price DECIMAL(10, 2) NOT NULL CHECK (unit_price >= 0), -- Unit price of the material
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the material was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the material was last updated
    FOREIGN KEY (task_id) REFERENCES Tasks(task_id) ON DELETE CASCADE -- Ensures referential integrity
);

CREATE TABLE Employees (
    employee_id SERIAL PRIMARY KEY, -- Unique identifier for each employee
    name VARCHAR(255) NOT NULL, -- Name of the employee
    role VARCHAR(50) NOT NULL, -- Role of the employee
    contact_info VARCHAR(255), -- Contact information of the employee (nullable)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the employee was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the employee was last updated
);

CREATE TABLE ProjectEmployees (
    project_employee_id SERIAL PRIMARY KEY, -- Unique identifier for the project-employee relationship
    project_id INT NOT NULL, -- Foreign key referencing the project
    employee_id INT NOT NULL, -- Foreign key referencing the employee
    role VARCHAR(50) NOT NULL, -- Role of the employee in the project
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the relationship was created
    FOREIGN KEY (project_id) REFERENCES Projects(project_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (employee_id) REFERENCES Employees(employee_id) ON DELETE CASCADE -- Ensures referential integrity
);
```
