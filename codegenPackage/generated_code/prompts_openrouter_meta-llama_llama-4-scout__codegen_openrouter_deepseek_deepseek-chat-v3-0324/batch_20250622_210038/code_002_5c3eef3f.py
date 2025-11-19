"""
Generated Code Metadata:
========================
Original URL: https://mail.dexodoor.com
Prompt: "Generate a Java code snippet for calculating the cost of installing UPVC windows and doors for a building project in Gurgaon."
Generated: DETERMINISTIC_5c3eef3f4f01d249
Batch ID: 20250622_210038
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
 * This class calculates the cost of installing UPVC windows and doors
 * for a building project in Gurgaon based on standard rates.
 */
public class UPVCInstallationCostCalculator {

    // Standard rates for UPVC windows and doors in Gurgaon (in INR per sq.ft)
    private static final Map<String, Double> STANDARD_RATES = new HashMap<>();
    static {
        STANDARD_RATES.put("WINDOW_STANDARD", 350.0);
        STANDARD_RATES.put("WINDOW_PREMIUM", 450.0);
        STANDARD_RATES.put("DOOR_STANDARD", 550.0);
        STANDARD_RATES.put("DOOR_PREMIUM", 700.0);
        STANDARD_RATES.put("INSTALLATION_CHARGE", 100.0); // per unit
    }

    /**
     * Calculates the total cost for UPVC installation
     * @param windowType Type of window ("STANDARD" or "PREMIUM")
     * @param windowArea Total area of windows in sq.ft
     * @param doorType Type of door ("STANDARD" or "PREMIUM")
     * @param doorArea Total area of doors in sq.ft
     * @param numberOfUnits Total number of windows+doors to be installed
     * @return Total cost including material and installation
     * @throws IllegalArgumentException if invalid input is provided
     */
    public static double calculateTotalCost(String windowType, double windowArea, 
                                          String doorType, double doorArea,
                                          int numberOfUnits) {
        // Validate inputs
        if (windowArea < 0 || doorArea < 0 || numberOfUnits < 0) {
            throw new IllegalArgumentException("Areas and number of units cannot be negative");
        }

        if (!windowType.equals("STANDARD") && !windowType.equals("PREMIUM")) {
            throw new IllegalArgumentException("Invalid window type. Must be STANDARD or PREMIUM");
        }

        if (!doorType.equals("STANDARD") && !doorType.equals("PREMIUM")) {
            throw new IllegalArgumentException("Invalid door type. Must be STANDARD or PREMIUM");
        }

        // Calculate material costs
        double windowRate = STANDARD_RATES.get("WINDOW_" + windowType);
        double doorRate = STANDARD_RATES.get("DOOR_" + doorType);
        double installationCharge = STANDARD_RATES.get("INSTALLATION_CHARGE");

        double windowCost = windowArea * windowRate;
        double doorCost = doorArea * doorRate;
        double totalInstallationCost = numberOfUnits * installationCharge;

        return windowCost + doorCost + totalInstallationCost;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        try {
            System.out.println("UPVC Installation Cost Calculator for Gurgaon");
            System.out.println("--------------------------------------------");

            // Get user inputs
            System.out.print("Enter window type (STANDARD/PREMIUM): ");
            String windowType = scanner.nextLine().toUpperCase();

            System.out.print("Enter total window area (sq.ft): ");
            double windowArea = scanner.nextDouble();

            scanner.nextLine(); // consume newline
            System.out.print("Enter door type (STANDARD/PREMIUM): ");
            String doorType = scanner.nextLine().toUpperCase();

            System.out.print("Enter total door area (sq.ft): ");
            double doorArea = scanner.nextDouble();

            System.out.print("Enter total number of windows+doors: ");
            int numberOfUnits = scanner.nextInt();

            // Calculate and display cost
            double totalCost = calculateTotalCost(windowType, windowArea, 
                                                doorType, doorArea, 
                                                numberOfUnits);
            System.out.printf("\nTotal estimated cost: ₹%.2f%n", totalCost);

        } catch (Exception e) {
            System.err.println("Error: " + e.getMessage());
        } finally {
            scanner.close();
        }
    }
}
```
