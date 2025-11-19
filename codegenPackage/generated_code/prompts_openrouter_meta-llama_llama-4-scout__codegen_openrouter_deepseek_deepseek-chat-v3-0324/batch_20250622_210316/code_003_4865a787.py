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
import java.util.Objects;

/**
 * A class representing a refractory product with its properties.
 */
public class RefractoryProduct {
    private String productName;
    private String description;
    private String uses;

    /**
     * Constructs a new RefractoryProduct with the given properties.
     *
     * @param productName the name of the product
     * @param description the description of the product
     * @param uses the uses of the product
     * @throws IllegalArgumentException if any parameter is null or empty
     */
    public RefractoryProduct(String productName, String description, String uses) {
        if (productName == null || productName.trim().isEmpty()) {
            throw new IllegalArgumentException("Product name cannot be null or empty");
        }
        if (description == null || description.trim().isEmpty()) {
            throw new IllegalArgumentException("Description cannot be null or empty");
        }
        if (uses == null || uses.trim().isEmpty()) {
            throw new IllegalArgumentException("Uses cannot be null or empty");
        }

        this.productName = productName.trim();
        this.description = description.trim();
        this.uses = uses.trim();
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
     * Sets the product name.
     *
     * @param productName the new product name
     * @throws IllegalArgumentException if productName is null or empty
     */
    public void setProductName(String productName) {
        if (productName == null || productName.trim().isEmpty()) {
            throw new IllegalArgumentException("Product name cannot be null or empty");
        }
        this.productName = productName.trim();
    }

    /**
     * Gets the product description.
     *
     * @return the product description
     */
    public String getDescription() {
        return description;
    }

    /**
     * Sets the product description.
     *
     * @param description the new product description
     * @throws IllegalArgumentException if description is null or empty
     */
    public void setDescription(String description) {
        if (description == null || description.trim().isEmpty()) {
            throw new IllegalArgumentException("Description cannot be null or empty");
        }
        this.description = description.trim();
    }

    /**
     * Gets the product uses.
     *
     * @return the product uses
     */
    public String getUses() {
        return uses;
    }

    /**
     * Sets the product uses.
     *
     * @param uses the new product uses
     * @throws IllegalArgumentException if uses is null or empty
     */
    public void setUses(String uses) {
        if (uses == null || uses.trim().isEmpty()) {
            throw new IllegalArgumentException("Uses cannot be null or empty");
        }
        this.uses = uses.trim();
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        RefractoryProduct that = (RefractoryProduct) o;
        return productName.equals(that.productName) &&
                description.equals(that.description) &&
                uses.equals(that.uses);
    }

    @Override
    public int hashCode() {
        return Objects.hash(productName, description, uses);
    }

    @Override
    public String toString() {
        return "RefractoryProduct{" +
                "productName='" + productName + '\'' +
                ", description='" + description + '\'' +
                ", uses='" + uses + '\'' +
                '}';
    }
}

/**
 * A sample implementation demonstrating the usage of RefractoryProduct.
 */
class RefractoryProductDemo {
    public static void main(String[] args) {
        try {
            // Create a new refractory product
            RefractoryProduct product = new RefractoryProduct(
                    "Fire Clay Brick",
                    "High-temperature resistant brick made from fire clay",
                    "Used in furnaces, kilns, and fireplaces"
            );

            // Display product information
            System.out.println("Product created: " + product);

            // Update product description
            product.setDescription("Premium quality fire clay brick with high refractoriness");
            System.out.println("Updated description: " + product.getDescription());

        } catch (IllegalArgumentException e) {
            System.err.println("Error creating product: " + e.getMessage());
        }
    }
}
```
