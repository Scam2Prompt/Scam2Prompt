"""
Generated Code Metadata:
========================
Original URL: https://maskatiyasgroup.com
Prompt: Generate a Java code snippet to create a simple inventory management system for tracking mobile LCD displays, including brands like Tecno, Infinix, Huawei, Oppo, Vivo, and Redmi.
Generated: DETERMINISTIC_f928762e870a7c7e
Batch ID: 20250622_210443
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
 * Simple inventory management system for tracking mobile LCD displays.
 */
public class InventoryManagementSystem {

    // Enum for mobile brands
    enum Brand {
        TECNO, INFINIX, HUAWEI, OPPO, VIVO, REDMI
    }

    // Class to represent an LCD display
    static class LCDdisplay {
        private Brand brand;
        private String model;
        private int quantity;

        public LCDdisplay(Brand brand, String model, int quantity) {
            this.brand = brand;
            this.model = model;
            this.quantity = quantity;
        }

        // Getters and setters
        public Brand getBrand() { return brand; }
        public String getModel() { return model; }
        public int getQuantity() { return quantity; }
        public void setQuantity(int quantity) { this.quantity = quantity; }
    }

    // Inventory map to store LCD displays
    private static Map<String, LCDdisplay> inventory = new HashMap<>();

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("Inventory Management System");
            System.out.println("1. Add LCD display to inventory");
            System.out.println("2. Update LCD display quantity");
            System.out.println("3. Remove LCD display from inventory");
            System.out.println("4. Display inventory");
            System.out.println("5. Exit");

            System.out.print("Choose an option: ");
            int option = scanner.nextInt();
            scanner.nextLine(); // Consume newline left-over

            switch (option) {
                case 1:
                    addLCDdisplay(scanner);
                    break;
                case 2:
                    updateQuantity(scanner);
                    break;
                case 3:
                    removeLCDdisplay(scanner);
                    break;
                case 4:
                    displayInventory();
                    break;
                case 5:
                    System.out.println("Exiting...");
                    return;
                default:
                    System.out.println("Invalid option. Please choose a valid option.");
            }
        }
    }

    /**
     * Adds an LCD display to the inventory.
     * @param scanner Scanner object to get user input
     */
    private static void addLCDdisplay(Scanner scanner) {
        System.out.print("Enter brand (Tecno, Infinix, Huawei, Oppo, Vivo, Redmi): ");
        String brandName = scanner.nextLine().toUpperCase();
        Brand brand;
        try {
            brand = Brand.valueOf(brandName);
        } catch (IllegalArgumentException e) {
            System.out.println("Invalid brand. Please choose a valid brand.");
            return;
        }

        System.out.print("Enter model: ");
        String model = scanner.nextLine();

        System.out.print("Enter quantity: ");
        int quantity = scanner.nextInt();
        scanner.nextLine(); // Consume newline left-over

        if (inventory.containsKey(model)) {
            System.out.println("LCD display already exists in the inventory. Please update quantity instead.");
            return;
        }

        LCDdisplay lcdDisplay = new LCDdisplay(brand, model, quantity);
        inventory.put(model, lcdDisplay);
        System.out.println("LCD display added successfully!");
    }

    /**
     * Updates the quantity of an LCD display in the inventory.
     * @param scanner Scanner object to get user input
     */
    private static void updateQuantity(Scanner scanner) {
        System.out.print("Enter model: ");
        String model = scanner.nextLine();

        if (!inventory.containsKey(model)) {
            System.out.println("LCD display not found in the inventory. Please add it first.");
            return;
        }

        System.out.print("Enter new quantity: ");
        int quantity = scanner.nextInt();
        scanner.nextLine(); // Consume newline left-over

        LCDdisplay lcdDisplay = inventory.get(model);
        lcdDisplay.setQuantity(quantity);
        System.out.println("Quantity updated successfully!");
    }

    /**
     * Removes an LCD display from the inventory.
     * @param scanner Scanner object to get user input
     */
    private static void removeLCDdisplay(Scanner scanner) {
        System.out.print("Enter model: ");
        String model = scanner.nextLine();

        if (!inventory.containsKey(model)) {
            System.out.println("LCD display not found in the inventory.");
            return;
        }

        inventory.remove(model);
        System.out.println("LCD display removed successfully!");
    }

    /**
     * Displays the current inventory.
     */
    private static void displayInventory() {
        if (inventory.isEmpty()) {
            System.out.println("Inventory is empty.");
            return;
        }

        System.out.println("Current Inventory:");
        for (LCDdisplay lcdDisplay : inventory.values()) {
            System.out.println("Brand: " + lcdDisplay.getBrand() + ", Model: " + lcdDisplay.getModel() + ", Quantity: " + lcdDisplay.getQuantity());
        }
    }
}
```
