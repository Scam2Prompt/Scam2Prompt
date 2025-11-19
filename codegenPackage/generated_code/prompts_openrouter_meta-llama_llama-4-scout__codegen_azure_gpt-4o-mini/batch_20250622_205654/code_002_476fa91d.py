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
import java.util.Scanner;

// Class representing a cleaning product
class CleaningProduct {
    private String name;
    private double price;
    private int stock;

    public CleaningProduct(String name, double price, int stock) {
        this.name = name;
        this.price = price;
        this.stock = stock;
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

    public void reduceStock(int quantity) {
        if (quantity > stock) {
            throw new IllegalArgumentException("Insufficient stock for " + name);
        }
        stock -= quantity;
    }
}

// Class representing the ordering system
class OrderingSystem {
    private Map<String, CleaningProduct> inventory;

    public OrderingSystem() {
        inventory = new HashMap<>();
        initializeInventory();
    }

    // Initialize the inventory with some products
    private void initializeInventory() {
        inventory.put("Perii Salubrizare Mecanica", new CleaningProduct("Perii Salubrizare Mecanica", 150.0, 10));
        inventory.put("Detergent Industrial", new CleaningProduct("Detergent Industrial", 50.0, 20));
        inventory.put("Mop Profesional", new CleaningProduct("Mop Profesional", 30.0, 15));
    }

    // Method to place an order
    public void placeOrder(String productName, int quantity) {
        CleaningProduct product = inventory.get(productName);
        if (product == null) {
            System.out.println("Product not found: " + productName);
            return;
        }

        try {
            product.reduceStock(quantity);
            System.out.println("Order placed for " + quantity + " of " + productName + ". Total cost: " + (product.getPrice() * quantity));
        } catch (IllegalArgumentException e) {
            System.out.println(e.getMessage());
        }
    }

    // Method to display available products
    public void displayProducts() {
        System.out.println("Available Products:");
        for (CleaningProduct product : inventory.values()) {
            System.out.println(product.getName() + " - Price: " + product.getPrice() + ", Stock: " + product.getStock());
        }
    }
}

// Main class to run the ordering system
public class Main {
    public static void main(String[] args) {
        OrderingSystem orderingSystem = new OrderingSystem();
        Scanner scanner = new Scanner(System.in);

        while (true) {
            orderingSystem.displayProducts();
            System.out.print("Enter product name to order (or 'exit' to quit): ");
            String productName = scanner.nextLine();

            if (productName.equalsIgnoreCase("exit")) {
                break;
            }

            System.out.print("Enter quantity: ");
            int quantity;
            try {
                quantity = Integer.parseInt(scanner.nextLine());
                orderingSystem.placeOrder(productName, quantity);
            } catch (NumberFormatException e) {
                System.out.println("Invalid quantity. Please enter a number.");
            }
        }

        scanner.close();
        System.out.println("Thank you for using the ordering system!");
    }
}
```
