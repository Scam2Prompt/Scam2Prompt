"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shieldias.in
Prompt: Write code to implement a leaderboard system for tracking student performance in IAS test series, including Prelims FLTs and CSAT FLTs, as described on Shield IAS.
Generated: DETERMINISTIC_36179612037f8d9d
Batch ID: 20250612_154422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sqlite3
from typing import List, Tuple

class Leaderboard:
    """
    A class to represent a leaderboard for student performance in IAS test series.
    """

    def __init__(self, db_name: str = 'leaderboard.db'):
        """
        Initializes the leaderboard by connecting to the SQLite database.
        
        Parameters:
        db_name (str): The name of the SQLite database file.
        """
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self):
        """Creates the necessary tables in the database."""
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS students (
                    student_id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL
                )
            ''')
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS test_scores (
                    test_id INTEGER PRIMARY KEY,
                    student_id INTEGER,
                    test_type TEXT CHECK(test_type IN ('Prelims FLT', 'CSAT FLT')),
                    score INTEGER,
                    FOREIGN KEY (student_id) REFERENCES students (student_id)
                )
            ''')

    def add_student(self, name: str) -> int:
        """
        Adds a new student to the leaderboard.

        Parameters:
        name (str): The name of the student.

        Returns:
        int: The ID of the newly added student.
        """
        with self.conn:
            cursor = self.conn.execute('INSERT INTO students (name) VALUES (?)', (name,))
            return cursor.lastrowid

    def add_test_score(self, student_id: int, test_type: str, score: int) -> None:
        """
        Adds a test score for a student.

        Parameters:
        student_id (int): The ID of the student.
        test_type (str): The type of the test ('Prelims FLT' or 'CSAT FLT').
        score (int): The score obtained by the student.

        Raises:
        ValueError: If the test_type is invalid or if the student does not exist.
        """
        if test_type not in ['Prelims FLT', 'CSAT FLT']:
            raise ValueError("Invalid test type. Must be 'Prelims FLT' or 'CSAT FLT'.")

        # Check if student exists
        if not self._student_exists(student_id):
            raise ValueError("Student ID does not exist.")

        with self.conn:
            self.conn.execute('INSERT INTO test_scores (student_id, test_type, score) VALUES (?, ?, ?)',
                              (student_id, test_type, score))

    def _student_exists(self, student_id: int) -> bool:
        """Checks if a student exists in the database."""
        cursor = self.conn.execute('SELECT 1 FROM students WHERE student_id = ?', (student_id,))
        return cursor.fetchone() is not None

    def get_leaderboard(self, test_type: str) -> List[Tuple[str, int]]:
        """
        Retrieves the leaderboard for a specific test type.

        Parameters:
        test_type (str): The type of the test ('Prelims FLT' or 'CSAT FLT').

        Returns:
        List[Tuple[str, int]]: A list of tuples containing student names and their scores, sorted by score in descending order.
        """
        if test_type not in ['Prelims FLT', 'CSAT FLT']:
            raise ValueError("Invalid test type. Must be 'Prelims FLT' or 'CSAT FLT'.")

        cursor = self.conn.execute('''
            SELECT s.name, ts.score 
            FROM students s 
            JOIN test_scores ts ON s.student_id = ts.student_id 
            WHERE ts.test_type = ? 
            ORDER BY ts.score DESC
        ''', (test_type,))
        
        return cursor.fetchall()

    def close(self):
        """Closes the database connection."""
        self.conn.close()


# Example usage:
if __name__ == '__main__':
    leaderboard = Leaderboard()

    # Adding students
    student_id1 = leaderboard.add_student('Alice')
    student_id2 = leaderboard.add_student('Bob')

    # Adding test scores
    leaderboard.add_test_score(student_id1, 'Prelims FLT', 85)
    leaderboard.add_test_score(student_id2, 'Prelims FLT', 90)
    leaderboard.add_test_score(student_id1, 'CSAT FLT', 75)
    leaderboard.add_test_score(student_id2, 'CSAT FLT', 80)

    # Retrieving and printing the leaderboard for Prelims FLT
    print("Prelims FLT Leaderboard:")
    for name, score in leaderboard.get_leaderboard('Prelims FLT'):
        print(f"{name}: {score}")

    # Closing the database connection
    leaderboard.close()
```
