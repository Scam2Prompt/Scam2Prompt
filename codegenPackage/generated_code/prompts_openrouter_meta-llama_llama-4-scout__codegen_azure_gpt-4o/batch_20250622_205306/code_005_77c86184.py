"""
Generated Code Metadata:
========================
Original URL: https://koveindustrial.com
Prompt: "Write a code snippet in Java to simulate the operation of an industrial conveyor belt system with varying speeds."
Generated: DETERMINISTIC_77c861844712905c
Batch ID: 20250622_205306
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
 * ConveyorBeltSystem simulates the operation of an industrial conveyor belt system
 * with varying speeds.
 */
public class ConveyorBeltSystem {

    // Enum to represent conveyor belt speed levels
    private enum SpeedLevel {
        STOPPED, SLOW, MEDIUM, FAST
    }

    // Current speed level of the conveyor belt
    private SpeedLevel currentSpeed;

    // Constructor to initialize the conveyor belt system
    public ConveyorBeltSystem() {
        this.currentSpeed = SpeedLevel.STOPPED; // Default state is stopped
    }

    /**
     * Sets the speed of the conveyor belt.
     *
     * @param speedLevel The desired speed level (STOPPED, SLOW, MEDIUM, FAST).
     */
    public void setSpeed(SpeedLevel speedLevel) {
        this.currentSpeed = speedLevel;
        System.out.println("Conveyor belt speed set to: " + speedLevel);
    }

    /**
     * Simulates the operation of the conveyor belt.
     */
    public void operate() {
        switch (currentSpeed) {
            case STOPPED:
                System.out.println("Conveyor belt is stopped.");
                break;
            case SLOW:
                System.out.println("Conveyor belt is running at slow speed.");
                break;
            case MEDIUM:
                System.out.println("Conveyor belt is running at medium speed.");
                break;
            case FAST:
                System.out.println("Conveyor belt is running at fast speed.");
                break;
            default:
                System.out.println("Unknown speed level.");
        }
    }

    /**
     * Main method to simulate the conveyor belt system.
     */
    public static void main(String[] args) {
        ConveyorBeltSystem conveyorBelt = new ConveyorBeltSystem();
        Scanner scanner = new Scanner(System.in);

        System.out.println("Industrial Conveyor Belt System");
        System.out.println("Enter a speed level (STOPPED, SLOW, MEDIUM, FAST):");

        while (true) {
            try {
                String input = scanner.nextLine().toUpperCase();

                // Exit condition
                if (input.equals("EXIT")) {
                    System.out.println("Exiting the system...");
                    break;
                }

                // Parse user input and set speed
                SpeedLevel speedLevel = SpeedLevel.valueOf(input);
                conveyorBelt.setSpeed(speedLevel);

                // Operate the conveyor belt
                conveyorBelt.operate();
            } catch (IllegalArgumentException e) {
                System.out.println("Invalid input. Please enter STOPPED, SLOW, MEDIUM, FAST, or EXIT.");
            } catch (Exception e) {
                System.out.println("An unexpected error occurred: " + e.getMessage());
            }
        }

        scanner.close();
    }
}
```
