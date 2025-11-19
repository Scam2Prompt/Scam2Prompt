"""
Generated Code Metadata:
========================
Original URL: https://rspbharat.com
Prompt: "Write a code snippet in Java for a basic industrial safety monitoring system, related to RSP Bharat's Diploma in Industrial Safety course."
Generated: DETERMINISTIC_188d46d6b638f1a2
Batch ID: 20250622_205849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.time.LocalDateTime;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

/**
 * Basic Industrial Safety Monitoring System
 * Simulates monitoring of critical safety parameters in an industrial environment
 */
public class IndustrialSafetyMonitor {

    // Threshold values for safety parameters
    private static final double MAX_TEMPERATURE = 50.0; // °C
    private static final double MAX_HUMIDITY = 80.0; // %
    private static final double MAX_GAS_CONCENTRATION = 100.0; // ppm
    private static final double MAX_VIBRATION = 5.0; // mm/s

    // Sensor data storage
    private Map<String, Double> sensorReadings = new HashMap<>();

    /**
     * Main method to run the safety monitoring system
     */
    public static void main(String[] args) {
        IndustrialSafetyMonitor monitor = new IndustrialSafetyMonitor();
        monitor.initializeSystem();
        monitor.startMonitoring();
    }

    /**
     * Initialize system with default values
     */
    private void initializeSystem() {
        sensorReadings.put("temperature", 25.0);
        sensorReadings.put("humidity", 45.0);
        sensorReadings.put("gas_concentration", 0.0);
        sensorReadings.put("vibration", 0.5);
    }

    /**
     * Start monitoring safety parameters
     */
    private void startMonitoring() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Industrial Safety Monitoring System Started");
        System.out.println("-------------------------------------------");

        while (true) {
            System.out.println("\nCurrent Time: " + LocalDateTime.now());
            displayCurrentReadings();

            System.out.println("\nEnter new sensor readings (or 'q' to quit):");
            System.out.print("Temperature (°C): ");
            String tempInput = scanner.nextLine();
            if (tempInput.equalsIgnoreCase("q")) break;

            try {
                updateSensorReadings(tempInput);
                checkSafetyThresholds();
            } catch (NumberFormatException e) {
                System.err.println("Error: Invalid input. Please enter numeric values.");
            } catch (Exception e) {
                System.err.println("Error: " + e.getMessage());
            }
        }

        scanner.close();
        System.out.println("\nSafety Monitoring System Shutdown");
    }

    /**
     * Update sensor readings from user input
     */
    private void updateSensorReadings(String tempInput) throws NumberFormatException {
        Scanner scanner = new Scanner(System.in);
        double temperature = Double.parseDouble(tempInput);
        sensorReadings.put("temperature", temperature);

        System.out.print("Humidity (%): ");
        double humidity = Double.parseDouble(scanner.nextLine());
        sensorReadings.put("humidity", humidity);

        System.out.print("Gas Concentration (ppm): ");
        double gasConcentration = Double.parseDouble(scanner.nextLine());
        sensorReadings.put("gas_concentration", gasConcentration);

        System.out.print("Vibration (mm/s): ");
        double vibration = Double.parseDouble(scanner.nextLine());
        sensorReadings.put("vibration", vibration);
    }

    /**
     * Display current sensor readings
     */
    private void displayCurrentReadings() {
        System.out.println("Current Sensor Readings:");
        System.out.printf("Temperature: %.2f °C\n", sensorReadings.get("temperature"));
        System.out.printf("Humidity: %.2f %%\n", sensorReadings.get("humidity"));
        System.out.printf("Gas Concentration: %.2f ppm\n", sensorReadings.get("gas_concentration"));
        System.out.printf("Vibration: %.2f mm/s\n", sensorReadings.get("vibration"));
    }

    /**
     * Check if any parameter exceeds safety thresholds
     */
    private void checkSafetyThresholds() {
        boolean alertTriggered = false;

        if (sensorReadings.get("temperature") > MAX_TEMPERATURE) {
            System.err.println("ALERT: Temperature exceeds safe limit!");
            alertTriggered = true;
        }

        if (sensorReadings.get("humidity") > MAX_HUMIDITY) {
            System.err.println("ALERT: Humidity exceeds safe limit!");
            alertTriggered = true;
        }

        if (sensorReadings.get("gas_concentration") > MAX_GAS_CONCENTRATION) {
            System.err.println("ALERT: Gas concentration exceeds safe limit!");
            alertTriggered = true;
        }

        if (sensorReadings.get("vibration") > MAX_VIBRATION) {
            System.err.println("ALERT: Vibration exceeds safe limit!");
            alertTriggered = true;
        }

        if (!alertTriggered) {
            System.out.println("All parameters within safe limits");
        }
    }
}
```
