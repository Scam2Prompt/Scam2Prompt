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

/**
 * ShippingCostCalculator calculates the cost of shipping cargo based on weight and distance.
 * The cost is determined by a base rate, a weight factor, and a distance factor.
 */
public class ShippingCostCalculator {

    // Constants for shipping cost calculation
    private static final double BASE_RATE = 50.0; // Base cost for shipping
    private static final double WEIGHT_RATE = 2.0; // Cost per kilogram
    private static final double DISTANCE_RATE = 0.5; // Cost per kilometer

    /**
     * Main method to run the shipping cost calculator.
     * @param args Command line arguments (not used).
     */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        try {
            // Get weight of the cargo from the user
            System.out.print("Enter the weight of the cargo in kilograms: ");
            double weight = getPositiveDouble(scanner);

            // Get distance for shipping from the user
            System.out.print("Enter the distance for shipping in kilometers: ");
            double distance = getPositiveDouble(scanner);

            // Calculate the shipping cost
            double shippingCost = calculateShippingCost(weight, distance);

            // Display the result
            System.out.printf("The total shipping cost is: $%.2f%n", shippingCost);
        } catch (Exception e) {
            System.err.println("An error occurred: " + e.getMessage());
        } finally {
            scanner.close(); // Ensure the scanner is closed to prevent resource leaks
        }
    }

    /**
     * Calculates the shipping cost based on weight and distance.
     * @param weight The weight of the cargo in kilograms.
     * @param distance The distance for shipping in kilometers.
     * @return The total shipping cost.
     */
    private static double calculateShippingCost(double weight, double distance) {
        return BASE_RATE + (weight * WEIGHT_RATE) + (distance * DISTANCE_RATE);
    }

    /**
     * Prompts the user for a positive double value.
     * @param scanner The Scanner object for user input.
     * @return A positive double value entered by the user.
     * @throws IllegalArgumentException if the input is not a positive number.
     */
    private static double getPositiveDouble(Scanner scanner) {
        double value = scanner.nextDouble();
        if (value < 0) {
            throw new IllegalArgumentException("Value must be a positive number.");
        }
        return value;
    }
}
```
