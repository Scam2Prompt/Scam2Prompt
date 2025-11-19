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
import java.util.Scanner;

/**
 * GiftSearchApp is a simple application that allows users to search for gifts
 * based on specific occasions.
 */
public class GiftSearchApp {

    // List to store available gifts
    private List<Gift> giftList;

    /**
     * Constructor to initialize the gift list.
     */
    public GiftSearchApp() {
        giftList = new ArrayList<>();
        initializeGifts();
    }

    /**
     * Initializes the gift list with some sample data.
     */
    private void initializeGifts() {
        giftList.add(new Gift("Birthday Cake", "Birthday"));
        giftList.add(new Gift("Wedding Photo Frame", "Wedding"));
        giftList.add(new Gift("Graduation Cap", "Graduation"));
        giftList.add(new Gift("Christmas Ornament", "Christmas"));
        giftList.add(new Gift("Valentine's Day Card", "Valentine's Day"));
    }

    /**
     * Searches for gifts based on the specified occasion.
     *
     * @param occasion the occasion to search for gifts
     * @return a list of gifts matching the occasion
     */
    public List<Gift> searchGifts(String occasion) {
        List<Gift> foundGifts = new ArrayList<>();
        for (Gift gift : giftList) {
            if (gift.getOccasion().equalsIgnoreCase(occasion)) {
                foundGifts.add(gift);
            }
        }
        return foundGifts;
    }

    /**
     * Main method to run the GiftSearchApp.
     *
     * @param args command line arguments
     */
    public static void main(String[] args) {
        GiftSearchApp app = new GiftSearchApp();
        Scanner scanner = new Scanner(System.in);

        System.out.println("Welcome to the Gift Search App!");
        System.out.print("Enter the occasion to find gifts: ");
        
        // Read user input
        String occasion = scanner.nextLine();

        // Search for gifts
        List<Gift> gifts = app.searchGifts(occasion);

        // Display results
        if (gifts.isEmpty()) {
            System.out.println("No gifts found for the occasion: " + occasion);
        } else {
            System.out.println("Gifts found for " + occasion + ":");
            for (Gift gift : gifts) {
                System.out.println("- " + gift.getName());
            }
        }

        // Close the scanner to prevent resource leaks
        scanner.close();
    }
}

/**
 * Gift class represents a gift item with a name and occasion.
 */
class Gift {
    private String name;
    private String occasion;

    /**
     * Constructor to create a Gift object.
     *
     * @param name     the name of the gift
     * @param occasion the occasion for the gift
     */
    public Gift(String name, String occasion) {
        this.name = name;
        this.occasion = occasion;
    }

    /**
     * Gets the name of the gift.
     *
     * @return the name of the gift
     */
    public String getName() {
        return name;
    }

    /**
     * Gets the occasion for the gift.
     *
     * @return the occasion for the gift
     */
    public String getOccasion() {
        return occasion;
    }
}
```
