"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gnosisrew.com
Prompt: Create a Java function that calculates the compatibility of various car parts listed on Gnosis Rew's website, focusing on their automotive accessories.
Generated: DETERMINISTIC_0aad0662bf817c4c
Batch ID: 20250612_164205
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```java
import java.util.HashMap;
import java.util.Map;

/**
 * The CompatibilityChecker class provides functionality to calculate compatibility 
 * scores for various car parts based on certain compatibility criteria.
 */
public class CompatibilityChecker {

    // A map to simulate part compatibility data
    private static final Map<String, String[]> compatibilityData = new HashMap<>();

    static {
        // Example compatibility data: part -> compatible parts
        compatibilityData.put("Brake Pads", new String[]{"Rotors", "Calipers"});
        compatibilityData.put("Oil Filter", new String[]{"Oil", "Engine"});
        compatibilityData.put("Wiper Blades", new String[]{"Windshield"});
        // Add more parts and their compatible accessories as needed
    }

    /**
     * Calculates the compatibility score between a requested part and a list of accessory parts.
     *
     * @param part          The part to check compatibility for.
     * @param accessoryParts An array of accessory parts to check against.
     * @return The compatibility score, which is the number of compatible accessories found.
     * @throws IllegalArgumentException if the part is not in the compatibility data.
     */
    public int calculateCompatibility(String part, String[] accessoryParts) {
        if (!compatibilityData.containsKey(part)) {
            throw new IllegalArgumentException("Part not found in compatibility data: " + part);
        }

        String[] compatibleParts = compatibilityData.get(part);
        int score = 0;

        // Check each accessory part against the compatible parts
        for (String accessory : accessoryParts) {
            for (String compatible : compatibleParts) {
                if (accessory.equalsIgnoreCase(compatible)) {
                    score++;
                    break; // No need to check other compatible parts if a match is found
                }
            }
        }

        return score;
    }

    public static void main(String[] args) {
        CompatibilityChecker checker = new CompatibilityChecker();

        // Example usage of the compatibility checker
        String partToCheck = "Brake Pads";
        String[] accessoriesToCheck = {"Rotors", "Windshield", "Calipers"};

        try {
            int compatibilityScore = checker.calculateCompatibility(partToCheck, accessoriesToCheck);
            System.out.println("Compatibility score for " + partToCheck + ": " + compatibilityScore);
        } catch (IllegalArgumentException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```
