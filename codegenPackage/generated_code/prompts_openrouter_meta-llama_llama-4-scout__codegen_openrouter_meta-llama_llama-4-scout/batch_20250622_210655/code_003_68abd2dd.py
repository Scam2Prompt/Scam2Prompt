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
/**
 * Calculates the costs of construction projects, including labor, materials, and equipment.
 * 
 * @author [Your Name]
 * @version 1.0
 */

// Define an enum for cost categories
enum CostCategory {
    LABOR,
    MATERIALS,
    EQUIPMENT
}

// Define a class for construction project costs
public class ConstructionProjectCosts {

    private double laborCost;
    private double materialsCost;
    private double equipmentCost;

    /**
     * Constructor to initialize costs.
     * 
     * @param laborCost     labor cost
     * @param materialsCost materials cost
     * @param equipmentCost equipment cost
     */
    public ConstructionProjectCosts(double laborCost, double materialsCost, double equipmentCost) {
        this.laborCost = laborCost;
        this.materialsCost = materialsCost;
        this.equipmentCost = equipmentCost;
    }

    /**
     * Calculates the total cost of the construction project.
     * 
     * @return total cost
     */
    public double calculateTotalCost() {
        return laborCost + materialsCost + equipmentCost;
    }

    /**
     * Calculates the cost by category.
     * 
     * @param category cost category
     * @return cost for the given category
     */
    public double calculateCostByCategory(CostCategory category) {
        return switch (category) {
            case LABOR -> laborCost;
            case MATERIALS -> materialsCost;
            case EQUIPMENT -> equipmentCost;
        };
    }

    /**
     * Updates the cost for a specific category.
     * 
     * @param category cost category
     * @param cost     new cost value
     */
    public void updateCost(CostCategory category, double cost) {
        if (cost < 0) {
            throw new IllegalArgumentException("Cost cannot be negative.");
        }

        switch (category) {
            case LABOR -> laborCost = cost;
            case MATERIALS -> materialsCost = cost;
            case EQUIPMENT -> equipmentCost = cost;
        };
    }

    public static void main(String[] args) {
        try {
            // Example usage
            ConstructionProjectCosts projectCosts = new ConstructionProjectCosts(10000, 50000, 20000);

            System.out.println("Total Cost: " + projectCosts.calculateTotalCost());
            System.out.println("Labor Cost: " + projectCosts.calculateCostByCategory(CostCategory.LABOR));
            System.out.println("Materials Cost: " + projectCosts.calculateCostByCategory(CostCategory.MATERIALS));
            System.out.println("Equipment Cost: " + projectCosts.calculateCostByCategory(CostCategory.EQUIPMENT));

            // Update labor cost
            projectCosts.updateCost(CostCategory.LABOR, 12000);
            System.out.println("Updated Total Cost: " + projectCosts.calculateTotalCost());

            // Attempt to update with invalid cost
            projectCosts.updateCost(CostCategory.LABOR, -1000);
        } catch (IllegalArgumentException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```
