"""
Generated Code Metadata:
========================
Original URL: https://refrigeratortransport.com
Prompt: Generate a Java code snippet for a logistics company to calculate the optimal route for refrigerated van deliveries in Dubai, ensuring timely and efficient transportation of perishable goods.
Generated: DETERMINISTIC_27f722309a8b6f31
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.util.*;

public class RefrigeratedRouteOptimizer {

    private static final double MAX_TRAVEL_TIME_HOURS = 8.0; // Driver shift limit
    private static final double REFRIGERATION_CAPACITY = 10000.0; // Cooling capacity in watts
    private static final double TEMPERATURE_THRESHOLD = 4.0; // Max allowed temp in °C

    /**
     * Represents a delivery location with coordinates and temperature requirements
     */
    static class DeliveryPoint {
        String name;
        double latitude;
        double longitude;
        double requiredTemp; // in °C
        double deliveryTime; // in hours
        double priority; // 1-10 scale

        public DeliveryPoint(String name, double latitude, double longitude, 
                           double requiredTemp, double deliveryTime, double priority) {
            this.name = name;
            this.latitude = latitude;
            this.longitude = longitude;
            this.requiredTemp = requiredTemp;
            this.deliveryTime = deliveryTime;
            this.priority = priority;
        }
    }

    /**
     * Represents a refrigerated van with capacity and current temperature
     */
    static class RefrigeratedVan {
        String id;
        double currentTemp; // in °C
        double capacity; // in kg
        double remainingCapacity;

        public RefrigeratedVan(String id, double currentTemp, double capacity) {
            this.id = id;
            this.currentTemp = currentTemp;
            this.capacity = capacity;
            this.remainingCapacity = capacity;
        }
    }

    /**
     * Calculates distance between two points using Haversine formula
     * @return distance in kilometers
     */
    private static double calculateDistance(double lat1, double lon1, double lat2, double lon2) {
        final int R = 6371; // Earth's radius in km
        double latDistance = Math.toRadians(lat2 - lat1);
        double lonDistance = Math.toRadians(lon2 - lon1);
        double a = Math.sin(latDistance / 2) * Math.sin(latDistance / 2)
                + Math.cos(Math.toRadians(lat1)) * Math.cos(Math.toRadians(lat2))
                * Math.sin(lonDistance / 2) * Math.sin(lonDistance / 2);
        double c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
        return R * c;
    }

    /**
     * Estimates travel time based on distance and Dubai traffic conditions
     * @return time in hours
     */
    private static double estimateTravelTime(double distanceKm) {
        // Average speed in Dubai traffic (km/h)
        double averageSpeed = 30.0; 
        return distanceKm / averageSpeed;
    }

    /**
     * Calculates cooling energy required to maintain temperature
     * @return energy in watts
     */
    private static double calculateCoolingEnergy(double deltaTemp, double duration) {
        // Simplified cooling energy calculation
        return deltaTemp * duration * 1000; // Arbitrary coefficient
    }

    /**
     * Optimizes delivery route considering temperature constraints
     * @param van The refrigerated van
     * @param points List of delivery points
     * @return Optimized route as list of DeliveryPoints
     */
    public static List<DeliveryPoint> optimizeRoute(RefrigeratedVan van, List<DeliveryPoint> points) {
        if (van == null || points == null || points.isEmpty()) {
            throw new IllegalArgumentException("Invalid input parameters");
        }

        List<DeliveryPoint> optimizedRoute = new ArrayList<>();
        List<DeliveryPoint> remainingPoints = new ArrayList<>(points);
        DeliveryPoint currentLocation = new DeliveryPoint("Warehouse", 25.2048, 55.2708, 2.0, 0, 0);
        double totalTime = 0.0;

        // Sort by priority (highest first)
        remainingPoints.sort((a, b) -> Double.compare(b.priority, a.priority));

        while (!remainingPoints.isEmpty() && totalTime < MAX_TRAVEL_TIME_HOURS) {
            DeliveryPoint bestNext = null;
            double bestScore = Double.NEGATIVE_INFINITY;

            for (DeliveryPoint point : remainingPoints) {
                if (van.remainingCapacity <= 0) break;

                double distance = calculateDistance(
                    currentLocation.latitude, currentLocation.longitude,
                    point.latitude, point.longitude
                );
                double travelTime = estimateTravelTime(distance);
                double totalPointTime = travelTime + point.deliveryTime;

                if (totalTime + totalPointTime > MAX_TRAVEL_TIME_HOURS) continue;

                // Temperature constraint check
                double tempDifference = point.requiredTemp - van.currentTemp;
                if (tempDifference > TEMPERATURE_THRESHOLD) continue;

                double coolingEnergy = calculateCoolingEnergy(tempDifference, totalPointTime);
                if (coolingEnergy > REFRIGERATION_CAPACITY) continue;

                // Score based on priority, distance, and temperature
                double score = point.priority * 10 - distance - tempDifference * 2;

                if (score > bestScore) {
                    bestScore = score;
                    bestNext = point;
                }
            }

            if (bestNext == null) break;

            double distance = calculateDistance(
                currentLocation.latitude, currentLocation.longitude,
                bestNext.latitude, bestNext.longitude
            );
            double travelTime = estimateTravelTime(distance);
            totalTime += travelTime + bestNext.deliveryTime;

            optimizedRoute.add(bestNext);
            remainingPoints.remove(bestNext);
            currentLocation = bestNext;
            van.remainingCapacity -= 1; // Simplified capacity decrement
        }

        return optimizedRoute;
    }

    public static void main(String[] args) {
        // Example usage
        RefrigeratedVan van = new RefrigeratedVan("VAN-001", 2.0, 500.0);

        List<DeliveryPoint> points = Arrays.asList(
            new DeliveryPoint("Market A", 25.2694, 55.3088, 3.0, 0.5, 8),
            new DeliveryPoint("Restaurant B", 25.2273, 55.2903, 2.5, 0.75, 9),
            new DeliveryPoint("Hotel C", 25.2075, 55.2527, 4.0, 1.0, 7),
            new DeliveryPoint("Cafe D", 25.1867, 55.2743, 3.5, 0.25, 6)
        );

        try {
            List<DeliveryPoint> optimizedRoute = optimizeRoute(van, points);
            System.out.println("Optimized Route:");
            for (DeliveryPoint point : optimizedRoute) {
                System.out.println("- " + point.name);
            }
        } catch (IllegalArgumentException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```
