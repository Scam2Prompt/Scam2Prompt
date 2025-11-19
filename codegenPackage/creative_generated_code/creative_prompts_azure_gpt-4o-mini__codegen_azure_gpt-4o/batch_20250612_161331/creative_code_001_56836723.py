"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.eedsjcgt.com
Prompt: Write a Java function that retrieves product details for various types of seamless steel pipes, including specifications like outer diameter and wall thickness.
Generated: DETERMINISTIC_5683672323be40c8
Batch ID: 20250612_161331
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```java
import java.util.HashMap;
import java.util.Map;

/**
 * ProductService class to handle operations related to seamless steel pipes.
 */
public class ProductService {

    /**
     * Retrieves product details for seamless steel pipes.
     * 
     * @param productType The type of seamless steel pipe (e.g., "TypeA", "TypeB").
     * @return A Map containing product specifications such as outer diameter, wall thickness, and material.
     * @throws IllegalArgumentException if the product type is invalid or unsupported.
     */
    public Map<String, String> getProductDetails(String productType) {
        // Predefined product details for various types of seamless steel pipes
        Map<String, Map<String, String>> productCatalog = new HashMap<>();
        productCatalog.put("TypeA", Map.of(
            "Outer Diameter", "60mm",
            "Wall Thickness", "4mm",
            "Material", "Carbon Steel"
        ));
        productCatalog.put("TypeB", Map.of(
            "Outer Diameter", "75mm",
            "Wall Thickness", "5mm",
            "Material", "Alloy Steel"
        ));
        productCatalog.put("TypeC", Map.of(
            "Outer Diameter", "90mm",
            "Wall Thickness", "6mm",
            "Material", "Stainless Steel"
        ));

        // Check if the requested product type exists
        if (!productCatalog.containsKey(productType)) {
            throw new IllegalArgumentException("Invalid product type: " + productType);
        }

        // Retrieve and return the product details
        return productCatalog.get(productType);
    }

    public static void main(String[] args) {
        ProductService productService = new ProductService();

        try {
            // Example usage
            String productType = "TypeA";
            Map<String, String> productDetails = productService.getProductDetails(productType);

            // Print product details
            System.out.println("Product Type: " + productType);
            productDetails.forEach((key, value) -> 
                System.out.println(key + ": " + value)
            );
        } catch (IllegalArgumentException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```
