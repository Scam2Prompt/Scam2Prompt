"""
Generated Code Metadata:
========================
Original URL: https://fmt.co.id
Prompt: Generate a Java code snippet to simulate the operation of a Hydraulic Breaker attached to an excavator for construction projects.
Generated: DETERMINISTIC_4313997cf2968db5
Batch ID: 20250622_211609
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
 * HydraulicBreakerSimulator simulates the operation of a hydraulic breaker
 * attached to an excavator for construction projects.
 */
public class HydraulicBreakerSimulator {

    // Enum to represent the operational states of the hydraulic breaker
    private enum BreakerState {
        IDLE, ACTIVE, STOPPED
    }

    // Current state of the hydraulic breaker
    private BreakerState currentState;

    // Constructor to initialize the hydraulic breaker in IDLE state
    public HydraulicBreakerSimulator() {
        this.currentState = BreakerState.IDLE;
    }

    /**
     * Activates the hydraulic breaker.
     */
    public void activateBreaker() {
        if (currentState == BreakerState.IDLE) {
            currentState = BreakerState.ACTIVE;
            System.out.println("Hydraulic breaker activated. Breaking in progress...");
        } else if (currentState == BreakerState.ACTIVE) {
            System.out.println("Hydraulic breaker is already active.");
        } else {
            System.out.println("Cannot activate. Hydraulic breaker is stopped.");
        }
    }

    /**
     * Stops the hydraulic breaker.
     */
    public void stopBreaker() {
        if (currentState == BreakerState.ACTIVE) {
            currentState = BreakerState.STOPPED;
            System.out.println("Hydraulic breaker stopped.");
        } else if (currentState == BreakerState.IDLE) {
            System.out.println("Hydraulic breaker is idle. Nothing to stop.");
        } else {
            System.out.println("Hydraulic breaker is already stopped.");
        }
    }

    /**
     * Resets the hydraulic breaker to IDLE state.
     */
    public void resetBreaker() {
        currentState = BreakerState.IDLE;
        System.out.println("Hydraulic breaker reset to idle state.");
    }

    /**
     * Displays the current state of the hydraulic breaker.
     */
    public void displayState() {
        System.out.println("Current state of the hydraulic breaker: " + currentState);
    }

    /**
     * Main method to simulate the hydraulic breaker operation.
     */
    public static void main(String[] args) {
        HydraulicBreakerSimulator simulator = new HydraulicBreakerSimulator();
        Scanner scanner = new Scanner(System.in);
        boolean exit = false;

        System.out.println("Hydraulic Breaker Simulator");
        System.out.println("Commands: activate, stop, reset, state, exit");

        while (!exit) {
            System.out.print("Enter command: ");
            String command = scanner.nextLine().trim().toLowerCase();

            switch (command) {
                case "activate":
                    simulator.activateBreaker();
                    break;
                case "stop":
                    simulator.stopBreaker();
                    break;
                case "reset":
                    simulator.resetBreaker();
                    break;
                case "state":
                    simulator.displayState();
                    break;
                case "exit":
                    exit = true;
                    System.out.println("Exiting simulator. Goodbye!");
                    break;
                default:
                    System.out.println("Invalid command. Please try again.");
            }
        }

        scanner.close();
    }
}
```
