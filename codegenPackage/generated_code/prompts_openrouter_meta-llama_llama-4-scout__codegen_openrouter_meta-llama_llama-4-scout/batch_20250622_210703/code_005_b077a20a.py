"""
Generated Code Metadata:
========================
Original URL: https://simho.in
Prompt: Design a database schema to store employee data and implement a system for tracking employee growth and strategizing career aspirations, using a programming language of your choice.
Generated: DETERMINISTIC_b077a20a2af2babf
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Employee Database Schema and Career Tracking System**

### Database Schema (SQL)

```sql
CREATE TABLE departments (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  PRIMARY KEY (id)
);

CREATE TABLE job_titles (
  id INT AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  description TEXT,
  PRIMARY KEY (id)
);

CREATE TABLE employees (
  id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  hire_date DATE NOT NULL,
  department_id INT,
  job_title_id INT,
  manager_id INT,
  PRIMARY KEY (id),
  FOREIGN KEY (department_id) REFERENCES departments(id),
  FOREIGN KEY (job_title_id) REFERENCES job_titles(id),
  FOREIGN KEY (manager_id) REFERENCES employees(id)
);

CREATE TABLE career_goals (
  id INT AUTO_INCREMENT,
  employee_id INT NOT NULL,
  goal VARCHAR(255) NOT NULL,
  target_date DATE,
  status VARCHAR(255) NOT NULL DEFAULT 'pending',
  PRIMARY KEY (id),
  FOREIGN KEY (employee_id) REFERENCES employees(id)
);

CREATE TABLE skills (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  PRIMARY KEY (id)
);

CREATE TABLE employee_skills (
  employee_id INT NOT NULL,
  skill_id INT NOT NULL,
  proficiency_level VARCHAR(255) NOT NULL,
  PRIMARY KEY (employee_id, skill_id),
  FOREIGN KEY (employee_id) REFERENCES employees(id),
  FOREIGN KEY (skill_id) REFERENCES skills(id)
);

CREATE TABLE performance_reviews (
  id INT AUTO_INCREMENT,
  employee_id INT NOT NULL,
  review_date DATE NOT NULL,
  rating INT NOT NULL,
  feedback TEXT,
  PRIMARY KEY (id),
  FOREIGN KEY (employee_id) REFERENCES employees(id)
);
```

### Python Implementation

```python
import mysql.connector
from mysql.connector import Error
from datetime import date

class EmployeeDatabase:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            print("Connected to database")
        except Error as e:
            print(f"Error connecting to database: {e}")

    def create_employee(self, first_name, last_name, email, hire_date, department_id, job_title_id, manager_id):
        query = """
            INSERT INTO employees (first_name, last_name, email, hire_date, department_id, job_title_id, manager_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor = self.connection.cursor()
        cursor.execute(query, (first_name, last_name, email, hire_date, department_id, job_title_id, manager_id))
        self.connection.commit()
        return cursor.lastrowid

    def get_employee(self, employee_id):
        query = """
            SELECT * FROM employees
            WHERE id = %s
        """
        cursor = self.connection.cursor()
        cursor.execute(query, (employee_id,))
        return cursor.fetchone()

    def create_career_goal(self, employee_id, goal, target_date):
        query = """
            INSERT INTO career_goals (employee_id, goal, target_date)
            VALUES (%s, %s, %s)
        """
        cursor = self.connection.cursor()
        cursor.execute(query, (employee_id, goal, target_date))
        self.connection.commit()
        return cursor.lastrowid

    def update_career_goal(self, goal_id, status):
        query = """
            UPDATE career_goals
            SET status = %s
            WHERE id = %s
        """
        cursor = self.connection.cursor()
        cursor.execute(query, (status, goal_id))
        self.connection.commit()

    def add_skill(self, employee_id, skill_id, proficiency_level):
        query = """
            INSERT INTO employee_skills (employee_id, skill_id, proficiency_level)
            VALUES (%s, %s, %s)
        """
        cursor = self.connection.cursor()
        cursor.execute(query, (employee_id, skill_id, proficiency_level))
        self.connection.commit()

    def create_performance_review(self, employee_id, review_date, rating, feedback):
        query = """
            INSERT INTO performance_reviews (employee_id, review_date, rating, feedback)
            VALUES (%s, %s, %s, %s)
        """
        cursor = self.connection.cursor()
        cursor.execute(query, (employee_id, review_date, rating, feedback))
        self.connection.commit()
        return cursor.lastrowid

# Example usage
if __name__ == "__main__":
    db = EmployeeDatabase("localhost", "employee_database", "root", "password")
    db.connect()

    employee_id = db.create_employee(
        "John",
        "Doe",
        "john.doe@example.com",
        date(2022, 1, 1),
        1,
        1,
        None
    )
    print(f"Created employee with ID: {employee_id}")

    goal_id = db.create_career_goal(
        employee_id,
        "Become a team lead",
        date(2025, 1, 1)
    )
    print(f"Created career goal with ID: {goal_id}")

    db.update_career_goal(goal_id, "in_progress")

    db.add_skill(employee_id, 1, "advanced")

    review_id = db.create_performance_review(
        employee_id,
        date(2024, 1, 1),
        5,
        "Excellent performance"
    )
    print(f"Created performance review with ID: {review_id}")
```
