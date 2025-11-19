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
import java.util.InputMismatchException;
import java.util.Scanner;

/**
 * This class simulates basic electrical theory calculations for an Electrical Technology course project.
 * It allows users to calculate Ohm's Law (Voltage, Current, Resistance) and Power.
 */
public class ElectricalTheorySimulator {

    private static final Scanner scanner = new Scanner(System.in);

    /**
     * Main method to run the simulator.
     * 
     * @param args Command line arguments (not used).
     */
    public static void main(String[] args) {
        while (true) {
            System.out.println("Welcome to the Electrical Theory Simulator!");
            System.out.println("Choose an option:");
            System.out.println("1. Calculate Voltage (V = I * R)");
            System.out.println("2. Calculate Current (I = V / R)");
            System.out.println("3. Calculate Resistance (R = V / I)");
            System.out.println("4. Calculate Power (P = V * I)");
            System.out.println("5. Exit");

            int choice = getUserChoice();

            switch (choice) {
                case 1:
                    calculateVoltage();
                    break;
                case 2:
                    calculateCurrent();
                    break;
                case 3:
                    calculateResistance();
                    break;
                case 4:
                    calculatePower();
                    break;
                case 5:
                    System.out.println("Exiting the simulator. Goodbye!");
                    return;
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        }
    }

    /**
     * Prompts the user for a valid integer choice.
     * 
     * @return The user's choice as an integer.
     */
    private static int getUserChoice() {
        int choice = 0;
        while (true) {
            try {
                System.out.print("Enter your choice: ");
                choice = scanner.nextInt();
                scanner.nextLine(); // Clear the buffer
                break;
            } catch (InputMismatchException e) {
                System.out.println("Invalid input. Please enter a number.");
                scanner.nextLine(); // Clear the invalid input
            }
        }
        return choice;
    }

    /**
     * Calculates and displays the voltage based on user input for current and resistance.
     */
    private static void calculateVoltage() {
        double current = getPositiveDouble("Enter current (I) in Amperes: ");
        double resistance = getPositiveDouble("Enter resistance (R) in Ohms: ");
        double voltage = current * resistance;
        System.out.printf("Calculated Voltage (V): %.2f Volts%n", voltage);
    }

    /**
     * Calculates and displays the current based on user input for voltage and resistance.
     */
    private static void calculateCurrent() {
        double voltage = getPositiveDouble("Enter voltage (V) in Volts: ");
        double resistance = getPositiveDouble("Enter resistance (R) in Ohms: ");
        double current = voltage / resistance;
        System.out.printf("Calculated Current (I): %.2f Amperes%n", current);
    }

    /**
     * Calculates and displays the resistance based on user input for voltage and current.
     */
    private static void calculateResistance() {
        double voltage = getPositiveDouble("Enter voltage (V) in Volts: ");
        double current = getPositiveDouble("Enter current (I) in Amperes: ");
        double resistance = voltage / current;
        System.out.printf("Calculated Resistance (R): %.2f Ohms%n", resistance);
    }

    /**
     * Calculates and displays the power based on user input for voltage and current.
     */
    private static void calculatePower() {
        double voltage = getPositiveDouble("Enter voltage (V) in Volts: ");
        double current = getPositiveDouble("Enter current (I) in Amperes: ");
        double power = voltage * current;
        System.out.printf("Calculated Power (P): %.2f Watts%n", power);
    }

    /**
     * Prompts the user for a positive double value.
     * 
     * @param prompt The message to display to the user.
     * @return The positive double value entered by the user.
     */
    private static double getPositiveDouble(String prompt) {
        double value = 0;
        while (true) {
            try {
                System.out.print(prompt);
                value = scanner.nextDouble();
                if (value <= 0) {
                    throw new IllegalArgumentException("Value must be positive.");
                }
                scanner.nextLine(); // Clear the buffer
                break;
            } catch (InputMismatchException e) {
                System.out.println("Invalid input. Please enter a valid number.");
                scanner.nextLine(); // Clear the invalid input
            } catch (IllegalArgumentException e) {
                System.out.println(e.getMessage());
            }
        }
        return value;
    }
}
```
