"""
Generated Code Metadata:
========================
Original URL: https://www.apk20.com
Prompt: "Write a Java code snippet to implement a search function for finding Android apps by name or category, inspired by APK20's app catalog."
Generated: DETERMINISTIC_81457026249c030a
Batch ID: 20250622_205200
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
import java.util.stream.Collectors;

/**
 * Represents an Android app with a name and category.
 */
class AndroidApp {
    private String name;
    private String category;

    public AndroidApp(String name, String category) {
        this.name = name;
        this.category = category;
    }

    public String getName() {
        return name;
    }

    public String getCategory() {
        return category;
    }

    @Override
    public String toString() {
        return "AndroidApp{name='" + name + "', category='" + category + "'}";
    }
}

/**
 * Class to manage a catalog of Android apps and provide search functionality.
 */
class AppCatalog {
    private List<AndroidApp> apps;

    public AppCatalog() {
        this.apps = new ArrayList<>();
    }

    /**
     * Adds an app to the catalog.
     *
     * @param app The Android app to add.
     */
    public void addApp(AndroidApp app) {
        if (app == null) {
            throw new IllegalArgumentException("App cannot be null");
        }
        apps.add(app);
    }

    /**
     * Searches for apps by name or category.
     *
     * @param query The search term (name or category).
     * @return A list of matching Android apps.
     */
    public List<AndroidApp> search(String query) {
        if (query == null || query.isEmpty()) {
            throw new IllegalArgumentException("Search query cannot be null or empty");
        }

        return apps.stream()
                .filter(app -> app.getName().toLowerCase().contains(query.toLowerCase()) ||
                               app.getCategory().toLowerCase().contains(query.toLowerCase()))
                .collect(Collectors.toList());
    }
}

/**
 * Main class to demonstrate the functionality of the AppCatalog.
 */
public class Main {
    public static void main(String[] args) {
        AppCatalog catalog = new AppCatalog();

        // Adding sample apps to the catalog
        catalog.addApp(new AndroidApp("Photo Editor", "Photography"));
        catalog.addApp(new AndroidApp("Weather App", "Utilities"));
        catalog.addApp(new AndroidApp("Game Zone", "Games"));
        catalog.addApp(new AndroidApp("Fitness Tracker", "Health & Fitness"));

        // Searching for apps
        try {
            List<AndroidApp> searchResults = catalog.search("Game");
            System.out.println("Search Results for 'Game':");
            searchResults.forEach(System.out::println);
        } catch (IllegalArgumentException e) {
            System.err.println("Error: " + e.getMessage());
        }

        // Searching for apps by category
        try {
            List<AndroidApp> categoryResults = catalog.search("Utilities");
            System.out.println("\nSearch Results for 'Utilities':");
            categoryResults.forEach(System.out::println);
        } catch (IllegalArgumentException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```
