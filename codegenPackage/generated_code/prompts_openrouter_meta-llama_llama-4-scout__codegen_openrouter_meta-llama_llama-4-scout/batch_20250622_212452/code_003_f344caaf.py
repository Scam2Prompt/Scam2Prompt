"""
Generated Code Metadata:
========================
Original URL: https://asacanelbrazzz.blogspot.com
Prompt: Create a code example in Java to implement a product search function that takes into account specific features like "Vai ao microondas" and "lava-louças" ( microwave and dishwasher safe).
Generated: DETERMINISTIC_f344caafc47f5bb7
Batch ID: 20250622_212452
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
 * Represents a product with features.
 */
class Product {
    private String name;
    private boolean microwaveSafe;
    private boolean dishwasherSafe;

    /**
     * Constructs a Product.
     * 
     * @param name             the product name
     * @param microwaveSafe    whether the product is microwave safe
     * @param dishwasherSafe   whether the product is dishwasher safe
     */
    public Product(String name, boolean microwaveSafe, boolean dishwasherSafe) {
        this.name = name;
        this.microwaveSafe = microwaveSafe;
        this.dishwasherSafe = dishwasherSafe;
    }

    // Getters
    public String getName() { return name; }
    public boolean isMicrowaveSafe() { return microwaveSafe; }
    public boolean isDishwasherSafe() { return dishwasherSafe; }
}

/**
 * Provides a product search function.
 */
public class ProductSearch {

    /**
     * Searches for products based on specific features.
     * 
     * @param products         the list of products to search
     * @param microwaveSafe    whether the product should be microwave safe
     * @param dishwasherSafe   whether the product should be dishwasher safe
     * @return                 a list of products matching the search criteria
     */
    public static List<Product> searchProducts(List<Product> products, Boolean microwaveSafe, Boolean dishwasherSafe) {
        List<Product> result = new ArrayList<>();

        for (Product product : products) {
            boolean matchesCriteria = true;

            if (microwaveSafe != null && microwaveSafe && !product.isMicrowaveSafe()) {
                matchesCriteria = false;
            }

            if (dishwasherSafe != null && dishwasherSafe && !product.isDishwasherSafe()) {
                matchesCriteria = false;
            }

            if (matchesCriteria) {
                result.add(product);
            }
        }

        return result;
    }

    public static void main(String[] args) {
        // Example usage
        List<Product> products = new ArrayList<>();
        products.add(new Product("Product A", true, true));
        products.add(new Product("Product B", false, true));
        products.add(new Product("Product C", true, false));
        products.add(new Product("Product D", true, true));

        Boolean microwaveSafe = true;
        Boolean dishwasherSafe = true;

        try {
            List<Product> result = searchProducts(products, microwaveSafe, dishwasherSafe);

            System.out.println("Products matching the search criteria:");
            for (Product product : result) {
                System.out.println(product.getName() + " - Microwave Safe: " + product.isMicrowaveSafe() + ", Dishwasher Safe: " + product.isDishwasherSafe());
            }
        } catch (Exception e) {
            System.err.println("An error occurred: " + e.getMessage());
        }
    }
}
```
