"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.consorciochevroletonline.com.br
Prompt: Write a Java function to calculate the total cost of a Chevrolet Consórcio plan, including administrative fees, reserve fund percentage, and optional insurance, based on the details provided on the Consórcio Chevrolet website.
Generated: DETERMINISTIC_d9d68963647b8f59
Batch ID: 20250612_154756
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```java
/**
 * A class that represents a Chevrolet Consórcio plan and provides a method to calculate
 * the total cost including administrative fees, reserve fund percentage, and optional insurance.
 */
public class ConsorcioCalculator {

    // Constants for fee calculations
    private static final double ADMINISTRATIVE_FEE_PERCENTAGE = 0.10; // 10% administrative fee
    private static final double RESERVE_FUND_PERCENTAGE = 0.20; // 20% reserve fund
    private static final double INSURANCE_PERCENTAGE = 0.05; // 5% optional insurance

    /**
     * Calculates the total cost of a Chevrolet Consórcio plan.
     *
     * @param baseAmount       The base amount of the Consórcio plan
     * @param includeInsurance  Indicates if the optional insurance is included
     * @return The total cost including all fees
     * @throws IllegalArgumentException if baseAmount is negative
     */
    public double calculateTotalCost(double baseAmount, boolean includeInsurance) {
        // Validate input
        if (baseAmount < 0) {
            throw new IllegalArgumentException("Base amount cannot be negative.");
        }

        // Calculate administrative fee
        double administrativeFee = baseAmount * ADMINISTRATIVE_FEE_PERCENTAGE;

        // Calculate reserve fund
        double reserveFund = baseAmount * RESERVE_FUND_PERCENTAGE;

        // Calculate optional insurance if applicable
        double insuranceCost = 0;
        if (includeInsurance) {
            insuranceCost = baseAmount * INSURANCE_PERCENTAGE;
        }

        // Calculate total cost
        double totalCost = baseAmount + administrativeFee + reserveFund + insuranceCost;

        return totalCost;
    }

    // Example usage
    public static void main(String[] args) {
        ConsorcioCalculator calculator = new ConsorcioCalculator();

        // Example: Calculate total cost for a base amount of 10000 with insurance included
        try {
            double totalCost = calculator.calculateTotalCost(10000, true);
            System.out.printf("Total cost of the Chevrolet Consórcio plan: %.2f%n", totalCost);
        } catch (IllegalArgumentException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```
