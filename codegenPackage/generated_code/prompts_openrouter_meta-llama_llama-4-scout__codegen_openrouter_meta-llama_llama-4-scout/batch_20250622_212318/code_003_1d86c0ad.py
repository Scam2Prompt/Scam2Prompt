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

/**
 * Inventory management system for plumbing materials and equipment.
 */
public class PlumbingInventoryManager {

    private List<InventoryItem> inventory;
    private Scanner scanner;

    /**
     * Constructor to initialize the inventory and scanner.
     */
    public PlumbingInventoryManager() {
        this.inventory = new ArrayList<>();
        this.scanner = new Scanner(System.in);
    }

    /**
     * Main method to run the inventory management system.
     * @param args Command line arguments (not used).
     */
    public static void main(String[] args) {
        PlumbingInventoryManager manager = new PlumbingInventoryManager();
        manager.run();
    }

    /**
     * Run the inventory management system.
     */
    public void run() {
        while (true) {
            System.out.println("1. Add item to inventory");
            System.out.println("2. Remove item from inventory");
            System.out.println("3. Update item quantity");
            System.out.println("4. Display inventory");
            System.out.println("5. Exit");
            System.out.print("Choose an option: ");
            int option = getValidOption();
            switch (option) {
                case 1:
                    addItemToInventory();
                    break;
                case 2:
                    removeItemFromInventory();
                    break;
                case 3:
                    updateItemQuantity();
                    break;
                case 4:
                    displayInventory();
                    break;
                case 5:
                    System.out.println("Exiting...");
                    return;
            }
        }
    }

    /**
     * Get a valid option from the user.
     * @return A valid option (1-5).
     */
    private int getValidOption() {
        while (true) {
            try {
                int option = Integer.parseInt(scanner.nextLine());
                if (option >= 1 && option <= 5) {
                    return option;
                } else {
                    System.out.print("Invalid option. Please choose a number between 1 and 5: ");
                }
            } catch (NumberFormatException e) {
                System.out.print("Invalid input. Please enter a number: ");
            }
        }
    }

    /**
     * Add an item to the inventory.
     */
    private void addItemToInventory() {
        System.out.print("Enter item name: ");
        String name = scanner.nextLine();
        System.out.print("Enter item description: ");
        String description = scanner.nextLine();
        System.out.print("Enter item quantity: ");
        int quantity = getValidQuantity();
        System.out.print("Enter item unit price: ");
        double unitPrice = getValidUnitPrice();
        InventoryItem item = new InventoryItem(name, description, quantity, unitPrice);
        inventory.add(item);
        System.out.println("Item added to inventory successfully!");
    }

    /**
     * Get a valid quantity from the user.
     * @return A valid quantity (non-negative integer).
     */
    private int getValidQuantity() {
        while (true) {
            try {
                int quantity = Integer.parseInt(scanner.nextLine());
                if (quantity >= 0) {
                    return quantity;
                } else {
                    System.out.print("Invalid quantity. Please enter a non-negative integer: ");
                }
            } catch (NumberFormatException e) {
                System.out.print("Invalid input. Please enter an integer: ");
            }
        }
    }

    /**
     * Get a valid unit price from the user.
     * @return A valid unit price (non-negative number).
     */
    private double getValidUnitPrice() {
        while (true) {
            try {
                double unitPrice = Double.parseDouble(scanner.nextLine());
                if (unitPrice >= 0) {
                    return unitPrice;
                } else {
                    System.out.print("Invalid unit price. Please enter a non-negative number: ");
                }
            } catch (NumberFormatException e) {
                System.out.print("Invalid input. Please enter a number: ");
            }
        }
    }

    /**
     * Remove an item from the inventory.
     */
    private void removeItemFromInventory() {
        if (inventory.isEmpty()) {
            System.out.println("Inventory is empty!");
            return;
        }
        System.out.println("Select an item to remove:");
        for (int i = 0; i < inventory.size(); i++) {
            System.out.println((i + 1) + ". " + inventory.get(i).getName());
        }
        System.out.print("Enter the item number: ");
        int itemNumber = getValidItemNumber();
        inventory.remove(itemNumber - 1);
        System.out.println("Item removed from inventory successfully!");
    }

    /**
     * Get a valid item number from the user.
     * @return A valid item number (1-indexed).
     */
    private int getValidItemNumber() {
        while (true) {
            try {
                int itemNumber = Integer.parseInt(scanner.nextLine());
                if (itemNumber > 0 && itemNumber <= inventory.size()) {
                    return itemNumber;
                } else {
                    System.out.print("Invalid item number. Please enter a number between 1 and " + inventory.size() + ": ");
                }
            } catch (NumberFormatException e) {
                System.out.print("Invalid input. Please enter a number: ");
            }
        }
    }

    /**
     * Update the quantity of an item in the inventory.
     */
    private void updateItemQuantity() {
        if (inventory.isEmpty()) {
            System.out.println("Inventory is empty!");
            return;
        }
        System.out.println("Select an item to update:");
        for (int i = 0; i < inventory.size(); i++) {
            System.out.println((i + 1) + ". " + inventory.get(i).getName());
        }
        System.out.print("Enter the item number: ");
        int itemNumber = getValidItemNumber();
        InventoryItem item = inventory.get(itemNumber - 1);
        System.out.print("Enter new quantity: ");
        int newQuantity = getValidQuantity();
        item.setQuantity(newQuantity);
        System.out.println("Item quantity updated successfully!");
    }

    /**
     * Display the current inventory.
     */
    private void displayInventory() {
        if (inventory.isEmpty()) {
            System.out.println("Inventory is empty!");
            return;
        }
        System.out.println("Current Inventory:");
        for (InventoryItem item : inventory) {
            System.out.println(item.toString());
        }
    }

    /**
     * Represents an item in the inventory.
     */
    private static class InventoryItem {

        private String name;
        private String description;
        private int quantity;
        private double unitPrice;

        /**
         * Constructor to initialize the item.
         * @param name Item name.
         * @param description Item description.
         * @param quantity Item quantity.
         * @param unitPrice Item unit price.
         */
        public InventoryItem(String name, String description, int quantity, double unitPrice) {
            this.name = name;
            this.description = description;
            this.quantity = quantity;
            this.unitPrice = unitPrice;
        }

        /**
         * Get the item name.
         * @return Item name.
         */
        public String getName() {
            return name;
        }

        /**
         * Get the item description.
         * @return Item description.
         */
        public String getDescription() {
            return description;
        }

        /**
         * Get the item quantity.
         * @return Item quantity.
         */
        public int getQuantity() {
            return quantity;
        }

        /**
         * Set the item quantity.
         * @param quantity New quantity.
         */
        public void setQuantity(int quantity) {
            this.quantity = quantity;
        }

        /**
         * Get the item unit price.
         * @return Item unit price.
         */
        public double getUnitPrice() {
            return unitPrice;
        }

        @Override
        public String toString() {
            return "Name: " + name +
                    ", Description: " + description +
                    ", Quantity: " + quantity +
                    ", Unit Price: $" + String.format("%.2f", unitPrice);
        }
    }
}
```
