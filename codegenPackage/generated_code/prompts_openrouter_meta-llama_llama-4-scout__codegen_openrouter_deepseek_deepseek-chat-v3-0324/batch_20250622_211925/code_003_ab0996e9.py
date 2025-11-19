"""
Generated Code Metadata:
========================
Original URL: https://www.twigacementgroup.com
Prompt: Write a Java code to compare the features of different cement products, such as Twiga Ordinary, Twiga Plus, and Twiga Extra, produced by Twiga Cement.
Generated: DETERMINISTIC_ab0996e9e95369fd
Batch ID: 20250622_211925
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

/**
 * This class represents a Cement Product with its features.
 */
class CementProduct {
    private String name;
    private String strength;
    private String settingTime;
    private String durability;
    private String price;

    /**
     * Constructor for CementProduct.
     * @param name Name of the cement product
     * @param strength Strength of the cement
     * @param settingTime Setting time of the cement
     * @param durability Durability of the cement
     * @param price Price of the cement
     */
    public CementProduct(String name, String strength, String settingTime, String durability, String price) {
        this.name = name;
        this.strength = strength;
        this.settingTime = settingTime;
        this.durability = durability;
        this.price = price;
    }

    // Getters for all properties
    public String getName() {
        return name;
    }

    public String getStrength() {
        return strength;
    }

    public String getSettingTime() {
        return settingTime;
    }

    public String getDurability() {
        return durability;
    }

    public String getPrice() {
        return price;
    }

    @Override
    public String toString() {
        return String.format(
            "Product: %s\nStrength: %s\nSetting Time: %s\nDurability: %s\nPrice: %s\n",
            name, strength, settingTime, durability, price
        );
    }
}

/**
 * This class compares different cement products and displays their features.
 */
public class CementProductComparator {

    private List<CementProduct> cementProducts;

    /**
     * Constructor initializes the list of cement products.
     */
    public CementProductComparator() {
        cementProducts = new ArrayList<>();
        // Initialize with sample data
        cementProducts.add(new CementProduct(
            "Twiga Ordinary",
            "32.5 MPa",
            "Standard",
            "Good",
            "Low"
        ));
        cementProducts.add(new CementProduct(
            "Twiga Plus",
            "42.5 MPa",
            "Fast",
            "Better",
            "Medium"
        ));
        cementProducts.add(new CementProduct(
            "Twiga Extra",
            "52.5 MPa",
            "Very Fast",
            "Best",
            "High"
        ));
    }

    /**
     * Displays all cement products and their features.
     */
    public void displayAllProducts() {
        System.out.println("=== Cement Product Comparison ===");
        for (CementProduct product : cementProducts) {
            System.out.println(product);
        }
    }

    /**
     * Compares a specific feature across all products.
     * @param feature The feature to compare (e.g., "strength", "price")
     * @throws IllegalArgumentException if the feature is invalid
     */
    public void compareFeature(String feature) {
        System.out.println("=== Comparing Feature: " + feature + " ===");
        for (CementProduct product : cementProducts) {
            switch (feature.toLowerCase()) {
                case "strength":
                    System.out.println(product.getName() + ": " + product.getStrength());
                    break;
                case "setting time":
                    System.out.println(product.getName() + ": " + product.getSettingTime());
                    break;
                case "durability":
                    System.out.println(product.getName() + ": " + product.getDurability());
                    break;
                case "price":
                    System.out.println(product.getName() + ": " + product.getPrice());
                    break;
                default:
                    throw new IllegalArgumentException("Invalid feature: " + feature);
            }
        }
    }

    public static void main(String[] args) {
        CementProductComparator comparator = new CementProductComparator();
        
        // Display all products
        comparator.displayAllProducts();

        // Compare specific features
        try {
            comparator.compareFeature("strength");
            comparator.compareFeature("price");
        } catch (IllegalArgumentException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```
