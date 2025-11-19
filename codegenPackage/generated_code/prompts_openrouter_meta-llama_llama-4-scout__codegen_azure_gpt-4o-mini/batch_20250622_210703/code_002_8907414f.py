"""
Generated Code Metadata:
========================
Original URL: https://ajfpkpackagingcompany.ajfpak.com
Prompt: Generate a Java code snippet to implement a "Get a Quote" feature for AJF Group of Companies' delivery services.
Generated: DETERMINISTIC_8907414f97d62e09
Batch ID: 20250622_210703
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
 * This class represents a service to get delivery quotes for AJF Group of Companies.
 */
public class DeliveryQuoteService {

    // A map to hold the base rates for different delivery types
    private static final Map<String, Double> deliveryRates = new HashMap<>();

    static {
        // Initialize delivery rates for different types of services
        deliveryRates.put("standard", 5.00);
        deliveryRates.put("express", 10.00);
        deliveryRates.put("overnight", 20.00);
    }

    /**
     * Calculates the delivery quote based on the type of service and distance.
     *
     * @param serviceType The type of delivery service (e.g., standard, express, overnight)
     * @param distance    The distance in miles for the delivery
     * @return The calculated quote or an error message if the input is invalid
     */
    public String getQuote(String serviceType, double distance) {
        // Validate input parameters
        if (distance < 0) {
            return "Error: Distance cannot be negative.";
        }

        Double baseRate = deliveryRates.get(serviceType.toLowerCase());
        if (baseRate == null) {
            return "Error: Invalid service type. Please choose from: standard, express, overnight.";
        }

        // Calculate the total quote
        double totalQuote = baseRate + (distance * 0.5); // $0.5 per mile
        return String.format("The delivery quote for %s service over %.2f miles is: $%.2f",
                serviceType, distance, totalQuote);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        DeliveryQuoteService quoteService = new DeliveryQuoteService();

        try {
            // User input for service type
            System.out.print("Enter delivery service type (standard, express, overnight): ");
            String serviceType = scanner.nextLine();

            // User input for distance
            System.out.print("Enter delivery distance in miles: ");
            double distance = scanner.nextDouble();

            // Get and display the quote
            String quote = quoteService.getQuote(serviceType, distance);
            System.out.println(quote);
        } catch (Exception e) {
            System.err.println("An error occurred: " + e.getMessage());
        } finally {
            scanner.close(); // Ensure the scanner is closed to prevent resource leaks
        }
    }
}
```
