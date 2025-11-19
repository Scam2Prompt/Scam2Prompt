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
import java.util.*;

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

class Route {
    List<Location> locations;
    double distance;
    double travelTime;

    public Route(List<Location> locations, double distance, double travelTime) {
        this.locations = locations;
        this.distance = distance;
        this.travelTime = travelTime;
    }
}

public class VidanjorRouteOptimizer {

    private static final double ISTANBUL_LATITUDE = 41.8781;
    private static final double ISTANBUL_LONGITUDE = 12.4922;
    private static final int EARTH_RADIUS_KM = 6371;

    /**
     * Calculate distance between two points on Earth's surface using Haversine formula.
     * @param loc1 First location
     * @param loc2 Second location
     * @return Distance in kilometers
     */
    private static double calculateDistance(Location loc1, Location loc2) {
        double dLat = Math.toRadians(loc2.latitude - loc1.latitude);
        double dLon = Math.toRadians(loc2.longitude - loc1.longitude);
        double lat1 = Math.toRadians(loc1.latitude);
        double lat2 = Math.toRadians(loc2.latitude);

        double a = Math.sin(dLat / 2) * Math.sin(dLat / 2) +
                Math.sin(dLon / 2) * Math.sin(dLon / 2) * Math.cos(lat1) * Math.cos(lat2);
        double c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
        return EARTH_RADIUS_KM * c;
    }

    /**
     * Calculate travel time based on distance and average speed.
     * @param distance Distance in kilometers
     * @param speed Average speed in km/h
     * @return Travel time in hours
     */
    private static double calculateTravelTime(double distance, double speed) {
        return distance / speed;
    }

    /**
     * Optimize route for vidanjör truck using Nearest Neighbor algorithm.
     * @param locations List of locations to visit
     * @param startLocation Starting location
     * @param speed Average speed in km/h
     * @return Optimal route
     */
    public static Route optimizeRoute(List<Location> locations, Location startLocation, double speed) {
        List<Location> routeLocations = new ArrayList<>();
        routeLocations.add(startLocation);
        locations.remove(startLocation);

        while (!locations.isEmpty()) {
            Location closestLocation = null;
            double minDistance = Double.MAX_VALUE;

            for (Location location : locations) {
                double distance = calculateDistance(routeLocations.get(routeLocations.size() - 1), location);
                if (distance < minDistance) {
                    minDistance = distance;
                    closestLocation = location;
                }
            }

            routeLocations.add(closestLocation);
            locations.remove(closestLocation);
        }

        double totalDistance = 0;
        for (int i = 0; i < routeLocations.size() - 1; i++) {
            totalDistance += calculateDistance(routeLocations.get(i), routeLocations.get(i + 1));
        }

        double travelTime = calculateTravelTime(totalDistance, speed);
        return new Route(routeLocations, totalDistance, travelTime);
    }

    public static void main(String[] args) {
        List<Location> locations = Arrays.asList(
                new Location("Location 1", 41.0123, 28.9756),
                new Location("Location 2", 41.0873, 29.0333),
                new Location("Location 3", 40.9353, 29.1244),
                new Location("Location 4", 41.1456, 28.8533)
        );

        Location startLocation = new Location("Depot", 41.8781, 12.4922);
        double speed = 30; // km/h

        Route optimalRoute = optimizeRoute(new ArrayList<>(locations), startLocation, speed);

        System.out.println("Optimal Route:");
        for (Location location : optimalRoute.locations) {
            System.out.println(location.name);
        }

        System.out.println("\nTotal Distance: " + optimalRoute.distance + " km");
        System.out.println("Total Travel Time: " + optimalRoute.travelTime + " hours");
    }
}
```
