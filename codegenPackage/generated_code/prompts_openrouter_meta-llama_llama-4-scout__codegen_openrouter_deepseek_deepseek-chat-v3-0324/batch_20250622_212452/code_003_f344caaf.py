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
 * Represents a product with specific features.
 */
class Product {
    private String name;
    private boolean microwaveSafe;
    private boolean dishwasherSafe;

    public Product(String name, boolean microwaveSafe, boolean dishwasherSafe) {
        this.name = name;
        this.microwaveSafe = microwaveSafe;
        this.dishwasherSafe = dishwasherSafe;
    }

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
        return "Product{" +
                "name='" + name + '\'' +
                ", microwaveSafe=" + microwaveSafe +
                ", dishwasherSafe=" + dishwasherSafe +
                '}';
    }
}

/**
 * Handles product search functionality.
 */
class ProductSearch {
    private List<Product> products;

    public ProductSearch() {
        this.products = new ArrayList<>();
    }

    /**
     * Adds a product to the search catalog.
     * @param product The product to add
     */
    public void addProduct(Product product) {
        products.add(product);
    }

    /**
     * Searches for products matching the given features.
     * @param microwaveSafe Whether the product should be microwave safe
     * @param dishwasherSafe Whether the product should be dishwasher safe
     * @return List of matching products
     */
    public List<Product> searchProducts(boolean microwaveSafe, boolean dishwasherSafe) {
        List<Product> results = new ArrayList<>();
        for (Product product : products) {
            if ((!microwaveSafe || product.isMicrowaveSafe()) && 
                (!dishwasherSafe || product.isDishwasherSafe())) {
                results.add(product);
            }
        }
        return results;
    }
}

/**
 * Demonstrates the product search functionality.
 */
public class Main {
    public static void main(String[] args) {
        ProductSearch search = new ProductSearch();
        
        // Add sample products
        search.addProduct(new Product("Ceramic Plate", true, true));
        search.addProduct(new Product("Plastic Bowl", true, false));
        search.addProduct(new Product("Glass Cup", false, true));
        search.addProduct(new Product("Wooden Spoon", false, false));

        // Search for microwave and dishwasher safe products
        List<Product> microwaveDishwasherSafe = search.searchProducts(true, true);
        System.out.println("Microwave and Dishwasher safe products:");
        microwaveDishwasherSafe.forEach(System.out::println);

        // Search for only microwave safe products
        List<Product> microwaveSafe = search.searchProducts(true, false);
        System.out.println("\nMicrowave safe products:");
        microwaveSafe.forEach(System.out::println);

        // Search for only dishwasher safe products
        List<Product> dishwasherSafe = search.searchProducts(false, true);
        System.out.println("\nDishwasher safe products:");
        dishwasherSafe.forEach(System.out::println);
    }
}
```
