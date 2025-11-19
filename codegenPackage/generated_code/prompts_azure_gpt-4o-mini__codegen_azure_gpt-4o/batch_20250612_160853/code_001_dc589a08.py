"""
Generated Code Metadata:
========================
Original URL: https://ramjiacro.com
Prompt: Write a Java function that calculates the production efficiency of a spinning unit, taking into account the state-of-the-art machinery used by companies like Ramji Acro.
Generated: DETERMINISTIC_dc589a0819993390
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.util.Objects;

public class ProductionEfficiencyCalculator {

    /**
     * Calculates the production efficiency of a spinning unit.
     *
     * @param actualOutput The actual output produced by the spinning unit (in kilograms).
     * @param expectedOutput The expected output based on the machinery's capacity (in kilograms).
     * @param downtimeHours The number of hours the machinery was down (in hours).
     * @param totalHours The total operational hours available (in hours).
     * @return The production efficiency as a percentage (0-100).
     * @throws IllegalArgumentException If any input parameter is invalid (e.g., negative values or downtimeHours > totalHours).
     */
    public static double calculateEfficiency(double actualOutput, double expectedOutput, double downtimeHours, double totalHours) {
        // Validate input parameters
        if (actualOutput < 0 || expectedOutput <= 0 || downtimeHours < 0 || totalHours <= 0 || downtimeHours > totalHours) {
            throw new IllegalArgumentException("Invalid input parameters. Ensure all values are positive and downtimeHours <= totalHours.");
        }

        // Calculate operational hours
        double operationalHours = totalHours - downtimeHours;

        // Avoid division by zero in case operationalHours is zero
        if (operationalHours <= 0) {
            return 0.0; // Efficiency is zero if no operational hours are available
        }

        // Calculate efficiency as a percentage
        double efficiency = (actualOutput / expectedOutput) * (operationalHours / totalHours) * 100;

        // Ensure efficiency is within bounds (0-100)
        return Math.max(0, Math.min(efficiency, 100));
    }

    public static void main(String[] args) {
        try {
            // Example usage
            double actualOutput = 950; // in kilograms
            double expectedOutput = 1000; // in kilograms
            double downtimeHours = 2; // in hours
            double totalHours = 24; // in hours

            double efficiency = calculateEfficiency(actualOutput, expectedOutput, downtimeHours, totalHours);
            System.out.println("Production Efficiency: " + efficiency + "%");
        } catch (IllegalArgumentException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```
