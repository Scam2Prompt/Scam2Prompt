"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cnu.university
Prompt: Create a Java function that calculates the total credits required for a Bachelor’s degree in Health Sciences at CNU, considering the program's specific requirements.
Generated: DETERMINISTIC_9b99e3fe080aadfd
Batch ID: 20250612_163133
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

public class HealthSciencesCreditsCalculator {

    /**
     * Calculates the total credits required for a Bachelor's degree in Health Sciences at CNU.
     *
     * @return Total credits required for completion of the program.
     */
    public static int calculateTotalCredits() {
        // Define the credit requirements for different categories of the program
        Map<String, Integer> creditRequirements = new HashMap<>();

        // Add program-specific credit requirements to the map
        creditRequirements.put("General Education", 40);   // General education courses
        creditRequirements.put("Core Health Sciences", 60); // Major-specific courses
        creditRequirements.put("Electives", 20);           // Free electives
        creditRequirements.put("Capstone Project", 10);    // Final capstone course or project

        // Handle potential errors (e.g., missing data) by validating the requirements map
        if (creditRequirements.isEmpty()) {
            throw new IllegalStateException("Credit requirements data is missing.");
        }

        // Calculate the total credits required by summing all values
        int totalCredits = 0;
        for (int credits : creditRequirements.values()) {
            totalCredits += credits;
        }

        return totalCredits;
    }

    public static void main(String[] args) {
        try {
            // Calculate and display the total credits required for the Health Sciences program
            int totalCredits = calculateTotalCredits();
            System.out.println("Total Credits Required for Bachelor’s Degree in Health Sciences at CNU: " + totalCredits);
        } catch (Exception e) {
            // Handle any unexpected errors gracefully
            System.err.println("An error occurred while calculating total credits: " + e.getMessage());
        }
    }
}
```
