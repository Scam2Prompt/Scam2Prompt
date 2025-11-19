"""
Generated Code Metadata:
========================
Original URL: https://dfivetechnologies.com
Prompt: Create a training module for database skills that shortens the learning curve for employees, based on DFIVE Technologies' technical training services.
Generated: DETERMINISTIC_5404d4d3258595d8
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from typing import List, Dict, Any, Optional
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class DatabaseTrainingModule:
    """
    A training module for database skills that provides hands-on experience with SQL operations.
    Designed to shorten the learning curve for employees at DFIVE Technologies.
    """
    
    def __init__(self, db_name: str = ":memory:"):
        """
        Initialize the training module with an in-memory SQLite database by default.
        
        Args:
            db_name (str): Name of the database file. Use ":memory:" for in-memory DB.
        """
        self.db_name = db_name
        self.conn = None
        self.cursor = None
        
    def __enter__(self):
        """Context manager entry point."""
        self.connect()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit point."""
        self.close()
        
    def connect(self) -> None:
        """Establish connection to the database."""
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
            logger.info(f"Connected to database: {self.db_name}")
        except sqlite3.Error as e:
            logger.error(f"Error connecting to database: {e}")
            raise
            
    def close(self) -> None:
        """Close the database connection."""
        if self.conn:
            self.conn.close()
            logger.info("Database connection closed")
            
    def execute_query(self, query: str, params: tuple = ()) -> Optional[List[Dict[str, Any]]]:
        """
        Execute a SQL query and return results as dictionaries.
        
        Args:
            query (str): SQL query to execute
            params (tuple): Parameters for the query
            
        Returns:
            Optional[List[Dict[str, Any]]]: Query results as dictionaries or None if error
        """
        try:
            self.cursor.execute(query, params)
            
            if query.strip().upper().startswith("SELECT"):
                columns = [col[0] for col in self.cursor.description]
                results = [dict(zip(columns, row)) for row in self.cursor.fetchall()]
                return results
            else:
                self.conn.commit()
                return None
                
        except sqlite3.Error as e:
            logger.error(f"Error executing query: {query}. Error: {e}")
            self.conn.rollback()
            raise
            
    def create_sample_tables(self) -> None:
        """Create sample tables for training purposes."""
        queries = [
            """
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                department TEXT NOT NULL,
                salary REAL,
                hire_date TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS departments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                budget REAL,
                location TEXT
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS projects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                start_date TEXT,
                end_date TEXT,
                budget REAL,
                department_id INTEGER,
                FOREIGN KEY (department_id) REFERENCES departments(id)
            )
            """
        ]
        
        try:
            for query in queries:
                self.execute_query(query)
            logger.info("Sample tables created successfully")
        except sqlite3.Error as e:
            logger.error(f"Error creating sample tables: {e}")
            raise
            
    def populate_sample_data(self) -> None:
        """Populate sample data for training exercises."""
        employees = [
            ("John Doe", "Engineering", 75000, "2020-01-15"),
            ("Jane Smith", "Marketing", 65000, "2019-05-20"),
            ("Bob Johnson", "Engineering", 80000, "2018-11-03"),
            ("Alice Brown", "HR", 60000, "2021-02-10")
        ]
        
        departments = [
            ("Engineering", 1000000, "Floor 3"),
            ("Marketing", 500000, "Floor 2"),
            ("HR", 300000, "Floor 1")
        ]
        
        projects = [
            ("Website Redesign", "2023-01-01", "2023-06-30", 200000, 1),
            ("Social Media Campaign", "2023-02-15", "2023-05-15", 100000, 2),
            ("Employee Training", "2023-03-01", "2023-12-31", 150000, 3)
        ]
        
        try:
            # Insert departments first due to foreign key constraints
            self.execute_query(
                "INSERT INTO departments (name, budget, location) VALUES (?, ?, ?)",
                departments[0]
            )
            self.execute_query(
                "INSERT INTO departments (name, budget, location) VALUES (?, ?, ?)",
                departments[1]
            )
            self.execute_query(
                "INSERT INTO departments (name, budget, location) VALUES (?, ?, ?)",
                departments[2]
            )
            
            # Insert employees
            for emp in employees:
                self.execute_query(
                    "INSERT INTO employees (name, department, salary, hire_date) VALUES (?, ?, ?, ?)",
                    emp
                )
                
            # Insert projects
            for proj in projects:
                self.execute_query(
                    "INSERT INTO projects (name, start_date, end_date, budget, department_id) VALUES (?, ?, ?, ?, ?)",
                    proj
                )
                
            logger.info("Sample data populated successfully")
        except sqlite3.Error as e:
            logger.error(f"Error populating sample data: {e}")
            raise
            
    def run_training_exercises(self) -> None:
        """Run a series of training exercises with increasing complexity."""
        exercises = [
            {
                "title": "Basic SELECT",
                "description": "Retrieve all employees",
                "solution": "SELECT * FROM employees"
            },
            {
                "title": "Filtering with WHERE",
                "description": "Find employees in the Engineering department",
                "solution": "SELECT * FROM employees WHERE department = 'Engineering'"
            },
            {
                "title": "Aggregation",
                "description": "Calculate average salary by department",
                "solution": "SELECT department, AVG(salary) as avg_salary FROM employees GROUP BY department"
            },
            {
                "title": "JOIN Operation",
                "description": "List projects with their department names",
                "solution": """SELECT p.name as project_name, d.name as department_name 
                              FROM projects p JOIN departments d ON p.department_id = d.id"""
            },
            {
                "title": "Subquery",
                "description": "Find employees earning more than the company average",
                "solution": """SELECT name, salary FROM employees 
                              WHERE salary > (SELECT AVG(salary) FROM employees)"""
            }
        ]
        
        print("\nDatabase Training Exercises\n" + "="*30)
        
        for i, exercise in enumerate(exercises, 1):
            print(f"\nExercise {i}: {exercise['title']}")
            print(f"Description: {exercise['description']}")
            
            try:
                result = self.execute_query(exercise["solution"])
                if result:
                    print("\nResult:")
                    for row in result:
                        print(row)
            except sqlite3.Error as e:
                print(f"\nError executing exercise: {e}")
                
            print("\nSolution:")
            print(exercise["solution"])
            
        print("\nTraining exercises completed!")

def main():
    """Main function to run the training module."""
    try:
        with DatabaseTrainingModule() as trainer:
            # Set up the training environment
            trainer.create_sample_tables()
            trainer.populate_sample_data()
            
            # Run the training exercises
            trainer.run_training_exercises()
            
    except Exception as e:
        logger.error(f"Error in training module: {e}")
        raise

if __name__ == "__main__":
    main()
```
