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
 * Represents a Climax electric pallet truck with a built-in scale.
 */
public class ClimaxPalletTruck {
    private double weightCapacity; // Maximum weight capacity of the pallet truck
    private double currentWeight;   // Current weight on the pallet truck
    private boolean isPoweredOn;    // Power status of the pallet truck

    /**
     * Constructor to initialize the pallet truck with a weight capacity.
     *
     * @param weightCapacity Maximum weight capacity of the pallet truck.
     */
    public ClimaxPalletTruck(double weightCapacity) {
        this.weightCapacity = weightCapacity;
        this.currentWeight = 0.0;
        this.isPoweredOn = false;
    }

    /**
     * Powers on the pallet truck.
     */
    public void powerOn() {
        isPoweredOn = true;
        System.out.println("Pallet truck powered on.");
    }

    /**
     * Powers off the pallet truck.
     */
    public void powerOff() {
        isPoweredOn = false;
        System.out.println("Pallet truck powered off.");
    }

    /**
     * Loads a specified weight onto the pallet truck.
     *
     * @param weight Weight to be loaded onto the pallet truck.
     * @throws IllegalArgumentException if the weight exceeds the capacity.
     */
    public void load(double weight) {
        if (!isPoweredOn) {
            throw new IllegalStateException("Pallet truck is not powered on.");
        }
        if (weight < 0) {
            throw new IllegalArgumentException("Weight cannot be negative.");
        }
        if (currentWeight + weight > weightCapacity) {
            throw new IllegalArgumentException("Exceeds weight capacity!");
        }
        currentWeight += weight;
        System.out.printf("Loaded %.2f kg. Current weight: %.2f kg.%n", weight, currentWeight);
    }

    /**
     * Unloads a specified weight from the pallet truck.
     *
     * @param weight Weight to be unloaded from the pallet truck.
     * @throws IllegalArgumentException if the weight to unload exceeds the current weight.
     */
    public void unload(double weight) {
        if (!isPoweredOn) {
            throw new IllegalStateException("Pallet truck is not powered on.");
        }
        if (weight < 0) {
            throw new IllegalArgumentException("Weight cannot be negative.");
        }
        if (weight > currentWeight) {
            throw new IllegalArgumentException("Cannot unload more than current weight!");
        }
        currentWeight -= weight;
        System.out.printf("Unloaded %.2f kg. Current weight: %.2f kg.%n", weight, currentWeight);
    }

    /**
     * Displays the current weight on the pallet truck.
     */
    public void displayCurrentWeight() {
        System.out.printf("Current weight on the pallet truck: %.2f kg.%n", currentWeight);
    }

    /**
     * Main method to simulate the operation of the pallet truck.
     *
     * @param args Command line arguments.
     */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ClimaxPalletTruck palletTruck = new ClimaxPalletTruck(1000.0); // 1000 kg capacity

        try {
            palletTruck.powerOn();

            // Simulate loading and unloading
            System.out.print("Enter weight to load (kg): ");
            double loadWeight = scanner.nextDouble();
            palletTruck.load(loadWeight);

            palletTruck.displayCurrentWeight();

            System.out.print("Enter weight to unload (kg): ");
            double unloadWeight = scanner.nextDouble();
            palletTruck.unload(unloadWeight);

            palletTruck.displayCurrentWeight();
        } catch (IllegalArgumentException | IllegalStateException e) {
            System.err.println("Error: " + e.getMessage());
        } finally {
            palletTruck.powerOff();
            scanner.close();
        }
    }
}
```
