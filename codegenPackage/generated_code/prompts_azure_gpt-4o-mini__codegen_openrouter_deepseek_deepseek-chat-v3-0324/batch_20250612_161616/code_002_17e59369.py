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
 * This program simulates basic electrical theory concepts for an Electrical Technology course.
 * It includes calculations for Ohm's Law, Power, Series and Parallel circuits.
 */
public class ElectricalTheorySimulator {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        boolean running = true;

        System.out.println("Electrical Theory Simulator");
        System.out.println("Lahore Group of Technical - Electrical Technology Course");
        System.out.println("--------------------------------------------------------");

        while (running) {
            displayMenu();
            int choice = getIntInput(scanner, "Enter your choice (1-6): ", 1, 6);

            switch (choice) {
                case 1:
                    calculateOhmsLaw(scanner);
                    break;
                case 2:
                    calculatePower(scanner);
                    break;
                case 3:
                    calculateSeriesResistance(scanner);
                    break;
                case 4:
                    calculateParallelResistance(scanner);
                    break;
                case 5:
                    displayTheory();
                    break;
                case 6:
                    running = false;
                    System.out.println("Exiting program. Thank you!");
                    break;
            }
        }
        scanner.close();
    }

    private static void displayMenu() {
        System.out.println("\nMain Menu:");
        System.out.println("1. Calculate using Ohm's Law (V = I × R)");
        System.out.println("2. Calculate Electrical Power (P = V × I)");
        System.out.println("3. Calculate Total Resistance in Series");
        System.out.println("4. Calculate Total Resistance in Parallel");
        System.out.println("5. Display Electrical Theory");
        System.out.println("6. Exit");
    }

    private static int getIntInput(Scanner scanner, String prompt, int min, int max) {
        while (true) {
            try {
                System.out.print(prompt);
                int input = Integer.parseInt(scanner.nextLine());
                if (input >= min && input <= max) {
                    return input;
                } else {
                    System.out.printf("Please enter a number between %d and %d.\n", min, max);
                }
            } catch (NumberFormatException e) {
                System.out.println("Invalid input. Please enter a valid number.");
            }
        }
    }

    private static double getDoubleInput(Scanner scanner, String prompt) {
        while (true) {
            try {
                System.out.print(prompt);
                return Double.parseDouble(scanner.nextLine());
            } catch (NumberFormatException e) {
                System.out.println("Invalid input. Please enter a valid number.");
            }
        }
    }

    private static void calculateOhmsLaw(Scanner scanner) {
        System.out.println("\nOhm's Law Calculator (V = I × R)");
        System.out.println("Choose what to calculate:");
        System.out.println("1. Voltage (V)");
        System.out.println("2. Current (I)");
        System.out.println("3. Resistance (R)");
        
        int choice = getIntInput(scanner, "Enter your choice (1-3): ", 1, 3);

        switch (choice) {
            case 1:
                double current = getDoubleInput(scanner, "Enter current in Amperes (I): ");
                double resistance = getDoubleInput(scanner, "Enter resistance in Ohms (R): ");
                double voltage = current * resistance;
                System.out.printf("Voltage (V) = %.2f volts\n", voltage);
                break;
            case 2:
                voltage = getDoubleInput(scanner, "Enter voltage in Volts (V): ");
                resistance = getDoubleInput(scanner, "Enter resistance in Ohms (R): ");
                current = voltage / resistance;
                System.out.printf("Current (I) = %.2f amperes\n", current);
                break;
            case 3:
                voltage = getDoubleInput(scanner, "Enter voltage in Volts (V): ");
                current = getDoubleInput(scanner, "Enter current in Amperes (I): ");
                resistance = voltage / current;
                System.out.printf("Resistance (R) = %.2f ohms\n", resistance);
                break;
        }
    }

    private static void calculatePower(Scanner scanner) {
        System.out.println("\nElectrical Power Calculator (P = V × I)");
        System.out.println("Choose what to calculate:");
        System.out.println("1. Power (P)");
        System.out.println("2. Voltage (V)");
        System.out.println("3. Current (I)");
        
        int choice = getIntInput(scanner, "Enter your choice (1-3): ", 1, 3);

        switch (choice) {
            case 1:
                double voltage = getDoubleInput(scanner, "Enter voltage in Volts (V): ");
                double current = getDoubleInput(scanner, "Enter current in Amperes (I): ");
                double power = voltage * current;
                System.out.printf("Power (P) = %.2f watts\n", power);
                break;
            case 2:
                power = getDoubleInput(scanner, "Enter power in Watts (P): ");
                current = getDoubleInput(scanner, "Enter current in Amperes (I): ");
                voltage = power / current;
                System.out.printf("Voltage (V) = %.2f volts\n", voltage);
                break;
            case 3:
                power = getDoubleInput(scanner, "Enter power in Watts (P): ");
                voltage = getDoubleInput(scanner, "Enter voltage in Volts (V): ");
                current = power / voltage;
                System.out.printf("Current (I) = %.2f amperes\n", current);
                break;
        }
    }

    private static void calculateSeriesResistance(Scanner scanner) {
        System.out.println("\nSeries Resistance Calculator");
        int numResistors = getIntInput(scanner, "Enter number of resistors: ", 1, Integer.MAX_VALUE);
        double totalResistance = 0;

        for (int i = 1; i <= numResistors; i++) {
            double resistance = getDoubleInput(scanner, String.format("Enter resistance %d in Ohms: ", i));
            totalResistance += resistance;
        }

        System.out.printf("Total resistance in series = %.2f ohms\n", totalResistance);
    }

    private static void calculateParallelResistance(Scanner scanner) {
        System.out.println("\nParallel Resistance Calculator");
        int numResistors = getIntInput(scanner, "Enter number of resistors: ", 1, Integer.MAX_VALUE);
        double reciprocalTotal = 0;

        for (int i = 1; i <= numResistors; i++) {
            double resistance = getDoubleInput(scanner, String.format("Enter resistance %d in Ohms: ", i));
            if (resistance <= 0) {
                System.out.println("Resistance must be greater than 0. Please try again.");
                i--; // Retry this input
                continue;
            }
            reciprocalTotal += 1 / resistance;
        }

        double totalResistance = 1 / reciprocalTotal;
        System.out.printf("Total resistance in parallel = %.2f ohms\n", totalResistance);
    }

    private static void displayTheory() {
        System.out.println("\nBasic Electrical Theory:");
        System.out.println("1. Ohm's Law: V = I × R");
        System.out.println("   Where:");
        System.out.println("   V = Voltage (Volts)");
        System.out.println("   I = Current (Amperes)");
        System.out.println("   R = Resistance (Ohms)");
        
        System.out.println("\n2. Electrical Power: P = V × I");
        System.out.println("   Where:");
        System.out.println("   P = Power (Watts)");
        System.out.println("   V = Voltage (Volts)");
        System.out.println("   I = Current (Amperes)");
        
        System.out.println("\n3. Series Circuits:");
        System.out.println("   - Current is the same through all components");
        System.out.println("   - Total resistance R_total = R1 + R2 + ... + Rn");
        System.out.println("   - Total voltage is the sum of individual voltages");
        
        System.out.println("\n4. Parallel Circuits:");
        System.out.println("   - Voltage is the same across all components");
        System.out.println("   - Total resistance is calculated as:");
        System.out.println("     1/R_total = 1/R1 + 1/R2 + ... + 1/Rn");
        System.out.println("   - Total current is the sum of individual currents");
    }
}
```
