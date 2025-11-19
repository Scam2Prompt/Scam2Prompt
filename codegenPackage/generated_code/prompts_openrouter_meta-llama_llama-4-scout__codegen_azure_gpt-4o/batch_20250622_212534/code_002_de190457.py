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

public class UltrasonicCleaningSimulator {

    // Class to represent the cleaning parameters
    static class CleaningParameters {
        private double frequency; // Frequency in kHz
        private double power;     // Power in watts
        private int cleaningTime; // Cleaning time in seconds

        public CleaningParameters(double frequency, double power, int cleaningTime) {
            if (frequency <= 0 || power <= 0 || cleaningTime <= 0) {
                throw new IllegalArgumentException("Frequency, power, and cleaning time must be positive values.");
            }
            this.frequency = frequency;
            this.power = power;
            this.cleaningTime = cleaningTime;
        }

        public double getFrequency() {
            return frequency;
        }

        public double getPower() {
            return power;
        }

        public int getCleaningTime() {
            return cleaningTime;
        }
    }

    // Method to simulate the cleaning process
    public static void simulateCleaning(CleaningParameters params) {
        // Validate input parameters
        if (params == null) {
            throw new IllegalArgumentException("Cleaning parameters cannot be null.");
        }

        System.out.println("Starting ultrasonic cleaning process...");
        System.out.println("Frequency: " + params.getFrequency() + " kHz");
        System.out.println("Power: " + params.getPower() + " watts");
        System.out.println("Cleaning Time: " + params.getCleaningTime() + " seconds");

        // Simulate cleaning process
        double cleanlinessLevel = calculateCleanliness(params);
        double processEfficiency = calculateEfficiency(params);

        // Output results
        System.out.println("Cleaning process completed.");
        System.out.printf("Cleanliness Level: %.2f%%\n", cleanlinessLevel);
        System.out.printf("Process Efficiency: %.2f%%\n", processEfficiency);
    }

    // Method to calculate cleanliness level based on parameters
    private static double calculateCleanliness(CleaningParameters params) {
        // Simulate cleanliness level as a function of frequency, power, and cleaning time
        double baseCleanliness = params.getFrequency() * 0.5 + params.getPower() * 0.3 + params.getCleaningTime() * 0.2;
        return Math.min(baseCleanliness, 100.0); // Cap cleanliness level at 100%
    }

    // Method to calculate process efficiency based on parameters
    private static double calculateEfficiency(CleaningParameters params) {
        // Simulate efficiency as a random factor influenced by frequency and power
        Random random = new Random();
        double efficiencyFactor = 0.8 + (random.nextDouble() * 0.2); // Random factor between 0.8 and 1.0
        double efficiency = (params.getFrequency() * 0.4 + params.getPower() * 0.6) * efficiencyFactor;
        return Math.min(efficiency, 100.0); // Cap efficiency at 100%
    }

    public static void main(String[] args) {
        try {
            // Example usage
            CleaningParameters params = new CleaningParameters(40.0, 500.0, 120);
            simulateCleaning(params);
        } catch (IllegalArgumentException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```
