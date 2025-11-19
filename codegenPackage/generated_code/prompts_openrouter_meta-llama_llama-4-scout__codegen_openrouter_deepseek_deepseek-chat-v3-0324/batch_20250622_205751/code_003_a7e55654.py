"""
Generated Code Metadata:
========================
Original URL: https://kataskeui.gr
Prompt: Create a Java application to calculate the energy performance certificate (ΠΕΑ) for a building, classifying it into one of the nine energy categories (from Α+ to Η).
Generated: DETERMINISTIC_a7e5565441e15514
Batch ID: 20250622_205751
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

public class PEACalculator {

    // Constants for energy category thresholds (kWh/m²/year)
    private static final Map<String, Double> ENERGY_CATEGORIES = new HashMap<>();
    static {
        ENERGY_CATEGORIES.put("A+", 25.0);
        ENERGY_CATEGORIES.put("A", 50.0);
        ENERGY_CATEGORIES.put("B", 75.0);
        ENERGY_CATEGORIES.put("C", 100.0);
        ENERGY_CATEGORIES.put("D", 150.0);
        ENERGY_CATEGORIES.put("E", 200.0);
        ENERGY_CATEGORIES.put("F", 300.0);
        ENERGY_CATEGORIES.put("G", 400.0);
        ENERGY_CATEGORIES.put("H", Double.MAX_VALUE);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        try {
            System.out.println("=== PEA Calculator ===");
            
            // Get building details
            System.out.print("Enter total annual energy consumption (kWh): ");
            double totalEnergy = getValidDoubleInput(scanner);
            
            System.out.print("Enter total building area (m²): ");
            double area = getValidDoubleInput(scanner);
            
            if (area <= 0) {
                throw new IllegalArgumentException("Building area must be greater than zero");
            }
            
            // Calculate energy performance
            double energyPerformance = totalEnergy / area;
            String category = determineEnergyCategory(energyPerformance);
            
            // Display results
            System.out.println("\n=== Results ===");
            System.out.printf("Energy Performance: %.2f kWh/m²/year%n", energyPerformance);
            System.out.println("Energy Category: " + category);
            
        } catch (Exception e) {
            System.err.println("Error: " + e.getMessage());
        } finally {
            scanner.close();
        }
    }

    private static double getValidDoubleInput(Scanner scanner) {
        while (true) {
            try {
                double value = Double.parseDouble(scanner.nextLine());
                if (value < 0) {
                    throw new IllegalArgumentException("Value cannot be negative");
                }
                return value;
            } catch (NumberFormatException e) {
                System.out.print("Invalid input. Please enter a valid number: ");
            }
        }
    }

    private static String determineEnergyCategory(double energyPerformance) {
        if (energyPerformance <= ENERGY_CATEGORIES.get("A+")) {
            return "A+";
        } else if (energyPerformance <= ENERGY_CATEGORIES.get("A")) {
            return "A";
        } else if (energyPerformance <= ENERGY_CATEGORIES.get("B")) {
            return "B";
        } else if (energyPerformance <= ENERGY_CATEGORIES.get("C")) {
            return "C";
        } else if (energyPerformance <= ENERGY_CATEGORIES.get("D")) {
            return "D";
        } else if (energyPerformance <= ENERGY_CATEGORIES.get("E")) {
            return "E";
        } else if (energyPerformance <= ENERGY_CATEGORIES.get("F")) {
            return "F";
        } else if (energyPerformance <= ENERGY_CATEGORIES.get("G")) {
            return "G";
        } else {
            return "H";
        }
    }
}
```
