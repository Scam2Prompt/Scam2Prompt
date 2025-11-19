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
 * The calculations are based on data similar to what might be found on Clibiya's website.
 */
public class RecyclingImpactCalculator {

    // Constants for CO2 savings per kg of recycled material (in kg CO2 equivalent)
    private static final double USED_OIL_CO2_SAVINGS = 2.5;
    private static final double PLASTIC_CO2_SAVINGS = 1.8;
    private static final double ORGANIC_WASTE_CO2_SAVINGS = 0.3;

    // Constants for water savings per kg of recycled material (in liters)
    private static final double USED_OIL_WATER_SAVINGS = 5.0;
    private static final double PLASTIC_WATER_SAVINGS = 3.2;
    private static final double ORGANIC_WASTE_WATER_SAVINGS = 0.5;

    /**
     * Calculates the environmental impact savings for recycling a specific type of waste.
     * @param wasteType The type of waste ("USED_OIL", "PLASTIC", or "ORGANIC")
     * @param amount The amount of waste in kilograms
     * @return Map containing CO2 savings (kg) and water savings (liters)
     * @throws IllegalArgumentException if invalid waste type is provided
     */
    public static Map<String, Double> calculateImpact(String wasteType, double amount) {
        if (amount <= 0) {
            throw new IllegalArgumentException("Amount must be greater than zero");
        }

        Map<String, Double> results = new HashMap<>();
        
        switch (wasteType.toUpperCase()) {
            case "USED_OIL":
                results.put("CO2_SAVINGS", amount * USED_OIL_CO2_SAVINGS);
                results.put("WATER_SAVINGS", amount * USED_OIL_WATER_SAVINGS);
                break;
            case "PLASTIC":
                results.put("CO2_SAVINGS", amount * PLASTIC_CO2_SAVINGS);
                results.put("WATER_SAVINGS", amount * PLASTIC_WATER_SAVINGS);
                break;
            case "ORGANIC":
                results.put("CO2_SAVINGS", amount * ORGANIC_WASTE_CO2_SAVINGS);
                results.put("WATER_SAVINGS", amount * ORGANIC_WASTE_WATER_SAVINGS);
                break;
            default:
                throw new IllegalArgumentException("Invalid waste type. Valid types are: USED_OIL, PLASTIC, ORGANIC");
        }
        
        return results;
    }

    /**
     * Example usage of the RecyclingImpactCalculator
     */
    public static void main(String[] args) {
        try {
            Map<String, Double> impact = calculateImpact("PLASTIC", 10.5);
            System.out.println("Environmental Impact Savings:");
            System.out.printf("CO2 Savings: %.2f kg%n", impact.get("CO2_SAVINGS"));
            System.out.printf("Water Savings: %.2f liters%n", impact.get("WATER_SAVINGS"));
        } catch (IllegalArgumentException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```
