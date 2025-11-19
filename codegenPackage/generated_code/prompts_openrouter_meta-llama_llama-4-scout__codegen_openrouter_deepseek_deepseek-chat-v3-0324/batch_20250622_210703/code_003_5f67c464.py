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
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Objects;

/**
 * Represents a window manufacturer with name and contact information.
 */
class Manufacturer {
    private String name;
    private String contactInfo;

    public Manufacturer(String name, String contactInfo) {
        this.name = Objects.requireNonNull(name, "Manufacturer name cannot be null");
        this.contactInfo = Objects.requireNonNull(contactInfo, "Contact info cannot be null");
    }

    public String getName() {
        return name;
    }

    public String getContactInfo() {
        return contactInfo;
    }

    @Override
    public String toString() {
        return "Manufacturer{" +
                "name='" + name + '\'' +
                ", contactInfo='" + contactInfo + '\'' +
                '}';
    }
}

/**
 * Represents a window with its properties and manufacturer.
 */
class Window {
    private String type;
    private double price;
    private String energyEfficiencyRating;
    private Manufacturer manufacturer;

    public Window(String type, double price, String energyEfficiencyRating, Manufacturer manufacturer) {
        this.type = Objects.requireNonNull(type, "Window type cannot be null");
        if (price <= 0) {
            throw new IllegalArgumentException("Price must be positive");
        }
        this.price = price;
        this.energyEfficiencyRating = Objects.requireNonNull(energyEfficiencyRating, 
            "Energy efficiency rating cannot be null");
        this.manufacturer = Objects.requireNonNull(manufacturer, "Manufacturer cannot be null");
    }

    public String getType() {
        return type;
    }

    public double getPrice() {
        return price;
    }

    public String getEnergyEfficiencyRating() {
        return energyEfficiencyRating;
    }

    public Manufacturer getManufacturer() {
        return manufacturer;
    }

    @Override
    public String toString() {
        return "Window{" +
                "type='" + type + '\'' +
                ", price=" + price +
                ", energyEfficiencyRating='" + energyEfficiencyRating + '\'' +
                ", manufacturer=" + manufacturer +
                '}';
    }
}

/**
 * Manages a collection of windows and provides query capabilities.
 */
class WindowCatalog {
    private List<Window> windows;
    private Map<String, List<Window>> windowsByType;
    private Map<String, List<Window>> windowsByManufacturer;

    public WindowCatalog() {
        this.windows = new ArrayList<>();
        this.windowsByType = new HashMap<>();
        this.windowsByManufacturer = new HashMap<>();
    }

    /**
     * Adds a window to the catalog.
     * @param window The window to add
     * @throws IllegalArgumentException if window is null
     */
    public void addWindow(Window window) {
        Objects.requireNonNull(window, "Window cannot be null");
        
        windows.add(window);
        
        // Index by type
        windowsByType.computeIfAbsent(window.getType(), k -> new ArrayList<>())
                    .add(window);
        
        // Index by manufacturer
        windowsByManufacturer.computeIfAbsent(window.getManufacturer().getName(), k -> new ArrayList<>())
                            .add(window);
    }

    /**
     * Gets all windows of a specific type.
     * @param type The window type to query
     * @return List of matching windows
     */
    public List<Window> getWindowsByType(String type) {
        return new ArrayList<>(windowsByType.getOrDefault(type, new ArrayList<>()));
    }

    /**
     * Gets all windows from a specific manufacturer.
     * @param manufacturerName The manufacturer name to query
     * @return List of matching windows
     */
    public List<Window> getWindowsByManufacturer(String manufacturerName) {
        return new ArrayList<>(windowsByManufacturer.getOrDefault(manufacturerName, new ArrayList<>()));
    }

    /**
     * Gets all windows with a specific energy efficiency rating.
     * @param rating The rating to query
     * @return List of matching windows
     */
    public List<Window> getWindowsByEnergyRating(String rating) {
        List<Window> result = new ArrayList<>();
        for (Window window : windows) {
            if (window.getEnergyEfficiencyRating().equals(rating)) {
                result.add(window);
            }
        }
        return result;
    }

    /**
     * Gets all windows within a price range.
     * @param minPrice Minimum price (inclusive)
     * @param maxPrice Maximum price (inclusive)
     * @return List of matching windows
     * @throws IllegalArgumentException if minPrice > maxPrice
     */
    public List<Window> getWindowsByPriceRange(double minPrice, double maxPrice) {
        if (minPrice > maxPrice) {
            throw new IllegalArgumentException("minPrice cannot be greater than maxPrice");
        }
        
        List<Window> result = new ArrayList<>();
        for (Window window : windows) {
            if (window.getPrice() >= minPrice && window.getPrice() <= maxPrice) {
                result.add(window);
            }
        }
        return result;
    }
}

public class Main {
    public static void main(String[] args) {
        // Create manufacturers
        Manufacturer manufacturer1 = new Manufacturer("EcoWindows", "contact@ecowindows.com");
        Manufacturer manufacturer2 = new Manufacturer("GreenGlass", "info@greenglass.com");

        // Create window catalog
        WindowCatalog catalog = new WindowCatalog();

        // Add windows to catalog
        catalog.addWindow(new Window("Double-glazed", 299.99, "A", manufacturer1));
        catalog.addWindow(new Window("Triple-glazed", 499.99, "A+", manufacturer1));
        catalog.addWindow(new Window("Single-glazed", 199.99, "B", manufacturer2));
        catalog.addWindow(new Window("Double-glazed", 349.99, "A", manufacturer2));

        // Query examples
        System.out.println("All double-glazed windows:");
        catalog.getWindowsByType("Double-glazed").forEach(System.out::println);

        System.out.println("\nWindows from EcoWindows:");
        catalog.getWindowsByManufacturer("EcoWindows").forEach(System.out::println);

        System.out.println("\nWindows with A rating:");
        catalog.getWindowsByEnergyRating("A").forEach(System.out::println);

        System.out.println("\nWindows between $200 and $400:");
        catalog.getWindowsByPriceRange(200, 400).forEach(System.out::println);
    }
}
```
