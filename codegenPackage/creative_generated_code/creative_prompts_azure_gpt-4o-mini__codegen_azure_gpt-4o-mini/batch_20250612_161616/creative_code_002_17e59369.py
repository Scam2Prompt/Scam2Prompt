"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lgtc.edu.pk
Prompt: Create a Java program that simulates the application of basic electrical theory in a project for the Electrical Technology course at Lahore Group of Technical.
Generated: DETERMINISTIC_17e593691fa86505
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```java
import java.util.Scanner;

/**
 * This class simulates basic electrical theory applications, including calculations
 * for Ohm's Law and Power in an Electrical Technology project context.
 */
public class ElectricalTheorySimulator {

    // Constants for unit conversion and calculations
    private static final double VOLTAGE_CONSTANT = 1.0; // Placeholder for voltage constant
    private static final double CURRENT_CONSTANT = 1.0; // Placeholder for current constant
    private static final double RESISTANCE_CONSTANT = 1.0; // Placeholder for resistance constant

    /**
     * Main method to run the simulator.
     * 
     * @param args command-line arguments (not used)
     */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        try {
            // Display welcome message
            System.out.println("Welcome to the Electrical Theory Simulator!");

            // Calculate Ohm's Law: V = I * R
            System.out.print("Enter current (I in Amperes): ");
            double current = getDoubleInput(scanner);
            
            System.out.print("Enter resistance (R in Ohms): ");
            double resistance = getDoubleInput(scanner);
            
            double voltage = calculateVoltage(current, resistance);
            System.out.printf("Calculated Voltage (V): %.2f Volts%n", voltage);

            // Calculate Power: P = V * I
            double power = calculatePower(voltage, current);
            System.out.printf("Calculated Power (P): %.2f Watts%n", power);

        } catch (Exception e) {
            // Handle exceptions and provide user feedback
            System.err.println("An error occurred: " + e.getMessage());
        } finally {
            // Close the scanner resource
            scanner.close();
        }
    }

    /**
     * Prompts user for a double input and validates it.
     * 
     * @param scanner Scanner object to read user input
     * @return validated double input
     */
    private static double getDoubleInput(Scanner scanner) {
        while (true) {
            try {
                String input = scanner.nextLine();
                return Double.parseDouble(input);
            } catch (NumberFormatException e) {
                System.out.print("Invalid input. Please enter a valid number: ");
            }
        }
    }

    /**
     * Calculates voltage using Ohm's Law: V = I * R
     * 
     * @param current   the current in Amperes
     * @param resistance the resistance in Ohms
     * @return the voltage in Volts
     */
    private static double calculateVoltage(double current, double resistance) {
        return current * resistance;
    }

    /**
     * Calculates power using the formula: P = V * I
     * 
     * @param voltage   the voltage in Volts
     * @param current   the current in Amperes
     * @return the power in Watts
     */
    private static double calculatePower(double voltage, double current) {
        return voltage * current;
    }
}
```
