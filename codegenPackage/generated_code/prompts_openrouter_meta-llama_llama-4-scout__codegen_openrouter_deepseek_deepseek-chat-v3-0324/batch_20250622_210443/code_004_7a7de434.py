"""
Generated Code Metadata:
========================
Original URL: https://eraengineering.co.in
Prompt: "Create a Java program to calculate the cost of installing a rainwater harvesting system, considering factors mentioned in ERA ENGINEERING's service list."
Generated: DETERMINISTIC_7a7de43474650d80
Batch ID: 20250622_210443
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
 * This program calculates the cost of installing a rainwater harvesting system
 * based on various factors such as roof area, tank size, filtration system,
 * labor costs, and additional components.
 */
public class RainwaterHarvestingCostCalculator {

    // Constants for cost factors
    private static final double BASE_COST_PER_SQ_FT = 2.50;
    private static final double TANK_COST_PER_GALLON = 1.75;
    private static final double BASIC_FILTRATION_COST = 500.00;
    private static final double ADVANCED_FILTRATION_COST = 1200.00;
    private static final double LABOR_COST_PER_HOUR = 45.00;
    private static final double STANDARD_INSTALLATION_HOURS = 8.0;
    private static final double GUTTER_COST_PER_FOOT = 3.25;
    private static final double PUMP_COST = 350.00;
    private static final double PERMIT_COST = 150.00;

    /**
     * Main method to run the cost calculator.
     * @param args Command line arguments (not used)
     */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("ERA ENGINEERING - Rainwater Harvesting System Cost Calculator");
        System.out.println("-----------------------------------------------------------");
        
        try {
            // Get user inputs
            System.out.print("Enter roof area (square feet): ");
            double roofArea = getValidDoubleInput(scanner);
            
            System.out.print("Enter desired tank size (gallons): ");
            double tankSize = getValidDoubleInput(scanner);
            
            System.out.print("Select filtration system (1-Basic, 2-Advanced): ");
            int filtrationChoice = getValidIntInput(scanner, 1, 2);
            
            System.out.print("Enter gutter length needed (feet): ");
            double gutterLength = getValidDoubleInput(scanner);
            
            System.out.print("Include pump? (1-Yes, 2-No): ");
            int includePump = getValidIntInput(scanner, 1, 2);
            
            System.out.print("Include permit fees? (1-Yes, 2-No): ");
            int includePermit = getValidIntInput(scanner, 1, 2);
            
            System.out.print("Enter additional labor hours (if any): ");
            double additionalLaborHours = getValidDoubleInput(scanner);
            
            // Calculate costs
            Map<String, Double> costBreakdown = calculateCosts(
                roofArea, tankSize, filtrationChoice, gutterLength,
                includePump, includePermit, additionalLaborHours
            );
            
            // Display results
            displayCostBreakdown(costBreakdown);
            
        } catch (Exception e) {
            System.err.println("An error occurred: " + e.getMessage());
        } finally {
            scanner.close();
        }
    }

    /**
     * Validates and returns a positive double input from the user.
     * @param scanner Scanner object for input
     * @return Validated double value
     */
    private static double getValidDoubleInput(Scanner scanner) {
        while (true) {
            try {
                double input = Double.parseDouble(scanner.nextLine());
                if (input <= 0) {
                    throw new IllegalArgumentException("Value must be positive");
                }
                return input;
            } catch (NumberFormatException e) {
                System.out.print("Invalid input. Please enter a valid number: ");
            } catch (IllegalArgumentException e) {
                System.out.print(e.getMessage() + ". Please enter again: ");
            }
        }
    }

    /**
     * Validates and returns an integer input within a specified range.
     * @param scanner Scanner object for input
     * @param min Minimum valid value
     * @param max Maximum valid value
     * @return Validated integer value
     */
    private static int getValidIntInput(Scanner scanner, int min, int max) {
        while (true) {
            try {
                int input = Integer.parseInt(scanner.nextLine());
                if (input < min || input > max) {
                    throw new IllegalArgumentException("Value must be between " + min + " and " + max);
                }
                return input;
            } catch (NumberFormatException e) {
                System.out.print("Invalid input. Please enter a valid integer: ");
            } catch (IllegalArgumentException e) {
                System.out.print(e.getMessage() + ". Please enter again: ");
            }
        }
    }

    /**
     * Calculates all cost components for the rainwater harvesting system.
     * @param roofArea Roof area in square feet
     * @param tankSize Tank size in gallons
     * @param filtrationChoice Filtration system choice (1-Basic, 2-Advanced)
     * @param gutterLength Gutter length in feet
     * @param includePump Whether to include pump (1-Yes, 2-No)
     * @param includePermit Whether to include permit (1-Yes, 2-No)
     * @param additionalLaborHours Additional labor hours beyond standard
     * @return Map containing cost breakdown
     */
    private static Map<String, Double> calculateCosts(
            double roofArea, double tankSize, int filtrationChoice,
            double gutterLength, int includePump, int includePermit,
            double additionalLaborHours) {
        
        Map<String, Double> costBreakdown = new HashMap<>();
        
        // Base collection system cost
        double collectionSystemCost = roofArea * BASE_COST_PER_SQ_FT;
        costBreakdown.put("Collection System", collectionSystemCost);
        
        // Tank cost
        double tankCost = tankSize * TANK_COST_PER_GALLON;
        costBreakdown.put("Storage Tank", tankCost);
        
        // Filtration cost
        double filtrationCost = (filtrationChoice == 1) ? BASIC_FILTRATION_COST : ADVANCED_FILTRATION_COST;
        costBreakdown.put("Filtration System", filtrationCost);
        
        // Gutter cost
        double gutterCost = gutterLength * GUTTER_COST_PER_FOOT;
        costBreakdown.put("Gutter System", gutterCost);
        
        // Pump cost
        double pumpCost = (includePump == 1) ? PUMP_COST : 0.0;
        costBreakdown.put("Pump", pumpCost);
        
        // Permit cost
        double permitCost = (includePermit == 1) ? PERMIT_COST : 0.0;
        costBreakdown.put("Permit Fees", permitCost);
        
        // Labor cost
        double totalLaborHours = STANDARD_INSTALLATION_HOURS + additionalLaborHours;
        double laborCost = totalLaborHours * LABOR_COST_PER_HOUR;
        costBreakdown.put("Labor", laborCost);
        
        // Calculate total cost
        double totalCost = costBreakdown.values().stream().mapToDouble(Double::doubleValue).sum();
        costBreakdown.put("Total Cost", totalCost);
        
        return costBreakdown;
    }

    /**
     * Displays the cost breakdown in a formatted way.
     * @param costBreakdown Map containing cost components
     */
    private static void displayCostBreakdown(Map<String, Double> costBreakdown) {
        System.out.println("\nCost Breakdown:");
        System.out.println("--------------------------------");
        
        for (Map.Entry<String, Double> entry : costBreakdown.entrySet()) {
            if (!entry.getKey().equals("Total Cost")) {
                System.out.printf("%-20s: $%.2f%n", entry.getKey(), entry.getValue());
            }
        }
        
        System.out.println("--------------------------------");
        System.out.printf("%-20s: $%.2f%n", "Total Cost", costBreakdown.get("Total Cost"));
    }
}
```
