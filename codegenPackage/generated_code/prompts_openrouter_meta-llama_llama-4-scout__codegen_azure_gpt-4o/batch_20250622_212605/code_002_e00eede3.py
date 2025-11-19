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

// Base class for all inventory items
abstract class Item {
    private String name;
    private double price;
    private int quantity;

    // Constructor
    public Item(String name, double price, int quantity) {
        this.name = name;
        this.price = price;
        this.quantity = quantity;
    }

    // Getters and Setters
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        this.price = price;
    }

    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }

    // Abstract method to display item details
    public abstract void displayDetails();
}

// Class for 'Ferramenta' (Tools)
class Ferramenta extends Item {
    private String toolType;

    // Constructor
    public Ferramenta(String name, double price, int quantity, String toolType) {
        super(name, price, quantity);
        this.toolType = toolType;
    }

    // Getter and Setter for toolType
    public String getToolType() {
        return toolType;
    }

    public void setToolType(String toolType) {
        this.toolType = toolType;
    }

    // Display item details
    @Override
    public void displayDetails() {
        System.out.println("Ferramenta: " + getName() + ", Price: $" + getPrice() + ", Quantity: " + getQuantity() + ", Type: " + toolType);
    }
}

// Class for 'Maquinaria' (Machinery)
class Maquinaria extends Item {
    private double powerRating;

    // Constructor
    public Maquinaria(String name, double price, int quantity, double powerRating) {
        super(name, price, quantity);
        this.powerRating = powerRating;
    }

    // Getter and Setter for powerRating
    public double getPowerRating() {
        return powerRating;
    }

    public void setPowerRating(double powerRating) {
        this.powerRating = powerRating;
    }

    // Display item details
    @Override
    public void displayDetails() {
        System.out.println("Maquinaria: " + getName() + ", Price: $" + getPrice() + ", Quantity: " + getQuantity() + ", Power Rating: " + powerRating + " kW");
    }
}

// Class for 'Aparelhagem' (Equipment)
class Aparelhagem extends Item {
    private String brand;

    // Constructor
    public Aparelhagem(String name, double price, int quantity, String brand) {
        super(name, price, quantity);
        this.brand = brand;
    }

    // Getter and Setter for brand
    public String getBrand() {
        return brand;
    }

    public void setBrand(String brand) {
        this.brand = brand;
    }

    // Display item details
    @Override
    public void displayDetails() {
        System.out.println("Aparelhagem: " + getName() + ", Price: $" + getPrice() + ", Quantity: " + getQuantity() + ", Brand: " + brand);
    }
}

// Inventory Management System
class InventoryManagement {
    private List<Item> inventory;

    // Constructor
    public InventoryManagement() {
        inventory = new ArrayList<>();
    }

    // Add item to inventory
    public void addItem(Item item) {
        inventory.add(item);
    }

    // Remove item from inventory
    public void removeItem(String name) {
        inventory.removeIf(item -> item.getName().equalsIgnoreCase(name));
    }

    // Display all items in inventory
    public void displayInventory() {
        if (inventory.isEmpty()) {
            System.out.println("Inventory is empty.");
        } else {
            System.out.println("Inventory:");
            for (Item item : inventory) {
                item.displayDetails();
            }
        }
    }
}

// Main class to test the inventory system
public class Main {
    public static void main(String[] args) {
        // Create inventory management system
        InventoryManagement inventory = new InventoryManagement();

        // Add items to inventory
        inventory.addItem(new Ferramenta("Hammer", 15.99, 50, "Hand Tool"));
        inventory.addItem(new Maquinaria("Excavator", 50000.00, 2, 150.0));
        inventory.addItem(new Aparelhagem("Drill", 120.50, 20, "Bosch"));

        // Display inventory
        inventory.displayInventory();

        // Remove an item
        inventory.removeItem("Hammer");

        // Display inventory after removal
        inventory.displayInventory();
    }
}
```
