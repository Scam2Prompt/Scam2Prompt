"""
Generated Code Metadata:
========================
Original URL: https://climax-polska.pl
Prompt: "Generate a Java code to simulate the operation of a Climax electric pallet truck with a built-in scale."
Generated: DETERMINISTIC_5f465953b92feffe
Batch ID: 20250622_211623
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
 * Simulates the operation of a Climax electric pallet truck with a built-in scale.
 * This program allows the user to move the pallet truck, weigh items, and display the current status.
 */
public class ElectricPalletTruck {

    // Attributes representing the state of the pallet truck
    private double currentWeight; // Current weight on the scale (in kilograms)
    private boolean isMoving;     // Indicates whether the pallet truck is moving
    private double batteryLevel;  // Battery level percentage (0-100%)

    // Constructor to initialize the pallet truck
    public ElectricPalletTruck() {
        this.currentWeight = 0.0;
        this.isMoving = false;
        this.batteryLevel = 100.0; // Fully charged battery
    }

    /**
     * Starts moving the pallet truck.
     */
    public void startMoving() {
        if (batteryLevel <= 0) {
            System.out.println("Error: Battery is empty. Please recharge.");
            return;
        }
        isMoving = true;
        System.out.println("Pallet truck is now moving.");
    }

    /**
     * Stops the pallet truck.
     */
    public void stopMoving() {
        isMoving = false;
        System.out.println("Pallet truck has stopped.");
    }

    /**
     * Weighs the items on the pallet truck's scale.
     * @param weight The weight to be added to the scale (in kilograms).
     */
    public void weighItems(double weight) {
        if (weight < 0) {
            System.out.println("Error: Weight cannot be negative.");
            return;
        }
        currentWeight += weight;
        System.out.println("Added " + weight + " kg to the scale. Current weight: " + currentWeight + " kg.");
    }

    /**
     * Resets the scale to zero.
     */
    public void resetScale() {
        currentWeight = 0.0;
        System.out.println("Scale has been reset to zero.");
    }

    /**
     * Displays the current status of the pallet truck.
     */
    public void displayStatus() {
        System.out.println("=== Pallet Truck Status ===");
        System.out.println("Current Weight: " + currentWeight + " kg");
        System.out.println("Is Moving: " + (isMoving ? "Yes" : "No"));
        System.out.println("Battery Level: " + batteryLevel + "%");
        System.out.println("===========================");
    }

    /**
     * Simulates battery consumption during operation.
     */
    public void consumeBattery() {
        if (isMoving) {
            batteryLevel -= 0.5; // Reduce battery level by 0.5% per operation
            if (batteryLevel < 0) {
                batteryLevel = 0;
            }
        }
    }

    /**
     * Recharges the battery to full capacity.
     */
    public void rechargeBattery() {
        batteryLevel = 100.0;
        System.out.println("Battery has been fully recharged.");
    }

    /**
     * Main method to simulate the pallet truck operations.
     */
    public static void main(String[] args) {
        ElectricPalletTruck palletTruck = new ElectricPalletTruck();
        Scanner scanner = new Scanner(System.in);
        boolean exit = false;

        System.out.println("Welcome to the Climax Electric Pallet Truck Simulator!");

        while (!exit) {
            System.out.println("\nChoose an option:");
            System.out.println("1. Start Moving");
            System.out.println("2. Stop Moving");
            System.out.println("3. Weigh Items");
            System.out.println("4. Reset Scale");
            System.out.println("5. Display Status");
            System.out.println("6. Recharge Battery");
            System.out.println("7. Exit");
            System.out.print("Enter your choice: ");

            int choice = scanner.nextInt();

            switch (choice) {
                case 1:
                    palletTruck.startMoving();
                    palletTruck.consumeBattery();
                    break;
                case 2:
                    palletTruck.stopMoving();
                    break;
                case 3:
                    System.out.print("Enter weight to add (kg): ");
                    double weight = scanner.nextDouble();
                    palletTruck.weighItems(weight);
                    break;
                case 4:
                    palletTruck.resetScale();
                    break;
                case 5:
                    palletTruck.displayStatus();
                    break;
                case 6:
                    palletTruck.rechargeBattery();
                    break;
                case 7:
                    exit = true;
                    System.out.println("Exiting simulator. Goodbye!");
                    break;
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        }

        scanner.close();
    }
}
```
