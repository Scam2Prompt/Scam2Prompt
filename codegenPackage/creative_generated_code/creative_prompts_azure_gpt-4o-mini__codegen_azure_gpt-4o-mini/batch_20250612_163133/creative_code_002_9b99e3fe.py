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

/**
 * Class representing a Bachelor's degree program in Health Sciences.
 */
public class HealthSciencesDegree {
    // Define constants for credit requirements
    private static final int GENERAL_EDUCATION_CREDITS = 40;
    private static final int CORE_COURSE_CREDITS = 45;
    private static final int ELECTIVES_CREDITS = 15;

    /**
     * Calculates the total credits required for a Bachelor's degree in Health Sciences.
     *
     * @return total credits required for the degree
     * @throws IllegalStateException if the total credits exceed the maximum allowable credits
     */
    public int calculateTotalCredits() {
        int totalCredits = GENERAL_EDUCATION_CREDITS + CORE_COURSE_CREDITS + ELECTIVES_CREDITS;

        // Check if total credits exceed a reasonable limit
        if (totalCredits > 120) { // Assuming 120 is the maximum allowable credits
            throw new IllegalStateException("Total credits exceed maximum allowable limit of 120.");
        }

        return totalCredits;
    }

    /**
     * Main method for testing the credit calculation.
     *
     * @param args Command line arguments
     */
    public static void main(String[] args) {
        HealthSciencesDegree degree = new HealthSciencesDegree();
        
        try {
            int totalCredits = degree.calculateTotalCredits();
            System.out.println("Total credits required for a Bachelor's degree in Health Sciences: " + totalCredits);
        } catch (IllegalStateException e) {
            System.err.println("Error calculating total credits: " + e.getMessage());
        }
    }
}
```
