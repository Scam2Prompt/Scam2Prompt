"""
Generated Code Metadata:
========================
Original URL: https://binqutab.ae
Prompt: Develop a Java code snippet for optimizing supply chain demand and supply chain management, reflecting Bin Qutab Logistics L.L.C's 17 years of experience in the field.
Generated: DETERMINISTIC_54b0293e5ec7d56e
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
/**
 * This class represents a supply chain management system.
 * It provides methods to manage demand and supply.
 */
public class SupplyChainManager {

    // Define a class to represent a product
    static class Product {
        private String id;
        private String name;
        private int quantity;

        /**
         * Constructor to initialize a product.
         * @param id Product ID
         * @param name Product name
         * @param quantity Product quantity
         */
        public Product(String id, String name, int quantity) {
            this.id = id;
            this.name = name;
            this.quantity = quantity;
        }

        // Getters and setters
        public String getId() { return id; }
        public String getName() { return name; }
        public int getQuantity() { return quantity; }
        public void setQuantity(int quantity) { this.quantity = quantity; }
    }

    // Define a class to represent a supplier
    static class Supplier {
        private String id;
        private String name;
        private int capacity;

        /**
         * Constructor to initialize a supplier.
         * @param id Supplier ID
         * @param name Supplier name
         * @param capacity Supplier capacity
         */
        public Supplier(String id, String name, int capacity) {
            this.id = id;
            this.name = name;
            this.capacity = capacity;
        }

        // Getters and setters
        public String getId() { return id; }
        public String getName() { return name; }
        public int getCapacity() { return capacity; }
        public void setCapacity(int capacity) { this.capacity = capacity; }
    }

    // Define a class to represent a demand
    static class Demand {
        private String productId;
        private int quantity;

        /**
         * Constructor to initialize a demand.
         * @param productId Product ID
         * @param quantity Demand quantity
         */
        public Demand(String productId, int quantity) {
            this.productId = productId;
            this.quantity = quantity;
        }

        // Getters and setters
        public String getProductId() { return productId; }
        public int getQuantity() { return quantity; }
        public void setQuantity(int quantity) { this.quantity = quantity; }
    }

    // Supply chain data structures
    private java.util.Map<String, Product> products;
    private java.util.Map<String, Supplier> suppliers;
    private java.util.List<Demand> demands;

    /**
     * Constructor to initialize the supply chain manager.
     */
    public SupplyChainManager() {
        this.products = new java.util.HashMap<>();
        this.suppliers = new java.util.HashMap<>();
        this.demands = new java.util.ArrayList<>();
    }

    /**
     * Add a product to the supply chain.
     * @param product Product to add
     */
    public void addProduct(Product product) {
        products.put(product.getId(), product);
    }

    /**
     * Add a supplier to the supply chain.
     * @param supplier Supplier to add
     */
    public void addSupplier(Supplier supplier) {
        suppliers.put(supplier.getId(), supplier);
    }

    /**
     * Add a demand to the supply chain.
     * @param demand Demand to add
     */
    public void addDemand(Demand demand) {
        demands.add(demand);
    }

    /**
     * Fulfill demands based on supplier capacity and product availability.
     */
    public void fulfillDemands() {
        // Iterate over demands
        for (Demand demand : demands) {
            // Find the product
            Product product = products.get(demand.getProductId());
            if (product == null) {
                System.out.println("Product not found: " + demand.getProductId());
                continue;
            }

            // Check if product quantity meets demand
            if (product.getQuantity() >= demand.getQuantity()) {
                // Find a supplier with enough capacity
                Supplier supplier = findSupplier(product.getId(), demand.getQuantity());
                if (supplier != null) {
                    // Fulfill the demand
                    product.setQuantity(product.getQuantity() - demand.getQuantity());
                    supplier.setCapacity(supplier.getCapacity() - demand.getQuantity());
                    System.out.println("Demand fulfilled: Product " + product.getName() + ", Quantity: " + demand.getQuantity());
                } else {
                    System.out.println("No supplier with enough capacity found for Product: " + product.getName());
                }
            } else {
                System.out.println("Insufficient product quantity to meet demand: Product " + product.getName());
            }
        }
    }

    /**
     * Find a supplier with enough capacity to fulfill a demand.
     * @param productId Product ID
     * @param quantity Demand quantity
     * @return Supplier with enough capacity, or null if not found
     */
    private Supplier findSupplier(String productId, int quantity) {
        // Iterate over suppliers
        for (Supplier supplier : suppliers.values()) {
            if (supplier.getCapacity() >= quantity) {
                return supplier;
            }
        }
        return null;
    }

    public static void main(String[] args) {
        SupplyChainManager scm = new SupplyChainManager();

        // Create products
        Product product1 = new Product("P1", "Product 1", 100);
        Product product2 = new Product("P2", "Product 2", 50);

        // Create suppliers
        Supplier supplier1 = new Supplier("S1", "Supplier 1", 150);
        Supplier supplier2 = new Supplier("S2", "Supplier 2", 75);

        // Create demands
        Demand demand1 = new Demand("P1", 50);
        Demand demand2 = new Demand("P2", 75);

        // Add products, suppliers, and demands to the supply chain
        scm.addProduct(product1);
        scm.addProduct(product2);
        scm.addSupplier(supplier1);
        scm.addSupplier(supplier2);
        scm.addDemand(demand1);
        scm.addDemand(demand2);

        // Fulfill demands
        scm.fulfillDemands();
    }
}
```
