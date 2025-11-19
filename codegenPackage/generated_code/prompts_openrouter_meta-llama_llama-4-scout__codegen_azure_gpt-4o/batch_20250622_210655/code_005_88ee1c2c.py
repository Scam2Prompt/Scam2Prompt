"""
Generated Code Metadata:
========================
Original URL: https://unisonplus.vn
Prompt: "Write a code snippet in Java to calculate the environmental impact of a construction project, considering factors mentioned in Unison Plus's safety and environmental regulations."
Generated: DETERMINISTIC_88ee1c2cb1f7f54e
Batch ID: 20250622_210655
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
 * EnvironmentalImpactCalculator
 * This class calculates the environmental impact of a construction project
 * based on factors defined in Unison Plus's safety and environmental regulations.
 */
public class EnvironmentalImpactCalculator {

    // Constants representing environmental factors and their weights
    private static final double AIR_POLLUTION_WEIGHT = 0.3;
    private static final double WATER_POLLUTION_WEIGHT = 0.25;
    private static final double NOISE_POLLUTION_WEIGHT = 0.2;
    private static final double WASTE_GENERATION_WEIGHT = 0.15;
    private static final double ENERGY_CONSUMPTION_WEIGHT = 0.1;

    /**
     * Calculates the environmental impact score of a construction project.
     *
     * @param factors A map containing the values for each environmental factor.
     *                Keys: "airPollution", "waterPollution", "noisePollution", "wasteGeneration", "energyConsumption"
     *                Values: Double values representing the severity of each factor (0 to 1 scale).
     * @return The calculated environmental impact score (0 to 1 scale).
     * @throws IllegalArgumentException if any factor value is out of range (0 to 1).
     */
    public static double calculateImpactScore(Map<String, Double> factors) throws IllegalArgumentException {
        // Validate input
        for (Map.Entry<String, Double> entry : factors.entrySet()) {
            if (entry.getValue() < 0 || entry.getValue() > 1) {
                throw new IllegalArgumentException("Factor value for " + entry.getKey() + " must be between 0 and 1.");
            }
        }

        // Calculate weighted impact score
        double impactScore = 0;
        impactScore += factors.getOrDefault("airPollution", 0.0) * AIR_POLLUTION_WEIGHT;
        impactScore += factors.getOrDefault("waterPollution", 0.0) * WATER_POLLUTION_WEIGHT;
        impactScore += factors.getOrDefault("noisePollution", 0.0) * NOISE_POLLUTION_WEIGHT;
        impactScore += factors.getOrDefault("wasteGeneration", 0.0) * WASTE_GENERATION_WEIGHT;
        impactScore += factors.getOrDefault("energyConsumption", 0.0) * ENERGY_CONSUMPTION_WEIGHT;

        return impactScore;
    }

    public static void main(String[] args) {
        // Example usage
        try {
            // Define environmental factors for a construction project
            Map<String, Double> factors = new HashMap<>();
            factors.put("airPollution", 0.7);
            factors.put("waterPollution", 0.5);
            factors.put("noisePollution", 0.6);
            factors.put("wasteGeneration", 0.4);
            factors.put("energyConsumption", 0.3);

            // Calculate the environmental impact score
            double impactScore = calculateImpactScore(factors);

            // Output the result
            System.out.println("Environmental Impact Score: " + impactScore);
        } catch (IllegalArgumentException e) {
            // Handle invalid input
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```
