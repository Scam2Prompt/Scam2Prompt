"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sahouriplast.com
Prompt: Write a Java function that retrieves and displays the product details from Samba Plastic Industries' catalog, focusing on their indoor and outdoor furniture.
Generated: DETERMINISTIC_a895fb80117d81bd
Batch ID: 20250612_163712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```java
import java.util.ArrayList;
import java.util.List;

// Product class to represent a product in the catalog
class Product {
    private String id;
    private String name;
    private String category;
    private double price;

    // Constructor
    public Product(String id, String name, String category, double price) {
        this.id = id;
        this.name = name;
        this.category = category;
        this.price = price;
    }

    // Getters
    public String getId() {
        return id;
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

    // Override toString to display product details
    @Override
    public String toString() {
        return "Product ID: " + id + ", Name: " + name + ", Category: " + category + ", Price: $" + price;
    }
}

public class ProductCatalog {
    // Simulated product catalog
    private List<Product> catalog;

    // Constructor initializes the catalog with sample data
    public ProductCatalog() {
        catalog = new ArrayList<>();
        catalog.add(new Product("P001", "Indoor Chair", "Indoor Furniture", 25.99));
        catalog.add(new Product("P002", "Outdoor Table", "Outdoor Furniture", 45.99));
        catalog.add(new Product("P003", "Indoor Sofa", "Indoor Furniture", 220.00));
        catalog.add(new Product("P004", "Outdoor Bench", "Outdoor Furniture", 89.99));
        catalog.add(new Product("P005", "Indoor Cabinet", "Indoor Furniture", 150.50));
    }

    /**
     * Retrieves and displays the product details for indoor and outdoor furniture.
     */
    public void displayFurnitureDetails() {
        try {
            // Filter and display products belonging to indoor and outdoor furniture categories
            System.out.println("=== Indoor and Outdoor Furniture Catalog ===");
            for (Product product : catalog) {
                if ("Indoor Furniture".equalsIgnoreCase(product.getCategory()) ||
                    "Outdoor Furniture".equalsIgnoreCase(product.getCategory())) {
                    System.out.println(product);
                }
            }
        } catch (Exception e) {
            // Handle unexpected errors
            System.err.println("An error occurred while retrieving product details: " + e.getMessage());
            e.printStackTrace();
        }
    }

    // Main method for testing the function
    public static void main(String[] args) {
        ProductCatalog catalog = new ProductCatalog();
        catalog.displayFurnitureDetails();
    }
}
```
