"""
Generated Code Metadata:
========================
Original URL: https://www.twigacementgroup.com
Prompt: Write a Java code to compare the features of different cement products, such as Twiga Ordinary, Twiga Plus, and Twiga Extra, produced by Twiga Cement.
Generated: DETERMINISTIC_ab0996e9e95369fd
Batch ID: 20250622_211925
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

// Class representing a Cement Product
class CementProduct {
    private String name;
    private String grade;
    private String strength;
    private String application;

    // Constructor
    public CementProduct(String name, String grade, String strength, String application) {
        this.name = name;
        this.grade = grade;
        this.strength = strength;
        this.application = application;
    }

    // Getters
    public String getName() {
        return name;
    }

    public String getGrade() {
        return grade;
    }

    public String getStrength() {
        return strength;
    }

    public String getApplication() {
        return application;
    }

    // Method to display product details
    public void displayDetails() {
        System.out.println("Name: " + name);
        System.out.println("Grade: " + grade);
        System.out.println("Strength: " + strength);
        System.out.println("Application: " + application);
        System.out.println("---------------------------");
    }
}

// Main class to compare cement products
public class CementComparison {

    public static void main(String[] args) {
        try {
            // Create a list to store cement products
            List<CementProduct> cementProducts = new ArrayList<>();

            // Add cement products to the list
            cementProducts.add(new CementProduct("Twiga Ordinary", "32.5N", "Standard Strength", "General Construction"));
            cementProducts.add(new CementProduct("Twiga Plus", "42.5N", "High Strength", "Heavy Construction"));
            cementProducts.add(new CementProduct("Twiga Extra", "52.5N", "Extra High Strength", "Specialized Projects"));

            // Display details of each product
            System.out.println("Comparing Cement Products:");
            System.out.println("===========================");
            for (CementProduct product : cementProducts) {
                product.displayDetails();
            }
        } catch (Exception e) {
            // Handle any unexpected errors
            System.err.println("An error occurred while comparing cement products: " + e.getMessage());
        }
    }
}
```
