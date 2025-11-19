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
import java.util.*;

// Enum for energy efficiency ratings
enum EnergyEfficiencyRating {
    A_PLUS,
    A,
    B,
    C,
    D,
    E,
    F,
    G
}

// Class to represent manufacturer details
class Manufacturer {
    private String name;
    private String country;

    public Manufacturer(String name, String country) {
        this.name = name;
        this.country = country;
    }

    public String getName() {
        return name;
    }

    public String getCountry() {
        return country;
    }
}

// Class to represent window details
class Window {
    private String type;
    private EnergyEfficiencyRating energyEfficiencyRating;
    private double price;
    private Manufacturer manufacturer;

    public Window(String type, EnergyEfficiencyRating energyEfficiencyRating, double price, Manufacturer manufacturer) {
        this.type = type;
        this.energyEfficiencyRating = energyEfficiencyRating;
        this.price = price;
        this.manufacturer = manufacturer;
    }

    public String getType() {
        return type;
    }

    public EnergyEfficiencyRating getEnergyEfficiencyRating() {
        return energyEfficiencyRating;
    }

    public double getPrice() {
        return price;
    }

    public Manufacturer getManufacturer() {
        return manufacturer;
    }
}

// Class to store and query window data
class WindowDatabase {
    private Map<String, Window> windows;

    public WindowDatabase() {
        this.windows = new HashMap<>();
    }

    // Add a window to the database
    public void addWindow(Window window) {
        windows.put(window.getType(), window);
    }

    // Get a window by type
    public Window getWindow(String type) {
        return windows.get(type);
    }

    // Get all windows with a specific energy efficiency rating
    public List<Window> getWindowsByEnergyEfficiencyRating(EnergyEfficiencyRating rating) {
        List<Window> result = new ArrayList<>();
        for (Window window : windows.values()) {
            if (window.getEnergyEfficiencyRating() == rating) {
                result.add(window);
            }
        }
        return result;
    }

    // Get all windows from a specific manufacturer
    public List<Window> getWindowsByManufacturer(Manufacturer manufacturer) {
        List<Window> result = new ArrayList<>();
        for (Window window : windows.values()) {
            if (window.getManufacturer().getName().equals(manufacturer.getName()) 
                && window.getManufacturer().getCountry().equals(manufacturer.getCountry())) {
                result.add(window);
            }
        }
        return result;
    }
}

public class Main {
    public static void main(String[] args) {
        // Create manufacturers
        Manufacturer manufacturer1 = new Manufacturer("Manufacturer1", "Country1");
        Manufacturer manufacturer2 = new Manufacturer("Manufacturer2", "Country2");

        // Create windows
        Window window1 = new Window("Window1", EnergyEfficiencyRating.A_PLUS, 100.0, manufacturer1);
        Window window2 = new Window("Window2", EnergyEfficiencyRating.A, 80.0, manufacturer1);
        Window window3 = new Window("Window3", EnergyEfficiencyRating.A_PLUS, 120.0, manufacturer2);

        // Create window database
        WindowDatabase database = new WindowDatabase();
        database.addWindow(window1);
        database.addWindow(window2);
        database.addWindow(window3);

        // Query database
        Window queriedWindow = database.getWindow("Window1");
        if (queriedWindow != null) {
            System.out.println("Queried Window: " + queriedWindow.getType());
            System.out.println("Energy Efficiency Rating: " + queriedWindow.getEnergyEfficiencyRating());
            System.out.println("Price: " + queriedWindow.getPrice());
            System.out.println("Manufacturer: " + queriedWindow.getManufacturer().getName() + ", " + queriedWindow.getManufacturer().getCountry());
        }

        List<Window> windowsWithRating = database.getWindowsByEnergyEfficiencyRating(EnergyEfficiencyRating.A_PLUS);
        System.out.println("Windows with A+ rating:");
        for (Window window : windowsWithRating) {
            System.out.println(window.getType());
        }

        List<Window> windowsFromManufacturer = database.getWindowsByManufacturer(manufacturer1);
        System.out.println("Windows from Manufacturer1:");
        for (Window window : windowsFromManufacturer) {
            System.out.println(window.getType());
        }
    }
}
```
