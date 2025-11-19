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
import java.util.List;
import java.util.Scanner;

/**
 * Represents an industrial cleaning product.
 */
class Product {
    private String name;
    private double price;
    private int quantity;

    /**
     * Constructs a Product object.
     * 
     * @param name     the product name
     * @param price    the product price
     * @param quantity the product quantity
     */
    public Product(String name, double price, int quantity) {
        this.name = name;
        this.price = price;
        this.quantity = quantity;
    }

    // Getters and setters
    public String getName() {
        return name;
    }

    public double getPrice() {
        return price;
    }

    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }
}

/**
 * Represents an order.
 */
class Order {
    private Product product;
    private int orderedQuantity;

    /**
     * Constructs an Order object.
     * 
     * @param product         the ordered product
     * @param orderedQuantity the quantity ordered
     */
    public Order(Product product, int orderedQuantity) {
        this.product = product;
        this.orderedQuantity = orderedQuantity;
    }

    // Getters
    public Product getProduct() {
        return product;
    }

    public int getOrderedQuantity() {
        return orderedQuantity;
    }
}

/**
 * Manages the inventory and delivery of industrial cleaning products.
 */
public class OrderingSystem {
    private List<Product> inventory;
    private List<Order> orders;

    /**
     * Constructs an OrderingSystem object.
     */
    public OrderingSystem() {
        this.inventory = new ArrayList<>();
        this.orders = new ArrayList<>();
    }

    /**
     * Adds a product to the inventory.
     * 
     * @param product the product to add
     */
    public void addProduct(Product product) {
        inventory.add(product);
    }

    /**
     * Places an order for a product.
     * 
     * @param productName     the name of the product to order
     * @param orderedQuantity the quantity to order
     * @throws Exception if the product is not in stock or the quantity exceeds the available stock
     */
    public void placeOrder(String productName, int orderedQuantity) throws Exception {
        Product product = getProduct(productName);
        if (product == null) {
            throw new Exception("Product not found");
        }
        if (orderedQuantity > product.getQuantity()) {
            throw new Exception("Insufficient stock");
        }
        product.setQuantity(product.getQuantity() - orderedQuantity);
        orders.add(new Order(product, orderedQuantity));
    }

    /**
     * Delivers an order.
     * 
     * @param productName the name of the product to deliver
     * @throws Exception if the order is not found
     */
    public void deliverOrder(String productName) throws Exception {
        Order order = getOrder(productName);
        if (order == null) {
            throw new Exception("Order not found");
        }
        orders.remove(order);
        System.out.println("Order delivered");
    }

    /**
     * Gets a product by name.
     * 
     * @param name the product name
     * @return the product, or null if not found
     */
    private Product getProduct(String name) {
        for (Product product : inventory) {
            if (product.getName().equals(name)) {
                return product;
            }
        }
        return null;
    }

    /**
     * Gets an order by product name.
     * 
     * @param productName the product name
     * @return the order, or null if not found
     */
    private Order getOrder(String productName) {
        for (Order order : orders) {
            if (order.getProduct().getName().equals(productName)) {
                return order;
            }
        }
        return null;
    }

    /**
     * Prints the current inventory.
     */
    public void printInventory() {
        System.out.println("Current Inventory:");
        for (Product product : inventory) {
            System.out.println(product.getName() + ": " + product.getQuantity());
        }
    }

    /**
     * Prints the current orders.
     */
    public void printOrders() {
        System.out.println("Current Orders:");
        for (Order order : orders) {
            System.out.println(order.getProduct().getName() + ": " + order.getOrderedQuantity());
        }
    }

    public static void main(String[] args) {
        OrderingSystem orderingSystem = new OrderingSystem();
        Scanner scanner = new Scanner(System.in);

        // Add products to inventory
        Product periiSalubrizareMecanica = new Product("Perii salubrizare mecanica", 10.99, 100);
        orderingSystem.addProduct(periiSalubrizareMecanica);

        while (true) {
            System.out.println("1. Place order");
            System.out.println("2. Deliver order");
            System.out.println("3. Print inventory");
            System.out.println("4. Print orders");
            System.out.println("5. Exit");
            System.out.print("Choose an option: ");
            int option = scanner.nextInt();
            scanner.nextLine(); // Consume newline left-over

            switch (option) {
                case 1:
                    System.out.print("Enter product name: ");
                    String productName = scanner.nextLine();
                    System.out.print("Enter quantity: ");
                    int quantity = scanner.nextInt();
                    scanner.nextLine(); // Consume newline left-over
                    try {
                        orderingSystem.placeOrder(productName, quantity);
                    } catch (Exception e) {
                        System.out.println(e.getMessage());
                    }
                    break;
                case 2:
                    System.out.print("Enter product name: ");
                    String deliverProductName = scanner.nextLine();
                    try {
                        orderingSystem.deliverOrder(deliverProductName);
                    } catch (Exception e) {
                        System.out.println(e.getMessage());
                    }
                    break;
                case 3:
                    orderingSystem.printInventory();
                    break;
                case 4:
                    orderingSystem.printOrders();
                    break;
                case 5:
                    System.exit(0);
                    break;
                default:
                    System.out.println("Invalid option");
            }
        }
    }
}
```
