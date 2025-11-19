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
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * A simple inventory management system for tracking mobile LCD displays.
 */
public class LCDInventorySystem {
    private Map<String, List<LCDDisplay>> inventory;

    /**
     * Enum representing supported mobile brands.
     */
    public enum Brand {
        TECNO, INFINIX, HUAWEI, OPPO, VIVO, REDMI
    }

    /**
     * Class representing an LCD display unit.
     */
    public static class LCDDisplay {
        private Brand brand;
        private String model;
        private int quantity;
        private double price;

        public LCDDisplay(Brand brand, String model, int quantity, double price) {
            this.brand = brand;
            this.model = model;
            this.quantity = quantity;
            this.price = price;
        }

        // Getters and setters
        public Brand getBrand() {
            return brand;
        }

        public String getModel() {
            return model;
        }

        public int getQuantity() {
            return quantity;
        }

        public void setQuantity(int quantity) {
            if (quantity < 0) {
                throw new IllegalArgumentException("Quantity cannot be negative");
            }
            this.quantity = quantity;
        }

        public double getPrice() {
            return price;
        }

        public void setPrice(double price) {
            if (price < 0) {
                throw new IllegalArgumentException("Price cannot be negative");
            }
            this.price = price;
        }

        @Override
        public String toString() {
            return String.format("Brand: %s, Model: %s, Quantity: %d, Price: $%.2f",
                    brand, model, quantity, price);
        }
    }

    /**
     * Initializes the inventory system.
     */
    public LCDInventorySystem() {
        inventory = new HashMap<>();
        for (Brand brand : Brand.values()) {
            inventory.put(brand.name(), new ArrayList<>());
        }
    }

    /**
     * Adds a new LCD display to the inventory.
     * @param brand The brand of the display
     * @param model The model number
     * @param quantity The quantity in stock
     * @param price The unit price
     * @throws IllegalArgumentException if brand is null or quantity/price are negative
     */
    public void addDisplay(Brand brand, String model, int quantity, double price) {
        if (brand == null) {
            throw new IllegalArgumentException("Brand cannot be null");
        }
        if (quantity < 0 || price < 0) {
            throw new IllegalArgumentException("Quantity and price must be non-negative");
        }

        LCDDisplay display = new LCDDisplay(brand, model, quantity, price);
        inventory.get(brand.name()).add(display);
    }

    /**
     * Updates the quantity of a specific display model.
     * @param brand The brand of the display
     * @param model The model number
     * @param newQuantity The new quantity
     * @throws IllegalArgumentException if display not found or quantity is negative
     */
    public void updateQuantity(Brand brand, String model, int newQuantity) {
        if (newQuantity < 0) {
            throw new IllegalArgumentException("Quantity cannot be negative");
        }

        List<LCDDisplay> brandDisplays = inventory.get(brand.name());
        for (LCDDisplay display : brandDisplays) {
            if (display.getModel().equals(model)) {
                display.setQuantity(newQuantity);
                return;
            }
        }
        throw new IllegalArgumentException("Display not found in inventory");
    }

    /**
     * Gets all displays for a specific brand.
     * @param brand The brand to query
     * @return List of displays for the brand
     */
    public List<LCDDisplay> getDisplaysByBrand(Brand brand) {
        return new ArrayList<>(inventory.get(brand.name()));
    }

    /**
     * Gets the total inventory value across all brands.
     * @return The total inventory value
     */
    public double getTotalInventoryValue() {
        double total = 0;
        for (List<LCDDisplay> brandDisplays : inventory.values()) {
            for (LCDDisplay display : brandDisplays) {
                total += display.getQuantity() * display.getPrice();
            }
        }
        return total;
    }

    /**
     * Prints the current inventory status.
     */
    public void printInventoryReport() {
        System.out.println("=== LCD Display Inventory Report ===");
        for (Brand brand : Brand.values()) {
            System.out.println("\nBrand: " + brand);
            List<LCDDisplay> displays = inventory.get(brand.name());
            if (displays.isEmpty()) {
                System.out.println("No displays in stock");
            } else {
                for (LCDDisplay display : displays) {
                    System.out.println(display);
                }
            }
        }
        System.out.printf("\nTotal Inventory Value: $%.2f\n", getTotalInventoryValue());
    }

    public static void main(String[] args) {
        LCDInventorySystem inventory = new LCDInventorySystem();

        // Add sample inventory
        inventory.addDisplay(Brand.TECNO, "Tecno Camon 19", 15, 89.99);
        inventory.addDisplay(Brand.INFINIX, "Infinix Hot 12", 20, 75.50);
        inventory.addDisplay(Brand.HUAWEI, "Huawei P50 Pro", 8, 149.99);
        inventory.addDisplay(Brand.OPPO, "Oppo Reno 8", 12, 99.99);
        inventory.addDisplay(Brand.VIVO, "Vivo Y21", 18, 65.00);
        inventory.addDisplay(Brand.REDMI, "Redmi Note 11", 25, 79.99);

        // Update quantity
        inventory.updateQuantity(Brand.TECNO, "Tecno Camon 19", 10);

        // Print inventory report
        inventory.printInventoryReport();
    }
}
```
