"""
Generated Code Metadata:
========================
Original URL: https://trysonicsolutions.com
Prompt: "Generate a code snippet in Java to simulate the ultrasonic cleaning process for industrial parts, taking into account parameters like frequency, power, and cleaning time, and outputting the cleanliness level and process efficiency."
Generated: DETERMINISTIC_de19045776a86711
Batch ID: 20250622_212534
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.util.Random;

/**
 * Simulates an ultrasonic cleaning process for industrial parts.
 */
public class UltrasonicCleanerSimulator {

    // Constants for simulation parameters
    private static final int MIN_FREQUENCY = 20; // kHz
    private static final int MAX_FREQUENCY = 100; // kHz
    private static final int MIN_POWER = 50; // Watts
    private static final int MAX_POWER = 500; // Watts
    private static final int MIN_TIME = 1; // minutes
    private static final int MAX_TIME = 30; // minutes

    /**
     * Simulates the ultrasonic cleaning process.
     * 
     * @param frequency The ultrasonic frequency in kHz (20-100)
     * @param power The power output in Watts (50-500)
     * @param time The cleaning time in minutes (1-30)
     * @return CleaningResult object containing cleanliness and efficiency
     * @throws IllegalArgumentException if parameters are out of bounds
     */
    public static CleaningResult simulateCleaning(int frequency, int power, int time) {
        // Validate input parameters
        if (frequency < MIN_FREQUENCY || frequency > MAX_FREQUENCY) {
            throw new IllegalArgumentException("Frequency must be between " + MIN_FREQUENCY + " and " + MAX_FREQUENCY + " kHz");
        }
        if (power < MIN_POWER || power > MAX_POWER) {
            throw new IllegalArgumentException("Power must be between " + MIN_POWER + " and " + MAX_POWER + " Watts");
        }
        if (time < MIN_TIME || time > MAX_TIME) {
            throw new IllegalArgumentException("Time must be between " + MIN_TIME + " and " + MAX_TIME + " minutes");
        }

        // Calculate cleanliness (0-100%)
        double cleanliness = calculateCleanliness(frequency, power, time);

        // Calculate efficiency (0-100%)
        double efficiency = calculateEfficiency(frequency, power, time);

        return new CleaningResult(cleanliness, efficiency);
    }

    /**
     * Calculates cleanliness based on process parameters.
     */
    private static double calculateCleanliness(int frequency, int power, int time) {
        // Base formula with some randomness to simulate real-world variation
        Random rand = new Random();
        double baseCleanliness = (frequency * 0.2) + (power * 0.1) + (time * 2.5);
        double variation = rand.nextDouble() * 10 - 5; // ±5% variation
        
        double cleanliness = baseCleanliness + variation;
        return Math.min(100, Math.max(0, cleanliness)); // Clamp between 0-100
    }

    /**
     * Calculates process efficiency based on parameters.
     */
    private static double calculateEfficiency(int frequency, int power, int time) {
        // Efficiency formula favors moderate parameters
        double freqFactor = 1 - Math.abs(0.6 - (frequency / 100.0));
        double powerFactor = 1 - Math.abs(0.7 - (power / 500.0));
        double timeFactor = 1 - Math.abs(0.5 - (time / 30.0));
        
        double efficiency = (freqFactor * 0.4 + powerFactor * 0.3 + timeFactor * 0.3) * 100;
        return Math.min(100, Math.max(0, efficiency)); // Clamp between 0-100
    }

    /**
     * Represents the result of a cleaning simulation.
     */
    public static class CleaningResult {
        private final double cleanliness; // Percentage (0-100)
        private final double efficiency; // Percentage (0-100)

        public CleaningResult(double cleanliness, double efficiency) {
            this.cleanliness = cleanliness;
            this.efficiency = efficiency;
        }

        public double getCleanliness() {
            return cleanliness;
        }

        public double getEfficiency() {
            return efficiency;
        }

        @Override
        public String toString() {
            return String.format("Cleanliness: %.1f%%, Efficiency: %.1f%%", cleanliness, efficiency);
        }
    }

    // Example usage
    public static void main(String[] args) {
        try {
            CleaningResult result = simulateCleaning(40, 300, 10);
            System.out.println(result);
        } catch (IllegalArgumentException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```
