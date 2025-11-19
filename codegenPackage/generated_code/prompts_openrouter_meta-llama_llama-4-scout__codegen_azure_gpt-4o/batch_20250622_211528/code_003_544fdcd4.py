"""
Generated Code Metadata:
========================
Original URL: https://bplservicescenter.com
Prompt: Create a Java program to calculate service charges for BPL appliance repairs based on the type of appliance and service required.
Generated: DETERMINISTIC_544fdcd4ce273826
Batch ID: 20250622_211528
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.util.Scanner;

/**
 * A program to calculate service charges for BPL appliance repairs
 * based on the type of appliance and service required.
 */
public class BPLServiceChargesCalculator {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        try {
            // Display menu for appliance types
            System.out.println("Select Appliance Type:");
            System.out.println("1. Refrigerator");
            System.out.println("2. Washing Machine");
            System.out.println("3. Microwave Oven");
            System.out.println("4. Air Conditioner");
            System.out.print("Enter your choice (1-4): ");
            int applianceType = scanner.nextInt();

            // Validate appliance type input
            if (applianceType < 1 || applianceType > 4) {
                System.out.println("Invalid appliance type selected. Please restart the program.");
                return;
            }

            // Display menu for service types
            System.out.println("\nSelect Service Type:");
            System.out.println("1. General Maintenance");
            System.out.println("2. Minor Repair");
            System.out.println("3. Major Repair");
            System.out.print("Enter your choice (1-3): ");
            int serviceType = scanner.nextInt();

            // Validate service type input
            if (serviceType < 1 || serviceType > 3) {
                System.out.println("Invalid service type selected. Please restart the program.");
                return;
            }

            // Calculate service charges
            double serviceCharge = calculateServiceCharge(applianceType, serviceType);

            // Display the calculated service charge
            System.out.printf("\nThe service charge for your selected options is: ₹%.2f\n", serviceCharge);

        } catch (Exception e) {
            System.out.println("An error occurred. Please ensure you enter valid numeric inputs.");
        } finally {
            scanner.close(); // Close the scanner to release resources
        }
    }

    /**
     * Calculates the service charge based on appliance type and service type.
     *
     * @param applianceType The type of appliance (1-4).
     * @param serviceType   The type of service (1-3).
     * @return The calculated service charge.
     */
    private static double calculateServiceCharge(int applianceType, int serviceType) {
        // Base charges for each appliance type
        double[] applianceBaseCharges = {500, 400, 300, 600}; // Refrigerator, Washing Machine, Microwave Oven, Air Conditioner

        // Multipliers for each service type
        double[] serviceMultipliers = {1.0, 1.5, 2.0}; // General Maintenance, Minor Repair, Major Repair

        // Calculate the service charge
        double baseCharge = applianceBaseCharges[applianceType - 1];
        double multiplier = serviceMultipliers[serviceType - 1];
        return baseCharge * multiplier;
    }
}
```
