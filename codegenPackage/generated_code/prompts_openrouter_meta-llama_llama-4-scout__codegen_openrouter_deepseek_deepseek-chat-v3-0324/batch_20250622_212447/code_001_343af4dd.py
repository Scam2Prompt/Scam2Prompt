"""
Generated Code Metadata:
========================
Original URL: https://vertiv.mitarbeiterangebote.de
Prompt: Write a Python script to implement a simple employee benefits portal login system, similar to the one on Vertiv GmbH's Mitarbeiterangebote page.
Generated: DETERMINISTIC_343af4dd12d79075
Batch ID: 20250622_212447
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import sqlite3
from getpass import getpass
from datetime import datetime

# Database setup and initialization
def initialize_database():
    """Initialize the SQLite database and create necessary tables."""
    conn = sqlite3.connect('employee_portal.db')
    cursor = conn.cursor()
    
    # Create employees table if not exists
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id TEXT UNIQUE NOT NULL,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            department TEXT NOT NULL,
            hire_date TEXT NOT NULL,
            last_login TEXT,
            is_active BOOLEAN DEFAULT 1
        )
    ''')
    
    # Create benefits table if not exists
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS benefits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id TEXT NOT NULL,
            benefit_type TEXT NOT NULL,
            enrollment_date TEXT NOT NULL,
            status TEXT DEFAULT 'Active',
            FOREIGN KEY (employee_id) REFERENCES employees (employee_id)
        )
    ''')
    
    conn.commit()
    conn.close()

# Password hashing function
def hash_password(password):
    """Hash a password using SHA-256 with a salt."""
    salt = "vertiv_salt"  # In production, use a unique salt per user
    return hashlib.sha256((password + salt).encode()).hexdigest()

# User authentication
def authenticate_user():
    """Authenticate employee credentials."""
    employee_id = input("Employee ID: ")
    password = getpass("Password: ")
    
    try:
        conn = sqlite3.connect('employee_portal.db')
        cursor = conn.cursor()
        
        cursor.execute(
            "SELECT password_hash, first_name, last_name, is_active FROM employees WHERE employee_id = ?",
            (employee_id,)
        )
        result = cursor.fetchone()
        
        if not result:
            print("Invalid credentials. Please try again.")
            return None
        
        stored_hash, first_name, last_name, is_active = result
        
        if not is_active:
            print("Your account is inactive. Please contact HR.")
            return None
            
        if hash_password(password) == stored_hash:
            # Update last login time
            cursor.execute(
                "UPDATE employees SET last_login = ? WHERE employee_id = ?",
                (datetime.now().isoformat(), employee_id)
            )
            conn.commit()
            print(f"Welcome, {first_name} {last_name}!")
            return employee_id
        else:
            print("Invalid credentials. Please try again.")
            return None
            
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None
    finally:
        conn.close()

# Employee dashboard
def show_employee_dashboard(employee_id):
    """Display the employee benefits dashboard."""
    try:
        conn = sqlite3.connect('employee_portal.db')
        cursor = conn.cursor()
        
        # Get employee info
        cursor.execute(
            "SELECT first_name, last_name, department FROM employees WHERE employee_id = ?",
            (employee_id,)
        )
        first_name, last_name, department = cursor.fetchone()
        
        # Get benefits
        cursor.execute(
            "SELECT benefit_type, enrollment_date, status FROM benefits WHERE employee_id = ?",
            (employee_id,)
        )
        benefits = cursor.fetchall()
        
        print("\n" + "="*50)
        print(f"EMPLOYEE BENEFITS PORTAL - {first_name} {last_name}")
        print("="*50)
        print(f"Department: {department}\n")
        
        print("Your Current Benefits:")
        print("-"*30)
        if benefits:
            for benefit in benefits:
                print(f"Type: {benefit[0]}")
                print(f"Enrolled: {benefit[1]}")
                print(f"Status: {benefit[2]}")
                print("-"*20)
        else:
            print("No benefits enrolled.")
        
        print("\nOptions:")
        print("1. View benefit details")
        print("2. Enroll in new benefit")
        print("3. Update personal information")
        print("4. Logout")
        
        choice = input("\nEnter your choice (1-4): ")
        return choice
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return '4'  # Force logout on error
    finally:
        conn.close()

# Main application loop
def main():
    """Main application entry point."""
    initialize_database()
    
    print("VERTIV EMPLOYEE BENEFITS PORTAL")
    print("="*30)
    
    while True:
        employee_id = authenticate_user()
        if not employee_id:
            continue
            
        while True:
            choice = show_employee_dashboard(employee_id)
            
            if choice == '1':
                print("\nBenefit details functionality would go here...")
                input("Press Enter to continue...")
            elif choice == '2':
                print("\nBenefit enrollment functionality would go here...")
                input("Press Enter to continue...")
            elif choice == '3':
                print("\nPersonal information update functionality would go here...")
                input("Press Enter to continue...")
            elif choice == '4':
                print("\nLogging out...")
                break
            else:
                print("\nInvalid choice. Please try again.")
                input("Press Enter to continue...")

if __name__ == "__main__":
    main()
```
