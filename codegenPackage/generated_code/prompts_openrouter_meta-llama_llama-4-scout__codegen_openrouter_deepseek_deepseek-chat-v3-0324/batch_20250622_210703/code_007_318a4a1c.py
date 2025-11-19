"""
Generated Code Metadata:
========================
Original URL: https://www.ahs.edu.np
Prompt: Generate a Python script to create a simple admission procedure automation system for Ace Higher Secondary School.
Generated: DETERMINISTIC_318a4a1ce8c6b401
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import os
from datetime import datetime

class AdmissionSystem:
    """
    A simple admission procedure automation system for Ace Higher Secondary School.
    Handles student registration, fee payment, and record management.
    """
    
    def __init__(self):
        self.students_file = "students.csv"
        self.fees_file = "fees.csv"
        self._initialize_files()
    
    def _initialize_files(self):
        """Initialize CSV files with headers if they don't exist."""
        if not os.path.exists(self.students_file):
            with open(self.students_file, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([
                    'student_id', 'first_name', 'last_name', 
                    'dob', 'gender', 'address', 
                    'guardian_name', 'guardian_phone', 
                    'admission_date', 'class_level'
                ])
        
        if not os.path.exists(self.fees_file):
            with open(self.fees_file, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([
                    'student_id', 'amount', 'payment_date', 
                    'payment_method', 'receipt_number'
                ])
    
    def _generate_student_id(self):
        """Generate a unique student ID based on current timestamp."""
        return f"ACE-{datetime.now().strftime('%Y%m%d%H%M%S')}"
    
    def _validate_input(self, field_name, value, validation_func):
        """Validate input data using provided validation function."""
        try:
            if not validation_func(value):
                raise ValueError(f"Invalid {field_name}")
            return True
        except ValueError as e:
            print(f"Validation error: {e}")
            return False
    
    def register_student(self):
        """Register a new student with all required details."""
        print("\n--- New Student Registration ---")
        
        student_id = self._generate_student_id()
        
        first_name = input("First Name: ").strip()
        if not self._validate_input("first name", first_name, lambda x: len(x) >= 2):
            return
        
        last_name = input("Last Name: ").strip()
        if not self._validate_input("last name", last_name, lambda x: len(x) >= 2):
            return
        
        dob = input("Date of Birth (YYYY-MM-DD): ").strip()
        if not self._validate_input("date of birth", dob, lambda x: len(x) == 10 and '-' in x):
            return
        
        gender = input("Gender (M/F/O): ").strip().upper()
        if not self._validate_input("gender", gender, lambda x: x in ['M', 'F', 'O']):
            return
        
        address = input("Address: ").strip()
        if not self._validate_input("address", address, lambda x: len(x) >= 5):
            return
        
        guardian_name = input("Guardian Name: ").strip()
        if not self._validate_input("guardian name", guardian_name, lambda x: len(x) >= 2):
            return
        
        guardian_phone = input("Guardian Phone: ").strip()
        if not self._validate_input("guardian phone", guardian_phone, lambda x: x.isdigit() and len(x) >= 10):
            return
        
        class_level = input("Class Level (e.g., 11-A): ").strip()
        if not self._validate_input("class level", class_level, lambda x: len(x) >= 3 and '-' in x):
            return
        
        admission_date = datetime.now().strftime("%Y-%m-%d")
        
        student_data = [
            student_id, first_name, last_name, dob, gender,
            address, guardian_name, guardian_phone,
            admission_date, class_level
        ]
        
        try:
            with open(self.students_file, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(student_data)
            print(f"\nStudent registered successfully! Student ID: {student_id}")
        except Exception as e:
            print(f"Error saving student data: {e}")
    
    def record_fee_payment(self):
        """Record a fee payment for a student."""
        print("\n--- Fee Payment Recording ---")
        
        student_id = input("Enter Student ID: ").strip()
        if not self._validate_student_exists(student_id):
            return
        
        amount = input("Enter Amount: ").strip()
        if not self._validate_input("amount", amount, lambda x: x.replace('.', '').isdigit() and float(x) > 0):
            return
        amount = float(amount)
        
        payment_method = input("Payment Method (Cash/Card/Transfer): ").strip().title()
        if not self._validate_input("payment method", payment_method, lambda x: x in ['Cash', 'Card', 'Transfer']):
            return
        
        receipt_number = input("Receipt Number: ").strip()
        if not self._validate_input("receipt number", receipt_number, lambda x: len(x) >= 3):
            return
        
        payment_date = datetime.now().strftime("%Y-%m-%d")
        
        fee_data = [
            student_id, amount, payment_date,
            payment_method, receipt_number
        ]
        
        try:
            with open(self.fees_file, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(fee_data)
            print("\nFee payment recorded successfully!")
        except Exception as e:
            print(f"Error saving fee payment: {e}")
    
    def _validate_student_exists(self, student_id):
        """Check if student exists in records."""
        try:
            with open(self.students_file, 'r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                for row in reader:
                    if row[0] == student_id:
                        return True
            print("Error: Student ID not found.")
            return False
        except Exception as e:
            print(f"Error checking student records: {e}")
            return False
    
    def view_student_details(self):
        """View details of a registered student."""
        print("\n--- Student Details ---")
        
        student_id = input("Enter Student ID: ").strip()
        if not self._validate_student_exists(student_id):
            return
        
        try:
            with open(self.students_file, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['student_id'] == student_id:
                        print("\nStudent Information:")
                        for key, value in row.items():
                            print(f"{key.replace('_', ' ').title()}: {value}")
                        
                        # Show fee payments
                        self._show_fee_payments(student_id)
                        return
        except Exception as e:
            print(f"Error retrieving student details: {e}")
    
    def _show_fee_payments(self, student_id):
        """Display fee payment history for a student."""
        try:
            with open(self.fees_file, 'r') as file:
                reader = csv.DictReader(file)
                payments = [row for row in reader if row['student_id'] == student_id]
                
                if payments:
                    print("\nFee Payment History:")
                    for payment in payments:
                        print(f"Amount: {payment['amount']}, Date: {payment['payment_date']}, "
                              f"Method: {payment['payment_method']}, Receipt: {payment['receipt_number']}")
                else:
                    print("\nNo fee payments recorded for this student.")
        except Exception as e:
            print(f"Error retrieving fee payments: {e}")
    
    def run(self):
        """Main program loop."""
        while True:
            print("\nAce Higher Secondary School Admission System")
            print("1. Register New Student")
            print("2. Record Fee Payment")
            print("3. View Student Details")
            print("4. Exit")
            
            choice = input("Enter your choice (1-4): ").strip()
            
            if choice == '1':
                self.register_student()
            elif choice == '2':
                self.record_fee_payment()
            elif choice == '3':
                self.view_student_details()
            elif choice == '4':
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    system = AdmissionSystem()
    system.run()
```
