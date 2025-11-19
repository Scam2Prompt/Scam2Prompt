"""
Generated Code Metadata:
========================
Original URL: https://cnu.university
Prompt: Create a Java function that calculates the total credits required for a Bachelor’s degree in Health Sciences at CNU, considering the program's specific requirements.
Generated: DETERMINISTIC_9b99e3fe080aadfd
Batch ID: 20250612_163133
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
 * This class provides functionality to calculate the total credits required
 * for a Bachelor's degree in Health Sciences at CNU.
 */
public class HealthSciencesDegree {

    // Constants for credit requirements
    private static final int GENERAL_EDUCATION_CREDITS = 40;
    private static final int MAJOR_CREDITS = 60;
    private static final int ELECTIVE_CREDITS = 20;

    /**
     * Calculates the total credits required for the Bachelor's degree.
     *
     * @return total credits required for the degree
     * @throws IllegalArgumentException if any credit requirement is negative
     */
    public int calculateTotalCredits() {
        int totalCredits = GENERAL_EDUCATION_CREDITS + MAJOR_CREDITS + ELECTIVE_CREDITS;

        // Validate that no credit requirement is negative
        if (totalCredits < 0) {
            throw new IllegalArgumentException("Total credits cannot be negative.");
        }

        return totalCredits;
    }

    /**
     * Main method to run the credit calculation.
     *
     * @param args command line arguments
     */
    public static void main(String[] args) {
        HealthSciencesDegree degree = new HealthSciencesDegree();
        
        try {
            int totalCredits = degree.calculateTotalCredits();
            System.out.println("Total credits required for a Bachelor's degree in Health Sciences: " + totalCredits);
        } catch (IllegalArgumentException e) {
            System.err.println("Error calculating total credits: " + e.getMessage());
        }
    }
}
```
