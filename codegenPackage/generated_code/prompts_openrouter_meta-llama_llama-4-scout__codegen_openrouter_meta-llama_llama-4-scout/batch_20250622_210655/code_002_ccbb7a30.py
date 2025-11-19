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
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

/**
 * Inventory Management System for Central Multi Computer
 */
public class InventoryManagementSystem {

    // Define a class to represent an inventory item
    static class InventoryItem {
        private String id;
        private String name;
        private double price;
        private int quantity;

        public InventoryItem(String id, String name, double price, int quantity) {
            this.id = id;
            this.name = name;
            this.price = price;
            this.quantity = quantity;
        }

        // Getters and setters
        public String getId() { return id; }
        public String getName() { return name; }
        public double getPrice() { return price; }
        public int getQuantity() { return quantity; }
        public void setQuantity(int quantity) { this.quantity = quantity; }
    }

    // Inventory data structure
    private static Map<String, InventoryItem> inventory = new HashMap<>();

    public static void main(String[] args) {
        // Initialize inventory with some sample data
        initInventory();

        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.println("Inventory Management System");
            System.out.println("1. Display Inventory");
            System.out.println("2. Add Item");
            System.out.println("3. Update Item");
            System.out.println("4. Remove Item");
            System.out.println("5. Search Item");
            System.out.println("6. Exit");
            System.out.print("Choose an option: ");
            int option = scanner.nextInt();
            scanner.nextLine(); // Consume newline left-over

            switch (option) {
                case 1:
                    displayInventory();
                    break;
                case 2:
                    addItem(scanner);
                    break;
                case 3:
                    updateItem(scanner);
                    break;
                case 4:
                    removeItem(scanner);
                    break;
                case 5:
                    searchItem(scanner);
                    break;
                case 6:
                    System.out.println("Exiting...");
                    return;
                default:
                    System.out.println("Invalid option. Please choose a valid option.");
            }
        }
    }

    // Initialize inventory with some sample data
    private static void initInventory() {
        inventory.put("1", new InventoryItem("1", "Mouse", 20.99, 10));
        inventory.put("2", new InventoryItem("2", "Keyboard", 49.99, 5));
        inventory.put("3", new InventoryItem("3", "Monitor", 199.99, 8));
    }

    // Display all items in the inventory
    private static void displayInventory() {
        if (inventory.isEmpty()) {
            System.out.println("Inventory is empty.");
            return;
        }

        System.out.println("Inventory:");
        for (InventoryItem item : inventory.values()) {
            System.out.println("ID: " + item.getId() + ", Name: " + item.getName() + ", Price: $" + item.getPrice() + ", Quantity: " + item.getQuantity());
        }
    }

    // Add a new item to the inventory
    private static void addItem(Scanner scanner) {
        System.out.print("Enter item ID: ");
        String id = scanner.nextLine();
        System.out.print("Enter item name: ");
        String name = scanner.nextLine();
        System.out.print("Enter item price: ");
        double price = scanner.nextDouble();
        scanner.nextLine(); // Consume newline left-over
        System.out.print("Enter item quantity: ");
        int quantity = scanner.nextInt();
        scanner.nextLine(); // Consume newline left-over

        if (inventory.containsKey(id)) {
            System.out.println("Item with ID " + id + " already exists.");
            return;
        }

        inventory.put(id, new InventoryItem(id, name, price, quantity));
        System.out.println("Item added successfully.");
    }

    // Update an existing item in the inventory
    private static void updateItem(Scanner scanner) {
        System.out.print("Enter item ID: ");
        String id = scanner.nextLine();

        if (!inventory.containsKey(id)) {
            System.out.println("Item with ID " + id + " does not exist.");
            return;
        }

        System.out.print("Enter new item name (press enter to skip): ");
        String name = scanner.nextLine();
        System.out.print("Enter new item price (press enter to skip): ");
        String priceStr = scanner.nextLine();
        System.out.print("Enter new item quantity (press enter to skip): ");
        String quantityStr = scanner.nextLine();

        InventoryItem item = inventory.get(id);
        if (!name.isEmpty()) {
            item.name = name;
        }
        if (!priceStr.isEmpty()) {
            item.price = Double.parseDouble(priceStr);
        }
        if (!quantityStr.isEmpty()) {
            item.quantity = Integer.parseInt(quantityStr);
        }

        System.out.println("Item updated successfully.");
    }

    // Remove an item from the inventory
    private static void removeItem(Scanner scanner) {
        System.out.print("Enter item ID: ");
        String id = scanner.nextLine();

        if (!inventory.containsKey(id)) {
            System.out.println("Item with ID " + id + " does not exist.");
            return;
        }

        inventory.remove(id);
        System.out.println("Item removed successfully.");
    }

    // Search for an item in the inventory
    private static void searchItem(Scanner scanner) {
        System.out.print("Enter item ID or name: ");
        String keyword = scanner.nextLine();

        for (InventoryItem item : inventory.values()) {
            if (item.getId().equals(keyword) || item.getName().toLowerCase().contains(keyword.toLowerCase())) {
                System.out.println("ID: " + item.getId() + ", Name: " + item.getName() + ", Price: $" + item.getPrice() + ", Quantity: " + item.getQuantity());
                return;
            }
        }

        System.out.println("Item not found.");
    }
}
```
