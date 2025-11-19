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
import java.util.HashMap;
import java.util.Map;

/**
 * A class to calculate moving service costs based on distance, weight, and service type.
 */
public class MovingCostCalculator {

    // Constants for service types
    public static final String CITY_MOVING = "sehir_ici_nakliye";
    public static final String SMALL_ITEM_MOVING = "kucuk_esya_nakliyesi";

    // Base prices for each service type (in Turkish Lira)
    private static final Map<String, Double> BASE_PRICES = new HashMap<>();
    static {
        BASE_PRICES.put(CITY_MOVING, 500.0);       // Base price for city moving
        BASE_PRICES.put(SMALL_ITEM_MOVING, 200.0); // Base price for small item moving
    }

    // Price per kilometer for each service type (in Turkish Lira)
    private static final Map<String, Double> PRICE_PER_KM = new HashMap<>();
    static {
        PRICE_PER_KM.put(CITY_MOVING, 5.0);       // Price per km for city moving
        PRICE_PER_KM.put(SMALL_ITEM_MOVING, 3.0); // Price per km for small item moving
    }

    // Price per kilogram for each service type (in Turkish Lira)
    private static final Map<String, Double> PRICE_PER_KG = new HashMap<>();
    static {
        PRICE_PER_KG.put(CITY_MOVING, 2.0);       // Price per kg for city moving
        PRICE_PER_KG.put(SMALL_ITEM_MOVING, 1.5); // Price per kg for small item moving
    }

    /**
     * Calculates the total moving cost based on distance, weight, and service type.
     * 
     * @param distance Distance in kilometers
     * @param weight Weight in kilograms
     * @param serviceType Type of service (use class constants)
     * @return Total cost in Turkish Lira
     * @throws IllegalArgumentException if parameters are invalid
     */
    public static double calculateCost(double distance, double weight, String serviceType) {
        // Validate input parameters
        if (distance <= 0) {
            throw new IllegalArgumentException("Distance must be greater than 0");
        }
        if (weight <= 0) {
            throw new IllegalArgumentException("Weight must be greater than 0");
        }
        if (!BASE_PRICES.containsKey(serviceType)) {
            throw new IllegalArgumentException("Invalid service type");
        }

        // Calculate cost components
        double basePrice = BASE_PRICES.get(serviceType);
        double distanceCost = distance * PRICE_PER_KM.get(serviceType);
        double weightCost = weight * PRICE_PER_KG.get(serviceType);

        // Calculate total cost
        return basePrice + distanceCost + weightCost;
    }

    /**
     * Example usage of the MovingCostCalculator.
     */
    public static void main(String[] args) {
        try {
            // Example calculation for city moving
            double cityMovingCost = calculateCost(10, 500, CITY_MOVING);
            System.out.printf("City moving cost: %.2f TL%n", cityMovingCost);

            // Example calculation for small item moving
            double smallItemCost = calculateCost(5, 100, SMALL_ITEM_MOVING);
            System.out.printf("Small item moving cost: %.2f TL%n", smallItemCost);

        } catch (IllegalArgumentException e) {
            System.err.println("Error calculating cost: " + e.getMessage());
        }
    }
}
```
