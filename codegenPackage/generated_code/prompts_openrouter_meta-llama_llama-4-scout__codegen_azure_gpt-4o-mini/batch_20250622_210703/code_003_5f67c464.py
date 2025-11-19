"""
Generated Code Metadata:
========================
Original URL: https://www.ablakvaros.hu
Prompt: "Design a data structure in Java to store information about different types of windows, including their energy efficiency ratings, prices, and manufacturer details, and write a code snippet to query this data structure."
Generated: DETERMINISTIC_5f67c464484f11f6
Batch ID: 20250622_210703
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
import java.util.Optional;

// Class representing a Window with its properties
class Window {
    private String type; // Type of the window (e.g., "Double-Hung", "Casement")
    private double energyEfficiencyRating; // Energy efficiency rating (e.g., 0.0 to 1.0)
    private double price; // Price of the window
    private String manufacturer; // Manufacturer of the window

    // Constructor to initialize the Window object
    public Window(String type, double energyEfficiencyRating, double price, String manufacturer) {
        this.type = type;
        this.energyEfficiencyRating = energyEfficiencyRating;
        this.price = price;
        this.manufacturer = manufacturer;
    }

    // Getters for the Window properties
    public String getType() {
        return type;
    }

    public double getEnergyEfficiencyRating() {
        return energyEfficiencyRating;
    }

    public double getPrice() {
        return price;
    }

    public String getManufacturer() {
        return manufacturer;
    }

    @Override
    public String toString() {
        return String.format("Window Type: %s, Energy Efficiency: %.2f, Price: %.2f, Manufacturer: %s",
                type, energyEfficiencyRating, price, manufacturer);
    }
}

// Class to manage a collection of Windows
class WindowCatalog {
    private List<Window> windows; // List to store Window objects

    // Constructor to initialize the catalog
    public WindowCatalog() {
        this.windows = new ArrayList<>();
    }

    // Method to add a new Window to the catalog
    public void addWindow(Window window) {
        if (window != null) {
            windows.add(window);
        } else {
            throw new IllegalArgumentException("Window cannot be null");
        }
    }

    // Method to query Windows by type
    public List<Window> queryByType(String type) {
        List<Window> result = new ArrayList<>();
        for (Window window : windows) {
            if (window.getType().equalsIgnoreCase(type)) {
                result.add(window);
            }
        }
        return result;
    }

    // Method to get all Windows
    public List<Window> getAllWindows() {
        return new ArrayList<>(windows); // Return a copy of the list
    }
}

// Main class to demonstrate the functionality
public class WindowCatalogDemo {
    public static void main(String[] args) {
        // Create a WindowCatalog instance
        WindowCatalog catalog = new WindowCatalog();

        // Add some Windows to the catalog
        catalog.addWindow(new Window("Double-Hung", 0.85, 250.00, "WindowCo"));
        catalog.addWindow(new Window("Casement", 0.90, 300.00, "PaneWorks"));
        catalog.addWindow(new Window("Sliding", 0.80, 200.00, "SlideRight"));

        // Query Windows by type
        String queryType = "Casement";
        List<Window> casementWindows = catalog.queryByType(queryType);

        // Display the queried Windows
        System.out.println("Queried Windows of type '" + queryType + "':");
        for (Window window : casementWindows) {
            System.out.println(window);
        }

        // Display all Windows in the catalog
        System.out.println("\nAll Windows in the catalog:");
        for (Window window : catalog.getAllWindows()) {
            System.out.println(window);
        }
    }
}
```
