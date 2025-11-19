"""
Generated Code Metadata:
========================
Original URL: https://albaik.day
Prompt: Generate a Java code snippet to create a simple console-based system for ordering Albaik's signature flavors, such as golden broasted chicken and zesty garlic sauce.
Generated: DETERMINISTIC_d926e75008c389fa
Batch ID: 20250622_211510
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
 * A simple console-based ordering system for Albaik's signature flavors.
 */
public class AlbaikOrderSystem {

    // A map to hold the available menu items and their prices
    private static final Map<String, Double> menu = new HashMap<>();

    static {
        // Initialize the menu with Albaik's signature flavors and their prices
        menu.put("Golden Broasted Chicken", 25.00);
        menu.put("Zesty Garlic Sauce", 5.00);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double totalCost = 0.0;

        System.out.println("Welcome to Albaik's Order System!");
        System.out.println("Available items:");

        // Display the menu items
        displayMenu();

        // Loop to take orders until the user decides to stop
        while (true) {
            System.out.print("Enter the item you want to order (or type 'exit' to finish): ");
            String item = scanner.nextLine().trim();

            // Check if the user wants to exit
            if (item.equalsIgnoreCase("exit")) {
                break;
            }

            // Process the order
            try {
                double price = processOrder(item);
                totalCost += price;
                System.out.printf("Added %s to your order. Price: $%.2f%n", item, price);
            } catch (IllegalArgumentException e) {
                System.out.println(e.getMessage());
            }
        }

        // Display the total cost of the order
        System.out.printf("Your total order cost is: $%.2f%n", totalCost);
        System.out.println("Thank you for ordering with Albaik!");
        scanner.close();
    }

    /**
     * Displays the menu items and their prices.
     */
    private static void displayMenu() {
        for (Map.Entry<String, Double> entry : menu.entrySet()) {
            System.out.printf("%s - $%.2f%n", entry.getKey(), entry.getValue());
        }
    }

    /**
     * Processes the order for a given item.
     *
     * @param item The name of the item to order.
     * @return The price of the ordered item.
     * @throws IllegalArgumentException if the item is not on the menu.
     */
    private static double processOrder(String item) {
        if (!menu.containsKey(item)) {
            throw new IllegalArgumentException("Item not found on the menu. Please try again.");
        }
        return menu.get(item);
    }
}
```
