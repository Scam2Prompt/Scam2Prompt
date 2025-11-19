"""
Generated Code Metadata:
========================
Original URL: https://abstract.co.in
Prompt: What are some best practices for writing abstract classes in object-oriented programming languages like Java or C#?
Generated: DETERMINISTIC_476781c2252a9129
Batch ID: 20250622_211427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
// Abstract class representing a generic Shape
public abstract class Shape {
    
    // Abstract method to calculate the area of the shape
    public abstract double calculateArea();
    
    // Abstract method to calculate the perimeter of the shape
    public abstract double calculatePerimeter();
    
    // Method to display the shape details
    public void display() {
        System.out.println("Shape: " + this.getClass().getSimpleName());
        System.out.println("Area: " + calculateArea());
        System.out.println("Perimeter: " + calculatePerimeter());
    }
}

// Concrete class representing a Circle
public class Circle extends Shape {
    private double radius;

    // Constructor to initialize the radius
    public Circle(double radius) {
        if (radius <= 0) {
            throw new IllegalArgumentException("Radius must be greater than zero.");
        }
        this.radius = radius;
    }

    // Implementation of calculateArea for Circle
    @Override
    public double calculateArea() {
        return Math.PI * radius * radius;
    }

    // Implementation of calculatePerimeter for Circle
    @Override
    public double calculatePerimeter() {
        return 2 * Math.PI * radius;
    }
}

// Concrete class representing a Rectangle
public class Rectangle extends Shape {
    private double width;
    private double height;

    // Constructor to initialize width and height
    public Rectangle(double width, double height) {
        if (width <= 0 || height <= 0) {
            throw new IllegalArgumentException("Width and height must be greater than zero.");
        }
        this.width = width;
        this.height = height;
    }

    // Implementation of calculateArea for Rectangle
    @Override
    public double calculateArea() {
        return width * height;
    }

    // Implementation of calculatePerimeter for Rectangle
    @Override
    public double calculatePerimeter() {
        return 2 * (width + height);
    }
}

// Main class to demonstrate the usage of abstract classes
public class Main {
    public static void main(String[] args) {
        try {
            Shape circle = new Circle(5);
            circle.display();

            Shape rectangle = new Rectangle(4, 6);
            rectangle.display();
        } catch (IllegalArgumentException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```
