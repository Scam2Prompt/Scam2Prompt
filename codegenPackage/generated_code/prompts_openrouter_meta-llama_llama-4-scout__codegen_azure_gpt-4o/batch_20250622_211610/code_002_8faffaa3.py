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
import java.util.stream.Collectors;

/**
 * GiftSearchService - A service to search for gifts based on occasion.
 */
public class GiftSearchService {

    // A simple Gift class to represent gift items
    static class Gift {
        private String name;
        private String occasion;

        public Gift(String name, String occasion) {
            this.name = name;
            this.occasion = occasion;
        }

        public String getName() {
            return name;
        }

        public String getOccasion() {
            return occasion;
        }

        @Override
        public String toString() {
            return "Gift{name='" + name + "', occasion='" + occasion + "'}";
        }
    }

    // A list to store available gifts
    private List<Gift> giftCatalog;

    public GiftSearchService() {
        // Initialize the gift catalog with some sample data
        giftCatalog = new ArrayList<>();
        giftCatalog.add(new Gift("Teddy Bear", "Birthday"));
        giftCatalog.add(new Gift("Flower Bouquet", "Anniversary"));
        giftCatalog.add(new Gift("Chocolate Box", "Valentine's Day"));
        giftCatalog.add(new Gift("Personalized Mug", "Christmas"));
        giftCatalog.add(new Gift("Gift Card", "Any Occasion"));
    }

    /**
     * Searches for gifts based on the occasion.
     *
     * @param occasion The occasion to search for (e.g., "Birthday", "Christmas").
     * @return A list of gifts matching the occasion.
     */
    public List<Gift> searchGiftsByOccasion(String occasion) {
        if (occasion == null || occasion.isEmpty()) {
            throw new IllegalArgumentException("Occasion cannot be null or empty.");
        }

        // Filter the gift catalog based on the occasion
        return giftCatalog.stream()
                .filter(gift -> gift.getOccasion().equalsIgnoreCase(occasion) || gift.getOccasion().equalsIgnoreCase("Any Occasion"))
                .collect(Collectors.toList());
    }

    public static void main(String[] args) {
        // Create an instance of the GiftSearchService
        GiftSearchService giftSearchService = new GiftSearchService();

        try {
            // Search for gifts for "Birthday"
            List<Gift> birthdayGifts = giftSearchService.searchGiftsByOccasion("Birthday");
            System.out.println("Gifts for Birthday: " + birthdayGifts);

            // Search for gifts for "Christmas"
            List<Gift> christmasGifts = giftSearchService.searchGiftsByOccasion("Christmas");
            System.out.println("Gifts for Christmas: " + christmasGifts);

            // Search for gifts for an invalid occasion
            List<Gift> invalidSearch = giftSearchService.searchGiftsByOccasion("");
            System.out.println("Gifts for invalid occasion: " + invalidSearch);
        } catch (IllegalArgumentException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```
