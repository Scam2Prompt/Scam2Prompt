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
import java.util.stream.Collectors;

/**
 * Represents a product with specific features.
 */
class Product {
    private String name;
    private boolean microwaveSafe;
    private boolean dishwasherSafe;

    // Constructor
    public Product(String name, boolean microwaveSafe, boolean dishwasherSafe) {
        this.name = name;
        this.microwaveSafe = microwaveSafe;
        this.dishwasherSafe = dishwasherSafe;
    }

    // Getters
    public String getName() {
        return name;
    }

    public boolean isMicrowaveSafe() {
        return microwaveSafe;
    }

    public boolean isDishwasherSafe() {
        return dishwasherSafe;
    }

    @Override
    public String toString() {
        return "Product{name='" + name + "', microwaveSafe=" + microwaveSafe + ", dishwasherSafe=" + dishwasherSafe + '}';
    }
}

/**
 * Service class to handle product search functionality.
 */
class ProductSearchService {

    private List<Product> products;

    // Constructor to initialize the product list
    public ProductSearchService(List<Product> products) {
        this.products = products;
    }

    /**
     * Searches for products based on microwave and dishwasher safety.
     *
     * @param microwaveSafe   Whether the product should be microwave safe.
     * @param dishwasherSafe  Whether the product should be dishwasher safe.
     * @return A list of products matching the criteria.
     */
    public List<Product> searchProducts(boolean microwaveSafe, boolean dishwasherSafe) {
        // Filter products based on the criteria using Java Streams
        return products.stream()
                .filter(product -> product.isMicrowaveSafe() == microwaveSafe && product.isDishwasherSafe() == dishwasherSafe)
                .collect(Collectors.toList());
    }
}

/**
 * Main class to demonstrate the product search functionality.
 */
public class ProductSearchApp {

    public static void main(String[] args) {
        // Initialize a list of products
        List<Product> productList = new ArrayList<>();
        productList.add(new Product("Plate", true, true));
        productList.add(new Product("Cup", true, false));
        productList.add(new Product("Bowl", false, true));
        productList.add(new Product("Pan", false, false));

        // Create the ProductSearchService
        ProductSearchService searchService = new ProductSearchService(productList);

        // Search for products that are both microwave and dishwasher safe
        List<Product> results = searchService.searchProducts(true, true);

        // Display the search results
        System.out.println("Products that are microwave and dishwasher safe:");
        for (Product product : results) {
            System.out.println(product);
        }
    }
}
```
