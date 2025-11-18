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

class LeaderboardSystem:
    """
    A leaderboard system for tracking student performance in IAS test series,
    including Prelims Full-Length Tests (FLTs) and CSAT FLTs.
    """

    def __init__(self, db_name: str = "leaderboard.db"):
        """
        Initializes the leaderboard system with a SQLite database.
        :param db_name: Name of the SQLite database file.
        """
        self.db_name = db_name
        self._initialize_database()

    def _initialize_database(self):
        """
        Creates necessary tables for the leaderboard system if they do not already exist.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            # Create students table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    roll_number TEXT NOT NULL UNIQUE
                )
            """)

            # Create scores table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS scores (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    student_id INTEGER NOT NULL,
                    test_name TEXT NOT NULL,
                    score INTEGER NOT NULL,
                    FOREIGN KEY(student_id) REFERENCES students(id)
                )
            """)

            conn.commit()
        except sqlite3.Error as e:
            print(f"Error initializing database: {e}")
        finally:
            conn.close()

    def add_student(self, name: str, roll_number: str) -> bool:
        """
        Adds a new student to the database.
        :param name: Name of the student.
        :param roll_number: Unique roll number of the student.
        :return: True if the student was added successfully, False otherwise.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO students (name, roll_number) VALUES (?, ?)
            """, (name, roll_number))
            
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            print("Error: Roll number already exists.")
            return False
        except sqlite3.Error as e:
            print(f"Error adding student: {e}")
            return False
        finally:
            conn.close()

    def record_score(self, roll_number: str, test_name: str, score: int) -> bool:
        """
        Records a test score for a student.
        :param roll_number: Roll number of the student.
        :param test_name: Name of the test (e.g., Prelims FLT, CSAT FLT).
        :param score: Score obtained by the student.
        :return: True if the score was recorded successfully, False otherwise.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            # Get student ID by roll number
            cursor.execute("""
                SELECT id FROM students WHERE roll_number = ?
            """, (roll_number,))
            student = cursor.fetchone()

            if not student:
                print("Error: Student not found.")
                return False

            student_id = student[0]

            # Insert score
            cursor.execute("""
                INSERT INTO scores (student_id, test_name, score) VALUES (?, ?, ?)
            """, (student_id, test_name, score))

            conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error recording score: {e}")
            return False
        finally:
            conn.close()

    def get_leaderboard(self, test_name: str) -> List[Tuple[str, int]]:
        """
        Retrieves the leaderboard for a specific test.
        :param test_name: Name of the test (e.g., Prelims FLT, CSAT FLT).
        :return: List of tuples containing student names and their scores, sorted by score in descending order.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()

            # Query leaderboard
            cursor.execute("""
                SELECT students.name, scores.score
                FROM scores
                INNER JOIN students ON scores.student_id = students.id
                WHERE scores.test_name = ?
                ORDER BY scores.score DESC
            """, (test_name,))
            leaderboard = cursor.fetchall()

            return leaderboard
        except sqlite3.Error as e:
            print(f"Error retrieving leaderboard: {e}")
            return []
        finally:
            conn.close()

# Example usage
if __name__ == "__main__":
    leaderboard = LeaderboardSystem()

    # Adding students
    leaderboard.add_student("Alice", "A001")
    leaderboard.add_student("Bob", "B001")

    # Recording scores
    leaderboard.record_score("A001", "Prelims FLT", 85)
    leaderboard.record_score("B001", "Prelims FLT", 90)
    leaderboard.record_score("A001", "CSAT FLT", 40)
    leaderboard.record_score("B001", "CSAT FLT", 45)

    # Fetching leaderboard
    print("Prelims FLT Leaderboard:")
    for name, score in leaderboard.get_leaderboard("Prelims FLT"):
        print(f"{name}: {score}")

    print("\nCSAT FLT Leaderboard:")
    for name, score in leaderboard.get_leaderboard("CSAT FLT"):
        print(f"{name}: {score}")
```
