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
import java.util.Scanner;

/**
 * This class simulates the ultrasonic cleaning process for industrial parts.
 */
public class UltrasonicCleaner {

    private double frequency; // Frequency of the ultrasonic waves in kHz
    private double power;     // Power of the ultrasonic cleaner in watts
    private int cleaningTime; // Cleaning time in minutes

    /**
     * Constructor to initialize the ultrasonic cleaner parameters.
     *
     * @param frequency    Frequency in kHz
     * @param power        Power in watts
     * @param cleaningTime  Cleaning time in minutes
     */
    public UltrasonicCleaner(double frequency, double power, int cleaningTime) {
        this.frequency = frequency;
        this.power = power;
        this.cleaningTime = cleaningTime;
    }

    /**
     * Simulates the cleaning process and calculates cleanliness level and efficiency.
     *
     * @return A string containing the cleanliness level and process efficiency.
     */
    public String simulateCleaning() {
        // Validate parameters
        if (frequency <= 0 || power <= 0 || cleaningTime <= 0) {
            throw new IllegalArgumentException("Frequency, power, and cleaning time must be positive values.");
        }

        // Calculate cleanliness level (arbitrary formula for simulation)
        double cleanlinessLevel = (frequency * power * cleaningTime) / 1000;

        // Calculate process efficiency (arbitrary formula for simulation)
        double processEfficiency = (cleanlinessLevel / (frequency * power)) * 100;

        return String.format("Cleanliness Level: %.2f%%, Process Efficiency: %.2f%%", cleanlinessLevel, processEfficiency);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        try {
            // User input for ultrasonic cleaner parameters
            System.out.print("Enter frequency (kHz): ");
            double frequency = scanner.nextDouble();

            System.out.print("Enter power (watts): ");
            double power = scanner.nextDouble();

            System.out.print("Enter cleaning time (minutes): ");
            int cleaningTime = scanner.nextInt();

            // Create an instance of UltrasonicCleaner
            UltrasonicCleaner cleaner = new UltrasonicCleaner(frequency, power, cleaningTime);

            // Simulate the cleaning process and output results
            String result = cleaner.simulateCleaning();
            System.out.println(result);
        } catch (IllegalArgumentException e) {
            System.err.println("Error: " + e.getMessage());
        } catch (Exception e) {
            System.err.println("An unexpected error occurred: " + e.getMessage());
        } finally {
            scanner.close(); // Ensure the scanner is closed to prevent resource leaks
        }
    }
}
```
