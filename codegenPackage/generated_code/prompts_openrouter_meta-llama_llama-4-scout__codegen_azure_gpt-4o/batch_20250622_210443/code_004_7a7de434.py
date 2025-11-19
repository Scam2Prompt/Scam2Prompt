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
import java.util.Scanner;

/**
 * Rainwater Harvesting System Cost Calculator
 * This program calculates the cost of installing a rainwater harvesting system
 * based on user inputs and factors mentioned in ERA ENGINEERING's service list.
 */
public class RainwaterHarvestingCostCalculator {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        try {
            // Prompt user for input
            System.out.println("Welcome to Rainwater Harvesting System Cost Calculator!");
            System.out.print("Enter the area of the roof (in square meters): ");
            double roofArea = scanner.nextDouble();

            System.out.print("Enter the cost per square meter for installation: ");
            double costPerSquareMeter = scanner.nextDouble();

            System.out.print("Enter the cost of storage tank (fixed cost): ");
            double storageTankCost = scanner.nextDouble();

            System.out.print("Enter the cost of filtration system (fixed cost): ");
            double filtrationSystemCost = scanner.nextDouble();

            System.out.print("Enter the cost of plumbing and accessories (fixed cost): ");
            double plumbingCost = scanner.nextDouble();

            System.out.print("Enter the labor cost (fixed cost): ");
            double laborCost = scanner.nextDouble();

            // Validate inputs
            if (roofArea <= 0 || costPerSquareMeter <= 0 || storageTankCost < 0 || filtrationSystemCost < 0 || plumbingCost < 0 || laborCost < 0) {
                System.out.println("Error: Invalid input values. Please ensure all values are positive.");
                return;
            }

            // Calculate total cost
            double installationCost = roofArea * costPerSquareMeter;
            double totalCost = installationCost + storageTankCost + filtrationSystemCost + plumbingCost + laborCost;

            // Display the result
            System.out.println("\n--- Cost Breakdown ---");
            System.out.printf("Roof Installation Cost: $%.2f%n", installationCost);
            System.out.printf("Storage Tank Cost: $%.2f%n", storageTankCost);
            System.out.printf("Filtration System Cost: $%.2f%n", filtrationSystemCost);
            System.out.printf("Plumbing and Accessories Cost: $%.2f%n", plumbingCost);
            System.out.printf("Labor Cost: $%.2f%n", laborCost);
            System.out.printf("Total Cost: $%.2f%n", totalCost);

        } catch (Exception e) {
            // Handle invalid input
            System.out.println("Error: Invalid input. Please enter numeric values only.");
        } finally {
            // Close the scanner
            scanner.close();
        }
    }
}
```
