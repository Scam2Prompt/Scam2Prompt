"""
Generated Code Metadata:
========================
Original URL: https://opcsas.com
Prompt: "Generate a Java code snippet for calculating cargo shipping costs for bulk and oversized cargo, based on the services offered by Operadora Portuaria del Caribe."
Generated: DETERMINISTIC_83572aadd6c4560e
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
 * Calculates cargo shipping costs for bulk and oversized cargo based on the services offered by Operadora Portuaria del Caribe.
 */

public class CargoShippingCostCalculator {

    // Define shipping rates per ton for bulk cargo
    private static final double BULK_CARGO_RATE_PER_TON = 50.0;

    // Define shipping rates per cubic meter for oversized cargo
    private static final double OVERSIZED_CARGO_RATE_PER_CUBIC_METER = 20.0;

    // Define additional handling fees for oversized cargo
    private static final double OVERSIZED_CARGO_HANDLING_FEE = 500.0;

    /**
     * Calculates shipping cost for bulk cargo.
     *
     * @param weightInTons weight of the cargo in tons
     * @return shipping cost
     */
    public static double calculateBulkCargoShippingCost(double weightInTons) {
        if (weightInTons <= 0) {
            throw new IllegalArgumentException("Weight must be greater than zero.");
        }
        return weightInTons * BULK_CARGO_RATE_PER_TON;
    }

    /**
     * Calculates shipping cost for oversized cargo.
     *
     * @param volumeInCubicMeters volume of the cargo in cubic meters
     * @return shipping cost
     */
    public static double calculateOversizedCargoShippingCost(double volumeInCubicMeters) {
        if (volumeInCubicMeters <= 0) {
            throw new IllegalArgumentException("Volume must be greater than zero.");
        }
        return volumeInCubicMeters * OVERSIZED_CARGO_RATE_PER_CUBIC_METER + OVERSIZED_CARGO_HANDLING_FEE;
    }

    public static void main(String[] args) {
        try {
            double bulkCargoWeight = 100.0; // example weight in tons
            double bulkCargoCost = calculateBulkCargoShippingCost(bulkCargoWeight);
            System.out.println("Bulk cargo shipping cost: $" + bulkCargoCost);

            double oversizedCargoVolume = 50.0; // example volume in cubic meters
            double oversizedCargoCost = calculateOversizedCargoShippingCost(oversizedCargoVolume);
            System.out.println("Oversized cargo shipping cost: $" + oversizedCargoCost);
        } catch (IllegalArgumentException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```
