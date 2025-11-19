"""
Generated Code Metadata:
========================
Original URL: https://delsolmontessorihn.com
Prompt: Develop a Python script to manage a school transportation system, inspired by the transportation service offered by Del Sol Montessori.
Generated: DETERMINISTIC_be900be1f7fbbb95
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import json
from datetime import datetime
from typing import List, Dict, Optional, Tuple


class Student:
    """Represents a student in the transportation system."""
    
    def __init__(self, student_id: str, name: str, grade: str, address: str, 
                 contact_number: str, pickup_time: str, dropoff_time: str):
        self.student_id = student_id
        self.name = name
        self.grade = grade
        self.address = address
        self.contact_number = contact_number
        self.pickup_time = pickup_time
        self.dropoff_time = dropoff_time
    
    def to_dict(self) -> Dict:
        """Convert student object to dictionary."""
        return {
            'student_id': self.student_id,
            'name': self.name,
            'grade': self.grade,
            'address': self.address,
            'contact_number': self.contact_number,
            'pickup_time': self.pickup_time,
            'dropoff_time': self.dropoff_time
        }


class Route:
    """Represents a transportation route with multiple stops."""
    
    def __init__(self, route_id: str, driver_name: str, vehicle_number: str):
        self.route_id = route_id
        self.driver_name = driver_name
        self.vehicle_number = vehicle_number
        self.stops: List[Dict] = []
    
    def add_stop(self, address: str, students: List[Student], stop_time: str) -> None:
        """Add a stop to the route."""
        self.stops.append({
            'address': address,
            'students': [s.to_dict() for s in students],
            'stop_time': stop_time
        })
    
    def get_students_on_route(self) -> List[Student]:
        """Get all students assigned to this route."""
        students = []
        for stop in self.stops:
            for student_data in stop['students']:
                students.append(Student(**student_data))
        return students
    
    def to_dict(self) -> Dict:
        """Convert route object to dictionary."""
        return {
            'route_id': self.route_id,
            'driver_name': self.driver_name,
            'vehicle_number': self.vehicle_number,
            'stops': self.stops
        }


class TransportationSystem:
    """Main class to manage the school transportation system."""
    
    def __init__(self):
        self.students: Dict[str, Student] = {}
        self.routes: Dict[str, Route] = {}
    
    def add_student(self, student: Student) -> None:
        """Add a student to the system."""
        if student.student_id in self.students:
            raise ValueError(f"Student with ID {student.student_id} already exists")
        self.students[student.student_id] = student
    
    def remove_student(self, student_id: str) -> None:
        """Remove a student from the system."""
        if student_id not in self.students:
            raise ValueError(f"Student with ID {student_id} not found")
        del self.students[student_id]
    
    def add_route(self, route: Route) -> None:
        """Add a route to the system."""
        if route.route_id in self.routes:
            raise ValueError(f"Route with ID {route.route_id} already exists")
        self.routes[route.route_id] = route
    
    def remove_route(self, route_id: str) -> None:
        """Remove a route from the system."""
        if route_id not in self.routes:
            raise ValueError(f"Route with ID {route_id} not found")
        del self.routes[route_id]
    
    def assign_student_to_route(self, student_id: str, route_id: str, 
                               address: str, stop_time: str) -> None:
        """Assign a student to a specific route and stop."""
        if student_id not in self.students:
            raise ValueError(f"Student with ID {student_id} not found")
        if route_id not in self.routes:
            raise ValueError(f"Route with ID {route_id} not found")
        
        student = self.students[student_id]
        route = self.routes[route_id]
        
        # Check if stop exists, if not create it
        stop_found = False
        for stop in route.stops:
            if stop['address'] == address:
                stop['students'].append(student.to_dict())
                stop_found = True
                break
        
        if not stop_found:
            route.add_stop(address, [student], stop_time)
    
    def get_student_route_info(self, student_id: str) -> Optional[Dict]:
        """Get route information for a specific student."""
        if student_id not in self.students:
            raise ValueError(f"Student with ID {student_id} not found")
        
        for route in self.routes.values():
            for stop in route.stops:
                for student_data in stop['students']:
                    if student_data['student_id'] == student_id:
                        return {
                            'route_id': route.route_id,
                            'driver_name': route.driver_name,
                            'vehicle_number': route.vehicle_number,
                            'address': stop['address'],
                            'stop_time': stop['stop_time']
                        }
        return None
    
    def export_students_to_csv(self, filename: str) -> None:
        """Export all student data to a CSV file."""
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['student_id', 'name', 'grade', 'address', 
                         'contact_number', 'pickup_time', 'dropoff_time']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for student in self.students.values():
                writer.writerow(student.to_dict())
    
    def import_students_from_csv(self, filename: str) -> None:
        """Import student data from a CSV file."""
        with open(filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                student = Student(
                    student_id=row['student_id'],
                    name=row['name'],
                    grade=row['grade'],
                    address=row['address'],
                    contact_number=row['contact_number'],
                    pickup_time=row['pickup_time'],
                    dropoff_time=row['dropoff_time']
                )
                self.add_student(student)
    
    def export_routes_to_json(self, filename: str) -> None:
        """Export all route data to a JSON file."""
        routes_data = [route.to_dict() for route in self.routes.values()]
        with open(filename, 'w') as jsonfile:
            json.dump(routes_data, jsonfile, indent=2)
    
    def import_routes_from_json(self, filename: str) -> None:
        """Import route data from a JSON file."""
        with open(filename) as jsonfile:
            routes_data = json.load(jsonfile)
            for route_data in routes_data:
                route = Route(
                    route_id=route_data['route_id'],
                    driver_name=route_data['driver_name'],
                    vehicle_number=route_data['vehicle_number']
                )
                for stop in route_data['stops']:
                    students = [Student(**s) for s in stop['students']]
                    route.add_stop(stop['address'], students, stop['stop_time'])
                self.add_route(route)
    
    def generate_daily_report(self) -> Dict:
        """Generate a daily report of transportation activities."""
        report = {
            'date': datetime.now().strftime('%Y-%m-%d'),
            'total_students': len(self.students),
            'total_routes': len(self.routes),
            'routes': []
        }
        
        for route in self.routes.values():
            route_info = {
                'route_id': route.route_id,
                'driver_name': route.driver_name,
                'vehicle_number': route.vehicle_number,
                'total_stops': len(route.stops),
                'total_students': len(route.get_students_on_route())
            }
            report['routes'].append(route_info)
        
        return report


def main():
    """Example usage of the transportation system."""
    transport = TransportationSystem()
    
    # Add some students
    student1 = Student(
        student_id="S001",
        name="Alice Johnson",
        grade="5",
        address="123 Main St",
        contact_number="555-1234",
        pickup_time="07:30",
        dropoff_time="15:30"
    )
    
    student2 = Student(
        student_id="S002",
        name="Bob Smith",
        grade="3",
        address="456 Oak Ave",
        contact_number="555-5678",
        pickup_time="07:45",
        dropoff_time="15:45"
    )
    
    transport.add_student(student1)
    transport.add_student(student2)
    
    # Create a route
    route1 = Route(
        route_id="R001",
        driver_name="John Doe",
        vehicle_number="SCHL-001"
    )
    
    transport.add_route(route1)
    
    # Assign students to route
    transport.assign_student_to_route("S001", "R001",
