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
import java.util.Scanner;

/**
 * Class to calculate the total cost of construction projects.
 */
public class ConstructionCostCalculator {

    // Constants for cost categories
    private static final String LABOR = "Labor";
    private static final String MATERIALS = "Materials";
    private static final String EQUIPMENT = "Equipment";

    // Map to store costs for each category
    private Map<String, Double> costs;

    /**
     * Constructor to initialize the costs map.
     */
    public ConstructionCostCalculator() {
        costs = new HashMap<>();
        costs.put(LABOR, 0.0);
        costs.put(MATERIALS, 0.0);
        costs.put(EQUIPMENT, 0.0);
    }

    /**
     * Method to set the cost for a specific category.
     *
     * @param category The category of cost (Labor, Materials, Equipment)
     * @param amount   The amount to set for the category
     * @throws IllegalArgumentException if the category is invalid
     */
    public void setCost(String category, double amount) {
        if (!costs.containsKey(category)) {
            throw new IllegalArgumentException("Invalid cost category: " + category);
        }
        costs.put(category, amount);
    }

    /**
     * Method to calculate the total cost of the project.
     *
     * @return The total cost as a double
     */
    public double calculateTotalCost() {
        return costs.values().stream().mapToDouble(Double::doubleValue).sum();
    }

    /**
     * Main method to run the cost calculator.
     *
     * @param args Command line arguments
     */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ConstructionCostCalculator calculator = new ConstructionCostCalculator();

        try {
            // Input labor cost
            System.out.print("Enter labor cost: ");
            calculator.setCost(LABOR, scanner.nextDouble());

            // Input materials cost
            System.out.print("Enter materials cost: ");
            calculator.setCost(MATERIALS, scanner.nextDouble());

            // Input equipment cost
            System.out.print("Enter equipment cost: ");
            calculator.setCost(EQUIPMENT, scanner.nextDouble());

            // Calculate and display total cost
            double totalCost = calculator.calculateTotalCost();
            System.out.printf("Total construction cost: %.2f%n", totalCost);
        } catch (IllegalArgumentException e) {
            System.err.println("Error: " + e.getMessage());
        } catch (Exception e) {
            System.err.println("An unexpected error occurred: " + e.getMessage());
        } finally {
            scanner.close();
        }
    }
}
```
