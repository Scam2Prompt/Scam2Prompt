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
/**
 * Calculates the production efficiency of a spinning unit.
 */
public class SpinningUnitEfficiencyCalculator {

    /**
     * Enum for different types of machinery.
     */
    public enum MachineryType {
        STATE_OF_THE_ART,
        STANDARD,
        LEGACY
    }

    /**
     * Calculates the production efficiency of a spinning unit.
     *
     * @param theoreticalCapacity the theoretical capacity of the spinning unit
     * @param actualProduction    the actual production of the spinning unit
     * @param machineryType       the type of machinery used
     * @return the production efficiency of the spinning unit
     */
    public static double calculateProductionEfficiency(double theoreticalCapacity, double actualProduction, MachineryType machineryType) {
        // Validate input parameters
        if (theoreticalCapacity <= 0) {
            throw new IllegalArgumentException("Theoretical capacity must be greater than zero");
        }
        if (actualProduction < 0) {
            throw new IllegalArgumentException("Actual production must be non-negative");
        }

        // Calculate production efficiency
        double efficiency = (actualProduction / theoreticalCapacity) * getMachineryEfficiencyFactor(machineryType);

        // Ensure efficiency is within valid range (0 to 1)
        return Math.max(0, Math.min(efficiency, 1));
    }

    /**
     * Returns the efficiency factor for the given machinery type.
     *
     * @param machineryType the type of machinery
     * @return the efficiency factor
     */
    private static double getMachineryEfficiencyFactor(MachineryType machineryType) {
        switch (machineryType) {
            case STATE_OF_THE_ART:
                return 0.95; // State-of-the-art machinery has an efficiency factor of 0.95
            case STANDARD:
                return 0.8; // Standard machinery has an efficiency factor of 0.8
            case LEGACY:
                return 0.6; // Legacy machinery has an efficiency factor of 0.6
            default:
                throw new UnsupportedOperationException("Unsupported machinery type");
        }
    }

    public static void main(String[] args) {
        try {
            double theoreticalCapacity = 1000; // Theoretical capacity of the spinning unit
            double actualProduction = 900; // Actual production of the spinning unit
            MachineryType machineryType = MachineryType.STATE_OF_THE_ART; // Type of machinery used

            double productionEfficiency = calculateProductionEfficiency(theoreticalCapacity, actualProduction, machineryType);
            System.out.println("Production Efficiency: " + productionEfficiency);
        } catch (Exception e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```
