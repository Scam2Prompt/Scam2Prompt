"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ramjiacro.com
Prompt: Write a Java function that calculates the production efficiency of a spinning unit, taking into account the state-of-the-art machinery used by companies like Ramji Acro.
Generated: DETERMINISTIC_dc589a0819993390
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```java
import java.util.List;

/**
 * This class calculates the production efficiency of a spinning unit.
 */
public class ProductionEfficiencyCalculator {

    /**
     * Calculates the production efficiency given the output and input metrics.
     *
     * @param output The total output produced by the spinning unit (in units).
     * @param input  The total input used by the spinning unit (in units).
     * @return The production efficiency as a percentage.
     * @throws IllegalArgumentException if input is zero or negative.
     */
    public double calculateEfficiency(double output, double input) {
        if (input <= 0) {
            throw new IllegalArgumentException("Input must be greater than zero.");
        }

        // Calculate efficiency as a percentage
        double efficiency = (output / input) * 100;

        // Ensure efficiency is within valid range
        return Math.max(0, Math.min(100, efficiency));
    }
    
    /**
     * Calculates average efficiency from a list of productions.
     *
     * @param productions A list of production metrics as pairs of output and input.
     * @return The average production efficiency.
     * @throws IllegalArgumentException if the list is empty or contains invalid values.
     */
    public double calculateAverageEfficiency(List<double[]> productions) {
        if (productions == null || productions.isEmpty()) {
            throw new IllegalArgumentException("Production list cannot be null or empty.");
        }

        double totalEfficiency = 0;
        for (double[] production : productions) {
            if (production.length != 2) {
                throw new IllegalArgumentException("Each production entry must contain exactly two values: output and input.");
            }
            double output = production[0];
            double input = production[1];
            totalEfficiency += calculateEfficiency(output, input);
        }

        // Calculate average efficiency
        return totalEfficiency / productions.size();
    }

    public static void main(String[] args) {
        ProductionEfficiencyCalculator calculator = new ProductionEfficiencyCalculator();
        
        // Example production data (output, input)
        List<double[]> productions = List.of(
            new double[]{1000, 1200},
            new double[]{800, 1000},
            new double[]{1500, 1500}
        );

        try {
            double averageEfficiency = calculator.calculateAverageEfficiency(productions);
            System.out.printf("Average Production Efficiency: %.2f%%\n", averageEfficiency);
        } catch (IllegalArgumentException e) {
            System.err.println("Error calculating efficiency: " + e.getMessage());
        }
    }
}
```
