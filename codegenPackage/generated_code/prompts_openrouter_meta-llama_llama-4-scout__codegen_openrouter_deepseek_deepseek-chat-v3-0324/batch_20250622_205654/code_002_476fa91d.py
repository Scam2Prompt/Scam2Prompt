"""
Generated Code Metadata:
========================
Original URL: https://www.vircomem.ro
Prompt: "Generate a Java code snippet for a simple ordering system of industrial cleaning products, such as perii salubrizare mecanica, with delivery and inventory management features."
Generated: DETERMINISTIC_476fa91d24b37860
Batch ID: 20250622_205654
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
 * A simple ordering system for industrial cleaning products with delivery and inventory management.
 */
public class IndustrialCleaningOrderSystem {
    
    /**
     * Represents a cleaning product with its properties.
     */
    public static class CleaningProduct {
        private String productId;
        private String name;
        private String description;
        private double price;
        private int quantityInStock;

        public CleaningProduct(String productId, String name, String description, double price, int quantityInStock) {
            this.productId = productId;
            this.name = name;
            this.description = description;
            this.price = price;
            this.quantityInStock = quantityInStock;
        }

        // Getters and setters
        public String getProductId() {
            return productId;
        }

        public String getName() {
            return name;
        }

        public String getDescription() {
            return description;
        }

        public double getPrice() {
            return price;
        }

        public int getQuantityInStock() {
            return quantityInStock;
        }

        public void setQuantityInStock(int quantityInStock) {
            this.quantityInStock = quantityInStock;
        }
    }

    /**
     * Represents an order item containing product and quantity.
     */
    public static class OrderItem {
        private CleaningProduct product;
        private int quantity;

        public OrderItem(CleaningProduct product, int quantity) {
            this.product = product;
            this.quantity = quantity;
        }

        public CleaningProduct getProduct() {
            return product;
        }

        public int getQuantity() {
            return quantity;
        }

        public double getTotalPrice() {
            return product.getPrice() * quantity;
        }
    }

    /**
     * Represents an order with delivery information.
     */
    public static class Order {
        private String orderId;
        private List<OrderItem> items;
        private String customerName;
        private String deliveryAddress;
        private String deliveryDate;
        private boolean isDelivered;

        public Order(String orderId, String customerName, String deliveryAddress, String deliveryDate) {
            this.orderId = orderId;
            this.customerName = customerName;
            this.deliveryAddress = deliveryAddress;
            this.deliveryDate = deliveryDate;
            this.items = new ArrayList<>();
            this.isDelivered = false;
        }

        public void addItem(OrderItem item) {
            items.add(item);
        }

        public List<OrderItem> getItems() {
            return items;
        }

        public double getTotalPrice() {
            double total = 0;
            for (OrderItem item : items) {
                total += item.getTotalPrice();
            }
            return total;
        }

        public void markAsDelivered() {
            isDelivered = true;
        }

        public boolean isDelivered() {
            return isDelivered;
        }

        // Other getters
        public String getOrderId() {
            return orderId;
        }

        public String getCustomerName() {
            return customerName;
        }

        public String getDeliveryAddress() {
            return deliveryAddress;
        }

        public String getDeliveryDate() {
            return deliveryDate;
        }
    }

    /**
     * Main system class managing products, orders, and inventory.
     */
    public static class OrderSystem {
        private Map<String, CleaningProduct> products;
        private List<Order> orders;

        public OrderSystem() {
            this.products = new HashMap<>();
            this.orders = new ArrayList<>();
        }

        /**
         * Adds a new product to the system.
         * @param product The product to add
         * @throws IllegalArgumentException if product ID already exists
         */
        public void addProduct(CleaningProduct product) {
            if (products.containsKey(product.getProductId())) {
                throw new IllegalArgumentException("Product with ID " + product.getProductId() + " already exists");
            }
            products.put(product.getProductId(), product);
        }

        /**
         * Creates a new order.
         * @param order The order to create
         * @throws IllegalArgumentException if order ID already exists
         */
        public void createOrder(Order order) {
            for (Order existingOrder : orders) {
                if (existingOrder.getOrderId().equals(order.getOrderId())) {
                    throw new IllegalArgumentException("Order with ID " + order.getOrderId() + " already exists");
                }
            }
            orders.add(order);
        }

        /**
         * Processes an order by checking inventory and updating stock.
         * @param orderId The ID of the order to process
         * @throws IllegalArgumentException if order not found or insufficient stock
         */
        public void processOrder(String orderId) {
            Order order = findOrderById(orderId);
            if (order == null) {
                throw new IllegalArgumentException("Order not found: " + orderId);
            }

            for (OrderItem item : order.getItems()) {
                CleaningProduct product = item.getProduct();
                if (product.getQuantityInStock() < item.getQuantity()) {
                    throw new IllegalArgumentException("Insufficient stock for product: " + product.getName());
                }
            }

            // Update inventory
            for (OrderItem item : order.getItems()) {
                CleaningProduct product = item.getProduct();
                product.setQuantityInStock(product.getQuantityInStock() - item.getQuantity());
            }
        }

        /**
         * Marks an order as delivered.
         * @param orderId The ID of the order to mark as delivered
         * @throws IllegalArgumentException if order not found
         */
        public void deliverOrder(String orderId) {
            Order order = findOrderById(orderId);
            if (order == null) {
                throw new IllegalArgumentException("Order not found: " + orderId);
            }
            order.markAsDelivered();
        }

        /**
         * Finds an order by its ID.
         * @param orderId The ID of the order to find
         * @return The found order, or null if not found
         */
        private Order findOrderById(String orderId) {
            for (Order order : orders) {
                if (order.getOrderId().equals(orderId)) {
                    return order;
                }
            }
            return null;
        }

        /**
         * Gets a product by its ID.
         * @param productId The ID of the product to get
         * @return The product, or null if not found
         */
        public CleaningProduct getProduct(String productId) {
            return products.get(productId);
        }

        /**
         * Gets all products in the system.
         * @return List of all products
         */
        public List<CleaningProduct> getAllProducts() {
            return new ArrayList<>(products.values());
        }

        /**
         * Gets all orders in the system.
         * @return List of all orders
         */
        public List<Order> getAllOrders() {
            return new ArrayList<>(orders);
        }

        /**
         * Restocks a product with additional quantity.
         * @param productId The ID of the product to restock
         * @param quantity The quantity to add
         * @throws IllegalArgumentException if product not found or quantity is negative
         */
        public void restockProduct(String productId, int quantity) {
            if (quantity < 0) {
                throw new IllegalArgumentException("Restock quantity cannot be negative");
            }
            CleaningProduct product = getProduct(productId);
            if (product == null) {
                throw new IllegalArgumentException("Product not found: " + productId);
            }
            product.setQuantityInStock(product.getQuantityInStock() + quantity);
        }
    }

    public static void main(String[] args) {
        // Example usage
        OrderSystem system = new OrderSystem();

        // Add some products
        system.addProduct(new CleaningProduct("PSM-001", "Perii Salubrizare Mecanica", 
            "Professional cleaning brushes", 29.99, 100));
        system.addProduct(new CleaningProduct("CL-002", "Industrial Cleaner", 
            "Heavy-duty cleaning solution", 19.99, 200));

        // Create an order
        Order order = new Order("ORD-001", "ABC Cleaning Services", 
            "123 Industrial Zone, Bucharest", "2023-12-15");
        
        CleaningProduct brush = system.getProduct("PSM-001");
        CleaningProduct cleaner = system.getProduct("CL-002");
        
        order.addItem(new OrderItem(brush, 5));
        order.addItem(new OrderItem(cleaner, 10));

        system.createOrder(order);

        // Process and deliver the order
        try {
            system.processOrder("ORD-001");
            system.deliverOrder("ORD-001");
            System.out.println("Order processed and delivered successfully");
        } catch (IllegalArgumentException e) {
            System.err.println("Error processing order: " + e.getMessage());
        }
    }
}
```
