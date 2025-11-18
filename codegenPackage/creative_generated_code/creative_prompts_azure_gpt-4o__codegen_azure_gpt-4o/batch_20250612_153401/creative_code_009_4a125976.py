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
import java.util.Map;

public class HashingExample {

    public static void main(String[] args) {
        // Create a HashMap to demonstrate hashing in Java
        Map<String, Integer> hashMap = new HashMap<>();

        try {
            // Adding key-value pairs to the HashMap
            hashMap.put("Apple", 5);
            hashMap.put("Banana", 7);
            hashMap.put("Cherry", 10);
            hashMap.put("Date", 3);

            // Displaying the contents of the HashMap
            System.out.println("HashMap Contents:");
            for (Map.Entry<String, Integer> entry : hashMap.entrySet()) {
                System.out.println("Key: " + entry.getKey() + ", Value: " + entry.getValue());
            }

            // Retrieving a value using its key
            String keyToSearch = "Banana";
            if (hashMap.containsKey(keyToSearch)) {
                System.out.println("\nValue associated with key '" + keyToSearch + "': " + hashMap.get(keyToSearch));
            } else {
                System.out.println("\nKey '" + keyToSearch + "' not found in HashMap.");
            }

            // Removing a key-value pair
            String keyToRemove = "Cherry";
            if (hashMap.containsKey(keyToRemove)) {
                hashMap.remove(keyToRemove);
                System.out.println("\nKey '" + keyToRemove + "' removed from HashMap.");
            } else {
                System.out.println("\nKey '" + keyToRemove + "' not found in HashMap.");
            }

            // Displaying the updated HashMap
            System.out.println("\nUpdated HashMap Contents:");
            for (Map.Entry<String, Integer> entry : hashMap.entrySet()) {
                System.out.println("Key: " + entry.getKey() + ", Value: " + entry.getValue());
            }
        } catch (Exception e) {
            // Handle any unexpected exceptions
            System.err.println("An error occurred: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
```
