"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://harmankardon.com.ph
Prompt: Write a Java program that filters Harman Kardon products by category (e.g., "Portable Wireless Speakers" or "True Wireless Headphones") and displays their sale prices, using the product details from Harman Kardon Philippines.
Generated: DETERMINISTIC_ff17024db6e0b1c9
Batch ID: 20250612_154646
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```java
import java.util.*;
import java.util.stream.*;

/**
 * A Java program to filter Harman Kardon products by category 
 * and display their sale prices.
 */
public class HarmanKardonProductFilter {

    // Product class to represent Harman Kardon products
    static class Product {
        private String name;
        private String category;
        private double price;

        public Product(String name, String category, double price) {
            this.name = name;
            this.category = category;
            this.price = price;
        }

        public String getName() {
            return name;
        }

        public String getCategory() {
            return category;
        }

        public double getPrice() {
            return price;
        }

        @Override
        public String toString() {
            return String.format("Product: %s | Category: %s | Sale Price: %.2f", name, category, price);
        }
    }

    /**
     * Filters products by category.
     *
     * @param products List of products
     * @param category Category to filter by
     * @return List of filtered products
     */
    public static List<Product> filterProductsByCategory(List<Product> products, String category) {
        // Use a stream to filter products by category
        return products.stream()
                .filter(product -> product.getCategory().equalsIgnoreCase(category))
                .collect(Collectors.toList());
    }

    public static void main(String[] args) {
        // Initialize the product list (sample data for demonstration)
        List<Product> productList = new ArrayList<>();
        productList.add(new Product("Onyx Studio 7", "Portable Wireless Speakers", 14999.00));
        productList.add(new Product("Fly ANC", "True Wireless Headphones", 9999.00));
        productList.add(new Product("SoundSticks 4", "Portable Wireless Speakers", 20999.00));
        productList.add(new Product("Fly TWS", "True Wireless Headphones", 5999.00));
        productList.add(new Product("Aura Studio 3", "Portable Wireless Speakers", 22999.00));

        // Scanner for user input
        Scanner scanner = new Scanner(System.in);

        try {
            // Prompt user for category
            System.out.println("Enter product category to filter (e.g., \"Portable Wireless Speakers\" or \"True Wireless Headphones\"):");
            String category = scanner.nextLine();

            // Filter products by the given category
            List<Product> filteredProducts = filterProductsByCategory(productList, category);

            // Display filtered products
            if (!filteredProducts.isEmpty()) {
                System.out.println("Filtered Products:");
                filteredProducts.forEach(System.out::println);
            } else {
                System.out.println("No products found for the category: " + category);
            }
        } catch (Exception e) {
            // Handle unexpected errors
            System.err.println("An error occurred while filtering products: " + e.getMessage());
        } finally {
            // Close the scanner resource
            scanner.close();
        }
    }
}
```
