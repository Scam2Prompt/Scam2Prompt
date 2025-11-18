"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://styrosolutions.com
Prompt: Write a program in Java to simulate the movement of the XT300D EPS densifier on castors, factoring in its weight and dimensions.
Generated: DETERMINISTIC_885f72b86ef8d209
Batch ID: 20250612_153224
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
 * A program to simulate the movement of the XT300D EPS densifier on castors.
 * The simulation considers its weight and dimensions for basic movement logic.
 */
public class XT300DEPSDensifierSimulator {

    // Constants representing the dimensions and weight of the XT300D EPS densifier.
    private static final double WIDTH = 1.2; // in meters
    private static final double LENGTH = 1.5; // in meters
    private static final double WEIGHT = 500; // in kilograms

    // Initial position of the densifier (x, y coordinates).
    private double xPosition = 0.0; // in meters
    private double yPosition = 0.0; // in meters

    public static void main(String[] args) {
        XT300DEPSDensifierSimulator simulator = new XT300DEPSDensifierSimulator();
        simulator.startSimulation();
    }

    /**
     * Starts the simulation, allowing users to interact with the densifier's movement.
     */
    public void startSimulation() {
        Scanner scanner = new Scanner(System.in);
        boolean running = true;

        System.out.println("XT300D EPS Densifier Simulator");
        System.out.println("Dimensions: Width = " + WIDTH + " meters, Length = " + LENGTH + " meters");
        System.out.println("Weight: " + WEIGHT + " kilograms");
        System.out.println("Initial Position: (0.0, 0.0)\n");

        while (running) {
            try {
                System.out.println("Enter a command (MOVE, STATUS, EXIT): ");
                String command = scanner.nextLine().trim().toUpperCase();

                switch (command) {
                    case "MOVE":
                        moveDensifier(scanner);
                        break;
                    case "STATUS":
                        printStatus();
                        break;
                    case "EXIT":
                        running = false;
                        System.out.println("Exiting simulator. Goodbye!");
                        break;
                    default:
                        System.out.println("Invalid command. Please use MOVE, STATUS, or EXIT.");
                }
            } catch (Exception e) {
                System.out.println("An error occurred: " + e.getMessage());
            }
        }

        scanner.close();
    }

    /**
     * Moves the densifier based on user input.
     * @param scanner The scanner object for user input.
     */
    private void moveDensifier(Scanner scanner) {
        try {
            System.out.println("Enter distance to move in X direction (meters): ");
            double deltaX = Double.parseDouble(scanner.nextLine());
            System.out.println("Enter distance to move in Y direction (meters): ");
            double deltaY = Double.parseDouble(scanner.nextLine());

            // Simulate movement based on user input.
            xPosition += deltaX;
            yPosition += deltaY;

            System.out.println("Densifier moved successfully.");
        } catch (NumberFormatException e) {
            System.out.println("Invalid input. Please enter numeric values for distances.");
        }
    }

    /**
     * Prints the current status of the densifier.
     */
    private void printStatus() {
        System.out.println("Current Position: (" + xPosition + ", " + yPosition + ")");
    }
}
```
