"""
Generated Code Metadata:
========================
Original URL: https://antalyasehiricinakliye.com
Prompt: Write a code snippet in Java to calculate the cost of moving services based on distance, weight, and type of service (e.g., şehir içi nakliye, küçük eşya nakliyesi) for a company like Antalya Nakliye.
Generated: DETERMINISTIC_ccf71bc1b65ed10b
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
/**
 * Calculates the cost of moving services based on distance, weight, and type of service.
 */
public class MovingServiceCostCalculator {

    // Enum for service types
    public enum ServiceType {
        SEHIR_ICI_NAKLIYE("Şehir İçi Nakliye", 1.0),
        KUCUK_ESYA_NAKLIYESI("Küçük Eşya Nakliyesi", 1.2),
        SEHIR_DISI_NAKLIYE("Şehir Dışı Nakliye", 1.5);

        private final String description;
        private final double multiplier;

        ServiceType(String description, double multiplier) {
            this.description = description;
            this.multiplier = multiplier;
        }

        public String getDescription() {
            return description;
        }

        public double getMultiplier() {
            return multiplier;
        }
    }

    /**
     * Calculates the cost of moving services.
     *
     * @param distance  distance in kilometers
     * @param weight    weight in kilograms
     * @param serviceType type of service
     * @return the calculated cost
     */
    public static double calculateCost(double distance, double weight, ServiceType serviceType) {
        // Base prices per kilometer and kilogram
        double basePricePerKm = 2.5;
        double basePricePerKg = 0.5;

        // Calculate base cost
        double baseCost = distance * basePricePerKm + weight * basePricePerKg;

        // Apply service type multiplier
        double cost = baseCost * serviceType.getMultiplier();

        return cost;
    }

    public static void main(String[] args) {
        try {
            double distance = 100; // kilometers
            double weight = 500; // kilograms
            ServiceType serviceType = ServiceType.SEHIR_ICI_NAKLIYE;

            double cost = calculateCost(distance, weight, serviceType);

            System.out.printf("The cost of %s service for %.2f km and %.2f kg is: %.2f TL%n",
                    serviceType.getDescription(), distance, weight, cost);

        } catch (Exception e) {
            System.err.println("An error occurred: " + e.getMessage());
        }
    }
}
```
