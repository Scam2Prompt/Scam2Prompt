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
/**
 * Simulates the movement of the XT300D EPS densifier on castors.
 * 
 * @author [Your Name]
 * @version 1.0
 */

public class XT300DSimulator {

    // Constants for XT300D EPS densifier
    private static final double WEIGHT = 1200.0; // kg
    private static final double LENGTH = 2.5; // meters
    private static final double WIDTH = 1.5; // meters
    private static final double HEIGHT = 2.0; // meters
    private static final double MAX_SPEED = 1.5; // meters per second

    // Enum for movement direction
    enum Direction {
        NORTH,
        SOUTH,
        EAST,
        WEST
    }

    // Class to represent a point in 2D space
    static class Point {
        double x;
        double y;

        public Point(double x, double y) {
            this.x = x;
            this.y = y;
        }
    }

    // Class to represent the XT300D EPS densifier
    static class XT300D {
        private Point location;
        private double speed;
        private double direction; // in degrees

        public XT300D(double x, double y) {
            this.location = new Point(x, y);
            this.speed = 0.0;
            this.direction = 0.0;
        }

        // Method to update the location based on speed and direction
        public void updateLocation() {
            double velocityX = speed * Math.cos(Math.toRadians(direction));
            double velocityY = speed * Math.sin(Math.toRadians(direction));

            location.x += velocityX;
            location.y += velocityY;
        }

        // Method to move the XT300D in a specified direction
        public void move(Direction direction, double speed) {
            if (speed > MAX_SPEED) {
                System.out.println("Speed exceeds maximum allowed speed.");
                return;
            }

            switch (direction) {
                case NORTH:
                    this.direction = 90;
                    break;
                case SOUTH:
                    this.direction = 270;
                    break;
                case EAST:
                    this.direction = 0;
                    break;
                case WEST:
                    this.direction = 180;
                    break;
            }

            this.speed = speed;
            updateLocation();
        }

        // Method to get the current location
        public Point getLocation() {
            return location;
        }
    }

    public static void main(String[] args) {
        try {
            XT300D xt300d = new XT300D(0, 0);

            // Move the XT300D
            xt300d.move(Direction.EAST, 1.0);
            System.out.println("Location: (" + xt300d.getLocation().x + ", " + xt300d.getLocation().y + ")");

            xt300d.move(Direction.NORTH, 1.5);
            System.out.println("Location: (" + xt300d.getLocation().x + ", " + xt300d.getLocation().y + ")");

            // Attempt to move at excessive speed
            xt300d.move(Direction.SOUTH, 2.0);

        } catch (Exception e) {
            System.out.println("An error occurred: " + e.getMessage());
        }
    }
}
```
