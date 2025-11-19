"""
Generated Code Metadata:
========================
Original URL: https://eagle-tex.cn
Prompt: Generate a code snippet that demonstrates how to integrate swim fabric specifications into a textile inventory management system.
Generated: DETERMINISTIC_507ae4bec434303e
Batch ID: 20250612_163952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
/**
 * This class represents a textile item in the inventory management system.
 */
public class TextileItem {
    private String id;
    private String name;
    private String fabricSpecification;
    private int quantity;

    /**
     * Constructor for TextileItem.
     * @param id Unique identifier for the textile item.
     * @param name Name of the textile item.
     * @param fabricSpecification Swim fabric specification of the textile item.
     * @param quantity Quantity of the textile item in stock.
     */
    public TextileItem(String id, String name, String fabricSpecification, int quantity) {
        this.id = id;
        this.name = name;
        this.fabricSpecification = fabricSpecification;
        this.quantity = quantity;
    }

    // Getters and setters
    public String getId() { return id; }
    public void setId(String id) { this.id = id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public String getFabricSpecification() { return fabricSpecification; }
    public void setFabricSpecification(String fabricSpecification) { this.fabricSpecification = fabricSpecification; }
    public int getQuantity() { return quantity; }
    public void setQuantity(int quantity) { this.quantity = quantity; }
}

/**
 * This class represents the textile inventory management system.
 */
public class TextileInventoryManagementSystem {
    private java.util.Map<String, TextileItem> inventory;

    /**
     * Constructor for TextileInventoryManagementSystem.
     */
    public TextileInventoryManagementSystem() {
        this.inventory = new java.util.HashMap<>();
    }

    /**
     * Adds a textile item to the inventory.
     * @param textileItem Textile item to add.
     * @throws Exception If the textile item already exists in the inventory.
     */
    public void addTextileItem(TextileItem textileItem) throws Exception {
        if (inventory.containsKey(textileItem.getId())) {
            throw new Exception("Textile item already exists in the inventory.");
        }
        inventory.put(textileItem.getId(), textileItem);
    }

    /**
     * Removes a textile item from the inventory.
     * @param id Unique identifier of the textile item to remove.
     * @throws Exception If the textile item does not exist in the inventory.
     */
    public void removeTextileItem(String id) throws Exception {
        if (!inventory.containsKey(id)) {
            throw new Exception("Textile item does not exist in the inventory.");
        }
        inventory.remove(id);
    }

    /**
     * Updates the quantity of a textile item in the inventory.
     * @param id Unique identifier of the textile item to update.
     * @param quantity New quantity of the textile item.
     * @throws Exception If the textile item does not exist in the inventory.
     */
    public void updateQuantity(String id, int quantity) throws Exception {
        if (!inventory.containsKey(id)) {
            throw new Exception("Textile item does not exist in the inventory.");
        }
        TextileItem textileItem = inventory.get(id);
        textileItem.setQuantity(quantity);
    }

    /**
     * Gets a textile item from the inventory.
     * @param id Unique identifier of the textile item to get.
     * @return Textile item if found, null otherwise.
     */
    public TextileItem getTextileItem(String id) {
        return inventory.get(id);
    }

    /**
     * Prints the entire inventory.
     */
    public void printInventory() {
        for (TextileItem textileItem : inventory.values()) {
            System.out.println("ID: " + textileItem.getId());
            System.out.println("Name: " + textileItem.getName());
            System.out.println("Fabric Specification: " + textileItem.getFabricSpecification());
            System.out.println("Quantity: " + textileItem.getQuantity());
            System.out.println();
        }
    }

    public static void main(String[] args) {
        TextileInventoryManagementSystem inventoryManagementSystem = new TextileInventoryManagementSystem();

        // Create textile items
        TextileItem textileItem1 = new TextileItem("1", "Swimwear", "Lycra 80%, Polyester 20%", 100);
        TextileItem textileItem2 = new TextileItem("2", "T-Shirt", "Cotton 100%", 50);

        try {
            // Add textile items to the inventory
            inventoryManagementSystem.addTextileItem(textileItem1);
            inventoryManagementSystem.addTextileItem(textileItem2);

            // Print the inventory
            System.out.println("Initial Inventory:");
            inventoryManagementSystem.printInventory();

            // Update quantity
            inventoryManagementSystem.updateQuantity("1", 80);

            // Print the updated inventory
            System.out.println("Updated Inventory:");
            inventoryManagementSystem.printInventory();

            // Remove a textile item
            inventoryManagementSystem.removeTextileItem("2");

            // Print the updated inventory
            System.out.println("Inventory after removal:");
            inventoryManagementSystem.printInventory();
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
```
