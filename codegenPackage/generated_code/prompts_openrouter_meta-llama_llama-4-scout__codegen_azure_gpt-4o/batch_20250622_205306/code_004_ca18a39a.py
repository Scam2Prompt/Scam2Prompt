"""
Generated Code Metadata:
========================
Original URL: https://tamstrucks.com
Prompt: Create a Java program to calculate the cost of shipping cargo based on weight and distance, similar to what TAMS TRUCKS might use.
Generated: DETERMINISTIC_ca18a39ad74a3c52
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

public class ShippingCostCalculator {

    // Constants for cost calculation
    private static final double COST_PER_KG = 0.50; // Cost per kilogram
    private static final double COST_PER_KM = 0.75; // Cost per kilometer

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        try {
            // Prompt user for weight of cargo
            System.out.print("Enter the weight of the cargo (in kilograms): ");
            double weight = scanner.nextDouble();
            if (weight <= 0) {
                throw new IllegalArgumentException("Weight must be greater than zero.");
            }

            // Prompt user for distance to be traveled
            System.out.print("Enter the distance to be traveled (in kilometers): ");
            double distance = scanner.nextDouble();
            if (distance <= 0) {
                throw new IllegalArgumentException("Distance must be greater than zero.");
            }

            // Calculate shipping cost
            double shippingCost = calculateShippingCost(weight, distance);

            // Display the result
            System.out.printf("The total shipping cost is: $%.2f%n", shippingCost);

        } catch (IllegalArgumentException e) {
            System.err.println("Error: " + e.getMessage());
        } catch (Exception e) {
            System.err.println("An unexpected error occurred. Please try again.");
        } finally {
            // Close the scanner to prevent resource leaks
            scanner.close();
        }
    }

    /**
     * Calculates the shipping cost based on weight and distance.
     *
     * @param weight  The weight of the cargo in kilograms.
     * @param distance The distance to be traveled in kilometers.
     * @return The total shipping cost.
     */
    private static double calculateShippingCost(double weight, double distance) {
        // Calculate cost based on weight and distance
        return (weight * COST_PER_KG) + (distance * COST_PER_KM);
    }
}
```
