"""
Generated Code Metadata:
========================
Original URL: https://enyakinvidanjor.com
Prompt: Create a Java program to calculate the optimal route for a vidanjör truck to take when servicing multiple locations across Istanbul, minimizing travel time and distance.
Generated: DETERMINISTIC_b35bc925e02a23e6
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class VidanjorRouteOptimizer {

    // Represents a location with coordinates
    static class Location {
        String name;
        double latitude;
        double longitude;

        public Location(String name, double latitude, double longitude) {
            this.name = name;
            this.latitude = latitude;
            this.longitude = longitude;
        }

        @Override
        public String toString() {
            return name + " (" + latitude + ", " + longitude + ")";
        }
    }

    // Calculates distance between two locations using Haversine formula
    private static double calculateDistance(Location loc1, Location loc2) {
        final int R = 6371; // Earth radius in km

        double latDistance = Math.toRadians(loc2.latitude - loc1.latitude);
        double lonDistance = Math.toRadians(loc2.longitude - loc1.longitude);
        double a = Math.sin(latDistance / 2) * Math.sin(latDistance / 2)
                + Math.cos(Math.toRadians(loc1.latitude)) * Math.cos(Math.toRadians(loc2.latitude))
                * Math.sin(lonDistance / 2) * Math.sin(lonDistance / 2);
        double c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
        return R * c;
    }

    // Finds the nearest neighbor for the current location
    private static Location findNearestNeighbor(Location current, List<Location> unvisited) {
        Location nearest = null;
        double minDistance = Double.MAX_VALUE;

        for (Location loc : unvisited) {
            double distance = calculateDistance(current, loc);
            if (distance < minDistance) {
                minDistance = distance;
                nearest = loc;
            }
        }
        return nearest;
    }

    // Optimizes route using Nearest Neighbor algorithm
    public static List<Location> optimizeRoute(List<Location> locations) {
        if (locations == null || locations.isEmpty()) {
            throw new IllegalArgumentException("Location list cannot be null or empty");
        }

        List<Location> unvisited = new ArrayList<>(locations);
        List<Location> optimizedRoute = new ArrayList<>();

        // Start with first location
        Location current = unvisited.remove(0);
        optimizedRoute.add(current);

        while (!unvisited.isEmpty()) {
            Location next = findNearestNeighbor(current, unvisited);
            optimizedRoute.add(next);
            unvisited.remove(next);
            current = next;
        }

        return optimizedRoute;
    }

    // Calculates total distance of a route
    public static double calculateTotalDistance(List<Location> route) {
        if (route == null || route.size() < 2) {
            return 0;
        }

        double totalDistance = 0;
        for (int i = 0; i < route.size() - 1; i++) {
            totalDistance += calculateDistance(route.get(i), route.get(i + 1));
        }
        return totalDistance;
    }

    public static void main(String[] args) {
        // Example locations in Istanbul
        List<Location> locations = new ArrayList<>();
        locations.add(new Location("Depot", 41.0082, 28.9784));
        locations.add(new Location("Besiktas", 41.0425, 29.0066));
        locations.add(new Location("Kadikoy", 40.9819, 29.0576));
        locations.add(new Location("Sisli", 41.0608, 28.9877));
        locations.add(new Location("Fatih", 41.0151, 28.9403));

        try {
            System.out.println("Original route:");
            locations.forEach(System.out::println);
            System.out.println("Total distance: " + calculateTotalDistance(locations) + " km");

            List<Location> optimizedRoute = optimizeRoute(locations);
            System.out.println("\nOptimized route:");
            optimizedRoute.forEach(System.out::println);
            System.out.println("Total distance: " + calculateTotalDistance(optimizedRoute) + " km");
        } catch (Exception e) {
            System.err.println("Error optimizing route: " + e.getMessage());
        }
    }
}
```
