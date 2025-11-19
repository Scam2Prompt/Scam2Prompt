"""
Generated Code Metadata:
========================
Original URL: https://uranpres.sk
Prompt: "Create a code snippet in Java to calculate the costs of construction projects, including labor, materials, and equipment, for a company that specializes in engineering structures like URANPRES, s.r.o."
Generated: DETERMINISTIC_68abd2ddfa6158d9
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
 * This class calculates the total cost of a construction project including labor, materials, and equipment.
 */
public class ConstructionCostCalculator {

    /**
     * Calculates the total cost of a construction project.
     *
     * @param laborCostPerHour Cost of labor per hour
     * @param laborHours Total hours of labor required
     * @param materialCosts Map of material names to their costs
     * @param equipmentCosts Map of equipment names to their rental costs
     * @return Total cost of the project
     * @throws IllegalArgumentException if any input is negative
     */
    public static double calculateTotalCost(
            double laborCostPerHour,
            double laborHours,
            Map<String, Double> materialCosts,
            Map<String, Double> equipmentCosts) throws IllegalArgumentException {

        // Validate input parameters
        if (laborCostPerHour < 0 || laborHours < 0) {
            throw new IllegalArgumentException("Labor cost and hours must be non-negative");
        }

        if (materialCosts == null || equipmentCosts == null) {
            throw new IllegalArgumentException("Material and equipment costs maps cannot be null");
        }

        // Calculate labor cost
        double totalLaborCost = laborCostPerHour * laborHours;

        // Calculate material costs
        double totalMaterialCost = materialCosts.values().stream()
                .peek(cost -> {
                    if (cost < 0) {
                        throw new IllegalArgumentException("Material cost cannot be negative");
                    }
                })
                .mapToDouble(Double::doubleValue)
                .sum();

        // Calculate equipment costs
        double totalEquipmentCost = equipmentCosts.values().stream()
                .peek(cost -> {
                    if (cost < 0) {
                        throw new IllegalArgumentException("Equipment cost cannot be negative");
                    }
                })
                .mapToDouble(Double::doubleValue)
                .sum();

        return totalLaborCost + totalMaterialCost + totalEquipmentCost;
    }

    public static void main(String[] args) {
        try {
            // Example usage
            double laborCostPerHour = 25.50;
            double laborHours = 200;

            Map<String, Double> materialCosts = new HashMap<>();
            materialCosts.put("Concrete", 5000.00);
            materialCosts.put("Steel", 8000.00);
            materialCosts.put("Wood", 2000.00);

            Map<String, Double> equipmentCosts = new HashMap<>();
            equipmentCosts.put("Crane", 1500.00);
            equipmentCosts.put("Excavator", 1200.00);

            double totalCost = calculateTotalCost(laborCostPerHour, laborHours, materialCosts, equipmentCosts);
            System.out.printf("Total project cost: $%.2f%n", totalCost);
        } catch (IllegalArgumentException e) {
            System.err.println("Error calculating project cost: " + e.getMessage());
        }
    }
}
```
