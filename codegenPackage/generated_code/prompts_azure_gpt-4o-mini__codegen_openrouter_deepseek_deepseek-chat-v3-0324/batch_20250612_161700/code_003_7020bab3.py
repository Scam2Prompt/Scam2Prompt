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
import java.time.LocalDateTime;
import java.time.temporal.ChronoUnit;
import java.util.HashMap;
import java.util.Map;

/**
 * This class calculates estimated delivery time for different cargo types
 * based on transportation methods used by OPC.
 */
public class DeliveryTimeCalculator {
    
    // Constants for transportation methods
    public static final String TRUCK = "TRUCK";
    public static final String SHIP = "SHIP";
    public static final String TRAIN = "TRAIN";
    public static final String AIR = "AIR";
    
    // Constants for cargo types
    public static final String HYDROCARBON = "HYDROCARBON";
    public static final String PERISHABLE = "PERISHABLE";
    public static final String GENERAL = "GENERAL";
    
    // Base speeds in km/h for each transportation method
    private static final Map<String, Integer> BASE_SPEEDS = new HashMap<>();
    static {
        BASE_SPEEDS.put(TRUCK, 60);
        BASE_SPEEDS.put(SHIP, 30);
        BASE_SPEEDS.put(TRAIN, 80);
        BASE_SPEEDS.put(AIR, 500);
    }
    
    // Speed modifiers for different cargo types (percentage)
    private static final Map<String, Double> CARGO_MODIFIERS = new HashMap<>();
    static {
        CARGO_MODIFIERS.put(HYDROCARBON, 0.8);  // 20% slower due to safety regulations
        CARGO_MODIFIERS.put(PERISHABLE, 1.2);   // 20% faster for perishables
        CARGO_MODIFIERS.put(GENERAL, 1.0);      // No modifier
    }
    
    /**
     * Calculates estimated delivery time based on distance, transportation method, and cargo type.
     * 
     * @param distance Distance in kilometers
     * @param transportMethod Transportation method (TRUCK, SHIP, TRAIN, AIR)
     * @param cargoType Cargo type (HYDROCARBON, PERISHABLE, GENERAL)
     * @param departureTime Time when cargo departs
     * @return Estimated arrival time
     * @throws IllegalArgumentException if invalid parameters are provided
     */
    public static LocalDateTime calculateDeliveryTime(double distance, String transportMethod, 
                                                     String cargoType, LocalDateTime departureTime) 
            throws IllegalArgumentException {
        
        // Validate input parameters
        if (distance <= 0) {
            throw new IllegalArgumentException("Distance must be positive");
        }
        
        if (!BASE_SPEEDS.containsKey(transportMethod)) {
            throw new IllegalArgumentException("Invalid transportation method: " + transportMethod);
        }
        
        if (!CARGO_MODIFIERS.containsKey(cargoType)) {
            throw new IllegalArgumentException("Invalid cargo type: " + cargoType);
        }
        
        if (departureTime == null) {
            throw new IllegalArgumentException("Departure time cannot be null");
        }
        
        // Calculate effective speed considering cargo type
        int baseSpeed = BASE_SPEEDS.get(transportMethod);
        double speedModifier = CARGO_MODIFIERS.get(cargoType);
        double effectiveSpeed = baseSpeed * speedModifier;
        
        // Calculate hours needed (distance / speed)
        double hoursNeeded = distance / effectiveSpeed;
        
        // Additional handling for specific cargo types
        if (cargoType.equals(HYDROCARBON)) {
            // Add mandatory safety checks (2 hours)
            hoursNeeded += 2;
        } else if (cargoType.equals(PERISHABLE)) {
            // No additional time needed
        } else {
            // GENERAL cargo - add standard 1 hour for documentation
            hoursNeeded += 1;
        }
        
        // Convert hours to minutes for more precise calculation
        long minutesToAdd = (long) (hoursNeeded * 60);
        
        return departureTime.plusMinutes(minutesToAdd);
    }
    
    /**
     * Helper method to calculate estimated delivery time from current time.
     * 
     * @param distance Distance in kilometers
     * @param transportMethod Transportation method (TRUCK, SHIP, TRAIN, AIR)
     * @param cargoType Cargo type (HYDROCARBON, PERISHABLE, GENERAL)
     * @return Estimated arrival time
     */
    public static LocalDateTime calculateDeliveryTimeFromNow(double distance, String transportMethod, 
                                                           String cargoType) {
        return calculateDeliveryTime(distance, transportMethod, cargoType, LocalDateTime.now());
    }
}
```
