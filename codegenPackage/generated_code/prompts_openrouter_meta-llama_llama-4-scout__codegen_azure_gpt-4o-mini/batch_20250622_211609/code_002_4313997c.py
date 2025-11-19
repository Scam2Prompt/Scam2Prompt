"""
Generated Code Metadata:
========================
Original URL: https://fmt.co.id
Prompt: Generate a Java code snippet to simulate the operation of a Hydraulic Breaker attached to an excavator for construction projects.
Generated: DETERMINISTIC_4313997cf2968db5
Batch ID: 20250622_211609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
/**
 * HydraulicBreakerSimulator simulates the operation of a hydraulic breaker
 * attached to an excavator for construction projects.
 */
public class HydraulicBreakerSimulator {
    
    // State variables
    private boolean isActive; // Indicates if the breaker is currently active
    private double pressure;  // Current hydraulic pressure in the system
    private final double maxPressure; // Maximum allowable pressure

    /**
     * Constructor to initialize the hydraulic breaker simulator.
     * 
     * @param maxPressure Maximum allowable pressure for the hydraulic breaker.
     */
    public HydraulicBreakerSimulator(double maxPressure) {
        if (maxPressure <= 0) {
            throw new IllegalArgumentException("Max pressure must be greater than zero.");
        }
        this.maxPressure = maxPressure;
        this.pressure = 0;
        this.isActive = false;
    }

    /**
     * Activates the hydraulic breaker, increasing the pressure.
     * 
     * @param increase Amount to increase the pressure.
     * @throws IllegalStateException if the breaker is already active.
     * @throws IllegalArgumentException if the increase would exceed max pressure.
     */
    public void activate(double increase) {
        if (isActive) {
            throw new IllegalStateException("Hydraulic breaker is already active.");
        }
        if (increase <= 0 || pressure + increase > maxPressure) {
            throw new IllegalArgumentException("Invalid pressure increase.");
        }
        pressure += increase;
        isActive = true;
        System.out.println("Hydraulic breaker activated. Current pressure: " + pressure);
    }

    /**
     * Deactivates the hydraulic breaker, resetting the pressure.
     */
    public void deactivate() {
        if (!isActive) {
            System.out.println("Hydraulic breaker is already inactive.");
            return;
        }
        pressure = 0;
        isActive = false;
        System.out.println("Hydraulic breaker deactivated.");
    }

    /**
     * Simulates the operation of the hydraulic breaker.
     * 
     * @throws IllegalStateException if the breaker is not active.
     */
    public void operate() {
        if (!isActive) {
            throw new IllegalStateException("Hydraulic breaker must be active to operate.");
        }
        System.out.println("Operating hydraulic breaker at pressure: " + pressure);
        // Simulate operation logic here (e.g., impact, vibration)
    }

    /**
     * Main method to demonstrate the functionality of the Hydraulic Breaker Simulator.
     */
    public static void main(String[] args) {
        try {
            HydraulicBreakerSimulator breaker = new HydraulicBreakerSimulator(100.0);
            breaker.activate(50.0);
            breaker.operate();
            breaker.deactivate();
        } catch (Exception e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```
