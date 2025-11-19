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
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/**
 * Represents a course offered by Potencia Academy.
 */
class Course {
    private String name;
    private double fee;

    public Course(String name, double fee) {
        this.name = name;
        this.fee = fee;
    }

    public String getName() {
        return name;
    }

    public double getFee() {
        return fee;
    }
}

/**
 * Represents a student enrolling in courses at Potencia Academy.
 */
class Student {
    private String name;
    private List<Course> enrolledCourses;

    public Student(String name) {
        this.name = name;
        this.enrolledCourses = new ArrayList<>();
    }

    public String getName() {
        return name;
    }

    public void enrollInCourse(Course course) {
        enrolledCourses.add(course);
    }

    public List<Course> getEnrolledCourses() {
        return enrolledCourses;
    }

    public double calculateTotalFees() {
        return enrolledCourses.stream().mapToDouble(Course::getFee).sum();
    }
}

/**
 * Main class to simulate the enrollment process at Potencia Academy.
 */
public class EnrollmentSystem {

    private static final Course JEE = new Course("JEE", 15000);
    private static final Course NEET = new Course("NEET", 12000);
    private static final Course FOUNDATION = new Course("Foundation", 10000);
    
    /**
     * Simulates the enrollment process for students.
     */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        try {
            System.out.print("Enter Student Name: ");
            String studentName = scanner.nextLine();

            Student student = new Student(studentName);
            boolean enrolling = true;

            // Enrollment loop
            while (enrolling) {
                System.out.println("Available courses:");
                System.out.println("1. JEE - ₹15,000");
                System.out.println("2. NEET - ₹12,000");
                System.out.println("3. Foundation - ₹10,000");
                System.out.println("4. Finish Enrollment");

                System.out.print("Select a course to enroll (1-4): ");
                int choice = Integer.parseInt(scanner.nextLine());

                switch (choice) {
                    case 1:
                        student.enrollInCourse(JEE);
                        System.out.println("Enrolled in " + JEE.getName());
                        break;
                    case 2:
                        student.enrollInCourse(NEET);
                        System.out.println("Enrolled in " + NEET.getName());
                        break;
                    case 3:
                        student.enrollInCourse(FOUNDATION);
                        System.out.println("Enrolled in " + FOUNDATION.getName());
                        break;
                    case 4:
                        enrolling = false;
                        break;
                    default:
                        System.out.println("Invalid choice, please try again.");
                }
            }

            // Display enrollment summary
            System.out.println("\nEnrollment Summary for " + student.getName() + ":");
            for (Course course : student.getEnrolledCourses()) {
                System.out.println(" - " + course.getName());
            }
            System.out.printf("Total Fees: ₹%.2f%n", student.calculateTotalFees());

        } catch (NumberFormatException e) {
            System.out.println("Invalid input, please enter a number.");
        } catch (Exception e) {
            System.out.println("An error occurred: " + e.getMessage());
        } finally {
            scanner.close();
        }
    }
}
```
