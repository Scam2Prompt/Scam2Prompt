"""
Generated Code Metadata:
========================
Original URL: https://mujeresautistas.com
Prompt: Design a system to handle student testimonials and reviews for Sakura Dance Studio, including data storage, moderation, and display on the website.
Generated: DETERMINISTIC_86cca86a54db4b65
Batch ID: 20250622_212236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import sqlite3
from datetime import datetime

# Database setup
DATABASE_NAME = "sakura_dance_studio.db"

def initialize_database():
    """
    Initialize the database and create necessary tables if they don't exist.
    """
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()
    
    # Create table for testimonials
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS testimonials (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_name TEXT NOT NULL,
        review TEXT NOT NULL,
        rating INTEGER NOT NULL CHECK(rating BETWEEN 1 AND 5),
        is_approved INTEGER DEFAULT 0, -- 0: Pending, 1: Approved
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    
    connection.commit()
    connection.close()

# Function to add a new testimonial
def add_testimonial(student_name, review, rating):
    """
    Add a new testimonial to the database.
    :param student_name: Name of the student providing the testimonial.
    :param review: The review text.
    :param rating: Rating between 1 and 5.
    """
    try:
        connection = sqlite3.connect(DATABASE_NAME)
        cursor = connection.cursor()
        
        cursor.execute("""
        INSERT INTO testimonials (student_name, review, rating)
        VALUES (?, ?, ?)
        """, (student_name, review, rating))
        
        connection.commit()
        print("Testimonial submitted successfully. Awaiting moderation.")
    except sqlite3.Error as e:
        print(f"Error adding testimonial: {e}")
    finally:
        connection.close()

# Function to moderate testimonials
def moderate_testimonial(testimonial_id, approve=True):
    """
    Approve or reject a testimonial.
    :param testimonial_id: ID of the testimonial to moderate.
    :param approve: Boolean indicating whether to approve (True) or reject (False).
    """
    try:
        connection = sqlite3.connect(DATABASE_NAME)
        cursor = connection.cursor()
        
        if approve:
            cursor.execute("""
            UPDATE testimonials
            SET is_approved = 1
            WHERE id = ?
            """, (testimonial_id,))
            print(f"Testimonial ID {testimonial_id} approved.")
        else:
            cursor.execute("""
            DELETE FROM testimonials
            WHERE id = ?
            """, (testimonial_id,))
            print(f"Testimonial ID {testimonial_id} rejected and deleted.")
        
        connection.commit()
    except sqlite3.Error as e:
        print(f"Error moderating testimonial: {e}")
    finally:
        connection.close()

# Function to display approved testimonials
def display_testimonials():
    """
    Fetch and display all approved testimonials.
    """
    try:
        connection = sqlite3.connect(DATABASE_NAME)
        cursor = connection.cursor()
        
        cursor.execute("""
        SELECT student_name, review, rating, created_at
        FROM testimonials
        WHERE is_approved = 1
        ORDER BY created_at DESC
        """)
        
        testimonials = cursor.fetchall()
        if testimonials:
            print("Approved Testimonials:")
            for testimonial in testimonials:
                student_name, review, rating, created_at = testimonial
                print(f"Name: {student_name}")
                print(f"Review: {review}")
                print(f"Rating: {rating}/5")
                print(f"Date: {created_at}")
                print("-" * 40)
        else:
            print("No approved testimonials available.")
    except sqlite3.Error as e:
        print(f"Error fetching testimonials: {e}")
    finally:
        connection.close()

# Main execution block
if __name__ == "__main__":
    # Initialize the database
    initialize_database()
    
    # Example usage
    # Add a new testimonial
    add_testimonial("Alice", "Amazing dance studio! Highly recommend.", 5)
    add_testimonial("Bob", "Great instructors and friendly environment.", 4)
    
    # Moderate testimonials
    moderate_testimonial(1, approve=True)  # Approve testimonial with ID 1
    moderate_testimonial(2, approve=False)  # Reject testimonial with ID 2
    
    # Display approved testimonials
    display_testimonials()
```
