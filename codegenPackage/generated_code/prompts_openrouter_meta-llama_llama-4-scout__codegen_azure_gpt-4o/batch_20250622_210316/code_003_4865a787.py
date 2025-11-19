"""
Generated Code Metadata:
========================
Original URL: https://aprisacv.com.mx
Prompt: "Design a data structure in Java to represent refractory products, including their properties like product name, description, and uses, and provide a sample implementation."
Generated: DETERMINISTIC_4865a7870ef8567c
Batch ID: 20250622_210316
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
 * Represents a refractory product with its properties.
 */
public class RefractoryProduct {
    private String productName;
    private String description;
    private List<String> uses;

    /**
     * Constructor to initialize a refractory product.
     *
     * @param productName Name of the product.
     * @param description Description of the product.
     * @param uses        List of uses for the product.
     */
    public RefractoryProduct(String productName, String description, List<String> uses) {
        if (productName == null || productName.isEmpty()) {
            throw new IllegalArgumentException("Product name cannot be null or empty.");
        }
        if (description == null || description.isEmpty()) {
            throw new IllegalArgumentException("Description cannot be null or empty.");
        }
        if (uses == null || uses.isEmpty()) {
            throw new IllegalArgumentException("Uses cannot be null or empty.");
        }

        this.productName = productName;
        this.description = description;
        this.uses = new ArrayList<>(uses);
    }

    /**
     * Gets the product name.
     *
     * @return Product name.
     */
    public String getProductName() {
        return productName;
    }

    /**
     * Sets the product name.
     *
     * @param productName Name of the product.
     */
    public void setProductName(String productName) {
        if (productName == null || productName.isEmpty()) {
            throw new IllegalArgumentException("Product name cannot be null or empty.");
        }
        this.productName = productName;
    }

    /**
     * Gets the description of the product.
     *
     * @return Product description.
     */
    public String getDescription() {
        return description;
    }

    /**
     * Sets the description of the product.
     *
     * @param description Description of the product.
     */
    public void setDescription(String description) {
        if (description == null || description.isEmpty()) {
            throw new IllegalArgumentException("Description cannot be null or empty.");
        }
        this.description = description;
    }

    /**
     * Gets the list of uses for the product.
     *
     * @return List of uses.
     */
    public List<String> getUses() {
        return new ArrayList<>(uses);
    }

    /**
     * Adds a new use to the product.
     *
     * @param use A new use for the product.
     */
    public void addUse(String use) {
        if (use == null || use.isEmpty()) {
            throw new IllegalArgumentException("Use cannot be null or empty.");
        }
        this.uses.add(use);
    }

    /**
     * Removes a use from the product.
     *
     * @param use The use to be removed.
     * @return True if the use was removed, false otherwise.
     */
    public boolean removeUse(String use) {
        return this.uses.remove(use);
    }

    /**
     * Provides a string representation of the refractory product.
     *
     * @return String representation of the product.
     */
    @Override
    public String toString() {
        return "RefractoryProduct{" +
                "productName='" + productName + '\'' +
                ", description='" + description + '\'' +
                ", uses=" + uses +
                '}';
    }

    /**
     * Sample implementation to demonstrate the usage of the RefractoryProduct class.
     */
    public static void main(String[] args) {
        try {
            // Create a list of uses for the product
            List<String> uses = new ArrayList<>();
            uses.add("High-temperature furnaces");
            uses.add("Kilns");
            uses.add("Incinerators");

            // Create a refractory product
            RefractoryProduct product = new RefractoryProduct(
                    "Firebrick",
                    "A brick capable of withstanding high temperatures.",
                    uses
            );

            // Print the product details
            System.out.println(product);

            // Add a new use
            product.addUse("Pizza ovens");
            System.out.println("After adding a new use: " + product);

            // Remove a use
            product.removeUse("Kilns");
            System.out.println("After removing a use: " + product);

        } catch (IllegalArgumentException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```
