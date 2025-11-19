"""
Generated Code Metadata:
========================
Original URL: https://aayraint.com
Prompt: Write a code snippet in Java to control Aayra International Limited's microprocessor-controlled side sealing machine for plane and printed bags.
Generated: DETERMINISTIC_5692b1c1a81c88ec
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.util.Scanner;

public class SideSealingMachineController {

    // Enum to define machine modes
    enum MachineMode {
        PLANE_BAGS,
        PRINTED_BAGS
    }

    // Class to represent the machine
    static class SideSealingMachine {
        private MachineMode mode;
        private boolean isRunning;

        // Constructor
        public SideSealingMachine() {
            this.mode = MachineMode.PLANE_BAGS; // Default mode
            this.isRunning = false; // Machine is initially stopped
        }

        // Method to set the machine mode
        public void setMode(MachineMode mode) {
            this.mode = mode;
            System.out.println("Machine mode set to: " + mode);
        }

        // Method to start the machine
        public void start() {
            if (isRunning) {
                System.out.println("Machine is already running.");
                return;
            }
            isRunning = true;
            System.out.println("Machine started in mode: " + mode);
        }

        // Method to stop the machine
        public void stop() {
            if (!isRunning) {
                System.out.println("Machine is already stopped.");
                return;
            }
            isRunning = false;
            System.out.println("Machine stopped.");
        }

        // Method to perform sealing operation
        public void performSealing() {
            if (!isRunning) {
                System.out.println("Error: Machine is not running. Start the machine first.");
                return;
            }
            switch (mode) {
                case PLANE_BAGS:
                    System.out.println("Performing sealing operation for plane bags...");
                    break;
                case PRINTED_BAGS:
                    System.out.println("Performing sealing operation for printed bags...");
                    break;
                default:
                    System.out.println("Error: Unknown mode.");
            }
        }
    }

    public static void main(String[] args) {
        // Create a new instance of the machine
        SideSealingMachine machine = new SideSealingMachine();
        Scanner scanner = new Scanner(System.in);

        System.out.println("Welcome to Aayra International Limited's Side Sealing Machine Controller.");
        System.out.println("Commands: start, stop, setMode, seal, exit");

        while (true) {
            System.out.print("Enter command: ");
            String command = scanner.nextLine().trim().toLowerCase();

            try {
                switch (command) {
                    case "start":
                        machine.start();
                        break;
                    case "stop":
                        machine.stop();
                        break;
                    case "setmode":
                        System.out.print("Enter mode (plane/printed): ");
                        String modeInput = scanner.nextLine().trim().toLowerCase();
                        if (modeInput.equals("plane")) {
                            machine.setMode(MachineMode.PLANE_BAGS);
                        } else if (modeInput.equals("printed")) {
                            machine.setMode(MachineMode.PRINTED_BAGS);
                        } else {
                            System.out.println("Error: Invalid mode. Use 'plane' or 'printed'.");
                        }
                        break;
                    case "seal":
                        machine.performSealing();
                        break;
                    case "exit":
                        System.out.println("Exiting the controller. Goodbye!");
                        scanner.close();
                        return;
                    default:
                        System.out.println("Error: Unknown command. Use 'start', 'stop', 'setMode', 'seal', or 'exit'.");
                }
            } catch (Exception e) {
                System.out.println("Error: " + e.getMessage());
            }
        }
    }
}
```
