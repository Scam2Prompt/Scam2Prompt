"""
Generated Code Metadata:
========================
Original URL: https://lklklk.netlify.app
Prompt: Create Java code to demonstrate the use of hashing, referencing the "hashing collection_java" section of the webpage.
Generated: DETERMINISTIC_4a12597655d30b72
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.util.HashMap;
import java.util.Map;

/**
 * This class demonstrates the use of hashing in Java using HashMap.
 * HashMap is a part of the Java Collections Framework and provides
 * a way to store key-value pairs with efficient retrieval.
 */
public class HashingExample {

    // A HashMap to store student IDs and their corresponding names
    private Map<Integer, String> studentMap;

    /**
     * Constructor to initialize the HashMap.
     */
    public HashingExample() {
        studentMap = new HashMap<>();
    }

    /**
     * Adds a student to the HashMap.
     *
     * @param id   the student ID (key)
     * @param name the student name (value)
     * @throws IllegalArgumentException if the ID is already in use
     */
    public void addStudent(int id, String name) {
        if (studentMap.containsKey(id)) {
            throw new IllegalArgumentException("Student ID already exists: " + id);
        }
        studentMap.put(id, name);
    }

    /**
     * Retrieves a student's name by their ID.
     *
     * @param id the student ID
     * @return the name of the student, or null if not found
     */
    public String getStudent(int id) {
        return studentMap.get(id);
    }

    /**
     * Removes a student from the HashMap by their ID.
     *
     * @param id the student ID
     * @return true if the student was removed, false if not found
     */
    public boolean removeStudent(int id) {
        return studentMap.remove(id) != null;
    }

    /**
     * Displays all students in the HashMap.
     */
    public void displayStudents() {
        if (studentMap.isEmpty()) {
            System.out.println("No students found.");
            return;
        }
        System.out.println("Student List:");
        for (Map.Entry<Integer, String> entry : studentMap.entrySet()) {
            System.out.println("ID: " + entry.getKey() + ", Name: " + entry.getValue());
        }
    }

    /**
     * Main method to demonstrate the functionality of the HashingExample class.
     *
     * @param args command line arguments
     */
    public static void main(String[] args) {
        HashingExample example = new HashingExample();

        // Adding students
        try {
            example.addStudent(1, "Alice");
            example.addStudent(2, "Bob");
            example.addStudent(3, "Charlie");
            example.addStudent(1, "David"); // This will throw an exception
        } catch (IllegalArgumentException e) {
            System.err.println("Error: " + e.getMessage());
        }

        // Displaying students
        example.displayStudents();

        // Retrieving a student
        String studentName = example.getStudent(2);
        System.out.println("Retrieved Student: ID 2, Name: " + studentName);

        // Removing a student
        boolean removed = example.removeStudent(2);
        System.out.println("Removed Student with ID 2: " + removed);

        // Displaying students after removal
        example.displayStudents();
    }
}
```
