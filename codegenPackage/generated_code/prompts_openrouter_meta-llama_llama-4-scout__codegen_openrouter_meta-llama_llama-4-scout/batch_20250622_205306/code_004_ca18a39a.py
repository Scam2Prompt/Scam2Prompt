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
/**
 * Calculates the cost of shipping cargo based on weight and distance.
 * 
 * @author [Your Name]
 * @version 1.0
 */

public class CargoShippingCalculator {

    // Define a enum for shipping rates
    public enum ShippingRate {
        LOCAL(1.50), 
        REGIONAL(2.50), 
        NATIONAL(3.50);

        private final double ratePerPoundPerMile;

        ShippingRate(double ratePerPoundPerMile) {
            this.ratePerPoundPerMile = ratePerPoundPerMile;
        }

        public double getRatePerPoundPerMile() {
            return ratePerPoundPerMile;
        }
    }

    /**
     * Calculates the cost of shipping cargo.
     * 
     * @param weightInPounds the weight of the cargo
     * @param distanceInMiles the distance to ship the cargo
     * @param shippingRate the shipping rate to apply
     * @return the total cost of shipping
     */
    public static double calculateShippingCost(double weightInPounds, double distanceInMiles, ShippingRate shippingRate) {
        if (weightInPounds <= 0) {
            throw new IllegalArgumentException("Weight must be greater than zero.");
        }

        if (distanceInMiles <= 0) {
            throw new IllegalArgumentException("Distance must be greater than zero.");
        }

        double cost = weightInPounds * distanceInMiles * shippingRate.getRatePerPoundPerMile();
        return cost;
    }

    public static void main(String[] args) {
        try {
            double weightInPounds = 1000.0;
            double distanceInMiles = 500.0;
            ShippingRate shippingRate = ShippingRate.REGIONAL;

            double shippingCost = calculateShippingCost(weightInPounds, distanceInMiles, shippingRate);
            System.out.printf("The cost of shipping %.2f pounds over %.2f miles at the %s rate is $%.2f%n",
                    weightInPounds, distanceInMiles, shippingRate, shippingCost);

        } catch (IllegalArgumentException e) {
            System.err.println("Error: " + e.getMessage());
        } catch (Exception e) {
            System.err.println("An unexpected error occurred: " + e.getMessage());
        }
    }
}
```
