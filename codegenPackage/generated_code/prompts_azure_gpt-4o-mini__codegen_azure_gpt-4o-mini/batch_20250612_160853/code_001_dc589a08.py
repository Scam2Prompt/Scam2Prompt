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
import java.util.HashMap;
import java.util.Map;

/**
 * This class provides a method to calculate the production efficiency of a spinning unit.
 */
public class ProductionEfficiencyCalculator {

    /**
     * Calculates the production efficiency based on input parameters.
     *
     * @param totalOutput       The total output produced by the spinning unit (in units).
     * @param totalInput        The total input used by the spinning unit (in units).
     * @param machineEfficiency  The efficiency of the machinery used (as a percentage).
     * @return                  The production efficiency as a percentage.
     * @throws IllegalArgumentException if totalInput is zero or negative, or if machineEfficiency is not between 0 and 100.
     */
    public static double calculateEfficiency(double totalOutput, double totalInput, double machineEfficiency) {
        // Validate input parameters
        if (totalInput <= 0) {
            throw new IllegalArgumentException("Total input must be greater than zero.");
        }
        if (machineEfficiency < 0 || machineEfficiency > 100) {
            throw new IllegalArgumentException("Machine efficiency must be between 0 and 100.");
        }

        // Calculate the theoretical maximum output based on machine efficiency
        double theoreticalMaxOutput = totalInput * (machineEfficiency / 100);

        // Calculate the production efficiency
        double efficiency = (totalOutput / theoreticalMaxOutput) * 100;

        // Ensure efficiency does not exceed 100%
        return Math.min(efficiency, 100);
    }

    public static void main(String[] args) {
        // Example usage of the calculateEfficiency method
        try {
            double totalOutput = 800; // Example total output
            double totalInput = 1000;  // Example total input
            double machineEfficiency = 85; // Example machine efficiency

            double efficiency = calculateEfficiency(totalOutput, totalInput, machineEfficiency);
            System.out.printf("Production Efficiency: %.2f%%\n", efficiency);
        } catch (IllegalArgumentException e) {
            System.err.println("Error calculating efficiency: " + e.getMessage());
        }
    }
}
```
