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
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

// Class representing a Student
class Student {
    private String name;
    private Map<String, Integer> subjectScores;

    // Constructor
    public Student(String name) {
        this.name = name;
        this.subjectScores = new HashMap<>();
    }

    // Add or update score for a subject
    public void updateScore(String subject, int score) {
        if (score < 0 || score > 100) {
            throw new IllegalArgumentException("Score must be between 0 and 100.");
        }
        subjectScores.put(subject, score);
    }

    // Get score for a specific subject
    public int getScore(String subject) {
        return subjectScores.getOrDefault(subject, 0);
    }

    // Get all scores
    public Map<String, Integer> getAllScores() {
        return new HashMap<>(subjectScores);
    }

    // Get student name
    public String getName() {
        return name;
    }
}

// Class representing the Learning Management System
class LearningManagementSystem {
    private List<Student> students;

    // Constructor
    public LearningManagementSystem() {
        this.students = new ArrayList<>();
    }

    // Add a new student
    public void addStudent(String name) {
        if (name == null || name.isEmpty()) {
            throw new IllegalArgumentException("Student name cannot be null or empty.");
        }
        students.add(new Student(name));
    }

    // Find a student by name
    public Student findStudent(String name) {
        for (Student student : students) {
            if (student.getName().equalsIgnoreCase(name)) {
                return student;
            }
        }
        throw new IllegalArgumentException("Student not found: " + name);
    }

    // Display all students and their scores
    public void displayAllStudents() {
        if (students.isEmpty()) {
            System.out.println("No students available.");
            return;
        }
        for (Student student : students) {
            System.out.println("Student: " + student.getName());
            System.out.println("Scores: " + student.getAllScores());
            System.out.println("----------------------");
        }
    }
}

// Main class to demonstrate the functionality
public class Main {
    public static void main(String[] args) {
        // Create an instance of the Learning Management System
        LearningManagementSystem lms = new LearningManagementSystem();

        try {
            // Add students
            lms.addStudent("Alice");
            lms.addStudent("Bob");

            // Update scores for subjects
            Student alice = lms.findStudent("Alice");
            alice.updateScore("수학", 95);
            alice.updateScore("체육", 88);

            Student bob = lms.findStudent("Bob");
            bob.updateScore("수학", 78);
            bob.updateScore("체육", 92);

            // Display all students and their scores
            lms.displayAllStudents();
        } catch (IllegalArgumentException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```
