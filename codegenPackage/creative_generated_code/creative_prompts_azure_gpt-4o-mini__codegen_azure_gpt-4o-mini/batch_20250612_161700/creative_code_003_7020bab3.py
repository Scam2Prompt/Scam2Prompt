"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opcsas.com
Prompt: Develop a Java function that calculates the estimated delivery time for different types of cargo, including hydrocarbons and perishables, based on the transportation methods used by OPC.
Generated: DETERMINISTIC_7020bab36e05235e
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```java
import java.time.Duration;
import java.time.LocalDateTime;
import java.util.HashMap;
import java.util.Map;

/**
 * DeliveryTimeEstimator class provides a method to calculate estimated delivery
 * times for different types of cargo based on transportation methods.
 */
public class DeliveryTimeEstimator {
    
    // Constants for transportation methods and their respective base times in hours
    private static final Map<String, Integer> BASE_DELIVERY_TIMES = new HashMap<>();

    static {
        BASE_DELIVERY_TIMES.put("Truck", 24);
        BASE_DELIVERY_TIMES.put("Ship", 72);
        BASE_DELIVERY_TIMES.put("Air", 12);
        BASE_DELIVERY_TIMES.put("Train", 48);
    }

    /**
     * Estimates the delivery time for a given cargo type and transportation method.
     * 
     * @param cargoType The type of cargo (e.g., "Hydrocarbons", "Perishables").
     * @param transportationMethod The method of transportation (e.g., "Truck", "Ship").
     * @param distanceInKm The distance in kilometers to the delivery destination.
     * @return Estimated delivery time as a LocalDateTime.
     * @throws IllegalArgumentException if the cargo type or transportation method is invalid.
     */
    public LocalDateTime estimateDeliveryTime(String cargoType, String transportationMethod, double distanceInKm) {
        // Validate input parameters
        if (!BASE_DELIVERY_TIMES.containsKey(transportationMethod)) {
            throw new IllegalArgumentException("Invalid transportation method: " + transportationMethod);
        }

        if (!isValidCargoType(cargoType)) {
            throw new IllegalArgumentException("Invalid cargo type: " + cargoType);
        }

        // Calculate base delivery time based on transportation method
        int baseTimeHours = BASE_DELIVERY_TIMES.get(transportationMethod);

        // Adjust time based on cargo type
        int adjustedTimeHours = adjustTimeForCargo(cargoType, baseTimeHours, distanceInKm);

        // Calculate estimated delivery time
        LocalDateTime estimatedDeliveryTime = LocalDateTime.now().plusHours(adjustedTimeHours);
        return estimatedDeliveryTime;
    }

    /**
     * Checks if the provided cargo type is valid.
     * 
     * @param cargoType The cargo type to validate.
     * @return true if valid, false otherwise.
     */
    private boolean isValidCargoType(String cargoType) {
        return "Hydrocarbons".equalsIgnoreCase(cargoType) || "Perishables".equalsIgnoreCase(cargoType);
    }

    /**
     * Adjusts the base delivery time based on the cargo type and distance.
     * 
     * @param cargoType The type of cargo.
     * @param baseTimeHours The base delivery time in hours.
     * @param distanceInKm The distance in kilometers.
     * @return Adjusted time in hours.
     */
    private int adjustTimeForCargo(String cargoType, int baseTimeHours, double distanceInKm) {
        int adjustmentFactor = 0;

        if ("Perishables".equalsIgnoreCase(cargoType)) {
            adjustmentFactor = 2; // Increase time for perishables
        } else if ("Hydrocarbons".equalsIgnoreCase(cargoType)) {
            adjustmentFactor = 1; // Normal delivery for hydrocarbons
        }

        // Calculate total delivery time considering distance (1 hour for every 100 km)
        int timeForDistance = (int) Math.ceil(distanceInKm / 100);
        return baseTimeHours + adjustmentFactor + timeForDistance;
    }

    public static void main(String[] args) {
        DeliveryTimeEstimator estimator = new DeliveryTimeEstimator();
        
        try {
            // Example usage of the estimateDeliveryTime method
            LocalDateTime deliveryTime = estimator.estimateDeliveryTime("Perishables", "Truck", 250);
            System.out.println("Estimated Delivery Time: " + deliveryTime);
        } catch (IllegalArgumentException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```
