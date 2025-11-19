"""
Generated Code Metadata:
========================
Original URL: https://fusionjiujitsu.com.br
Prompt: "Write a Python script to analyze student progress and generate reports based on their attendance and performance in Jiu-Jitsu classes at Fusion Jiu Jitsu School."
Generated: DETERMINISTIC_44199c98089a63a8
Batch ID: 20250622_210806
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
from collections import defaultdict

class StudentProgressAnalyzer:
    """
    Analyzes student progress and generates reports based on attendance and performance.
    """
    
    def __init__(self, attendance_file, performance_file, output_dir='reports'):
        """
        Initialize the analyzer with file paths and output directory.
        
        Args:
            attendance_file (str): Path to attendance CSV file
            performance_file (str): Path to performance CSV file
            output_dir (str): Directory to save reports (default: 'reports')
        """
        self.attendance_file = attendance_file
        self.performance_file = performance_file
        self.output_dir = output_dir
        self.students = defaultdict(dict)
        
        # Create output directory if it doesn't exist
        os.makedirs(self.output_dir, exist_ok=True)
    
    def load_data(self):
        """
        Load and parse attendance and performance data from CSV files.
        """
        try:
            # Load attendance data
            with open(self.attendance_file, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    student_id = row['student_id']
                    self.students[student_id]['name'] = row['name']
                    self.students[student_id]['belt_level'] = row['belt_level']
                    self.students[student_id].setdefault('attendance', []).append(row['date'])
            
            # Load performance data
            with open(self.performance_file, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    student_id = row['student_id']
                    self.students[student_id].setdefault('performance', []).append({
                        'date': row['date'],
                        'technique': row['technique'],
                        'score': float(row['score']),
                        'notes': row['notes']
                    })
        
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Data file not found: {e.filename}")
        except Exception as e:
            raise Exception(f"Error loading data: {str(e)}")
    
    def calculate_metrics(self):
        """
        Calculate various metrics for each student.
        """
        for student_id, data in self.students.items():
            # Attendance metrics
            attendance_dates = [datetime.strptime(d, '%Y-%m-%d') for d in data['attendance']]
            data['total_classes'] = len(attendance_dates)
            data['first_class'] = min(attendance_dates).strftime('%Y-%m-%d')
            data['last_class'] = max(attendance_dates).strftime('%Y-%m-%d')
            
            # Performance metrics
            if 'performance' in data:
                scores = [p['score'] for p in data['performance']]
                data['avg_score'] = sum(scores) / len(scores)
                data['max_score'] = max(scores)
                data['min_score'] = min(scores)
                data['techniques_learned'] = len({p['technique'] for p in data['performance']})
    
    def generate_individual_report(self, student_id):
        """
        Generate an individual report for a student.
        
        Args:
            student_id (str): ID of the student
            
        Returns:
            str: Report content
        """
        if student_id not in self.students:
            raise ValueError(f"Student ID {student_id} not found")
        
        data = self.students[student_id]
        report = [
            f"Fusion Jiu Jitsu School - Student Progress Report",
            f"\nStudent: {data['name']}",
            f"Belt Level: {data['belt_level']}",
            f"\nAttendance Summary:",
            f"- Total Classes Attended: {data['total_classes']}",
            f"- First Class: {data['first_class']}",
            f"- Last Class: {data['last_class']}",
        ]
        
        if 'performance' in data:
            report.extend([
                f"\nPerformance Summary:",
                f"- Average Score: {data['avg_score']:.2f}",
                f"- Highest Score: {data['max_score']:.2f}",
                f"- Lowest Score: {data['min_score']:.2f}",
                f"- Techniques Learned: {data['techniques_learned']}",
                f"\nRecent Notes:"
            ])
            
            # Add last 3 performance notes
            for note in data['performance'][-3:]:
                report.append(f"- {note['date']}: {note['notes']}")
        
        return '\n'.join(report)
    
    def generate_all_reports(self):
        """
        Generate reports for all students and save them to files.
        """
        try:
            for student_id in self.students:
                report = self.generate_individual_report(student_id)
                filename = os.path.join(self.output_dir, f"report_{student_id}.txt")
                with open(filename, 'w') as file:
                    file.write(report)
            return True
        except Exception as e:
            print(f"Error generating reports: {str(e)}")
            return False
    
    def generate_summary_report(self):
        """
        Generate a summary report for all students.
        """
        try:
            summary = [
                "Fusion Jiu Jitsu School - Summary Report",
                f"\nGenerated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
                f"\nTotal Students: {len(self.students)}",
                "\nAttendance Overview:"
            ]
            
            # Calculate attendance statistics
            total_classes = [s['total_classes'] for s in self.students.values()]
            summary.append(f"- Average classes attended: {sum(total_classes)/len(total_classes):.1f}")
            summary.append(f"- Most active student: {max(total_classes)} classes")
            summary.append(f"- Least active student: {min(total_classes)} classes")
            
            # Belt level distribution
            belt_counts = defaultdict(int)
            for student in self.students.values():
                belt_counts[student['belt_level']] += 1
            
            summary.append("\nBelt Level Distribution:")
            for belt, count in sorted(belt_counts.items()):
                summary.append(f"- {belt}: {count} students")
            
            # Performance overview
            if any('performance' in s for s in self.students.values()):
                avg_scores = [s['avg_score'] for s in self.students.values() if 'avg_score' in s]
                summary.extend([
                    "\nPerformance Overview:",
                    f"- Average score across all students: {sum(avg_scores)/len(avg_scores):.2f}",
                    f"- Highest average score: {max(avg_scores):.2f}",
                    f"- Lowest average score: {min(avg_scores):.2f}"
                ])
            
            filename = os.path.join(self.output_dir, "summary_report.txt")
            with open(filename, 'w') as file:
                file.write('\n'.join(summary))
            
            return True
        except Exception as e:
            print(f"Error generating summary report: {str(e)}")
            return False

def main():
    try:
        # Initialize analyzer with data files
        analyzer = StudentProgressAnalyzer(
            attendance_file='attendance.csv',
            performance_file='performance.csv'
        )
        
        # Load and process data
        analyzer.load_data()
        analyzer.calculate_metrics()
        
        # Generate reports
        analyzer.generate_all_reports()
        analyzer.generate_summary_report()
        
        print("Reports generated successfully in the 'reports' directory.")
    
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
```
