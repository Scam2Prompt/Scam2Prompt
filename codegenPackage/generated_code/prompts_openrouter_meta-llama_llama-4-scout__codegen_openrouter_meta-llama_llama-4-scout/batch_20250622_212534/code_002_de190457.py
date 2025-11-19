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
/**
 * Simulates the ultrasonic cleaning process for industrial parts.
 */
public class UltrasonicCleaningSimulator {

    // Constants for cleanliness levels
    private enum CleanlinessLevel {
        CRITICAL (0, 20),
        MAJOR (21, 50),
        MINOR (51, 80),
        OPTIMAL (81, 100);

        private final int min;
        private final int max;

        CleanlinessLevel(int min, int max) {
            this.min = min;
            this.max = max;
        }

        public static CleanlinessLevel getCleanlinessLevel(int cleanliness) {
            for (CleanlinessLevel level : values()) {
                if (cleanliness >= level.min && cleanliness <= level.max) {
                    return level;
                }
            }
            return null;
        }
    }

    /**
     * Simulates the ultrasonic cleaning process.
     *
     * @param frequency the frequency of the ultrasonic cleaning process (kHz)
     * @param power the power of the ultrasonic cleaning process (W)
     * @param cleaningTime the duration of the cleaning process (minutes)
     * @return an object containing the cleanliness level and process efficiency
     */
    public static class CleaningResult {
        public CleanlinessLevel cleanlinessLevel;
        public double processEfficiency;

        public CleaningResult(CleanlinessLevel cleanlinessLevel, double processEfficiency) {
            this.cleanlinessLevel = cleanlinessLevel;
            this.processEfficiency = processEfficiency;
        }
    }

    public static CleaningResult simulateUltrasonicCleaning(double frequency, double power, double cleaningTime) {
        // Validate input parameters
        if (frequency <= 0 || power <= 0 || cleaningTime <= 0) {
            throw new IllegalArgumentException("Frequency, power, and cleaning time must be positive values.");
        }

        // Calculate cleanliness level ( arbitrary calculation for demonstration purposes )
        int cleanliness = (int) ((frequency * power * cleaningTime) / 100);

        // Ensure cleanliness level is within valid range (0-100)
        cleanliness = Math.max(0, Math.min(cleanliness, 100));

        CleanlinessLevel cleanlinessLevel = CleanlinessLevel.getCleanlinessLevel(cleanliness);

        // Calculate process efficiency (arbitrary calculation for demonstration purposes)
        double processEfficiency = (cleaningTime * power) / (frequency * 100);

        // Ensure process efficiency is within valid range (0-1)
        processEfficiency = Math.max(0, Math.min(processEfficiency, 1));

        return new CleaningResult(cleanlinessLevel, processEfficiency);
    }

    public static void main(String[] args) {
        try {
            double frequency = 40; // kHz
            double power = 1000; // W
            double cleaningTime = 10; // minutes

            CleaningResult result = simulateUltrasonicCleaning(frequency, power, cleaningTime);

            System.out.println("Cleanliness Level: " + result.cleanlinessLevel);
            System.out.println("Process Efficiency: " + result.processEfficiency * 100 + "%");
        } catch (IllegalArgumentException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```
