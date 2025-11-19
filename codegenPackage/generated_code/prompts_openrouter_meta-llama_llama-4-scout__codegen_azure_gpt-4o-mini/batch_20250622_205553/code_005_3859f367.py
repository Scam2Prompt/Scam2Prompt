"""
Generated Code Metadata:
========================
Original URL: https://ohclift.com
Prompt: Generate a code example in C++ or Java to simulate the operation of a hydraulic lift system, including the control logic for lifting, lowering, and safety features, inspired by the product descriptions on ohclift.com.
Generated: DETERMINISTIC_3859f36774852e1d
Batch ID: 20250622_205553
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
 * HydraulicLiftSystem simulates the operation of a hydraulic lift system.
 * It includes control logic for lifting, lowering, and safety features.
 */
public class HydraulicLiftSystem {
    private boolean isLifted;
    private boolean isOperational;
    private final int MAX_HEIGHT = 10; // Maximum height the lift can reach
    private int currentHeight;

    public HydraulicLiftSystem() {
        this.isLifted = false;
        this.isOperational = true;
        this.currentHeight = 0;
    }

    /**
     * Lifts the hydraulic lift if it is operational and not already lifted.
     */
    public void lift() {
        if (!isOperational) {
            System.out.println("Lift is not operational. Cannot lift.");
            return;
        }
        if (isLifted) {
            System.out.println("Lift is already at maximum height.");
            return;
        }
        currentHeight++;
        if (currentHeight >= MAX_HEIGHT) {
            isLifted = true;
            System.out.println("Lift is now at maximum height.");
        } else {
            System.out.println("Lift raised to height: " + currentHeight);
        }
    }

    /**
     * Lowers the hydraulic lift if it is operational and not already at ground level.
     */
    public void lower() {
        if (!isOperational) {
            System.out.println("Lift is not operational. Cannot lower.");
            return;
        }
        if (currentHeight <= 0) {
            System.out.println("Lift is already at ground level.");
            return;
        }
        currentHeight--;
        if (currentHeight == 0) {
            isLifted = false;
            System.out.println("Lift is now at ground level.");
        } else {
            System.out.println("Lift lowered to height: " + currentHeight);
        }
    }

    /**
     * Stops the operation of the lift, marking it as non-operational.
     */
    public void stop() {
        isOperational = false;
        System.out.println("Lift has been stopped and is non-operational.");
    }

    /**
     * Starts the operation of the lift, marking it as operational.
     */
    public void start() {
        isOperational = true;
        System.out.println("Lift is now operational.");
    }

    public static void main(String[] args) {
        HydraulicLiftSystem lift = new HydraulicLiftSystem();
        Scanner scanner = new Scanner(System.in);
        String command;

        System.out.println("Welcome to the Hydraulic Lift System.");
        System.out.println("Commands: lift, lower, stop, start, exit");

        while (true) {
            System.out.print("Enter command: ");
            command = scanner.nextLine().toLowerCase();

            switch (command) {
                case "lift":
                    lift.lift();
                    break;
                case "lower":
                    lift.lower();
                    break;
                case "stop":
                    lift.stop();
                    break;
                case "start":
                    lift.start();
                    break;
                case "exit":
                    System.out.println("Exiting the Hydraulic Lift System.");
                    scanner.close();
                    return;
                default:
                    System.out.println("Invalid command. Please try again.");
            }
        }
    }
}
```
