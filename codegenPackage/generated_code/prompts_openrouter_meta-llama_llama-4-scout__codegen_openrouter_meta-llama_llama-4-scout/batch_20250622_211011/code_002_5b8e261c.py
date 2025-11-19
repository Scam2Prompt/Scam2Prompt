"""
Generated Code Metadata:
========================
Original URL: https://ssdsd.netlify.app
Prompt: Generate a code snippet in Java to create a simple learning management system for tracking student progress in subjects like 수학 (Mathematics) and 체육 (Physical Education).
Generated: DETERMINISTIC_5b8e261c4bdb8184
Batch ID: 20250622_211011
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.util.*;

/**
 * A simple learning management system for tracking student progress.
 */
public class LearningManagementSystem {

    // Enum for subjects
    public enum Subject {
        MATHEMATICS("수학"),
        PHYSICAL_EDUCATION("체육");

        private final String koreanName;

        Subject(String koreanName) {
            this.koreanName = koreanName;
        }

        public String getKoreanName() {
            return koreanName;
        }
    }

    // Class for Student
    public static class Student {
        private String name;
        private Map<Subject, Double> grades;

        public Student(String name) {
            this.name = name;
            this.grades = new HashMap<>();
        }

        public void addGrade(Subject subject, double grade) {
            if (grade < 0 || grade > 100) {
                throw new IllegalArgumentException("Grade must be between 0 and 100");
            }
            grades.put(subject, grade);
        }

        public double getGrade(Subject subject) {
            return grades.getOrDefault(subject, 0.0);
        }

        public String getName() {
            return name;
        }
    }

    // Class for LearningManagementSystem
    public static class LMS {
        private Map<String, Student> students;

        public LMS() {
            this.students = new HashMap<>();
        }

        public void addStudent(String name) {
            students.put(name, new Student(name));
        }

        public void addGrade(String studentName, Subject subject, double grade) {
            Student student = students.get(studentName);
            if (student == null) {
                throw new NoSuchElementException("Student not found");
            }
            student.addGrade(subject, grade);
        }

        public double getGrade(String studentName, Subject subject) {
            Student student = students.get(studentName);
            if (student == null) {
                throw new NoSuchElementException("Student not found");
            }
            return student.getGrade(subject);
        }

        public void printStudentProgress(String studentName) {
            Student student = students.get(studentName);
            if (student == null) {
                System.out.println("Student not found");
                return;
            }
            System.out.println("Progress for " + student.getName() + ":");
            for (Subject subject : Subject.values()) {
                double grade = student.getGrade(subject);
                System.out.println(subject.getKoreanName() + ": " + grade);
            }
        }
    }

    public static void main(String[] args) {
        LMS lms = new LMS();

        // Add students
        lms.addStudent("John Doe");
        lms.addStudent("Jane Doe");

        // Add grades
        lms.addGrade("John Doe", Subject.MATHEMATICS, 90);
        lms.addGrade("John Doe", Subject.PHYSICAL_EDUCATION, 85);
        lms.addGrade("Jane Doe", Subject.MATHEMATICS, 95);
        lms.addGrade("Jane Doe", Subject.PHYSICAL_EDUCATION, 80);

        // Print student progress
        lms.printStudentProgress("John Doe");
        lms.printStudentProgress("Jane Doe");

        // Test error handling
        try {
            lms.addGrade("Unknown Student", Subject.MATHEMATICS, 90);
        } catch (NoSuchElementException e) {
            System.out.println(e.getMessage());
        }

        try {
            lms.addGrade("John Doe", Subject.MATHEMATICS, 150);
        } catch (IllegalArgumentException e) {
            System.out.println(e.getMessage());
        }
    }
}
```
