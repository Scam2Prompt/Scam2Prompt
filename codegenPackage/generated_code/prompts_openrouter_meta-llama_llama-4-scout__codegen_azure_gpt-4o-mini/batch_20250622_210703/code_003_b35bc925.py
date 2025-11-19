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
import java.util.List;
import java.util.PriorityQueue;
import java.util.Comparator;

// Class representing a location with coordinates
class Location {
    private String name;
    private double latitude;
    private double longitude;

    public Location(String name, double latitude, double longitude) {
        this.name = name;
        this.latitude = latitude;
        this.longitude = longitude;
    }

    public String getName() {
        return name;
    }

    public double getLatitude() {
        return latitude;
    }

    public double getLongitude() {
        return longitude;
    }

    // Calculate distance to another location using Haversine formula
    public double distanceTo(Location other) {
        final int R = 6371; // Radius of the earth in km
        double latDistance = Math.toRadians(other.getLatitude() - this.latitude);
        double lonDistance = Math.toRadians(other.getLongitude() - this.longitude);
        double a = Math.sin(latDistance / 2) * Math.sin(latDistance / 2) +
                   Math.cos(Math.toRadians(this.latitude)) * Math.cos(Math.toRadians(other.getLatitude())) *
                   Math.sin(lonDistance / 2) * Math.sin(lonDistance / 2);
        double c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
        return R * c; // Distance in km
    }
}

// Class representing the route optimizer
class RouteOptimizer {
    private List<Location> locations;

    public RouteOptimizer(List<Location> locations) {
        this.locations = locations;
    }

    // Method to calculate the optimal route using a simple nearest neighbor algorithm
    public List<Location> calculateOptimalRoute() {
        if (locations.isEmpty()) {
            throw new IllegalArgumentException("Location list cannot be empty.");
        }

        List<Location> optimalRoute = new ArrayList<>();
        boolean[] visited = new boolean[locations.size()];
        Location currentLocation = locations.get(0); // Start from the first location
        optimalRoute.add(currentLocation);
        visited[0] = true;

        for (int i = 1; i < locations.size(); i++) {
            int nextIndex = -1;
            double minDistance = Double.MAX_VALUE;

            // Find the nearest unvisited location
            for (int j = 0; j < locations.size(); j++) {
                if (!visited[j]) {
                    double distance = currentLocation.distanceTo(locations.get(j));
                    if (distance < minDistance) {
                        minDistance = distance;
                        nextIndex = j;
                    }
                }
            }

            // Move to the next location
            if (nextIndex != -1) {
                currentLocation = locations.get(nextIndex);
                optimalRoute.add(currentLocation);
                visited[nextIndex] = true;
            }
        }

        return optimalRoute;
    }
}

// Main class to run the program
public class VidanjörRoutePlanner {
    public static void main(String[] args) {
        // Sample locations in Istanbul
        List<Location> locations = new ArrayList<>();
        locations.add(new Location("Location A", 41.0082, 28.9784)); // Example coordinates
        locations.add(new Location("Location B", 41.0151, 28.9790));
        locations.add(new Location("Location C", 41.0085, 28.9788));
        locations.add(new Location("Location D", 41.0136, 28.9550));

        // Create RouteOptimizer instance
        RouteOptimizer optimizer = new RouteOptimizer(locations);

        try {
            // Calculate and print the optimal route
            List<Location> optimalRoute = optimizer.calculateOptimalRoute();
            System.out.println("Optimal Route:");
            for (Location loc : optimalRoute) {
                System.out.println(loc.getName());
            }
        } catch (IllegalArgumentException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```
