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
import java.util.Random;

/**
 * Simulates the operation of a Hydraulic Breaker attached to an excavator.
 * This class models the breaker's behavior including power, impact frequency,
 * and operational state.
 */
public class HydraulicBreaker {
    private boolean isActive;
    private int powerLevel; // Range: 1-10 (1: lowest, 10: highest)
    private int impactFrequency; // Impacts per minute
    private Random random;

    /**
     * Initializes a new HydraulicBreaker with default settings.
     */
    public HydraulicBreaker() {
        this.isActive = false;
        this.powerLevel = 5; // Default medium power
        this.impactFrequency = 100; // Default 100 impacts per minute
        this.random = new Random();
    }

    /**
     * Activates the hydraulic breaker.
     * @throws IllegalStateException if the breaker is already active.
     */
    public void activate() {
        if (isActive) {
            throw new IllegalStateException("Breaker is already active.");
        }
        isActive = true;
        System.out.println("Hydraulic Breaker activated.");
    }

    /**
     * Deactivates the hydraulic breaker.
     * @throws IllegalStateException if the breaker is already inactive.
     */
    public void deactivate() {
        if (!isActive) {
            throw new IllegalStateException("Breaker is already inactive.");
        }
        isActive = false;
        System.out.println("Hydraulic Breaker deactivated.");
    }

    /**
     * Sets the power level of the breaker.
     * @param powerLevel The power level (1-10).
     * @throws IllegalArgumentException if powerLevel is out of range.
     */
    public void setPowerLevel(int powerLevel) {
        if (powerLevel < 1 || powerLevel > 10) {
            throw new IllegalArgumentException("Power level must be between 1 and 10.");
        }
        this.powerLevel = powerLevel;
        System.out.println("Power level set to: " + powerLevel);
    }

    /**
     * Sets the impact frequency of the breaker.
     * @param impactFrequency Impacts per minute (must be positive).
     * @throws IllegalArgumentException if impactFrequency is non-positive.
     */
    public void setImpactFrequency(int impactFrequency) {
        if (impactFrequency <= 0) {
            throw new IllegalArgumentException("Impact frequency must be positive.");
        }
        this.impactFrequency = impactFrequency;
        System.out.println("Impact frequency set to: " + impactFrequency + " impacts per minute");
    }

    /**
     * Simulates the breaker operation for a given duration.
     * @param durationMinutes Duration of operation in minutes.
     * @throws IllegalStateException if breaker is not active.
     * @throws IllegalArgumentException if duration is non-positive.
     */
    public void operate(int durationMinutes) {
        if (!isActive) {
            throw new IllegalStateException("Cannot operate: Breaker is inactive.");
        }
        if (durationMinutes <= 0) {
            throw new IllegalArgumentException("Duration must be positive.");
        }

        System.out.println("Operating Hydraulic Breaker for " + durationMinutes + " minutes...");
        int totalImpacts = durationMinutes * impactFrequency;

        for (int i = 1; i <= totalImpacts; i++) {
            // Simulate random material resistance (1-10)
            int materialResistance = random.nextInt(10) + 1;
            if (materialResistance <= powerLevel) {
                System.out.println("Impact #" + i + ": Material broken successfully.");
            } else {
                System.out.println("Impact #" + i + ": Material too hard. Adjust power level.");
            }
        }
    }

    /**
     * Returns the current power level.
     * @return Current power level (1-10).
     */
    public int getPowerLevel() {
        return powerLevel;
    }

    /**
     * Returns the current impact frequency.
     * @return Current impact frequency (impacts per minute).
     */
    public int getImpactFrequency() {
        return impactFrequency;
    }

    /**
     * Checks if the breaker is active.
     * @return true if active, false otherwise.
     */
    public boolean isActive() {
        return isActive;
    }

    // Example usage
    public static void main(String[] args) {
        HydraulicBreaker breaker = new HydraulicBreaker();
        try {
            breaker.activate();
            breaker.setPowerLevel(8);
            breaker.setImpactFrequency(120);
            breaker.operate(2);
            breaker.deactivate();
        } catch (Exception e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```
