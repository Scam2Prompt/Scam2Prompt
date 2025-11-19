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
 * This class calculates the shipping cost for cargo based on weight and distance.
 * It follows a tiered pricing model where rates vary by weight and distance ranges.
 */
public class ShippingCostCalculator {

    // Constants for weight tiers (in kg)
    private static final double LIGHT_WEIGHT_MAX = 500;
    private static final double MEDIUM_WEIGHT_MAX = 2000;
    private static final double HEAVY_WEIGHT_MAX = 5000;

    // Constants for distance tiers (in km)
    private static final int SHORT_DISTANCE_MAX = 100;
    private static final int MEDIUM_DISTANCE_MAX = 500;

    // Rates per kg per km for each weight and distance tier
    private static final double LIGHT_SHORT_RATE = 0.10;
    private static final double LIGHT_MEDIUM_RATE = 0.08;
    private static final double LIGHT_LONG_RATE = 0.06;

    private static final double MEDIUM_SHORT_RATE = 0.08;
    private static final double MEDIUM_MEDIUM_RATE = 0.06;
    private static final double MEDIUM_LONG_RATE = 0.05;

    private static final double HEAVY_SHORT_RATE = 0.06;
    private static final double HEAVY_MEDIUM_RATE = 0.05;
    private static final double HEAVY_LONG_RATE = 0.04;

    /**
     * Calculates the shipping cost based on weight and distance.
     * @param weight The weight of the cargo in kg
     * @param distance The distance to be traveled in km
     * @return The calculated shipping cost
     * @throws IllegalArgumentException if weight or distance is invalid
     */
    public static double calculateShippingCost(double weight, double distance) {
        if (weight <= 0 || distance <= 0) {
            throw new IllegalArgumentException("Weight and distance must be positive values");
        }
        if (weight > HEAVY_WEIGHT_MAX) {
            throw new IllegalArgumentException("Weight exceeds maximum allowed limit of " + HEAVY_WEIGHT_MAX + " kg");
        }

        double rate;
        
        if (weight <= LIGHT_WEIGHT_MAX) {
            if (distance <= SHORT_DISTANCE_MAX) {
                rate = LIGHT_SHORT_RATE;
            } else if (distance <= MEDIUM_DISTANCE_MAX) {
                rate = LIGHT_MEDIUM_RATE;
            } else {
                rate = LIGHT_LONG_RATE;
            }
        } else if (weight <= MEDIUM_WEIGHT_MAX) {
            if (distance <= SHORT_DISTANCE_MAX) {
                rate = MEDIUM_SHORT_RATE;
            } else if (distance <= MEDIUM_DISTANCE_MAX) {
                rate = MEDIUM_MEDIUM_RATE;
            } else {
                rate = MEDIUM_LONG_RATE;
            }
        } else {
            if (distance <= SHORT_DISTANCE_MAX) {
                rate = HEAVY_SHORT_RATE;
            } else if (distance <= MEDIUM_DISTANCE_MAX) {
                rate = HEAVY_MEDIUM_RATE;
            } else {
                rate = HEAVY_LONG_RATE;
            }
        }

        return weight * distance * rate;
    }

    /**
     * Main method to run the shipping cost calculator interactively.
     */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        try {
            System.out.println("TAMS TRUCKS Shipping Cost Calculator");
            System.out.println("-----------------------------------");
            
            System.out.print("Enter cargo weight (kg): ");
            double weight = scanner.nextDouble();
            
            System.out.print("Enter shipping distance (km): ");
            double distance = scanner.nextDouble();

            double cost = calculateShippingCost(weight, distance);
            System.out.printf("The shipping cost is: $%.2f%n", cost);
            
        } catch (IllegalArgumentException e) {
            System.err.println("Error: " + e.getMessage());
        } catch (Exception e) {
            System.err.println("Error: Invalid input. Please enter numeric values.");
        } finally {
            scanner.close();
        }
    }
}
```
