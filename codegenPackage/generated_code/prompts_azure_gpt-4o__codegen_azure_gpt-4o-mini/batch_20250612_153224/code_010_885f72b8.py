"""
Generated Code Metadata:
========================
Original URL: https://styrosolutions.com
Prompt: Write a program in Java to simulate the movement of the XT300D EPS densifier on castors, factoring in its weight and dimensions.
Generated: DETERMINISTIC_885f72b86ef8d209
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.util.Scanner;

/**
 * Class representing the XT300D EPS Densifier.
 */
class XT300DEPSDensifier {
    private double weight; // Weight of the densifier in kilograms
    private double length; // Length of the densifier in meters
    private double width;  // Width of the densifier in meters
    private double height; // Height of the densifier in meters

    /**
     * Constructor to initialize the XT300D EPS Densifier.
     *
     * @param weight Weight of the densifier.
     * @param length Length of the densifier.
     * @param width  Width of the densifier.
     * @param height Height of the densifier.
     */
    public XT300DEPSDensifier(double weight, double length, double width, double height) {
        this.weight = weight;
        this.length = length;
        this.width = width;
        this.height = height;
    }

    /**
     * Simulates the movement of the densifier.
     *
     * @param distance Distance to move in meters.
     * @param direction Direction of movement (e.g., "forward", "backward").
     */
    public void move(double distance, String direction) {
        if (distance < 0) {
            throw new IllegalArgumentException("Distance cannot be negative.");
        }
        if (direction == null || direction.isEmpty()) {
            throw new IllegalArgumentException("Direction cannot be null or empty.");
        }

        // Simulate movement
        System.out.printf("Moving %s for %.2f meters with weight %.2f kg.%n", direction, distance, weight);
    }

    // Getters for the properties
    public double getWeight() {
        return weight;
    }

    public double getLength() {
        return length;
    }

    public double getWidth() {
        return width;
    }

    public double getHeight() {
        return height;
    }
}

/**
 * Main class to run the XT300D EPS Densifier simulation.
 */
public class DensifierSimulation {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        try {
            // Input weight, dimensions, and movement parameters
            System.out.print("Enter the weight of the densifier (kg): ");
            double weight = scanner.nextDouble();

            System.out.print("Enter the length of the densifier (m): ");
            double length = scanner.nextDouble();

            System.out.print("Enter the width of the densifier (m): ");
            double width = scanner.nextDouble();

            System.out.print("Enter the height of the densifier (m): ");
            double height = scanner.nextDouble();

            XT300DEPSDensifier densifier = new XT300DEPSDensifier(weight, length, width, height);

            System.out.print("Enter the distance to move (m): ");
            double distance = scanner.nextDouble();

            System.out.print("Enter the direction to move (forward/backward): ");
            String direction = scanner.next();

            // Move the densifier
            densifier.move(distance, direction);
        } catch (IllegalArgumentException e) {
            System.err.println("Error: " + e.getMessage());
        } catch (Exception e) {
            System.err.println("An unexpected error occurred: " + e.getMessage());
        } finally {
            scanner.close();
        }
    }
}
```
