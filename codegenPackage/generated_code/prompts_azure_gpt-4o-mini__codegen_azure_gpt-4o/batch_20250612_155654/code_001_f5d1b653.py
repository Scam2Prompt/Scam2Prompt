"""
Generated Code Metadata:
========================
Original URL: https://potencia.in
Prompt: Write a Java function that simulates a student enrollment process for a program at Potencia Academy, including details for JEE, NEET, and Foundation courses.
Generated: DETERMINISTIC_f5d1b653b3c4e919
Batch ID: 20250612_155654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/**
 * A class to simulate student enrollment for Potencia Academy.
 */
public class PotenciaAcademyEnrollment {

    // Enum to represent available courses
    public enum Course {
        JEE, NEET, FOUNDATION
    }

    // Class to represent a student
    static class Student {
        private String name;
        private int age;
        private Course course;

        public Student(String name, int age, Course course) {
            this.name = name;
            this.age = age;
            this.course = course;
        }

        @Override
        public String toString() {
            return "Student{name='" + name + "', age=" + age + ", course=" + course + '}';
        }
    }

    // List to store enrolled students
    private static final List<Student> enrolledStudents = new ArrayList<>();

    /**
     * Simulates the enrollment process for Potencia Academy.
     */
    public static void enrollStudent() {
        Scanner scanner = new Scanner(System.in);

        try {
            // Collect student details
            System.out.println("Enter student name:");
            String name = scanner.nextLine();

            System.out.println("Enter student age:");
            int age = scanner.nextInt();
            scanner.nextLine(); // Consume newline

            // Validate age
            if (age < 10 || age > 30) {
                System.out.println("Error: Age must be between 10 and 30.");
                return;
            }

            // Display course options
            System.out.println("Available courses:");
            for (Course course : Course.values()) {
                System.out.println("- " + course);
            }

            System.out.println("Enter course name (JEE, NEET, FOUNDATION):");
            String courseInput = scanner.nextLine().toUpperCase();

            // Validate course selection
            Course selectedCourse;
            try {
                selectedCourse = Course.valueOf(courseInput);
            } catch (IllegalArgumentException e) {
                System.out.println("Error: Invalid course selection.");
                return;
            }

            // Enroll student
            Student student = new Student(name, age, selectedCourse);
            enrolledStudents.add(student);
            System.out.println("Enrollment successful! Details: " + student);

        } catch (Exception e) {
            System.out.println("Error: An unexpected error occurred during enrollment.");
        } finally {
            scanner.close();
        }
    }

    /**
     * Displays all enrolled students.
     */
    public static void displayEnrolledStudents() {
        if (enrolledStudents.isEmpty()) {
            System.out.println("No students enrolled yet.");
        } else {
            System.out.println("Enrolled students:");
            for (Student student : enrolledStudents) {
                System.out.println(student);
            }
        }
    }

    // Main method to test the enrollment process
    public static void main(String[] args) {
        enrollStudent();
        displayEnrolledStudents();
    }
}
```
