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
import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;

/**
 * Class representing a point in the logistics network.
 */
class Location {
    String name;
    double latitude;
    double longitude;

    public Location(String name, double latitude, double longitude) {
        this.name = name;
        this.latitude = latitude;
        this.longitude = longitude;
    }
}

/**
 * Class representing a delivery route.
 */
class Route {
    List<Location> locations;
    double totalDistance;

    public Route() {
        this.locations = new ArrayList<>();
        this.totalDistance = 0.0;
    }

    public void addLocation(Location location, double distance) {
        locations.add(location);
        totalDistance += distance;
    }

    public double getTotalDistance() {
        return totalDistance;
    }

    public List<Location> getLocations() {
        return locations;
    }
}

/**
 * Class to calculate the optimal route for refrigerated van deliveries.
 */
public class DeliveryRouteOptimizer {

    /**
     * Calculates the distance between two locations using the Haversine formula.
     *
     * @param loc1 First location
     * @param loc2 Second location
     * @return Distance in kilometers
     */
    private double calculateDistance(Location loc1, Location loc2) {
        final int EARTH_RADIUS = 6371; // Radius of the earth in km
        double latDistance = Math.toRadians(loc2.latitude - loc1.latitude);
        double lonDistance = Math.toRadians(loc2.longitude - loc1.longitude);
        double a = Math.sin(latDistance / 2) * Math.sin(latDistance / 2) +
                Math.cos(Math.toRadians(loc1.latitude)) * Math.cos(Math.toRadians(loc2.latitude)) *
                Math.sin(lonDistance / 2) * Math.sin(lonDistance / 2);
        double c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
        return EARTH_RADIUS * c; // Convert to kilometers
    }

    /**
     * Finds the optimal delivery route using a simple greedy algorithm.
     *
     * @param start Starting location
     * @param deliveries List of delivery locations
     * @return Optimal route
     */
    public Route findOptimalRoute(Location start, List<Location> deliveries) {
        Route optimalRoute = new Route();
        optimalRoute.addLocation(start, 0.0); // Start from the initial location

        boolean[] visited = new boolean[deliveries.size()];
        Location currentLocation = start;

        for (int i = 0; i < deliveries.size(); i++) {
            double minDistance = Double.MAX_VALUE;
            int nextIndex = -1;

            // Find the nearest unvisited delivery location
            for (int j = 0; j < deliveries.size(); j++) {
                if (!visited[j]) {
                    double distance = calculateDistance(currentLocation, deliveries.get(j));
                    if (distance < minDistance) {
                        minDistance = distance;
                        nextIndex = j;
                    }
                }
            }

            // If a next location is found, add it to the route
            if (nextIndex != -1) {
                visited[nextIndex] = true;
                currentLocation = deliveries.get(nextIndex);
                optimalRoute.addLocation(currentLocation, minDistance);
            }
        }

        return optimalRoute;
    }

    public static void main(String[] args) {
        try {
            DeliveryRouteOptimizer optimizer = new DeliveryRouteOptimizer();

            // Define starting location
            Location start = new Location("Warehouse", 25.276987, 55.296249);

            // Define delivery locations
            List<Location> deliveries = new ArrayList<>();
            deliveries.add(new Location("Location A", 25.276987, 55.296249));
            deliveries.add(new Location("Location B", 25.276987, 55.296249));
            deliveries.add(new Location("Location C", 25.276987, 55.296249));

            // Calculate the optimal route
            Route optimalRoute = optimizer.findOptimalRoute(start, deliveries);

            // Output the optimal route
            System.out.println("Optimal Delivery Route:");
            for (Location loc : optimalRoute.getLocations()) {
                System.out.println(loc.name);
            }
            System.out.println("Total Distance: " + optimalRoute.getTotalDistance() + " km");

        } catch (Exception e) {
            System.err.println("An error occurred while calculating the delivery route: " + e.getMessage());
        }
    }
}
```
