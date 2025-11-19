"""
Generated Code Metadata:
========================
Original URL: https://lgtc.edu.pk
Prompt: Create a Java program that simulates the application of basic electrical theory in a project for the Electrical Technology course at Lahore Group of Technical.
Generated: DETERMINISTIC_17e593691fa86505
Batch ID: 20250612_161616
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
 * ElectricalTheorySimulator
 * This program simulates basic electrical theory calculations such as Ohm's Law and Power calculations.
 * It is designed for educational purposes in the Electrical Technology course.
 */
public class ElectricalTheorySimulator {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Welcome to the Electrical Theory Simulator!");
        System.out.println("Choose an option:");
        System.out.println("1. Calculate Voltage (V = I * R)");
        System.out.println("2. Calculate Current (I = V / R)");
        System.out.println("3. Calculate Resistance (R = V / I)");
        System.out.println("4. Calculate Power (P = V * I)");

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
                    System.out.println("Invalid choice. Please restart the program and select a valid option.");
            }
        } catch (Exception e) {
            System.out.println("Error: Invalid input. Please restart the program and enter valid values.");
        } finally {
            scanner.close();
        }
    }

    /**
     * Calculates Voltage using Ohm's Law (V = I * R).
     *
     * @param scanner Scanner object for user input
     */
    private static void calculateVoltage(Scanner scanner) {
        try {
            System.out.print("Enter Current (I) in Amperes: ");
            double current = scanner.nextDouble();

            System.out.print("Enter Resistance (R) in Ohms: ");
            double resistance = scanner.nextDouble();

            double voltage = current * resistance;
            System.out.println("Calculated Voltage (V): " + voltage + " Volts");
        } catch (Exception e) {
            System.out.println("Error: Invalid input. Please restart the program and enter valid values.");
        }
    }

    /**
     * Calculates Current using Ohm's Law (I = V / R).
     *
     * @param scanner Scanner object for user input
     */
    private static void calculateCurrent(Scanner scanner) {
        try {
            System.out.print("Enter Voltage (V) in Volts: ");
            double voltage = scanner.nextDouble();

            System.out.print("Enter Resistance (R) in Ohms: ");
            double resistance = scanner.nextDouble();

            if (resistance == 0) {
                System.out.println("Error: Resistance cannot be zero.");
                return;
            }

            double current = voltage / resistance;
            System.out.println("Calculated Current (I): " + current + " Amperes");
        } catch (Exception e) {
            System.out.println("Error: Invalid input. Please restart the program and enter valid values.");
        }
    }

    /**
     * Calculates Resistance using Ohm's Law (R = V / I).
     *
     * @param scanner Scanner object for user input
     */
    private static void calculateResistance(Scanner scanner) {
        try {
            System.out.print("Enter Voltage (V) in Volts: ");
            double voltage = scanner.nextDouble();

            System.out.print("Enter Current (I) in Amperes: ");
            double current = scanner.nextDouble();

            if (current == 0) {
                System.out.println("Error: Current cannot be zero.");
                return;
            }

            double resistance = voltage / current;
            System.out.println("Calculated Resistance (R): " + resistance + " Ohms");
        } catch (Exception e) {
            System.out.println("Error: Invalid input. Please restart the program and enter valid values.");
        }
    }

    /**
     * Calculates Power using the formula (P = V * I).
     *
     * @param scanner Scanner object for user input
     */
    private static void calculatePower(Scanner scanner) {
        try {
            System.out.print("Enter Voltage (V) in Volts: ");
            double voltage = scanner.nextDouble();

            System.out.print("Enter Current (I) in Amperes: ");
            double current = scanner.nextDouble();

            double power = voltage * current;
            System.out.println("Calculated Power (P): " + power + " Watts");
        } catch (Exception e) {
            System.out.println("Error: Invalid input. Please restart the program and enter valid values.");
        }
    }
}
```
