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

Here is the requested code in Java:

```java
import java.util.Scanner;

/**
 * HydraulicLiftSystem simulates the operation of a hydraulic lift system.
 * It includes control logic for lifting, lowering, and safety features.
 */
public class HydraulicLiftSystem {

    // Enum to represent the state of the lift
    private enum LiftState {
        IDLE, LIFTING, LOWERING, EMERGENCY_STOP
    }

    // Current state of the lift
    private LiftState currentState = LiftState.IDLE;

    // Maximum and minimum height of the lift (in meters)
    private final double MAX_HEIGHT = 10.0;
    private final double MIN_HEIGHT = 0.0;

    // Current height of the lift
    private double currentHeight = 0.0;

    // Safety flag for emergency stop
    private boolean emergencyStopActivated = false;

    /**
     * Lifts the hydraulic system by a specified amount.
     *
     * @param amount The amount to lift (in meters).
     */
    public void lift(double amount) {
        if (emergencyStopActivated) {
            System.out.println("Emergency stop activated. Cannot lift.");
            return;
        }

        if (currentState == LiftState.LIFTING || currentState == LiftState.IDLE) {
            currentState = LiftState.LIFTING;
            currentHeight += amount;

            if (currentHeight > MAX_HEIGHT) {
                currentHeight = MAX_HEIGHT;
                System.out.println("Lift reached maximum height.");
            } else {
                System.out.println("Lifted to height: " + currentHeight + " meters.");
            }

            currentState = LiftState.IDLE; // Return to idle state after operation
        } else {
            System.out.println("Cannot lift. Current state: " + currentState);
        }
    }

    /**
     * Lowers the hydraulic system by a specified amount.
     *
     * @param amount The amount to lower (in meters).
     */
    public void lower(double amount) {
        if (emergencyStopActivated) {
            System.out.println("Emergency stop activated. Cannot lower.");
            return;
        }

        if (currentState == LiftState.LOWERING || currentState == LiftState.IDLE) {
            currentState = LiftState.LOWERING;
            currentHeight -= amount;

            if (currentHeight < MIN_HEIGHT) {
                currentHeight = MIN_HEIGHT;
                System.out.println("Lift reached minimum height.");
            } else {
                System.out.println("Lowered to height: " + currentHeight + " meters.");
            }

            currentState = LiftState.IDLE; // Return to idle state after operation
        } else {
            System.out.println("Cannot lower. Current state: " + currentState);
        }
    }

    /**
     * Activates the emergency stop feature.
     */
    public void activateEmergencyStop() {
        emergencyStopActivated = true;
        currentState = LiftState.EMERGENCY_STOP;
        System.out.println("Emergency stop activated. All operations halted.");
    }

    /**
     * Deactivates the emergency stop feature.
     */
    public void deactivateEmergencyStop() {
        emergencyStopActivated = false;
        currentState = LiftState.IDLE;
        System.out.println("Emergency stop deactivated. System is now operational.");
    }

    /**
     * Displays the current status of the hydraulic lift system.
     */
    public void displayStatus() {
        System.out.println("Current Height: " + currentHeight + " meters");
        System.out.println("Current State: " + currentState);
        System.out.println("Emergency Stop Activated: " + emergencyStopActivated);
    }

    /**
     * Main method to simulate the hydraulic lift system.
     */
    public static void main(String[] args) {
        HydraulicLiftSystem liftSystem = new HydraulicLiftSystem();
        Scanner scanner = new Scanner(System.in);

        System.out.println("Hydraulic Lift System Simulation");
        System.out.println("Commands: lift <amount>, lower <amount>, emergency_stop, deactivate_stop, status, exit");

        while (true) {
            System.out.print("Enter command: ");
            String command = scanner.nextLine();

            try {
                if (command.startsWith("lift")) {
                    double amount = Double.parseDouble(command.split(" ")[1]);
                    liftSystem.lift(amount);
                } else if (command.startsWith("lower")) {
                    double amount = Double.parseDouble(command.split(" ")[1]);
                    liftSystem.lower(amount);
                } else if (command.equals("emergency_stop")) {
                    liftSystem.activateEmergencyStop();
                } else if (command.equals("deactivate_stop")) {
                    liftSystem.deactivateEmergencyStop();
                } else if (command.equals("status")) {
                    liftSystem.displayStatus();
                } else if (command.equals("exit")) {
                    System.out.println("Exiting simulation.");
                    break;
                } else {
                    System.out.println("Invalid command. Please try again.");
                }
            } catch (Exception e) {
                System.out.println("Error processing command: " + e.getMessage());
            }
        }

        scanner.close();
    }
}
```
