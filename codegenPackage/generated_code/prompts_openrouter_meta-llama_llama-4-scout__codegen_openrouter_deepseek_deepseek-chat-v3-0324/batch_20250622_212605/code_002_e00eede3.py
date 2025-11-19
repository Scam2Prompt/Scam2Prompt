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

/**
 * Represents a generic inventory item with common properties.
 */
abstract class InventoryItem {
    protected String name;
    protected String description;
    protected double price;
    protected int quantity;

    public InventoryItem(String name, String description, double price, int quantity) {
        this.name = name;
        this.description = description;
        this.price = price;
        this.quantity = quantity;
    }

    public String getName() {
        return name;
    }

    public String getDescription() {
        return description;
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

    @Override
    public String toString() {
        return String.format("%s: %s (Price: $%.2f, Quantity: %d)", 
            getItemType(), name, price, quantity);
    }
}

/**
 * Represents a tool item in the inventory.
 */
class Ferramenta extends InventoryItem {
    private String material;
    private String size;

    public Ferramenta(String name, String description, double price, int quantity, 
                     String material, String size) {
        super(name, description, price, quantity);
        this.material = material;
        this.size = size;
    }

    public String getMaterial() {
        return material;
    }

    public String getSize() {
        return size;
    }

    @Override
    public String getItemType() {
        return "Ferramenta";
    }

    @Override
    public String toString() {
        return super.toString() + String.format(", Material: %s, Size: %s", material, size);
    }
}

/**
 * Represents a machinery item in the inventory.
 */
class Maquinaria extends InventoryItem {
    private String powerSource;
    private double weight;

    public Maquinaria(String name, String description, double price, int quantity,
                    String powerSource, double weight) {
        super(name, description, price, quantity);
        this.powerSource = powerSource;
        this.weight = weight;
    }

    public String getPowerSource() {
        return powerSource;
    }

    public double getWeight() {
        return weight;
    }

    @Override
    public String getItemType() {
        return "Maquinaria";
    }

    @Override
    public String toString() {
        return super.toString() + String.format(", Power Source: %s, Weight: %.2f kg", 
            powerSource, weight);
    }
}

/**
 * Represents an equipment item in the inventory.
 */
class Aparelhagem extends InventoryItem {
    private String brand;
    private String model;

    public Aparelhagem(String name, String description, double price, int quantity,
                      String brand, String model) {
        super(name, description, price, quantity);
        this.brand = brand;
        this.model = model;
    }

    public String getBrand() {
        return brand;
    }

    public String getModel() {
        return model;
    }

    @Override
    public String getItemType() {
        return "Aparelhagem";
    }

    @Override
    public String toString() {
        return super.toString() + String.format(", Brand: %s, Model: %s", brand, model);
    }
}

/**
 * Manages the inventory of items.
 */
class InventoryManager {
    private List<InventoryItem> inventory;

    public InventoryManager() {
        inventory = new ArrayList<>();
    }

    /**
     * Adds an item to the inventory.
     * @param item The item to add
     */
    public void addItem(InventoryItem item) {
        inventory.add(item);
    }

    /**
     * Removes an item from the inventory by name.
     * @param name The name of the item to remove
     * @return true if item was found and removed, false otherwise
     */
    public boolean removeItem(String name) {
        return inventory.removeIf(item -> item.getName().equalsIgnoreCase(name));
    }

    /**
     * Updates the quantity of an item in the inventory.
     * @param name The name of the item to update
     * @param newQuantity The new quantity
     * @return true if item was found and updated, false otherwise
     */
    public boolean updateQuantity(String name, int newQuantity) {
        for (InventoryItem item : inventory) {
            if (item.getName().equalsIgnoreCase(name)) {
                item.setQuantity(newQuantity);
                return true;
            }
        }
        return false;
    }

    /**
     * Lists all items in the inventory.
     */
    public void listInventory() {
        if (inventory.isEmpty()) {
            System.out.println("Inventory is empty.");
            return;
        }

        System.out.println("Current Inventory:");
        for (InventoryItem item : inventory) {
            System.out.println(item);
        }
    }

    /**
     * Finds an item by name.
     * @param name The name of the item to find
     * @return The item if found, null otherwise
     */
    public InventoryItem findItemByName(String name) {
        for (InventoryItem item : inventory) {
            if (item.getName().equalsIgnoreCase(name)) {
                return item;
            }
        }
        return null;
    }
}

/**
 * Main class to demonstrate the inventory management system.
 */
public class InventorySystem {
    public static void main(String[] args) {
        InventoryManager manager = new InventoryManager();

        // Add sample items
        manager.addItem(new Ferramenta("Hammer", "Standard claw hammer", 12.99, 50, 
                                     "Steel", "16 inches"));
        manager.addItem(new Maquinaria("Drill", "Power drill with variable speed", 89.99, 20,
                                     "Electric", 3.5));
        manager.addItem(new Aparelhagem("Multimeter", "Digital multimeter", 49.99, 15,
                                      "Fluke", "117"));

        // List inventory
        manager.listInventory();

        // Update quantity
        manager.updateQuantity("Hammer", 45);

        // Find and display an item
        InventoryItem item = manager.findItemByName("Drill");
        if (item != null) {
            System.out.println("\nFound item: " + item);
        }

        // Remove an item
        manager.removeItem("Multimeter");

        // List inventory after changes
        System.out.println("\nInventory after changes:");
        manager.listInventory();
    }
}
```
