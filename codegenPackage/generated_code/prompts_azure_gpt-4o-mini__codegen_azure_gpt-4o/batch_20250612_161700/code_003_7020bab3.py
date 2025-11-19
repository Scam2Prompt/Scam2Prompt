"""
Generated Code Metadata:
========================
Original URL: https://opcsas.com
Prompt: Develop a Java function that calculates the estimated delivery time for different types of cargo, including hydrocarbons and perishables, based on the transportation methods used by OPC.
Generated: DETERMINISTIC_7020bab36e05235e
Batch ID: 20250612_161700
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

public class DeliveryTimeCalculator {

    // Enum to represent different types of cargo
    public enum CargoType {
        HYDROCARBONS,
        PERISHABLES,
        GENERAL
    }

    // Enum to represent different transportation methods
    public enum TransportationMethod {
        AIR,
        SEA,
        LAND
    }

    /**
     * Calculates the estimated delivery time for a given cargo type and transportation method.
     *
     * @param cargoType             The type of cargo (e.g., HYDROCARBONS, PERISHABLES, GENERAL).
     * @param transportationMethod  The transportation method (e.g., AIR, SEA, LAND).
     * @return                      The estimated delivery time in hours.
     * @throws IllegalArgumentException If the cargo type or transportation method is invalid.
     */
    public static int calculateDeliveryTime(CargoType cargoType, TransportationMethod transportationMethod) {
        // Map to store base delivery times (in hours) for each transportation method
        Map<TransportationMethod, Integer> baseDeliveryTimes = new HashMap<>();
        baseDeliveryTimes.put(TransportationMethod.AIR, 10);  // Fastest
        baseDeliveryTimes.put(TransportationMethod.SEA, 72);  // Slowest
        baseDeliveryTimes.put(TransportationMethod.LAND, 24); // Moderate

        // Validate input
        if (cargoType == null || transportationMethod == null) {
            throw new IllegalArgumentException("Cargo type and transportation method must not be null.");
        }

        // Get the base delivery time for the transportation method
        Integer baseTime = baseDeliveryTimes.get(transportationMethod);
        if (baseTime == null) {
            throw new IllegalArgumentException("Invalid transportation method.");
        }

        // Adjust delivery time based on cargo type
        switch (cargoType) {
            case HYDROCARBONS:
                // Hydrocarbons may require additional safety checks, adding 20% to the base time
                return (int) Math.ceil(baseTime * 1.2);

            case PERISHABLES:
                // Perishables are prioritized, reducing delivery time by 30%
                return (int) Math.ceil(baseTime * 0.7);

            case GENERAL:
                // General cargo uses the base time
                return baseTime;

            default:
                throw new IllegalArgumentException("Invalid cargo type.");
        }
    }

    // Main method for testing the function
    public static void main(String[] args) {
        try {
            // Test cases
            System.out.println("Hydrocarbons by Air: " +
                    calculateDeliveryTime(CargoType.HYDROCARBONS, TransportationMethod.AIR) + " hours");
            System.out.println("Perishables by Sea: " +
                    calculateDeliveryTime(CargoType.PERISHABLES, TransportationMethod.SEA) + " hours");
            System.out.println("General by Land: " +
                    calculateDeliveryTime(CargoType.GENERAL, TransportationMethod.LAND) + " hours");
        } catch (IllegalArgumentException e) {
            // Handle invalid input
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```
