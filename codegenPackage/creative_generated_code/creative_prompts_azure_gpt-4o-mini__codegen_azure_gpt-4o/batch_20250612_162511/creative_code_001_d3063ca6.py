"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pgngaya.in
Prompt: Write a Python script that simulates the transport management system for a school, considering the constraints mentioned by Param Gyan Niketan regarding bus routes and stops.
Generated: DETERMINISTIC_d3063ca6458e34b2
Batch ID: 20250612_162511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Transport Management System for Param Gyan Niketan School
This script simulates a system to manage bus routes and stops efficiently.

Features:
- Add and view bus routes
- Add and view bus stops for each route
- Assign students to specific bus stops
- View summary of routes, stops, and assigned students
"""

# Import necessary modules
import sys

class TransportManagementSystem:
    def __init__(self):
        """Initialize the system with empty routes and students."""
        self.routes = {}  # Dictionary to store routes and their stops
        self.students = {}  # Dictionary to store students and assigned stops

    def add_route(self, route_id):
        """
        Adds a new route.

        Parameters:
        route_id (str): Unique identifier for the route.
        """
        if route_id not in self.routes:
            self.routes[route_id] = []
            print(f"Route '{route_id}' added successfully.")
        else:
            print(f"Route '{route_id}' already exists.")

    def add_stop_to_route(self, route_id, stop_name):
        """
        Adds a new stop to a specific route.

        Parameters:
        route_id (str): Unique identifier for the route.
        stop_name (str): Name of the stop to add.
        """
        if route_id in self.routes:
            if stop_name not in self.routes[route_id]:
                self.routes[route_id].append(stop_name)
                print(f"Stop '{stop_name}' added to route '{route_id}'.")
            else:
                print(f"Stop '{stop_name}' already exists in route '{route_id}'.")
        else:
            print(f"Route '{route_id}' does not exist. Please add the route first.")

    def assign_student_to_stop(self, student_name, route_id, stop_name):
        """
        Assigns a student to a specific stop on a route.

        Parameters:
        student_name (str): Name of the student.
        route_id (str): Unique identifier for the route.
        stop_name (str): Name of the stop.
        """
        if route_id in self.routes:
            if stop_name in self.routes[route_id]:
                self.students[student_name] = (route_id, stop_name)
                print(f"Student '{student_name}' assigned to stop '{stop_name}' on route '{route_id}'.")
            else:
                print(f"Stop '{stop_name}' does not exist in route '{route_id}'.")
        else:
            print(f"Route '{route_id}' does not exist.")

    def view_routes(self):
        """Displays all routes and their stops."""
        print("\nRoutes and Stops:")
        for route_id, stops in self.routes.items():
            print(f"Route '{route_id}': {', '.join(stops) if stops else 'No stops added'}")

    def view_students(self):
        """Displays all students and their assigned stops."""
        print("\nStudents Assigned to Stops:")
        if not self.students:
            print("No students assigned.")
        else:
            for student_name, (route_id, stop_name) in self.students.items():
                print(f"Student '{student_name}': Route '{route_id}', Stop '{stop_name}'")

    def run(self):
        """Main method to run the transport management system."""
        while True:
            print("\nTransport Management System")
            print("1. Add Route")
            print("2. Add Stop to Route")
            print("3. Assign Student to Stop")
            print("4. View Routes")
            print("5. View Students")
            print("6. Exit")
            
            try:
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    route_id = input("Enter Route ID: ")
                    self.add_route(route_id)
                elif choice == 2:
                    route_id = input("Enter Route ID: ")
                    stop_name = input("Enter Stop Name: ")
                    self.add_stop_to_route(route_id, stop_name)
                elif choice == 3:
                    student_name = input("Enter Student Name: ")
                    route_id = input("Enter Route ID: ")
                    stop_name = input("Enter Stop Name: ")
                    self.assign_student_to_stop(student_name, route_id, stop_name)
                elif choice == 4:
                    self.view_routes()
                elif choice == 5:
                    self.view_students()
                elif choice == 6:
                    print("Exiting the system. Goodbye!")
                    sys.exit()
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 6.")

# Entry point of the script
if __name__ == "__main__":
    system = TransportManagementSystem()
    system.run()
```
