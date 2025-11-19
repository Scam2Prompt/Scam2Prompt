"""
Generated Code Metadata:
========================
Original URL: https://cmcbukittinggi.co.id
Prompt: Generate a Java program to manage inventory for a store like Central Multi Computer that sells computer accessories.
Generated: DETERMINISTIC_ccbb7a3041118c3e
Batch ID: 20250622_210655
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

// Class representing an inventory item
class InventoryItem {
    private String name;
    private int quantity;
    private double price;

    public InventoryItem(String name, int quantity, double price) {
        this.name = name;
        this.quantity = quantity;
        this.price = price;
    }

    public String getName() {
        return name;
    }

    public int getQuantity() {
        return quantity;
    }

    public double getPrice() {
        return price;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }

    @Override
    public String toString() {
        return String.format("Item: %s, Quantity: %d, Price: %.2f", name, quantity, price);
    }
}

// Class to manage the inventory
class InventoryManager {
    private List<InventoryItem> items;

    public InventoryManager() {
        items = new ArrayList<>();
    }

    // Method to add a new item to the inventory
    public void addItem(String name, int quantity, double price) {
        items.add(new InventoryItem(name, quantity, price));
    }

    // Method to update the quantity of an existing item
    public void updateItemQuantity(String name, int quantity) {
        for (InventoryItem item : items) {
            if (item.getName().equalsIgnoreCase(name)) {
                item.setQuantity(quantity);
                return;
            }
        }
        System.out.println("Item not found: " + name);
    }

    // Method to display all items in the inventory
    public void displayInventory() {
        if (items.isEmpty()) {
            System.out.println("Inventory is empty.");
            return;
        }
        for (InventoryItem item : items) {
            System.out.println(item);
        }
    }
}

// Main class to run the inventory management program
public class InventoryApp {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        InventoryManager inventoryManager = new InventoryManager();
        String command;

        System.out.println("Welcome to the Inventory Management System");
        
        // Main loop for user commands
        while (true) {
            System.out.println("Enter command (add, update, display, exit): ");
            command = scanner.nextLine().trim().toLowerCase();

            switch (command) {
                case "add":
                    try {
                        System.out.print("Enter item name: ");
                        String name = scanner.nextLine();
                        System.out.print("Enter item quantity: ");
                        int quantity = Integer.parseInt(scanner.nextLine());
                        System.out.print("Enter item price: ");
                        double price = Double.parseDouble(scanner.nextLine());
                        inventoryManager.addItem(name, quantity, price);
                        System.out.println("Item added successfully.");
                    } catch (NumberFormatException e) {
                        System.out.println("Invalid input. Please enter numeric values for quantity and price.");
                    }
                    break;

                case "update":
                    System.out.print("Enter item name to update: ");
                    String itemName = scanner.nextLine();
                    System.out.print("Enter new quantity: ");
                    try {
                        int newQuantity = Integer.parseInt(scanner.nextLine());
                        inventoryManager.updateItemQuantity(itemName, newQuantity);
                        System.out.println("Item quantity updated successfully.");
                    } catch (NumberFormatException e) {
                        System.out.println("Invalid input. Please enter a numeric value for quantity.");
                    }
                    break;

                case "display":
                    inventoryManager.displayInventory();
                    break;

                case "exit":
                    System.out.println("Exiting the Inventory Management System.");
                    scanner.close();
                    return;

                default:
                    System.out.println("Unknown command. Please try again.");
            }
        }
    }
}
```
