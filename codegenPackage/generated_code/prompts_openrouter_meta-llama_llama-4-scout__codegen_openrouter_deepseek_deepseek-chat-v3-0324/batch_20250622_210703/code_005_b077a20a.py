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

```python
# employee_career_tracker.py
import sqlite3
from typing import List, Dict, Optional
from dataclasses import dataclass
from datetime import date

@dataclass
class Employee:
    id: int
    first_name: str
    last_name: str
    email: str
    hire_date: date
    department: str
    position: str
    salary: float

@dataclass
class Skill:
    id: int
    name: str
    description: str

@dataclass
class EmployeeSkill:
    employee_id: int
    skill_id: int
    proficiency_level: int
    date_acquired: date

@dataclass
class CareerGoal:
    id: int
    employee_id: int
    goal: str
    target_date: date
    status: str  # e.g., 'Not Started', 'In Progress', 'Completed'

class EmployeeCareerTracker:
    def __init__(self, db_path: str = 'employee_career.db'):
        self.db_path = db_path
        self._initialize_database()

    def _initialize_database(self):
        """Initialize the database with required tables"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Create employees table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS employees (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    hire_date DATE NOT NULL,
                    department TEXT NOT NULL,
                    position TEXT NOT NULL,
                    salary REAL NOT NULL
                )
            ''')
            
            # Create skills table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS skills (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT UNIQUE NOT NULL,
                    description TEXT
                )
            ''')
            
            # Create employee_skills junction table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS employee_skills (
                    employee_id INTEGER,
                    skill_id INTEGER,
                    proficiency_level INTEGER CHECK(proficiency_level BETWEEN 1 AND 5),
                    date_acquired DATE NOT NULL,
                    PRIMARY KEY (employee_id, skill_id),
                    FOREIGN KEY (employee_id) REFERENCES employees(id) ON DELETE CASCADE,
                    FOREIGN KEY (skill_id) REFERENCES skills(id) ON DELETE CASCADE
                )
            ''')
            
            # Create career_goals table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS career_goals (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    employee_id INTEGER,
                    goal TEXT NOT NULL,
                    target_date DATE NOT NULL,
                    status TEXT NOT NULL,
                    FOREIGN KEY (employee_id) REFERENCES employees(id) ON DELETE CASCADE
                )
            ''')
            conn.commit()

    def add_employee(self, employee: Employee) -> int:
        """Add a new employee to the database"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO employees (first_name, last_name, email, hire_date, department, position, salary)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (
                employee.first_name,
                employee.last_name,
                employee.email,
                employee.hire_date,
                employee.department,
                employee.position,
                employee.salary
            ))
            conn.commit()
            return cursor.lastrowid

    def get_employee(self, employee_id: int) -> Optional[Employee]:
        """Retrieve an employee by ID"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM employees WHERE id = ?', (employee_id,))
            row = cursor.fetchone()
            if row:
                return Employee(*row)
            return None

    def add_skill(self, skill: Skill) -> int:
        """Add a new skill to the database"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO skills (name, description)
                VALUES (?, ?)
            ''', (skill.name, skill.description))
            conn.commit()
            return cursor.lastrowid

    def add_employee_skill(self, employee_skill: EmployeeSkill) -> bool:
        """Add a skill to an employee's profile"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO employee_skills (employee_id, skill_id, proficiency_level, date_acquired)
                    VALUES (?, ?, ?, ?)
                ''', (
                    employee_skill.employee_id,
                    employee_skill.skill_id,
                    employee_skill.proficiency_level,
                    employee_skill.date_acquired
                ))
                conn.commit()
                return True
        except sqlite3.IntegrityError:
            return False

    def get_employee_skills(self, employee_id: int) -> List[Dict]:
        """Get all skills for a specific employee"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT s.id, s.name, s.description, es.proficiency_level, es.date_acquired
                FROM skills s
                JOIN employee_skills es ON s.id = es.skill_id
                WHERE es.employee_id = ?
            ''', (employee_id,))
            return [
                {
                    'id': row[0],
                    'name': row[1],
                    'description': row[2],
                    'proficiency_level': row[3],
                    'date_acquired': row[4]
                }
                for row in cursor.fetchall()
            ]

    def add_career_goal(self, goal: CareerGoal) -> int:
        """Add a career goal for an employee"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO career_goals (employee_id, goal, target_date, status)
                VALUES (?, ?, ?, ?)
            ''', (
                goal.employee_id,
                goal.goal,
                goal.target_date,
                goal.status
            ))
            conn.commit()
            return cursor.lastrowid

    def get_employee_goals(self, employee_id: int) -> List[CareerGoal]:
        """Get all career goals for a specific employee"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT id, employee_id, goal, target_date, status
                FROM career_goals
                WHERE employee_id = ?
            ''', (employee_id,))
            return [CareerGoal(*row) for row in cursor.fetchall()]

    def update_goal_status(self, goal_id: int, new_status: str) -> bool:
        """Update the status of a career goal"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE career_goals
                SET status = ?
                WHERE id = ?
            ''', (new_status, goal_id))
            conn.commit()
            return cursor.rowcount > 0

    def get_employees_by_department(self, department: str) -> List[Employee]:
        """Get all employees in a specific department"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT * FROM employees
                WHERE department = ?
            ''', (department,))
            return [Employee(*row) for row in cursor.fetchall()]

    def get_skill_distribution(self) -> Dict[str, int]:
        """Get distribution of skills across all employees"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT s.name, COUNT(es.employee_id)
                FROM skills s
                LEFT JOIN employee_skills es ON s.id = es.skill_id
                GROUP BY s.name
            ''')
            return {row[0]: row[1] for row in cursor.fetchall()}

    def close(self):
        """Close the database connection"""
        pass  # SQLite connection is managed by context manager
```
