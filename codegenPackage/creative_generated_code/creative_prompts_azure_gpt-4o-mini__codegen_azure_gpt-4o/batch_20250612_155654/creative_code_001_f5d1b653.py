"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://potencia.in
Prompt: Write a Java function that simulates a student enrollment process for a program at Potencia Academy, including details for JEE, NEET, and Foundation courses.
Generated: DETERMINISTIC_f5d1b653b3c4e919
Batch ID: 20250612_155654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```java
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

/**
 * A class to simulate the student enrollment process at Potencia Academy.
 */
public class EnrollmentSystem {

    // Store course details
    private static final Map<String, String> courses = new HashMap<>();

    static {
        courses.put("JEE", "Joint Entrance Examination course for engineering aspirants.");
        courses.put("NEET", "National Eligibility cum Entrance Test course for medical aspirants.");
        courses.put("Foundation", "Foundation course for building strong basics in Science and Mathematics for grades 8-10.");
    }

    /**
     * Method to enroll a student in a course.
     *
     * @param studentName Name of the student
     * @param courseName  Name of the course
     */
    public static void enrollStudent(String studentName, String courseName) {
        // Validate course name
        if (!courses.containsKey(courseName)) {
            System.out.println("Error: Invalid course name. Please choose JEE, NEET, or Foundation.");
            return;
        }

        // Enrollment successful
        System.out.println("Enrollment successful!");
        System.out.println("Student Name: " + studentName);
        System.out.println("Enrolled Course: " + courseName);
        System.out.println("Course Details: " + courses.get(courseName));
    }

    /**
     * Main method to simulate the student enrollment process.
     *
     * @param args Command-line arguments
     */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Prompt user for student name
        System.out.print("Enter student name: ");
        String studentName = scanner.nextLine();

        // Prompt user for course name
        System.out.print("Enter course name (JEE, NEET, Foundation): ");
        String courseName = scanner.nextLine();

        // Enroll the student
        enrollStudent(studentName, courseName);

        // Close the scanner
        scanner.close();
    }
}
```
