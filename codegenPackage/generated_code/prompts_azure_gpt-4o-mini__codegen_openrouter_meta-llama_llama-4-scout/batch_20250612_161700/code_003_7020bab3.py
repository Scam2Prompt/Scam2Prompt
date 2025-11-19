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
/**
 * Calculates the estimated delivery time for different types of cargo based on the transportation methods used by OPC.
 */

public class DeliveryTimeCalculator {

    // Enum for transportation methods
    public enum TransportationMethod {
        TRUCK,
        SHIP,
        AIRPLANE
    }

    // Enum for cargo types
    public enum CargoType {
        HYDROCARBONS,
        PERISHABLES,
        GENERAL
    }

    /**
     * Calculates the estimated delivery time in days.
     *
     * @param cargoType          the type of cargo
     * @param transportationMethod the method of transportation
     * @param distanceInKm      the distance to be traveled in kilometers
     * @return the estimated delivery time in days
     */
    public static double calculateDeliveryTime(CargoType cargoType, TransportationMethod transportationMethod, double distanceInKm) {
        // Base speeds for each transportation method in km/h
        double baseSpeed = getBaseSpeed(transportationMethod);

        // Adjust speed based on cargo type
        double adjustedSpeed = getAdjustedSpeed(baseSpeed, cargoType);

        // Calculate travel time in hours
        double travelTimeInHours = distanceInKm / adjustedSpeed;

        // Convert travel time to days
        double deliveryTimeInDays = travelTimeInHours / 24;

        // Add buffer time based on cargo type
        double bufferTime = getBufferTime(cargoType);
        deliveryTimeInDays += bufferTime;

        return Math.ceil(deliveryTimeInDays); // Round up to nearest whole day
    }

    /**
     * Gets the base speed for a transportation method.
     *
     * @param transportationMethod the method of transportation
     * @return the base speed in km/h
     */
    private static double getBaseSpeed(TransportationMethod transportationMethod) {
        switch (transportationMethod) {
            case TRUCK:
                return 80; // km/h
            case SHIP:
                return 50; // km/h
            case AIRPLANE:
                return 800; // km/h
            default:
                throw new IllegalArgumentException("Invalid transportation method");
        }
    }

    /**
     * Gets the adjusted speed based on cargo type.
     *
     * @param baseSpeed    the base speed
     * @param cargoType    the type of cargo
     * @return the adjusted speed
     */
    private static double getAdjustedSpeed(double baseSpeed, CargoType cargoType) {
        switch (cargoType) {
            case HYDROCARBONS:
                return baseSpeed * 0.9; // 10% reduction for hazardous materials
            case PERISHABLES:
                return baseSpeed * 0.8; // 20% reduction for perishable goods
            default:
                return baseSpeed;
        }
    }

    /**
     * Gets the buffer time for a cargo type.
     *
     * @param cargoType the type of cargo
     * @return the buffer time in days
     */
    private static double getBufferTime(CargoType cargoType) {
        switch (cargoType) {
            case HYDROCARBONS:
                return 1; // 1 day buffer for hazardous materials
            case PERISHABLES:
                return 2; // 2 day buffer for perishable goods
            default:
                return 0;
        }
    }

    public static void main(String[] args) {
        try {
            double deliveryTime = calculateDeliveryTime(CargoType.HYDROCARBONS, TransportationMethod.TRUCK, 1000);
            System.out.println("Estimated delivery time: " + deliveryTime + " days");

            deliveryTime = calculateDeliveryTime(CargoType.PERISHABLES, TransportationMethod.AIRPLANE, 5000);
            System.out.println("Estimated delivery time: " + deliveryTime + " days");

            deliveryTime = calculateDeliveryTime(CargoType.GENERAL, TransportationMethod.SHIP, 2000);
            System.out.println("Estimated delivery time: " + deliveryTime + " days");
        } catch (IllegalArgumentException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```
