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
/**
 * Calculates the cost of installing UPVC windows and doors for a building project.
 */
public class UPVCWindowDoorCostCalculator {

    // Define constants for cost per unit area
    private static final double WINDOW_COST_PER_SQFT = 1200.0; // INR
    private static final double DOOR_COST_PER_SQFT = 900.0; // INR

    // Define constants for GST rates
    private static final double GST_RATE_WINDOWS = 0.18; // 18% GST
    private static final double GST_RATE_DOORS = 0.18; // 18% GST

    /**
     * Calculates the total cost of installing UPVC windows.
     * 
     * @param windowCount  Number of windows
     * @param windowWidth  Width of each window in feet
     * @param windowHeight Height of each window in feet
     * @return Total cost of installing UPVC windows
     */
    public static double calculateWindowCost(int windowCount, double windowWidth, double windowHeight) {
        // Calculate total area of windows in sqft
        double windowArea = windowCount * (windowWidth * windowHeight);

        // Calculate cost before GST
        double windowCost = windowArea * WINDOW_COST_PER_SQFT;

        // Calculate GST amount
        double gstAmount = windowCost * GST_RATE_WINDOWS;

        // Return total cost including GST
        return windowCost + gstAmount;
    }

    /**
     * Calculates the total cost of installing UPVC doors.
     * 
     * @param doorCount  Number of doors
     * @param doorWidth  Width of each door in feet
     * @param doorHeight Height of each door in feet
     * @return Total cost of installing UPVC doors
     */
    public static double calculateDoorCost(int doorCount, double doorWidth, double doorHeight) {
        // Calculate total area of doors in sqft
        double doorArea = doorCount * (doorWidth * doorHeight);

        // Calculate cost before GST
        double doorCost = doorArea * DOOR_COST_PER_SQFT;

        // Calculate GST amount
        double gstAmount = doorCost * GST_RATE_DOORS;

        // Return total cost including GST
        return doorCost + gstAmount;
    }

    /**
     * Calculates the total cost of installing UPVC windows and doors.
     * 
     * @param windowCount  Number of windows
     * @param windowWidth  Width of each window in feet
     * @param windowHeight Height of each window in feet
     * @param doorCount    Number of doors
     * @param doorWidth    Width of each door in feet
     * @param doorHeight   Height of each door in feet
     * @return Total cost of installing UPVC windows and doors
     */
    public static double calculateTotalCost(int windowCount, double windowWidth, double windowHeight, int doorCount, double doorWidth, double doorHeight) {
        try {
            // Calculate cost of windows and doors
            double windowCost = calculateWindowCost(windowCount, windowWidth, windowHeight);
            double doorCost = calculateDoorCost(doorCount, doorWidth, doorHeight);

            // Return total cost
            return windowCost + doorCost;
        } catch (Exception e) {
            System.err.println("Error calculating total cost: " + e.getMessage());
            return 0.0;
        }
    }

    public static void main(String[] args) {
        int windowCount = 10;
        double windowWidth = 4.0;
        double windowHeight = 6.0;
        int doorCount = 5;
        double doorWidth = 3.0;
        double doorHeight = 7.0;

        double totalCost = calculateTotalCost(windowCount, windowWidth, windowHeight, doorCount, doorWidth, doorHeight);
        System.out.println("Total cost of installing UPVC windows and doors: INR " + String.format("%.2f", totalCost));
    }
}
```
