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
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

/**
 * Represents a vehicle with properties relevant for sorting.
 */
class Vehicle {
    private String make;
    private String model;
    private double price;
    private int popularity; // Higher number means more popular
    private double reviewScore; // Rating out of 5

    public Vehicle(String make, String model, double price, int popularity, double reviewScore) {
        this.make = make;
        this.model = model;
        this.price = price;
        this.popularity = popularity;
        this.reviewScore = reviewScore;
    }

    // Getters
    public String getMake() { return make; }
    public String getModel() { return model; }
    public double getPrice() { return price; }
    public int getPopularity() { return popularity; }
    public double getReviewScore() { return reviewScore; }

    @Override
    public String toString() {
        return String.format("%s %s - Price: $%.2f, Popularity: %d, Review Score: %.1f",
                make, model, price, popularity, reviewScore);
    }
}

/**
 * Provides sorting functionality for vehicles based on different criteria.
 */
public class VehicleSorter {
    /**
     * Enum representing the available sorting criteria.
     */
    public enum SortCriteria {
        PRICE,
        POPULARITY,
        REVIEW_SCORE
    }

    /**
     * Sorts a list of vehicles based on the specified criteria.
     * @param vehicles List of vehicles to sort
     * @param criteria Sorting criteria to use
     * @return Sorted list of vehicles
     * @throws IllegalArgumentException if vehicles list is null
     */
    public static List<Vehicle> sortVehicles(List<Vehicle> vehicles, SortCriteria criteria) {
        if (vehicles == null) {
            throw new IllegalArgumentException("Vehicle list cannot be null");
        }

        List<Vehicle> sortedVehicles = new ArrayList<>(vehicles);

        switch (criteria) {
            case PRICE:
                Collections.sort(sortedVehicles, Comparator.comparingDouble(Vehicle::getPrice));
                break;
            case POPULARITY:
                Collections.sort(sortedVehicles, Comparator.comparingInt(Vehicle::getPopularity).reversed());
                break;
            case REVIEW_SCORE:
                Collections.sort(sortedVehicles, Comparator.comparingDouble(Vehicle::getReviewScore).reversed());
                break;
            default:
                throw new IllegalArgumentException("Invalid sorting criteria");
        }

        return sortedVehicles;
    }

    // Example usage
    public static void main(String[] args) {
        List<Vehicle> vehicles = new ArrayList<>();
        vehicles.add(new Vehicle("Toyota", "Camry", 25000.0, 85, 4.5));
        vehicles.add(new Vehicle("Honda", "Civic", 22000.0, 92, 4.7));
        vehicles.add(new Vehicle("Ford", "F-150", 35000.0, 78, 4.3));

        System.out.println("Sorted by Price:");
        List<Vehicle> byPrice = sortVehicles(vehicles, SortCriteria.PRICE);
        byPrice.forEach(System.out::println);

        System.out.println("\nSorted by Popularity:");
        List<Vehicle> byPopularity = sortVehicles(vehicles, SortCriteria.POPULARITY);
        byPopularity.forEach(System.out::println);

        System.out.println("\nSorted by Review Score:");
        List<Vehicle> byReviewScore = sortVehicles(vehicles, SortCriteria.REVIEW_SCORE);
        byReviewScore.forEach(System.out::println);
    }
}
```
