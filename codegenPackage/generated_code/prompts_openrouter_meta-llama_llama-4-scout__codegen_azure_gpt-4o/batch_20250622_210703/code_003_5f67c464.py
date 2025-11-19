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

// Class to represent a Window
class Window {
    private String type; // Type of window (e.g., "Sliding", "Casement", etc.)
    private double energyEfficiencyRating; // Energy efficiency rating (e.g., 0-10 scale)
    private double price; // Price of the window
    private String manufacturer; // Manufacturer details

    // Constructor
    public Window(String type, double energyEfficiencyRating, double price, String manufacturer) {
        this.type = type;
        this.energyEfficiencyRating = energyEfficiencyRating;
        this.price = price;
        this.manufacturer = manufacturer;
    }

    // Getters
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

    // Override toString for easy display
    @Override
    public String toString() {
        return "Window{" +
                "type='" + type + '\'' +
                ", energyEfficiencyRating=" + energyEfficiencyRating +
                ", price=" + price +
                ", manufacturer='" + manufacturer + '\'' +
                '}';
    }
}

// Class to manage a collection of windows
class WindowCatalog {
    private List<Window> windows; // List to store windows

    // Constructor
    public WindowCatalog() {
        this.windows = new ArrayList<>();
    }

    // Method to add a window to the catalog
    public void addWindow(Window window) {
        if (window == null) {
            throw new IllegalArgumentException("Window cannot be null");
        }
        windows.add(window);
    }

    // Method to query windows by type
    public List<Window> queryByType(String type) {
        List<Window> result = new ArrayList<>();
        for (Window window : windows) {
            if (window.getType().equalsIgnoreCase(type)) {
                result.add(window);
            }
        }
        return result;
    }

    // Method to query windows by energy efficiency rating (greater than or equal to a threshold)
    public List<Window> queryByEnergyEfficiency(double minRating) {
        List<Window> result = new ArrayList<>();
        for (Window window : windows) {
            if (window.getEnergyEfficiencyRating() >= minRating) {
                result.add(window);
            }
        }
        return result;
    }

    // Method to query windows by price range
    public List<Window> queryByPriceRange(double minPrice, double maxPrice) {
        List<Window> result = new ArrayList<>();
        for (Window window : windows) {
            if (window.getPrice() >= minPrice && window.getPrice() <= maxPrice) {
                result.add(window);
            }
        }
        return result;
    }
}

// Main class to demonstrate functionality
public class WindowCatalogDemo {
    public static void main(String[] args) {
        // Create a catalog
        WindowCatalog catalog = new WindowCatalog();

        // Add windows to the catalog
        catalog.addWindow(new Window("Sliding", 8.5, 250.0, "Manufacturer A"));
        catalog.addWindow(new Window("Casement", 9.0, 300.0, "Manufacturer B"));
        catalog.addWindow(new Window("Awning", 7.5, 200.0, "Manufacturer C"));
        catalog.addWindow(new Window("Sliding", 6.0, 220.0, "Manufacturer D"));

        // Query by type
        System.out.println("Query by type 'Sliding':");
        List<Window> slidingWindows = catalog.queryByType("Sliding");
        for (Window window : slidingWindows) {
            System.out.println(window);
        }

        // Query by energy efficiency rating
        System.out.println("\nQuery by energy efficiency rating >= 8.0:");
        List<Window> efficientWindows = catalog.queryByEnergyEfficiency(8.0);
        for (Window window : efficientWindows) {
            System.out.println(window);
        }

        // Query by price range
        System.out.println("\nQuery by price range 200.0 to 300.0:");
        List<Window> affordableWindows = catalog.queryByPriceRange(200.0, 300.0);
        for (Window window : affordableWindows) {
            System.out.println(window);
        }
    }
}
```
