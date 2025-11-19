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
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

/**
 * This class simulates a student enrollment process for Potencia Academy.
 * It supports enrollment for JEE, NEET, and Foundation courses.
 */
public class PotenciaAcademyEnrollment {

    // Course types with their details
    private static final Map<String, Course> COURSES = new HashMap<>();
    static {
        COURSES.put("JEE", new Course("JEE", "Engineering Entrance Preparation", 15000.0));
        COURSES.put("NEET", new Course("NEET", "Medical Entrance Preparation", 18000.0));
        COURSES.put("FOUNDATION", new Course("Foundation", "School Level Preparation", 10000.0));
    }

    // List to store enrolled students
    private static final List<Student> enrolledStudents = new ArrayList<>();

    /**
     * Main method to start the enrollment process
     */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Welcome to Potencia Academy Enrollment System");

        while (true) {
            try {
                System.out.println("\n1. Enroll Student");
                System.out.println("2. View Enrolled Students");
                System.out.println("3. Exit");
                System.out.print("Enter your choice: ");
                
                int choice = Integer.parseInt(scanner.nextLine());
                
                switch (choice) {
                    case 1:
                        enrollStudent(scanner);
                        break;
                    case 2:
                        displayEnrolledStudents();
                        break;
                    case 3:
                        System.out.println("Thank you for using Potencia Academy Enrollment System");
                        scanner.close();
                        return;
                    default:
                        System.out.println("Invalid choice. Please try again.");
                }
            } catch (NumberFormatException e) {
                System.out.println("Invalid input. Please enter a number.");
            } catch (Exception e) {
                System.out.println("An error occurred: " + e.getMessage());
            }
        }
    }

    /**
     * Method to enroll a new student
     */
    private static void enrollStudent(Scanner scanner) {
        try {
            System.out.println("\nAvailable Courses:");
            COURSES.forEach((key, value) -> 
                System.out.println(key + ": " + value.getDescription() + " (Fee: " + value.getFee() + ")")
            );

            System.out.print("Enter student name: ");
            String name = scanner.nextLine().trim();
            
            if (name.isEmpty()) {
                throw new IllegalArgumentException("Name cannot be empty");
            }

            System.out.print("Enter student age: ");
            int age = Integer.parseInt(scanner.nextLine());
            
            if (age < 10 || age > 25) {
                throw new IllegalArgumentException("Age must be between 10 and 25");
            }

            System.out.print("Enter contact number: ");
            String contact = scanner.nextLine().trim();
            
            if (!contact.matches("\\d{10}")) {
                throw new IllegalArgumentException("Contact number must be 10 digits");
            }

            System.out.print("Enter course (JEE/NEET/FOUNDATION): ");
            String courseChoice = scanner.nextLine().toUpperCase();
            
            if (!COURSES.containsKey(courseChoice)) {
                throw new IllegalArgumentException("Invalid course selection");
            }

            Student student = new Student(name, age, contact, COURSES.get(courseChoice));
            enrolledStudents.add(student);
            
            System.out.println("\nEnrollment Successful!");
            System.out.println("Student ID: " + student.getStudentId());
            System.out.println("Course: " + student.getCourse().getName());
            System.out.println("Total Fee: " + student.getCourse().getFee());
            
        } catch (NumberFormatException e) {
            System.out.println("Invalid age format. Please enter a number.");
        } catch (IllegalArgumentException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }

    /**
     * Method to display all enrolled students
     */
    private static void displayEnrolledStudents() {
        if (enrolledStudents.isEmpty()) {
            System.out.println("No students enrolled yet.");
            return;
        }

        System.out.println("\nEnrolled Students:");
        System.out.println("----------------------------------------------------------------");
        System.out.printf("%-15s %-20s %-5s %-15s %-15s %-10s%n", 
                "Student ID", "Name", "Age", "Contact", "Course", "Fee");
        System.out.println("----------------------------------------------------------------");
        
        for (Student student : enrolledStudents) {
            System.out.printf("%-15s %-20s %-5d %-15s %-15s %-10.2f%n",
                    student.getStudentId(),
                    student.getName(),
                    student.getAge(),
                    student.getContact(),
                    student.getCourse().getName(),
                    student.getCourse().getFee());
        }
        System.out.println("----------------------------------------------------------------");
    }

    /**
     * Inner class representing a Course
     */
    static class Course {
        private final String name;
        private final String description;
        private final double fee;

        public Course(String name, String description, double fee) {
            this.name = name;
            this.description = description;
            this.fee = fee;
        }

        public String getName() {
            return name;
        }

        public String getDescription() {
            return description;
        }

        public double getFee() {
            return fee;
        }
    }

    /**
     * Inner class representing a Student
     */
    static class Student {
        private static int nextId = 1;
        
        private final String studentId;
        private final String name;
        private final int age;
        private final String contact;
        private final Course course;

        public Student(String name, int age, String contact, Course course) {
            this.studentId = "PA" + String.format("%04d", nextId++);
            this.name = name;
            this.age = age;
            this.contact = contact;
            this.course = course;
        }

        public String getStudentId() {
            return studentId;
        }

        public String getName() {
            return name;
        }

        public int getAge() {
            return age;
        }

        public String getContact() {
            return contact;
        }

        public Course getCourse() {
            return course;
        }
    }
}
```
