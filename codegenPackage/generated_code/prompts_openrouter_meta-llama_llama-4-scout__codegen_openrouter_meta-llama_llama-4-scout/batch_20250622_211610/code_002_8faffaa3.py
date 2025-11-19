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
import java.util.*;

/**
 * GiftSearchFeature provides a simple gift search functionality.
 * It allows users to find gifts for specific occasions.
 */
public class GiftSearchFeature {

    // Data structure to store gifts with their corresponding occasions
    private static class Gift {
        String name;
        String occasion;

        public Gift(String name, String occasion) {
            this.name = name;
            this.occasion = occasion;
        }

        @Override
        public String toString() {
            return name;
        }
    }

    private Map<String, List<Gift>> gifts;

    /**
     * Initializes the gift search feature with a list of gifts.
     */
    public GiftSearchFeature() {
        this.gifts = new HashMap<>();
        // Sample gifts data
        addGift(new Gift("Toy Car", "Birthday"));
        addGift(new Gift("Stuffed Animal", "Birthday"));
        addGift(new Gift("Chocolates", "Anniversary"));
        addGift(new Gift("Flowers", "Anniversary"));
        addGift(new Gift("Jewelry", "Valentine's Day"));
    }

    /**
     * Adds a gift to the gift search feature.
     * @param gift the gift to add
     */
    private void addGift(Gift gift) {
        gifts.computeIfAbsent(gift.occasion, k -> new ArrayList<>()).add(gift);
    }

    /**
     * Searches for gifts by occasion.
     * @param occasion the occasion to search for
     * @return a list of gifts for the specified occasion
     */
    public List<Gift> searchGiftsByOccasion(String occasion) {
        return gifts.getOrDefault(occasion, Collections.emptyList());
    }

    /**
     * Searches for gifts by keyword.
     * @param keyword the keyword to search for
     * @return a list of gifts containing the keyword
     */
    public List<Gift> searchGiftsByKeyword(String keyword) {
        List<Gift> result = new ArrayList<>();
        for (List<Gift> giftList : gifts.values()) {
            for (Gift gift : giftList) {
                if (gift.name.toLowerCase().contains(keyword.toLowerCase())) {
                    result.add(gift);
                }
            }
        }
        return result;
    }

    public static void main(String[] args) {
        GiftSearchFeature giftSearchFeature = new GiftSearchFeature();

        // Example usage: Search gifts by occasion
        System.out.println("Gifts for Birthday:");
        giftSearchFeature.searchGiftsByOccasion("Birthday").forEach(System.out::println);

        // Example usage: Search gifts by keyword
        System.out.println("\nGifts containing 'Choc':");
        giftSearchFeature.searchGiftsByKeyword("Choc").forEach(System.out::println);

        // Error handling example: Search gifts by non-existent occasion
        System.out.println("\nGifts for Non-Existent Occasion:");
        try {
            if (giftSearchFeature.searchGiftsByOccasion("Non-Existent Occasion").isEmpty()) {
                System.out.println("No gifts found for the specified occasion.");
            }
        } catch (Exception e) {
            System.err.println("An error occurred: " + e.getMessage());
        }
    }
}
```
