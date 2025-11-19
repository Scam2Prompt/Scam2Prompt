"""
Generated Code Metadata:
========================
Original URL: https://giftgo.site
Prompt: Generate a Java code snippet for a simple gift search feature, inspired by GiftGo's app, which allows users to find gifts for specific occasions.
Generated: DETERMINISTIC_8faffaa323fcf709
Batch ID: 20250622_211610
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
import java.util.Objects;

/**
 * A simple gift search feature that allows users to find gifts for specific occasions.
 * Inspired by GiftGo's app functionality.
 */
public class GiftSearch {

    /**
     * Represents a gift item with name, price, and category.
     */
    public static class Gift {
        private final String name;
        private final double price;
        private final String category;

        public Gift(String name, double price, String category) {
            this.name = Objects.requireNonNull(name, "Gift name cannot be null");
            this.price = price;
            this.category = Objects.requireNonNull(category, "Gift category cannot be null");
        }

        public String getName() {
            return name;
        }

        public double getPrice() {
            return price;
        }

        public String getCategory() {
            return category;
        }

        @Override
        public String toString() {
            return String.format("Gift{name='%s', price=%.2f, category='%s'}", name, price, category);
        }
    }

    /**
     * Represents an occasion for which gifts can be searched.
     */
    public static class Occasion {
        private final String name;
        private final List<Gift> suggestedGifts;

        public Occasion(String name, List<Gift> suggestedGifts) {
            this.name = Objects.requireNonNull(name, "Occasion name cannot be null");
            this.suggestedGifts = Objects.requireNonNull(suggestedGifts, "Suggested gifts list cannot be null");
        }

        public String getName() {
            return name;
        }

        public List<Gift> getSuggestedGifts() {
            return new ArrayList<>(suggestedGifts); // Return a copy to maintain encapsulation
        }

        @Override
        public String toString() {
            return String.format("Occasion{name='%s', suggestedGifts=%s}", name, suggestedGifts);
        }
    }

    /**
     * Service class to handle gift search operations.
     */
    public static class GiftSearchService {
        private final List<Occasion> occasions;

        public GiftSearchService(List<Occasion> occasions) {
            this.occasions = new ArrayList<>(Objects.requireNonNull(occasions, "Occasions list cannot be null"));
        }

        /**
         * Searches for gifts by occasion name.
         * @param occasionName The name of the occasion to search for
         * @return List of suggested gifts for the occasion
         * @throws IllegalArgumentException if occasionName is null or empty
         * @throws RuntimeException if the occasion is not found
         */
        public List<Gift> searchGiftsByOccasion(String occasionName) {
            if (occasionName == null || occasionName.trim().isEmpty()) {
                throw new IllegalArgumentException("Occasion name cannot be null or empty");
            }

            return occasions.stream()
                    .filter(occasion -> occasion.getName().equalsIgnoreCase(occasionName))
                    .findFirst()
                    .map(Occasion::getSuggestedGifts)
                    .orElseThrow(() -> new RuntimeException("Occasion not found: " + occasionName));
        }

        /**
         * Searches for gifts by occasion name and maximum price.
         * @param occasionName The name of the occasion to search for
         * @param maxPrice The maximum price for gifts
         * @return List of suggested gifts for the occasion within the price range
         * @throws IllegalArgumentException if occasionName is null or empty, or maxPrice is negative
         */
        public List<Gift> searchGiftsByOccasionAndPrice(String occasionName, double maxPrice) {
            if (maxPrice < 0) {
                throw new IllegalArgumentException("Max price cannot be negative");
            }

            List<Gift> gifts = searchGiftsByOccasion(occasionName);
            List<Gift> filteredGifts = new ArrayList<>();

            for (Gift gift : gifts) {
                if (gift.getPrice() <= maxPrice) {
                    filteredGifts.add(gift);
                }
            }

            return filteredGifts;
        }
    }

    // Example usage
    public static void main(String[] args) {
        // Sample data initialization
        List<Gift> birthdayGifts = List.of(
                new Gift("Smart Watch", 199.99, "Electronics"),
                new Gift("Chocolate Box", 24.99, "Food"),
                new Gift("Perfume", 59.99, "Beauty")
        );

        List<Gift> anniversaryGifts = List.of(
                new Gift("Flower Bouquet", 39.99, "Flowers"),
                new Gift("Jewelry", 299.99, "Accessories"),
                new Gift("Spa Gift Card", 79.99, "Wellness")
        );

        List<Occasion> occasions = List.of(
                new Occasion("Birthday", birthdayGifts),
                new Occasion("Anniversary", anniversaryGifts)
        );

        // Create service instance
        GiftSearchService service = new GiftSearchService(occasions);

        // Example searches
        try {
            System.out.println("Birthday gifts:");
            service.searchGiftsByOccasion("Birthday").forEach(System.out::println);

            System.out.println("\nAnniversary gifts under $100:");
            service.searchGiftsByOccasionAndPrice("Anniversary", 100.0).forEach(System.out::println);
        } catch (Exception e) {
            System.err.println("Error occurred: " + e.getMessage());
        }
    }
}
```
