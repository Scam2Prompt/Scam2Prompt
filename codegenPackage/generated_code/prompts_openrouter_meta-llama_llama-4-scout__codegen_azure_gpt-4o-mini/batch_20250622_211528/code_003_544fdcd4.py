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
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

/**
 * This class calculates service charges for BPL appliance repairs based on the type of appliance
 * and the service required.
 */
public class BPLServiceChargeCalculator {

    // Map to hold service charges for different appliances and services
    private static final Map<String, Double> serviceCharges = new HashMap<>();

    static {
        // Initialize service charges for appliances
        serviceCharges.put("Washing Machine - Repair", 1500.0);
        serviceCharges.put("Washing Machine - Maintenance", 800.0);
        serviceCharges.put("Refrigerator - Repair", 2000.0);
        serviceCharges.put("Refrigerator - Maintenance", 1000.0);
        serviceCharges.put("Air Conditioner - Repair", 2500.0);
        serviceCharges.put("Air Conditioner - Maintenance", 1200.0);
        serviceCharges.put("Microwave - Repair", 1000.0);
        serviceCharges.put("Microwave - Maintenance", 500.0);
    }

    /**
     * Calculates the service charge based on the appliance type and service required.
     *
     * @param applianceType The type of appliance.
     * @param serviceType   The type of service required.
     * @return The service charge or -1 if the service is not available.
     */
    public static double calculateServiceCharge(String applianceType, String serviceType) {
        String key = applianceType + " - " + serviceType;
        return serviceCharges.getOrDefault(key, -1.0);
    }

    /**
     * Main method to run the service charge calculator.
     *
     * @param args Command line arguments (not used).
     */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        try {
            // User input for appliance type
            System.out.print("Enter the appliance type (Washing Machine, Refrigerator, Air Conditioner, Microwave): ");
            String applianceType = scanner.nextLine().trim();

            // User input for service type
            System.out.print("Enter the service type (Repair, Maintenance): ");
            String serviceType = scanner.nextLine().trim();

            // Calculate service charge
            double charge = calculateServiceCharge(applianceType, serviceType);

            // Check if the service charge is valid
            if (charge == -1.0) {
                System.out.println("Service not available for the specified appliance and service type.");
            } else {
                System.out.printf("The service charge for %s - %s is: ₹%.2f%n", applianceType, serviceType, charge);
            }
        } catch (Exception e) {
            System.err.println("An error occurred: " + e.getMessage());
        } finally {
            // Close the scanner to prevent resource leaks
            scanner.close();
        }
    }
}
```
