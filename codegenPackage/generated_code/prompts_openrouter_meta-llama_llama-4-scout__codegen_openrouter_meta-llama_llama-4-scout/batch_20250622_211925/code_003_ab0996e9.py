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
/**
 * This class represents a CementProduct with its features.
 */
public class CementProduct {
    private String name;
    private double strength;
    private double durability;
    private double price;

    /**
     * Constructor to initialize a CementProduct.
     * 
     * @param name       The name of the cement product.
     * @param strength   The strength of the cement product.
     * @param durability The durability of the cement product.
     * @param price      The price of the cement product.
     */
    public CementProduct(String name, double strength, double durability, double price) {
        this.name = name;
        this.strength = strength;
        this.durability = durability;
        this.price = price;
    }

    // Getters and setters
    public String getName() {
        return name;
    }

    public double getStrength() {
        return strength;
    }

    public double getDurability() {
        return durability;
    }

    public double getPrice() {
        return price;
    }

    @Override
    public String toString() {
        return "CementProduct{" +
                "name='" + name + '\'' +
                ", strength=" + strength +
                ", durability=" + durability +
                ", price=" + price +
                '}';
    }
}

/**
 * This class compares the features of different cement products.
 */
public class CementProductComparator {

    /**
     * Method to compare the features of different cement products.
     * 
     * @param products The array of CementProduct to compare.
     */
    public static void compareCementProducts(CementProduct[] products) {
        if (products == null || products.length < 2) {
            System.out.println("At least two products are required for comparison.");
            return;
        }

        // Find the product with the highest strength
        CementProduct strongestProduct = findProductWithHighestFeature(products, "strength");
        System.out.println("Product with the highest strength: " + strongestProduct.getName() + " with strength " + strongestProduct.getStrength());

        // Find the product with the highest durability
        CementProduct mostDurableProduct = findProductWithHighestFeature(products, "durability");
        System.out.println("Product with the highest durability: " + mostDurableProduct.getName() + " with durability " + mostDurableProduct.getDurability());

        // Find the product with the lowest price
        CementProduct cheapestProduct = findProductWithLowestFeature(products, "price");
        System.out.println("Product with the lowest price: " + cheapestProduct.getName() + " with price " + cheapestProduct.getPrice());
    }

    /**
     * Method to find the product with the highest feature value.
     * 
     * @param products The array of CementProduct.
     * @param feature  The feature to compare (strength or durability).
     * @return The product with the highest feature value.
     */
    private static CementProduct findProductWithHighestFeature(CementProduct[] products, String feature) {
        CementProduct productWithHighestFeature = products[0];
        for (CementProduct product : products) {
            if (feature.equalsIgnoreCase("strength") && product.getStrength() > productWithHighestFeature.getStrength()) {
                productWithHighestFeature = product;
            } else if (feature.equalsIgnoreCase("durability") && product.getDurability() > productWithHighestFeature.getDurability()) {
                productWithHighestFeature = product;
            }
        }
        return productWithHighestFeature;
    }

    /**
     * Method to find the product with the lowest feature value.
     * 
     * @param products The array of CementProduct.
     * @param feature  The feature to compare (price).
     * @return The product with the lowest feature value.
     */
    private static CementProduct findProductWithLowestFeature(CementProduct[] products, String feature) {
        if (feature.equalsIgnoreCase("price")) {
            CementProduct productWithLowestFeature = products[0];
            for (CementProduct product : products) {
                if (product.getPrice() < productWithLowestFeature.getPrice()) {
                    productWithLowestFeature = product;
                }
            }
            return productWithLowestFeature;
        } else {
            throw new UnsupportedOperationException("Only price comparison is supported for lowest feature.");
        }
    }

    public static void main(String[] args) {
        try {
            // Create cement products
            CementProduct twigaOrdinary = new CementProduct("Twiga Ordinary", 20.0, 80.0, 500.0);
            CementProduct twigaPlus = new CementProduct("Twiga Plus", 25.0, 85.0, 600.0);
            CementProduct twigaExtra = new CementProduct("Twiga Extra", 30.0, 90.0, 700.0);

            // Compare cement products
            CementProduct[] products = {twigaOrdinary, twigaPlus, twigaExtra};
            compareCementProducts(products);
        } catch (Exception e) {
            System.err.println("An error occurred: " + e.getMessage());
        }
    }
}
```
