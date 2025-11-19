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
/**
 * Calculates the total cost of a Chevrolet Consórcio plan.
 */
public class ChevroletConsorcioCalculator {

    /**
     * Calculates the total cost of a Chevrolet Consórcio plan.
     *
     * @param vehicleValue         the value of the vehicle
     * @param administrativeFee    the administrative fee percentage
     * @param reserveFundPercentage the reserve fund percentage
     * @param insurancePremium      the optional insurance premium
     * @return the total cost of the plan
     */
    public static double calculateTotalCost(double vehicleValue, double administrativeFee, double reserveFundPercentage, Double insurancePremium) {
        // Calculate administrative fee
        double administrativeFeeAmount = vehicleValue * (administrativeFee / 100);

        // Calculate reserve fund amount
        double reserveFundAmount = vehicleValue * (reserveFundPercentage / 100);

        // Calculate total cost without insurance
        double totalCostWithoutInsurance = vehicleValue + administrativeFeeAmount + reserveFundAmount;

        // Add insurance premium if provided
        double totalCost;
        if (insurancePremium != null) {
            totalCost = totalCostWithoutInsurance + insurancePremium;
        } else {
            totalCost = totalCostWithoutInsurance;
        }

        return totalCost;
    }

    public static void main(String[] args) {
        try {
            double vehicleValue = 50000.0; // Example vehicle value
            double administrativeFee = 2.5; // Example administrative fee percentage
            double reserveFundPercentage = 1.0; // Example reserve fund percentage
            Double insurancePremium = 1500.0; // Example insurance premium

            double totalCost = calculateTotalCost(vehicleValue, administrativeFee, reserveFundPercentage, insurancePremium);
            System.out.printf("Total cost: R$ %.2f%n", totalCost);

            // Test without insurance
            totalCost = calculateTotalCost(vehicleValue, administrativeFee, reserveFundPercentage, null);
            System.out.printf("Total cost without insurance: R$ %.2f%n", totalCost);
        } catch (Exception e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```
