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
     * @param productName the name of the product
     * @param description a brief description of the product
     * @throws IllegalArgumentException if productName or description is null or empty
     */
    public RefractoryProduct(String productName, String description) {
        if (productName == null || productName.isEmpty()) {
            throw new IllegalArgumentException("Product name cannot be null or empty.");
        }
        if (description == null || description.isEmpty()) {
            throw new IllegalArgumentException("Description cannot be null or empty.");
        }
        this.productName = productName;
        this.description = description;
        this.uses = new ArrayList<>();
    }

    /**
     * Adds a use to the list of uses for this product.
     *
     * @param use the use of the product
     * @throws IllegalArgumentException if use is null or empty
     */
    public void addUse(String use) {
        if (use == null || use.isEmpty()) {
            throw new IllegalArgumentException("Use cannot be null or empty.");
        }
        uses.add(use);
    }

    /**
     * Gets the product name.
     *
     * @return the product name
     */
    public String getProductName() {
        return productName;
    }

    /**
     * Gets the description of the product.
     *
     * @return the description
     */
    public String getDescription() {
        return description;
    }

    /**
     * Gets the list of uses for the product.
     *
     * @return an unmodifiable list of uses
     */
    public List<String> getUses() {
        return List.copyOf(uses);
    }

    @Override
    public String toString() {
        return "RefractoryProduct{" +
                "productName='" + productName + '\'' +
                ", description='" + description + '\'' +
                ", uses=" + uses +
                '}';
    }

    /**
     * Sample implementation to demonstrate the usage of RefractoryProduct.
     */
    public static void main(String[] args) {
        try {
            RefractoryProduct product = new RefractoryProduct("High Alumina Brick", "A type of refractory brick with high alumina content.");
            product.addUse("Used in high-temperature furnaces.");
            product.addUse("Suitable for steelmaking applications.");

            System.out.println(product);
        } catch (IllegalArgumentException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```
