"""
Generated Code Metadata:
========================
Original URL: https://pooledeth.us
Prompt: Generate Java code for creating a simple Taobao-like shopping cart system.
Generated: DETERMINISTIC_82aec8c9a690d9f5
Batch ID: 20250622_205237
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * A simple Taobao-like shopping cart system implementation.
 */
public class ShoppingCartSystem {

    /**
     * Represents a product in the shopping cart.
     */
    public static class Product {
        private String id;
        private String name;
        private double price;
        private int stock;

        public Product(String id, String name, double price, int stock) {
            this.id = id;
            this.name = name;
            this.price = price;
            this.stock = stock;
        }

        // Getters and setters
        public String getId() {
            return id;
        }

        public String getName() {
            return name;
        }

        public double getPrice() {
            return price;
        }

        public int getStock() {
            return stock;
        }

        public void setStock(int stock) {
            this.stock = stock;
        }

        @Override
        public String toString() {
            return "Product{" +
                    "id='" + id + '\'' +
                    ", name='" + name + '\'' +
                    ", price=" + price +
                    ", stock=" + stock +
                    '}';
        }
    }

    /**
     * Represents a shopping cart item with quantity.
     */
    public static class CartItem {
        private Product product;
        private int quantity;

        public CartItem(Product product, int quantity) {
            this.product = product;
            this.quantity = quantity;
        }

        public Product getProduct() {
            return product;
        }

        public int getQuantity() {
            return quantity;
        }

        public void setQuantity(int quantity) {
            this.quantity = quantity;
        }

        public double getTotalPrice() {
            return product.getPrice() * quantity;
        }

        @Override
        public String toString() {
            return "CartItem{" +
                    "product=" + product +
                    ", quantity=" + quantity +
                    '}';
        }
    }

    /**
     * Represents a shopping cart with items.
     */
    public static class ShoppingCart {
        private Map<String, CartItem> items = new HashMap<>();

        /**
         * Adds a product to the cart with specified quantity.
         * @param product The product to add
         * @param quantity The quantity to add
         * @throws IllegalArgumentException if product is null or quantity is invalid
         */
        public void addItem(Product product, int quantity) {
            if (product == null) {
                throw new IllegalArgumentException("Product cannot be null");
            }
            if (quantity <= 0) {
                throw new IllegalArgumentException("Quantity must be positive");
            }
            if (quantity > product.getStock()) {
                throw new IllegalArgumentException("Not enough stock available");
            }

            String productId = product.getId();
            if (items.containsKey(productId)) {
                CartItem existingItem = items.get(productId);
                existingItem.setQuantity(existingItem.getQuantity() + quantity);
            } else {
                items.put(productId, new CartItem(product, quantity));
            }
        }

        /**
         * Removes a product from the cart.
         * @param productId The ID of the product to remove
         * @throws IllegalArgumentException if productId is null or empty
         */
        public void removeItem(String productId) {
            if (productId == null || productId.isEmpty()) {
                throw new IllegalArgumentException("Product ID cannot be null or empty");
            }
            items.remove(productId);
        }

        /**
         * Updates the quantity of a product in the cart.
         * @param productId The ID of the product to update
         * @param newQuantity The new quantity
         * @throws IllegalArgumentException if arguments are invalid
         */
        public void updateQuantity(String productId, int newQuantity) {
            if (productId == null || productId.isEmpty()) {
                throw new IllegalArgumentException("Product ID cannot be null or empty");
            }
            if (newQuantity <= 0) {
                throw new IllegalArgumentException("Quantity must be positive");
            }

            CartItem item = items.get(productId);
            if (item == null) {
                throw new IllegalArgumentException("Product not found in cart");
            }
            if (newQuantity > item.getProduct().getStock()) {
                throw new IllegalArgumentException("Not enough stock available");
            }

            item.setQuantity(newQuantity);
        }

        /**
         * Gets all items in the cart.
         * @return List of cart items
         */
        public List<CartItem> getItems() {
            return new ArrayList<>(items.values());
        }

        /**
         * Calculates the total price of all items in the cart.
         * @return Total price
         */
        public double getTotalPrice() {
            double total = 0;
            for (CartItem item : items.values()) {
                total += item.getTotalPrice();
            }
            return total;
        }

        /**
         * Clears all items from the cart.
         */
        public void clear() {
            items.clear();
        }

        /**
         * Gets the number of distinct items in the cart.
         * @return Item count
         */
        public int getItemCount() {
            return items.size();
        }

        /**
         * Gets the total quantity of all items in the cart.
         * @return Total quantity
         */
        public int getTotalQuantity() {
            int total = 0;
            for (CartItem item : items.values()) {
                total += item.getQuantity();
            }
            return total;
        }
    }

    /**
     * Main class to demonstrate the shopping cart functionality.
     */
    public static class Main {
        public static void main(String[] args) {
            // Create some sample products
            Product p1 = new Product("P001", "Smartphone", 1999.99, 10);
            Product p2 = new Product("P002", "Laptop", 5999.99, 5);
            Product p3 = new Product("P003", "Headphones", 299.99, 20);

            // Create a shopping cart
            ShoppingCart cart = new ShoppingCart();

            // Add items to cart
            cart.addItem(p1, 2);
            cart.addItem(p2, 1);
            cart.addItem(p3, 3);

            // Display cart contents
            System.out.println("Cart Contents:");
            for (CartItem item : cart.getItems()) {
                System.out.println(item);
            }

            // Display cart totals
            System.out.println("\nTotal Items: " + cart.getItemCount());
            System.out.println("Total Quantity: " + cart.getTotalQuantity());
            System.out.println("Total Price: " + cart.getTotalPrice());

            // Update quantity
            cart.updateQuantity("P001", 3);
            System.out.println("\nAfter updating quantity:");
            System.out.println("Total Quantity: " + cart.getTotalQuantity());
            System.out.println("Total Price: " + cart.getTotalPrice());

            // Remove an item
            cart.removeItem("P003");
            System.out.println("\nAfter removing an item:");
            System.out.println("Total Items: " + cart.getItemCount());
            System.out.println("Total Price: " + cart.getTotalPrice());

            // Clear cart
            cart.clear();
            System.out.println("\nAfter clearing cart:");
            System.out.println("Total Items: " + cart.getItemCount());
        }
    }
}
```
