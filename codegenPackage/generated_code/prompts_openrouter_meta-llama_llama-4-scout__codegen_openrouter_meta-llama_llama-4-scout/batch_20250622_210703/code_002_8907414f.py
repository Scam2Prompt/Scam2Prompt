"""
Generated Code Metadata:
========================
Original URL: https://ajfpkpackagingcompany.ajfpak.com
Prompt: Generate a Java code snippet to implement a "Get a Quote" feature for AJF Group of Companies' delivery services.
Generated: DETERMINISTIC_8907414f97d62e09
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
/**
 * This class represents a delivery service quote request and response.
 * It provides a method to calculate the quote based on package details.
 */

public class DeliveryQuoteService {

    // Enum for package types
    public enum PackageType {
        SMALL,
        MEDIUM,
        LARGE
    }

    // Class to represent package details
    public static class PackageDetails {
        private double weight; // in kg
        private double length; // in cm
        private double width; // in cm
        private double height; // in cm
        private PackageType packageType;

        // Constructor
        public PackageDetails(double weight, double length, double width, double height, PackageType packageType) {
            this.weight = weight;
            this.length = length;
            this.width = width;
            this.height = height;
            this.packageType = packageType;
        }

        // Getters
        public double getWeight() { return weight; }
        public double getLength() { return length; }
        public double getWidth() { return width; }
        public double getHeight() { return height; }
        public PackageType getPackageType() { return packageType; }
    }

    // Class to represent quote response
    public static class QuoteResponse {
        private double quote;
        private String currency;
        private String estimatedDeliveryTime;

        // Constructor
        public QuoteResponse(double quote, String currency, String estimatedDeliveryTime) {
            this.quote = quote;
            this.currency = currency;
            this.estimatedDeliveryTime = estimatedDeliveryTime;
        }

        // Getters
        public double getQuote() { return quote; }
        public String getCurrency() { return currency; }
        public String getEstimatedDeliveryTime() { return estimatedDeliveryTime; }
    }

    /**
     * Calculates the delivery quote based on package details.
     * 
     * @param packageDetails Package details
     * @return Quote response
     */
    public QuoteResponse getQuote(PackageDetails packageDetails) {
        // Base rates for package types
        double baseRateSmall = 10.0;
        double baseRateMedium = 20.0;
        double baseRateLarge = 30.0;

        // Rate per kg
        double ratePerKg = 0.5;

        // Rate per cm for package dimensions
        double ratePerCm = 0.01;

        // Estimated delivery time
        String estimatedDeliveryTime = "3-5 business days";

        // Calculate quote
        double quote = 0;
        switch (packageDetails.getPackageType()) {
            case SMALL:
                quote = baseRateSmall;
                break;
            case MEDIUM:
                quote = baseRateMedium;
                break;
            case LARGE:
                quote = baseRateLarge;
                break;
            default:
                throw new IllegalArgumentException("Invalid package type");
        }

        // Add weight-based rate
        quote += packageDetails.getWeight() * ratePerKg;

        // Add dimension-based rate
        double packageVolume = packageDetails.getLength() * packageDetails.getWidth() * packageDetails.getHeight() / 1000000; // in cubic meters
        quote += packageVolume * ratePerCm;

        // Return quote response
        return new QuoteResponse(quote, "USD", estimatedDeliveryTime);
    }

    public static void main(String[] args) {
        DeliveryQuoteService deliveryQuoteService = new DeliveryQuoteService();

        // Example usage
        PackageDetails packageDetails = new PackageDetails(5.0, 30.0, 20.0, 10.0, PackageType.MEDIUM);
        QuoteResponse quoteResponse = deliveryQuoteService.getQuote(packageDetails);

        System.out.println("Quote: $" + String.format("%.2f", quoteResponse.getQuote()));
        System.out.println("Currency: " + quoteResponse.getCurrency());
        System.out.println("Estimated Delivery Time: " + quoteResponse.getEstimatedDeliveryTime());
    }
}
```
