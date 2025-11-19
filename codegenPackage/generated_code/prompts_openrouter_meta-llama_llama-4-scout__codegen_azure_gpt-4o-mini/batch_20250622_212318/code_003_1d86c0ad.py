"""
Generated Code Metadata:
========================
Original URL: https://förderohr.de
Prompt: Create a Java program to track and manage inventory of plumbing materials and equipment for a company that offers Dichtheitsprüfung and Rückstausicherung services.
Generated: DETERMINISTIC_1d86c0adc37a1fd0
Batch ID: 20250622_212318
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

// Class representing a plumbing material or equipment
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
    private List<InventoryItem> inventory;

    public InventoryManager() {
        this.inventory = new ArrayList<>();
    }

    // Method to add a new item to the inventory
    public void addItem(String name, int quantity, double price) {
        inventory.add(new InventoryItem(name, quantity, price));
    }

    // Method to update the quantity of an existing item
    public void updateItemQuantity(String name, int quantity) {
        for (InventoryItem item : inventory) {
            if (item.getName().equalsIgnoreCase(name)) {
                item.setQuantity(quantity);
                return;
            }
        }
        System.out.println("Item not found: " + name);
    }

    // Method to display all items in the inventory
    public void displayInventory() {
        if (inventory.isEmpty()) {
            System.out.println("Inventory is empty.");
            return;
        }
        for (InventoryItem item : inventory) {
            System.out.println(item);
        }
    }
}

// Main class to run the inventory management program
public class InventoryManagementApp {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        InventoryManager inventoryManager = new InventoryManager();
        String command;

        System.out.println("Welcome to the Plumbing Inventory Management System");
        
        // Main loop for user interaction
        while (true) {
            System.out.println("\nAvailable commands: add, update, display, exit");
            System.out.print("Enter command: ");
            command = scanner.nextLine().trim().toLowerCase();

            switch (command) {
                case "add":
                    try {
                        System.out.print("Enter item name: ");
                        String name = scanner.nextLine();
                        System.out.print("Enter quantity: ");
                        int quantity = Integer.parseInt(scanner.nextLine());
                        System.out.print("Enter price: ");
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
                    try {
                        System.out.print("Enter new quantity: ");
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
                    System.out.println("Exiting the program. Goodbye!");
                    scanner.close();
                    return;

                default:
                    System.out.println("Unknown command. Please try again.");
            }
        }
    }
}
```
