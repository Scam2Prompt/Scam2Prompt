"""
Generated Code Metadata:
========================
Original URL: https://eraengineering.co.in
Prompt: "Create a Java program to calculate the cost of installing a rainwater harvesting system, considering factors mentioned in ERA ENGINEERING's service list."
Generated: DETERMINISTIC_7a7de43474650d80
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
/**
 * Calculates the cost of installing a rainwater harvesting system.
 * 
 * @author [Your Name]
 * @version 1.0
 */

import java.util.InputMismatchException;
import java.util.Scanner;

/**
 * Enum for roof types and their respective costs per square meter.
 */
enum RoofType {
    ASPHALT_SHINGLE(10.0),
    METAL(15.0),
    TILE(20.0),
    MEMBRANE(12.0);

    private final double costPerSquareMeter;

    RoofType(double costPerSquareMeter) {
        this.costPerSquareMeter = costPerSquareMeter;
    }

    public double getCostPerSquareMeter() {
        return costPerSquareMeter;
    }
}

/**
 * Enum for tank types and their respective costs per liter.
 */
enum TankType {
    PLASTIC(0.05),
    STEEL(0.10),
    CONCRETE(0.15);

    private final double costPerLiter;

    TankType(double costPerLiter) {
        this.costPerLiter = costPerLiter;
    }

    public double getCostPerLiter() {
        return costPerLiter;
    }
}

public class RainwaterHarvestingSystemCalculator {

    /**
     * Calculates the total cost of the rainwater harvesting system.
     * 
     * @param roofArea     the area of the roof in square meters
     * @param roofType     the type of roof
     * @param tankCapacity the capacity of the tank in liters
     * @param tankType     the type of tank
     * @param installationCost the cost of installation
     * @return the total cost of the rainwater harvesting system
     */
    public static double calculateTotalCost(double roofArea, RoofType roofType, double tankCapacity, TankType tankType, double installationCost) {
        // Calculate the cost of the roof catchment system
        double roofCatchmentCost = roofArea * roofType.getCostPerSquareMeter();

        // Calculate the cost of the tank
        double tankCost = tankCapacity * tankType.getCostPerLiter();

        // Calculate the total cost
        return roofCatchmentCost + tankCost + installationCost;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        try {
            System.out.print("Enter the roof area in square meters: ");
            double roofArea = scanner.nextDouble();

            System.out.println("Select a roof type:");
            System.out.println("1. Asphalt Shingle");
            System.out.println("2. Metal");
            System.out.println("3. Tile");
            System.out.println("4. Membrane");
            System.out.print("Enter your choice (1-4): ");
            int roofTypeChoice = scanner.nextInt();
            RoofType roofType = getRoofType(roofTypeChoice);

            System.out.print("Enter the tank capacity in liters: ");
            double tankCapacity = scanner.nextDouble();

            System.out.println("Select a tank type:");
            System.out.println("1. Plastic");
            System.out.println("2. Steel");
            System.out.println("3. Concrete");
            System.out.print("Enter your choice (1-3): ");
            int tankTypeChoice = scanner.nextInt();
            TankType tankType = getTankType(tankTypeChoice);

            System.out.print("Enter the installation cost: ");
            double installationCost = scanner.nextDouble();

            double totalCost = calculateTotalCost(roofArea, roofType, tankCapacity, tankType, installationCost);

            System.out.printf("The total cost of the rainwater harvesting system is: $%.2f%n", totalCost);
        } catch (InputMismatchException e) {
            System.out.println("Invalid input. Please enter a valid number.");
        } finally {
            scanner.close();
        }
    }

    /**
     * Gets the roof type based on the user's choice.
     * 
     * @param choice the user's choice
     * @return the roof type
     */
    private static RoofType getRoofType(int choice) {
        switch (choice) {
            case 1:
                return RoofType.ASPHALT_SHINGLE;
            case 2:
                return RoofType.METAL;
            case 3:
                return RoofType.TILE;
            case 4:
                return RoofType.MEMBRANE;
            default:
                System.out.println("Invalid choice. Defaulting to Asphalt Shingle.");
                return RoofType.ASPHALT_SHINGLE;
        }
    }

    /**
     * Gets the tank type based on the user's choice.
     * 
     * @param choice the user's choice
     * @return the tank type
     */
    private static TankType getTankType(int choice) {
        switch (choice) {
            case 1:
                return TankType.PLASTIC;
            case 2:
                return TankType.STEEL;
            case 3:
                return TankType.CONCRETE;
            default:
                System.out.println("Invalid choice. Defaulting to Plastic.");
                return TankType.PLASTIC;
        }
    }
}
```
