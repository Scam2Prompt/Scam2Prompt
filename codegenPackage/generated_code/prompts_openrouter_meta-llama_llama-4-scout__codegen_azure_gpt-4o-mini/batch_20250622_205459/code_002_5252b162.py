"""
Generated Code Metadata:
========================
Original URL: https://clibiya.com
Prompt: "Generate a Java code snippet for calculating the environmental impact of recycling different types of waste, such as used oil, plastic, and organic waste, as described on Clibiya's website."
Generated: DETERMINISTIC_5252b1627be85052
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.util.HashMap;
import java.util.Map;

/**
 * This class calculates the environmental impact of recycling different types of waste.
 */
public class RecyclingImpactCalculator {

    // Constants representing the environmental impact factors for each waste type (in kg CO2 equivalent)
    private static final Map<String, Double> IMPACT_FACTORS = new HashMap<>();

    static {
        IMPACT_FACTORS.put("used_oil", 2.5); // kg CO2 equivalent per liter of used oil recycled
        IMPACT_FACTORS.put("plastic", 1.5);   // kg CO2 equivalent per kg of plastic recycled
        IMPACT_FACTORS.put("organic", 0.1);    // kg CO2 equivalent per kg of organic waste recycled
    }

    /**
     * Calculates the total environmental impact of recycling given amounts of different waste types.
     *
     * @param wasteAmounts A map containing the amounts of each waste type (in kg or liters).
     * @return The total environmental impact in kg CO2 equivalent.
     * @throws IllegalArgumentException if the waste type is not recognized or the amount is negative.
     */
    public double calculateImpact(Map<String, Double> wasteAmounts) {
        double totalImpact = 0.0;

        for (Map.Entry<String, Double> entry : wasteAmounts.entrySet()) {
            String wasteType = entry.getKey();
            double amount = entry.getValue();

            // Validate the amount
            if (amount < 0) {
                throw new IllegalArgumentException("Amount of waste cannot be negative: " + amount);
            }

            // Calculate impact for recognized waste types
            if (IMPACT_FACTORS.containsKey(wasteType)) {
                totalImpact += amount * IMPACT_FACTORS.get(wasteType);
            } else {
                throw new IllegalArgumentException("Unrecognized waste type: " + wasteType);
            }
        }

        return totalImpact;
    }

    public static void main(String[] args) {
        RecyclingImpactCalculator calculator = new RecyclingImpactCalculator();

        // Example usage
        Map<String, Double> wasteAmounts = new HashMap<>();
        wasteAmounts.put("used_oil", 10.0); // 10 liters of used oil
        wasteAmounts.put("plastic", 5.0);   // 5 kg of plastic
        wasteAmounts.put("organic", 20.0);  // 20 kg of organic waste

        try {
            double impact = calculator.calculateImpact(wasteAmounts);
            System.out.printf("Total environmental impact of recycling: %.2f kg CO2 equivalent%n", impact);
        } catch (IllegalArgumentException e) {
            System.err.println("Error calculating impact: " + e.getMessage());
        }
    }
}
```
