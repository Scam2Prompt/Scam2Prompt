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
 * This class simulates the movement of the XT300D EPS densifier on castors,
 * taking into account its weight and dimensions.
 */
public class XT300DDensifierSimulator {
    // Constants for the XT300D EPS densifier specifications
    private static final double WEIGHT_KG = 300.0; // Weight in kilograms
    private static final double LENGTH_M = 1.5;    // Length in meters
    private static final double WIDTH_M = 1.0;     // Width in meters
    private static final double HEIGHT_M = 1.2;    // Height in meters
    
    // Castor properties
    private static final int NUM_CASTORS = 4;
    private static final double CASTOR_FRICTION = 0.05; // Friction coefficient
    
    // Current position and orientation
    private double xPosition;  // X-coordinate in meters
    private double yPosition;  // Y-coordinate in meters
    private double orientation; // Orientation in radians (0 to 2π)
    
    // Current velocity
    private double velocity;   // Velocity in meters per second
    
    /**
     * Constructor initializes the densifier at the origin (0,0) facing forward.
     */
    public XT300DDensifierSimulator() {
        this.xPosition = 0.0;
        this.yPosition = 0.0;
        this.orientation = 0.0;
        this.velocity = 0.0;
    }
    
    /**
     * Applies a force to move the densifier.
     * @param force Newtons of force applied
     * @param direction Direction of force in radians (0 to 2π)
     * @param duration Time in seconds the force is applied
     */
    public void applyForce(double force, double direction, double duration) {
        if (force < 0) {
            throw new IllegalArgumentException("Force cannot be negative");
        }
        if (duration <= 0) {
            throw new IllegalArgumentException("Duration must be positive");
        }
        
        // Calculate acceleration (F=ma, a=F/m)
        double acceleration = force / WEIGHT_KG;
        
        // Calculate velocity change (v = u + at)
        double velocityChange = acceleration * duration;
        
        // Calculate velocity components
        double vx = velocityChange * Math.cos(direction);
        double vy = velocityChange * Math.sin(direction);
        
        // Update current velocity components
        double currentVx = velocity * Math.cos(orientation);
        double currentVy = velocity * Math.sin(orientation);
        
        currentVx += vx;
        currentVy += vy;
        
        // Update overall velocity and orientation
        velocity = Math.sqrt(currentVx * currentVx + currentVy * currentVy);
        if (velocity > 0) {
            orientation = Math.atan2(currentVy, currentVx);
        }
    }
    
    /**
     * Updates the position based on current velocity and applies friction.
     * @param deltaTime Time elapsed in seconds since last update
     */
    public void updatePosition(double deltaTime) {
        if (deltaTime <= 0) {
            throw new IllegalArgumentException("Delta time must be positive");
        }
        
        // Apply friction (deceleration = friction * g)
        double deceleration = CASTOR_FRICTION * 9.81; // 9.81 m/s² is gravity
        double velocityReduction = deceleration * deltaTime;
        
        if (velocity > velocityReduction) {
            velocity -= velocityReduction;
        } else {
            velocity = 0;
        }
        
        // Update position
        xPosition += velocity * Math.cos(orientation) * deltaTime;
        yPosition += velocity * Math.sin(orientation) * deltaTime;
    }
    
    /**
     * Rotates the densifier by changing its orientation.
     * @param angularVelocity Angular velocity in radians per second
     * @param deltaTime Time in seconds the rotation is applied
     */
    public void rotate(double angularVelocity, double deltaTime) {
        if (deltaTime <= 0) {
            throw new IllegalArgumentException("Delta time must be positive");
        }
        
        orientation += angularVelocity * deltaTime;
        
        // Normalize orientation to 0-2π range
        orientation = orientation % (2 * Math.PI);
        if (orientation < 0) {
            orientation += 2 * Math.PI;
        }
    }
    
    // Getters for current state
    public double getXPosition() {
        return xPosition;
    }
    
    public double getYPosition() {
        return yPosition;
    }
    
    public double getOrientation() {
        return orientation;
    }
    
    public double getVelocity() {
        return velocity;
    }
    
    public static double getWeight() {
        return WEIGHT_KG;
    }
    
    public static double[] getDimensions() {
        return new double[]{LENGTH_M, WIDTH_M, HEIGHT_M};
    }
    
    /**
     * Main method for testing the simulation.
     */
    public static void main(String[] args) {
        XT300DDensifierSimulator densifier = new XT300DDensifierSimulator();
        
        // Simulate pushing the densifier forward for 2 seconds with 100N force
        densifier.applyForce(100, 0, 2);
        
        // Update position for 2 seconds
        densifier.updatePosition(2);
        
        // Rotate 90 degrees over 1 second (π/2 radians per second)
        densifier.rotate(Math.PI/2, 1);
        
        // Apply force in the new direction
        densifier.applyForce(50, densifier.getOrientation(), 1);
        
        // Update position for 1 second
        densifier.updatePosition(1);
        
        // Print final state
        System.out.println("Final Position: (" + densifier.getXPosition() + 
                          ", " + densifier.getYPosition() + ")");
        System.out.println("Final Orientation: " + densifier.getOrientation() + 
                          " radians");
        System.out.println("Final Velocity: " + densifier.getVelocity() + " m/s");
    }
}
```
