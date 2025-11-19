"""
Generated Code Metadata:
========================
Original URL: https://www.reliableridesllc.org
Prompt: Write a code snippet in Java to implement a simple vehicle sorting algorithm, sorting cars by price, popularity, or review score, as seen on the Reliable Rides LLC website.
Generated: DETERMINISTIC_d56069f43548e66c
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

// Class representing a Vehicle
class Vehicle {
    private String name;
    private double price;
    private int popularity; // Assume popularity is a score from 1 to 100
    private double reviewScore; // Assume review score is from 1.0 to 5.0

    // Constructor
    public Vehicle(String name, double price, int popularity, double reviewScore) {
        this.name = name;
        this.price = price;
        this.popularity = popularity;
        this.reviewScore = reviewScore;
    }

    // Getters
    public String getName() {
        return name;
    }

    public double getPrice() {
        return price;
    }

    public int getPopularity() {
        return popularity;
    }

    public double getReviewScore() {
        return reviewScore;
    }

    @Override
    public String toString() {
        return String.format("Vehicle{name='%s', price=%.2f, popularity=%d, reviewScore=%.1f}", 
                             name, price, popularity, reviewScore);
    }
}

// Class to handle sorting of vehicles
public class VehicleSorter {

    // Method to sort vehicles based on the specified criteria
    public static List<Vehicle> sortVehicles(List<Vehicle> vehicles, String criteria) {
        if (vehicles == null || criteria == null) {
            throw new IllegalArgumentException("Vehicle list and criteria must not be null");
        }

        // Sort based on the criteria
        switch (criteria.toLowerCase()) {
            case "price":
                vehicles.sort(Comparator.comparingDouble(Vehicle::getPrice));
                break;
            case "popularity":
                vehicles.sort(Comparator.comparingInt(Vehicle::getPopularity).reversed());
                break;
            case "review":
                vehicles.sort(Comparator.comparingDouble(Vehicle::getReviewScore).reversed());
                break;
            default:
                throw new IllegalArgumentException("Invalid sorting criteria: " + criteria);
        }
        return vehicles;
    }

    // Main method for testing
    public static void main(String[] args) {
        // Sample vehicle list
        List<Vehicle> vehicles = new ArrayList<>();
        vehicles.add(new Vehicle("Car A", 20000, 85, 4.5));
        vehicles.add(new Vehicle("Car B", 15000, 90, 4.0));
        vehicles.add(new Vehicle("Car C", 30000, 70, 4.8));

        // Sort by price
        System.out.println("Sorting by price:");
        sortVehicles(vehicles, "price").forEach(System.out::println);

        // Sort by popularity
        System.out.println("\nSorting by popularity:");
        sortVehicles(vehicles, "popularity").forEach(System.out::println);

        // Sort by review score
        System.out.println("\nSorting by review score:");
        sortVehicles(vehicles, "review").forEach(System.out::println);
    }
}
```
