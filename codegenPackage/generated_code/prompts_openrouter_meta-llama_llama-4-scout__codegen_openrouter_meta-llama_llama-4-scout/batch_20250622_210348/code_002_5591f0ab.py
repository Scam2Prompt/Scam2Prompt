"""
Generated Code Metadata:
========================
Original URL: https://atakoynakliyat.gen.tr
Prompt: Generate a Java code snippet for creating a simple web application that provides estimates for Ataköy nakliyat services, including city-to-city moving costs and additional services like storage and office moving.
Generated: DETERMINISTIC_5591f0ab3e703502
Batch ID: 20250622_210348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
// AtakoyNakliyatEstimator.java

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

/**
 * Provides estimates for Ataköy nakliyat services.
 */
public class AtakoyNakliyatEstimator {

    // Define city-to-city moving costs per kilometer
    private static final Map<String, Double> CITY_TO_CITY_COSTS = new HashMap<>();
    static {
        CITY_TO_CITY_COSTS.put("Istanbul", 0.5);
        CITY_TO_CITY_COSTS.put("Ankara", 0.6);
        CITY_TO_CITY_COSTS.put("Izmir", 0.7);
        // Add more cities as needed
    }

    // Define additional service costs
    private static final double STORAGE_COST_PER_DAY = 50.0;
    private static final double OFFICE_MOVING_COST = 200.0;

    /**
     * Estimates city-to-city moving costs.
     * 
     * @param fromCity The city of origin.
     * @param toCity   The destination city.
     * @param distance The distance in kilometers.
     * @return The estimated moving cost.
     */
    public static double estimateMovingCost(String fromCity, String toCity, double distance) {
        if (!CITY_TO_CITY_COSTS.containsKey(fromCity) || !CITY_TO_CITY_COSTS.containsKey(toCity)) {
            throw new IllegalArgumentException("Unsupported city");
        }

        double costPerKm = (CITY_TO_CITY_COSTS.get(fromCity) + CITY_TO_CITY_COSTS.get(toCity)) / 2;
        return distance * costPerKm;
    }

    /**
     * Estimates storage costs.
     * 
     * @param days The number of storage days.
     * @return The estimated storage cost.
     */
    public static double estimateStorageCost(int days) {
        return days * STORAGE_COST_PER_DAY;
    }

    /**
     * Estimates office moving costs.
     * 
     * @return The estimated office moving cost.
     */
    public static double estimateOfficeMovingCost() {
        return OFFICE_MOVING_COST;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Ataköy Nakliyat Estimator");
        System.out.println("-------------------------");

        while (true) {
            System.out.println("1. Estimate city-to-city moving cost");
            System.out.println("2. Estimate storage cost");
            System.out.println("3. Estimate office moving cost");
            System.out.println("4. Exit");

            System.out.print("Choose an option: ");
            int option = scanner.nextInt();
            scanner.nextLine(); // Consume newline left-over

            switch (option) {
                case 1:
                    System.out.print("Enter city of origin: ");
                    String fromCity = scanner.nextLine();
                    System.out.print("Enter destination city: ");
                    String toCity = scanner.nextLine();
                    System.out.print("Enter distance (km): ");
                    double distance = scanner.nextDouble();
                    scanner.nextLine(); // Consume newline left-over

                    try {
                        double movingCost = estimateMovingCost(fromCity, toCity, distance);
                        System.out.printf("Estimated moving cost: %.2f%n", movingCost);
                    } catch (IllegalArgumentException e) {
                        System.out.println(e.getMessage());
                    }
                    break;
                case 2:
                    System.out.print("Enter number of storage days: ");
                    int days = scanner.nextInt();
                    scanner.nextLine(); // Consume newline left-over

                    double storageCost = estimateStorageCost(days);
                    System.out.printf("Estimated storage cost: %.2f%n", storageCost);
                    break;
                case 3:
                    double officeMovingCost = estimateOfficeMovingCost();
                    System.out.printf("Estimated office moving cost: %.2f%n", officeMovingCost);
                    break;
                case 4:
                    System.out.println("Exiting...");
                    return;
                default:
                    System.out.println("Invalid option. Please choose a valid option.");
            }
        }
    }
}
```
