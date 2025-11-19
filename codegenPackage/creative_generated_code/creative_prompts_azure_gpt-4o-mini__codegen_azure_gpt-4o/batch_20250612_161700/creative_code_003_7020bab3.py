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
import java.util.HashMap;
import java.util.Map;

public class DeliveryEstimator {

    /**
     * Enum representing different cargo types.
     */
    public enum CargoType {
        HYDROCARBONS, PERISHABLES, GENERAL
    }

    /**
     * Enum representing different transportation methods.
     */
    public enum TransportMethod {
        AIR, SEA, LAND
    }

    /**
     * Method to calculate the estimated delivery time for cargo.
     * 
     * @param cargoType       The type of cargo (e.g., HYDROCARBONS, PERISHABLES, GENERAL).
     * @param transportMethod The transportation method (e.g., AIR, SEA, LAND).
     * @return The estimated delivery time in hours.
     * @throws IllegalArgumentException If an invalid cargo type or transportation method is used.
     */
    public static int calculateDeliveryTime(CargoType cargoType, TransportMethod transportMethod) {
        // Delivery time matrix based on cargo type and transportation method
        Map<CargoType, Map<TransportMethod, Integer>> deliveryTimeMatrix = new HashMap<>();

        // Populate delivery times for hydrocarbons
        Map<TransportMethod, Integer> hydrocarbonsDeliveryTimes = new HashMap<>();
        hydrocarbonsDeliveryTimes.put(TransportMethod.AIR, 24); // 24 hours
        hydrocarbonsDeliveryTimes.put(TransportMethod.SEA, 120); // 120 hours
        hydrocarbonsDeliveryTimes.put(TransportMethod.LAND, 48); // 48 hours
        deliveryTimeMatrix.put(CargoType.HYDROCARBONS, hydrocarbonsDeliveryTimes);

        // Populate delivery times for perishables
        Map<TransportMethod, Integer> perishablesDeliveryTimes = new HashMap<>();
        perishablesDeliveryTimes.put(TransportMethod.AIR, 12); // 12 hours
        perishablesDeliveryTimes.put(TransportMethod.SEA, 72); // 72 hours
        perishablesDeliveryTimes.put(TransportMethod.LAND, 36); // 36 hours
        deliveryTimeMatrix.put(CargoType.PERISHABLES, perishablesDeliveryTimes);

        // Populate delivery times for general cargo
        Map<TransportMethod, Integer> generalDeliveryTimes = new HashMap<>();
        generalDeliveryTimes.put(TransportMethod.AIR, 48); // 48 hours
        generalDeliveryTimes.put(TransportMethod.SEA, 144); // 144 hours
        generalDeliveryTimes.put(TransportMethod.LAND, 60); // 60 hours
        deliveryTimeMatrix.put(CargoType.GENERAL, generalDeliveryTimes);

        // Fetch the delivery time based on cargo type and transportation method
        if (deliveryTimeMatrix.containsKey(cargoType)) {
            Map<TransportMethod, Integer> transportTimes = deliveryTimeMatrix.get(cargoType);
            if (transportTimes.containsKey(transportMethod)) {
                return transportTimes.get(transportMethod);
            } else {
                throw new IllegalArgumentException("Invalid transportation method: " + transportMethod);
            }
        } else {
            throw new IllegalArgumentException("Invalid cargo type: " + cargoType);
        }
    }

    public static void main(String[] args) {
        try {
            // Example usage of the calculateDeliveryTime function
            int deliveryTime = calculateDeliveryTime(CargoType.PERISHABLES, TransportMethod.AIR);
            System.out.println("Estimated delivery time: " + deliveryTime + " hours");
        } catch (IllegalArgumentException e) {
            // Handle invalid input gracefully
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```
