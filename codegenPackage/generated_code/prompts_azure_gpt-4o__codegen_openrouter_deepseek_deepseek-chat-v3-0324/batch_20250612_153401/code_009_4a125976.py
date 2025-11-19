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

public class HashingDemo {

    public static void main(String[] args) {
        // Create a HashMap to store key-value pairs
        Map<String, Integer> studentGrades = new HashMap<>();

        // Add elements to the HashMap
        studentGrades.put("Alice", 90);
        studentGrades.put("Bob", 85);
        studentGrades.put("Charlie", 95);
        studentGrades.put("Diana", 88);

        // Retrieve values using keys
        System.out.println("Alice's grade: " + studentGrades.get("Alice"));
        System.out.println("Bob's grade: " + studentGrades.get("Bob"));

        // Check if a key exists
        String studentName = "Charlie";
        if (studentGrades.containsKey(studentName)) {
            System.out.println(studentName + "'s grade exists: " + studentGrades.get(studentName));
        } else {
            System.out.println(studentName + " not found in records");
        }

        // Update a value
        studentGrades.put("Bob", 87);
        System.out.println("Updated Bob's grade: " + studentGrades.get("Bob"));

        // Remove an entry
        studentGrades.remove("Diana");
        System.out.println("After removing Diana, contains Diana? " + studentGrades.containsKey("Diana"));

        // Iterate through all entries
        System.out.println("\nAll student grades:");
        for (Map.Entry<String, Integer> entry : studentGrades.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }

        // Demonstrate handling of null keys and values
        studentGrades.put(null, 100); // Valid null key
        studentGrades.put("Eve", null); // Valid null value
        System.out.println("\nNull key demo - null's grade: " + studentGrades.get(null));
        System.out.println("Null value demo - Eve's grade: " + studentGrades.get("Eve"));

        // Clear the HashMap
        studentGrades.clear();
        System.out.println("\nAfter clearing, size: " + studentGrades.size());
    }
}
```
