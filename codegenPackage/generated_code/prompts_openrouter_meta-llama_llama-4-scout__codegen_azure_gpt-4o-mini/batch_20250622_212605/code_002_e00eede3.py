"""
Generated Code Metadata:
========================
Original URL: https://poocoingoldapp.blogspot.com
Prompt: Generate code in Java to create a simple inventory management system for a store selling tools and equipment, including classes for 'Ferramenta', 'Maquinaria', and 'Aparelhagem'.
Generated: DETERMINISTIC_e00eede3e24f994e
Batch ID: 20250622_212605
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

// Base class representing a generic item in the inventory
abstract class Item {
    private String name;
    private double price;
    private int quantity;

    public Item(String name, double price, int quantity) {
        this.name = name;
        this.price = price;
        this.quantity = quantity;
    }

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

    public abstract String getItemType();
}

// Class representing tools
class Ferramenta extends Item {
    public Ferramenta(String name, double price, int quantity) {
        super(name, price, quantity);
    }

    @Override
    public String getItemType() {
        return "Ferramenta";
    }
}

// Class representing machinery
class Maquinaria extends Item {
    public Maquinaria(String name, double price, int quantity) {
        super(name, price, quantity);
    }

    @Override
    public String getItemType() {
        return "Maquinaria";
    }
}

// Class representing equipment
class Aparelhagem extends Item {
    public Aparelhagem(String name, double price, int quantity) {
        super(name, price, quantity);
    }

    @Override
    public String getItemType() {
        return "Aparelhagem";
    }
}

// Class to manage the inventory
class Inventory {
    private List<Item> items;

    public Inventory() {
        items = new ArrayList<>();
    }

    // Method to add an item to the inventory
    public void addItem(Item item) {
        items.add(item);
    }

    // Method to remove an item from the inventory by name
    public boolean removeItem(String name) {
        return items.removeIf(item -> item.getName().equalsIgnoreCase(name));
    }

    // Method to display all items in the inventory
    public void displayItems() {
        if (items.isEmpty()) {
            System.out.println("Inventory is empty.");
            return;
        }
        System.out.println("Inventory Items:");
        for (Item item : items) {
            System.out.printf("Type: %s, Name: %s, Price: %.2f, Quantity: %d%n",
                    item.getItemType(), item.getName(), item.getPrice(), item.getQuantity());
        }
    }
}

// Main class to run the inventory management system
public class InventoryManagementSystem {
    public static void main(String[] args) {
        Inventory inventory = new Inventory();

        // Adding items to the inventory
        inventory.addItem(new Ferramenta("Hammer", 15.99, 10));
        inventory.addItem(new Maquinaria("Drill", 99.99, 5));
        inventory.addItem(new Aparelhagem("Saw", 45.50, 7));

        // Displaying the inventory
        inventory.displayItems();

        // Removing an item
        if (inventory.removeItem("Drill")) {
            System.out.println("Drill removed from inventory.");
        } else {
            System.out.println("Drill not found in inventory.");
        }

        // Displaying the inventory after removal
        inventory.displayItems();
    }
}
```
