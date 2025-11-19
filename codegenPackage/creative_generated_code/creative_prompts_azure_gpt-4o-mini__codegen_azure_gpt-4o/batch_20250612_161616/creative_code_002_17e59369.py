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
 * ElectricalTheorySimulator
 * 
 * This program simulates basic electrical calculations based on Ohm's Law and Power formulas.
 * It allows users to calculate voltage, current, resistance, or power based on provided values.
 * Designed for educational purposes in the Electrical Technology course.
 */
public class ElectricalTheorySimulator {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Welcome to Electrical Theory Simulator!");
        System.out.println("Select the calculation you want to perform:");
        System.out.println("1. Calculate Voltage (V)");
        System.out.println("2. Calculate Current (I)");
        System.out.println("3. Calculate Resistance (R)");
        System.out.println("4. Calculate Power (P)");

        try {
            System.out.print("Enter your choice (1-4): ");
            int choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    calculateVoltage(scanner);
                    break;
                case 2:
                    calculateCurrent(scanner);
                    break;
                case 3:
                    calculateResistance(scanner);
                    break;
                case 4:
                    calculatePower(scanner);
                    break;
                default:
                    System.out.println("Invalid choice. Please restart and select a valid option.");
            }
        } catch (Exception e) {
            System.out.println("Error: Invalid input. Please restart and enter valid numerical values.");
        } finally {
            scanner.close();  // Ensure scanner is closed to release system resources
        }

        System.out.println("Thank you for using Electrical Theory Simulator!");
    }

    /**
     * Calculates voltage using the formula V = I * R.
     * 
     * @param scanner Scanner object to read input values.
     */
    private static void calculateVoltage(Scanner scanner) {
        System.out.println("Voltage Calculation (V = I * R)");
        try {
            System.out.print("Enter Current (I) in amps: ");
            double current = scanner.nextDouble();

            System.out.print("Enter Resistance (R) in ohms: ");
            double resistance = scanner.nextDouble();

            double voltage = current * resistance;
            System.out.printf("Calculated Voltage: %.2f volts%n", voltage);
        } catch (Exception e) {
            System.out.println("Error: Invalid input. Please enter valid numerical values.");
        }
    }

    /**
     * Calculates current using the formula I = V / R.
     * 
     * @param scanner Scanner object to read input values.
     */
    private static void calculateCurrent(Scanner scanner) {
        System.out.println("Current Calculation (I = V / R)");
        try {
            System.out.print("Enter Voltage (V) in volts: ");
            double voltage = scanner.nextDouble();

            System.out.print("Enter Resistance (R) in ohms: ");
            double resistance = scanner.nextDouble();

            if (resistance == 0) {
                System.out.println("Error: Resistance cannot be zero.");
                return;
            }

            double current = voltage / resistance;
            System.out.printf("Calculated Current: %.2f amps%n", current);
        } catch (Exception e) {
            System.out.println("Error: Invalid input. Please enter valid numerical values.");
        }
    }

    /**
     * Calculates resistance using the formula R = V / I.
     * 
     * @param scanner Scanner object to read input values.
     */
    private static void calculateResistance(Scanner scanner) {
        System.out.println("Resistance Calculation (R = V / I)");
        try {
            System.out.print("Enter Voltage (V) in volts: ");
            double voltage = scanner.nextDouble();

            System.out.print("Enter Current (I) in amps: ");
            double current = scanner.nextDouble();

            if (current == 0) {
                System.out.println("Error: Current cannot be zero.");
                return;
            }

            double resistance = voltage / current;
            System.out.printf("Calculated Resistance: %.2f ohms%n", resistance);
        } catch (Exception e) {
            System.out.println("Error: Invalid input. Please enter valid numerical values.");
        }
    }

    /**
     * Calculates power using the formula P = V * I.
     * 
     * @param scanner Scanner object to read input values.
     */
    private static void calculatePower(Scanner scanner) {
        System.out.println("Power Calculation (P = V * I)");
        try {
            System.out.print("Enter Voltage (V) in volts: ");
            double voltage = scanner.nextDouble();

            System.out.print("Enter Current (I) in amps: ");
            double current = scanner.nextDouble();

            double power = voltage * current;
            System.out.printf("Calculated Power: %.2f watts%n", power);
        } catch (Exception e) {
            System.out.println("Error: Invalid input. Please enter valid numerical values.");
        }
    }
}
```
