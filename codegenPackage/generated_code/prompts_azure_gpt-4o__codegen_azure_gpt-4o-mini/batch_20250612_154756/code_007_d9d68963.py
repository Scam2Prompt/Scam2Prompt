"""
Generated Code Metadata:
========================
Original URL: https://www.consorciochevroletonline.com.br
Prompt: Write a Java function to calculate the total cost of a Chevrolet Consórcio plan, including administrative fees, reserve fund percentage, and optional insurance, based on the details provided on the Consórcio Chevrolet website.
Generated: DETERMINISTIC_d9d68963647b8f59
Batch ID: 20250612_154756
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.math.BigDecimal;
import java.math.RoundingMode;

/**
 * This class provides a method to calculate the total cost of a Chevrolet Consórcio plan.
 */
public class ConsorcioCalculator {

    /**
     * Calculates the total cost of a Chevrolet Consórcio plan.
     *
     * @param basePrice          The base price of the vehicle.
     * @param adminFeePercentage The percentage of the administrative fee.
     * @param reserveFundPercentage The percentage of the reserve fund.
     * @param insuranceAmount     The optional insurance amount.
     * @return The total cost of the Consórcio plan.
     * @throws IllegalArgumentException if any input value is negative.
     */
    public static BigDecimal calculateTotalCost(BigDecimal basePrice, 
                                                 BigDecimal adminFeePercentage, 
                                                 BigDecimal reserveFundPercentage, 
                                                 BigDecimal insuranceAmount) {
        // Validate input parameters
        if (basePrice.compareTo(BigDecimal.ZERO) < 0 || 
            adminFeePercentage.compareTo(BigDecimal.ZERO) < 0 || 
            reserveFundPercentage.compareTo(BigDecimal.ZERO) < 0 || 
            insuranceAmount.compareTo(BigDecimal.ZERO) < 0) {
            throw new IllegalArgumentException("Input values must be non-negative.");
        }

        // Calculate administrative fee
        BigDecimal adminFee = basePrice.multiply(adminFeePercentage).divide(BigDecimal.valueOf(100), RoundingMode.HALF_UP);

        // Calculate reserve fund
        BigDecimal reserveFund = basePrice.multiply(reserveFundPercentage).divide(BigDecimal.valueOf(100), RoundingMode.HALF_UP);

        // Calculate total cost
        BigDecimal totalCost = basePrice.add(adminFee).add(reserveFund).add(insuranceAmount);

        // Return the total cost rounded to two decimal places
        return totalCost.setScale(2, RoundingMode.HALF_UP);
    }

    public static void main(String[] args) {
        // Example usage
        try {
            BigDecimal basePrice = new BigDecimal("30000"); // Base price of the vehicle
            BigDecimal adminFeePercentage = new BigDecimal("5"); // 5% administrative fee
            BigDecimal reserveFundPercentage = new BigDecimal("10"); // 10% reserve fund
            BigDecimal insuranceAmount = new BigDecimal("1500"); // Optional insurance amount

            BigDecimal totalCost = calculateTotalCost(basePrice, adminFeePercentage, reserveFundPercentage, insuranceAmount);
            System.out.println("Total Cost of the Consórcio Plan: " + totalCost);
        } catch (IllegalArgumentException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```
