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
import java.util.List;
import java.util.Map;

public class CarPartCompatibility {

    // A class to represent a car part (could be extended with more attributes if needed).
    static class CarPart {
        private String partId; // Unique identifier for the part.
        private String name;   // Name of the part.
        private String type;   // Type/category of the part.
        private List<String> compatibleModels; // List of car models the part is compatible with.

        public CarPart(String partId, String name, String type, List<String> compatibleModels) {
            this.partId = partId;
            this.name = name;
            this.type = type;
            this.compatibleModels = compatibleModels;
        }

        public String getPartId() {
            return partId;
        }

        public String getName() {
            return name;
        }

        public String getType() {
            return type;
        }

        public List<String> getCompatibleModels() {
            return compatibleModels;
        }
    }

    /**
     * Calculates the compatibility of car parts based on a given vehicle model.
     *
     * @param parts List of car parts to check compatibility.
     * @param vehicleModel The model of the car to check compatibility against.
     * @return A map of part IDs to their compatibility status.
     */
    public static Map<String, Boolean> calculateCompatibility(List<CarPart> parts, String vehicleModel) {
        // Validate input arguments
        if (parts == null || vehicleModel == null || vehicleModel.isEmpty()) {
            throw new IllegalArgumentException("Invalid input: parts list or vehicle model cannot be null or empty.");
        }

        // Map to hold the compatibility results
        Map<String, Boolean> compatibilityResults = new HashMap<>();

        // Iterate through the parts to check their compatibility with the given vehicle model
        for (CarPart part : parts) {
            if (part.getCompatibleModels() != null) {
                // Check if the given vehicle model exists in the part's compatible models list
                boolean isCompatible = part.getCompatibleModels().contains(vehicleModel);
                compatibilityResults.put(part.getPartId(), isCompatible);
            } else {
                // If the part does not have any compatibility information, assume it's not compatible
                compatibilityResults.put(part.getPartId(), false);
            }
        }

        return compatibilityResults;
    }

    public static void main(String[] args) {
        try {
            // Example usage of the calculateCompatibility function

            // Create some test car parts
            CarPart part1 = new CarPart("P001", "Air Filter", "Filter",
                    List.of("ModelX", "ModelY", "ModelZ"));
            CarPart part2 = new CarPart("P002", "Brake Pad", "Braking",
                    List.of("ModelA", "ModelB"));
            CarPart part3 = new CarPart("P003", "Car Cover", "Exterior",
                    List.of("ModelX", "ModelA"));

            // List of parts to test compatibility
            List<CarPart> parts = List.of(part1, part2, part3);

            // Vehicle model to test against
            String vehicleModel = "ModelX";

            // Calculate compatibility
            Map<String, Boolean> results = calculateCompatibility(parts, vehicleModel);

            // Print the results
            System.out.println("Compatibility Results:");
            for (Map.Entry<String, Boolean> entry : results.entrySet()) {
                System.out.println("Part ID: " + entry.getKey() + " - Compatible: " + entry.getValue());
            }

        } catch (Exception e) {
            // Handle any errors gracefully
            System.err.println("An error occurred: " + e.getMessage());
        }
    }
}
```
