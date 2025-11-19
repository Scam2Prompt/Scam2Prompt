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

/**
 * Inventory Management System for a store selling computer accessories.
 * This program allows adding, viewing, updating, and deleting inventory items.
 */
public class InventoryManager {

    // Class to represent an inventory item
    static class Item {
        private int id;
        private String name;
        private int quantity;
        private double price;

        public Item(int id, String name, int quantity, double price) {
            this.id = id;
            this.name = name;
            this.quantity = quantity;
            this.price = price;
        }

        public int getId() {
            return id;
        }

        public String getName() {
            return name;
        }

        public int getQuantity() {
            return quantity;
        }

        public void setQuantity(int quantity) {
            this.quantity = quantity;
        }

        public double getPrice() {
            return price;
        }

        public void setPrice(double price) {
            this.price = price;
        }

        @Override
        public String toString() {
            return "ID: " + id + ", Name: " + name + ", Quantity: " + quantity + ", Price: $" + price;
        }
    }

    // List to store inventory items
    private static List<Item> inventory = new ArrayList<>();
    private static int nextId = 1; // Auto-increment ID for items

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        boolean running = true;

        while (running) {
            System.out.println("\nInventory Management System");
            System.out.println("1. Add Item");
            System.out.println("2. View Items");
            System.out.println("3. Update Item");
            System.out.println("4. Delete Item");
            System.out.println("5. Exit");
            System.out.print("Choose an option: ");

            try {
                int choice = Integer.parseInt(scanner.nextLine());

                switch (choice) {
                    case 1:
                        addItem(scanner);
                        break;
                    case 2:
                        viewItems();
                        break;
                    case 3:
                        updateItem(scanner);
                        break;
                    case 4:
                        deleteItem(scanner);
                        break;
                    case 5:
                        running = false;
                        System.out.println("Exiting the program. Goodbye!");
                        break;
                    default:
                        System.out.println("Invalid choice. Please try again.");
                }
            } catch (NumberFormatException e) {
                System.out.println("Invalid input. Please enter a number.");
            }
        }

        scanner.close();
    }

    /**
     * Adds a new item to the inventory.
     *
     * @param scanner Scanner object for user input
     */
    private static void addItem(Scanner scanner) {
        System.out.print("Enter item name: ");
        String name = scanner.nextLine();

        System.out.print("Enter item quantity: ");
        int quantity = Integer.parseInt(scanner.nextLine());

        System.out.print("Enter item price: ");
        double price = Double.parseDouble(scanner.nextLine());

        Item newItem = new Item(nextId++, name, quantity, price);
        inventory.add(newItem);
        System.out.println("Item added successfully!");
    }

    /**
     * Displays all items in the inventory.
     */
    private static void viewItems() {
        if (inventory.isEmpty()) {
            System.out.println("No items in inventory.");
        } else {
            System.out.println("Inventory Items:");
            for (Item item : inventory) {
                System.out.println(item);
            }
        }
    }

    /**
     * Updates an existing item in the inventory.
     *
     * @param scanner Scanner object for user input
     */
    private static void updateItem(Scanner scanner) {
        System.out.print("Enter item ID to update: ");
        int id = Integer.parseInt(scanner.nextLine());

        Item itemToUpdate = findItemById(id);
        if (itemToUpdate == null) {
            System.out.println("Item not found.");
            return;
        }

        System.out.print("Enter new quantity: ");
        int newQuantity = Integer.parseInt(scanner.nextLine());

        System.out.print("Enter new price: ");
        double newPrice = Double.parseDouble(scanner.nextLine());

        itemToUpdate.setQuantity(newQuantity);
        itemToUpdate.setPrice(newPrice);
        System.out.println("Item updated successfully!");
    }

    /**
     * Deletes an item from the inventory.
     *
     * @param scanner Scanner object for user input
     */
    private static void deleteItem(Scanner scanner) {
        System.out.print("Enter item ID to delete: ");
        int id = Integer.parseInt(scanner.nextLine());

        Item itemToDelete = findItemById(id);
        if (itemToDelete == null) {
            System.out.println("Item not found.");
            return;
        }

        inventory.remove(itemToDelete);
        System.out.println("Item deleted successfully!");
    }

    /**
     * Finds an item in the inventory by its ID.
     *
     * @param id ID of the item to find
     * @return Item object if found, null otherwise
     */
    private static Item findItemById(int id) {
        for (Item item : inventory) {
            if (item.getId() == id) {
                return item;
            }
        }
        return null;
    }
}
```
