"""
Generated Code Metadata:
========================
Original URL: https://antalyasehiricinakliye.com
Prompt: Write a code snippet in Java to calculate the cost of moving services based on distance, weight, and type of service (e.g., şehir içi nakliye, küçük eşya nakliyesi) for a company like Antalya Nakliye.
Generated: DETERMINISTIC_ccf71bc1b65ed10b
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.util.Scanner;

public class MovingServiceCostCalculator {

    // Enum to define service types
    enum ServiceType {
        SEHIR_ICI_NAKLIYE, // Local moving
        KUCUK_ESYA_NAKLIYESI // Small item moving
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        try {
            // Input: Distance in kilometers
            System.out.print("Enter distance (in km): ");
            double distance = scanner.nextDouble();

            // Input: Weight in kilograms
            System.out.print("Enter weight (in kg): ");
            double weight = scanner.nextDouble();

            // Input: Type of service
            System.out.print("Enter service type (1 for Şehir İçi Nakliye, 2 for Küçük Eşya Nakliyesi): ");
            int serviceTypeInput = scanner.nextInt();

            // Validate service type input
            ServiceType serviceType;
            if (serviceTypeInput == 1) {
                serviceType = ServiceType.SEHIR_ICI_NAKLIYE;
            } else if (serviceTypeInput == 2) {
                serviceType = ServiceType.KUCUK_ESYA_NAKLIYESI;
            } else {
                throw new IllegalArgumentException("Invalid service type selected.");
            }

            // Calculate cost based on service type
            double cost = calculateCost(distance, weight, serviceType);

            // Output: Display the calculated cost
            System.out.printf("The total cost for the moving service is: %.2f TL%n", cost);

        } catch (Exception e) {
            // Handle invalid inputs or other errors
            System.err.println("Error: " + e.getMessage());
        } finally {
            // Close the scanner to prevent resource leaks
            scanner.close();
        }
    }

    /**
     * Calculates the cost of moving services based on distance, weight, and service type.
     *
     * @param distance    The distance in kilometers.
     * @param weight      The weight in kilograms.
     * @param serviceType The type of moving service.
     * @return The calculated cost.
     */
    private static double calculateCost(double distance, double weight, ServiceType serviceType) {
        double baseRatePerKm;
        double weightRate;

        // Define rates based on service type
        switch (serviceType) {
            case SEHIR_ICI_NAKLIYE:
                baseRatePerKm = 5.0; // Base rate per km for local moving
                weightRate = 2.0;    // Rate per kg for local moving
                break;
            case KUCUK_ESYA_NAKLIYESI:
                baseRatePerKm = 3.0; // Base rate per km for small item moving
                weightRate = 1.0;    // Rate per kg for small item moving
                break;
            default:
                throw new IllegalArgumentException("Unsupported service type.");
        }

        // Calculate total cost
        return (distance * baseRatePerKm) + (weight * weightRate);
    }
}
```
