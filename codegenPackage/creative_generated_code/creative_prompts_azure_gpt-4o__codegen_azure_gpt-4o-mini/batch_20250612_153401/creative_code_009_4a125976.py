"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lklklk.netlify.app
Prompt: Create Java code to demonstrate the use of hashing, referencing the "hashing collection_java" section of the webpage.
Generated: DETERMINISTIC_4a12597655d30b72
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```java
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;

/**
 * This class demonstrates the use of hashing in Java using HashMap and HashSet.
 * HashMap is used for key-value pair storage, while HashSet is used for storing unique elements.
 */
public class HashingDemo {

    /**
     * Main method to run the hashing demonstration.
     * 
     * @param args Command-line arguments (not used).
     */
    public static void main(String[] args) {
        // Demonstrate HashMap
        Map<String, Integer> studentGrades = new HashMap<>();
        
        // Adding key-value pairs (student name and grade)
        studentGrades.put("Alice", 90);
        studentGrades.put("Bob", 85);
        studentGrades.put("Charlie", 95);
        
        // Print all student grades
        System.out.println("Student Grades:");
        for (Map.Entry<String, Integer> entry : studentGrades.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }

        // Accessing a specific value
        String studentName = "Alice";
        Integer grade = studentGrades.get(studentName);
        if (grade != null) {
            System.out.println(studentName + "'s grade: " + grade);
        } else {
            System.err.println("No grade found for student: " + studentName);
        }

        // Demonstrate HashSet
        HashSet<String> uniqueStudents = new HashSet<>();
        
        // Adding students (duplicates will be ignored)
        uniqueStudents.add("Alice");
        uniqueStudents.add("Bob");
        uniqueStudents.add("Alice"); // Duplicate entry, should not be added

        // Print all unique students
        System.out.println("Unique Students:");
        for (String student : uniqueStudents) {
            System.out.println(student);
        }
        
        // Error handling example: check for null values
        try {
            // Attempt to retrieve a grade for a non-existent student
            Integer nonExistentGrade = studentGrades.get("David");
            if (nonExistentGrade == null) {
                throw new IllegalArgumentException("Grade not found for a non-existent student.");
            }
        } catch (IllegalArgumentException e) {
            System.err.println(e.getMessage());
        }
    }
}
```
