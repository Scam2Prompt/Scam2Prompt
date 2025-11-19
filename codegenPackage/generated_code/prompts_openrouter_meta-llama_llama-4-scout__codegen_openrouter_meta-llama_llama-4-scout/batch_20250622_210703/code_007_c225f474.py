"""
Generated Code Metadata:
========================
Original URL: https://www.twincityjacuzzi.com
Prompt: Write a code snippet in Java to simulate the experience of using a Jacuzzi hot tub, including temperature control and jet settings.
Generated: DETERMINISTIC_c225f474aa8695ff
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
/**
 * Simulates the experience of using a Jacuzzi hot tub.
 */
public class JacuzziHotTub {

    // Temperature settings in degrees Fahrenheit
    private double temperature;
    private double minTemperature = 80.0;
    private double maxTemperature = 104.0;

    // Jet settings
    private boolean jetsOn;
    private int jetSpeed; // 1-5, where 1 is low and 5 is high

    /**
     * Initializes the Jacuzzi hot tub with default settings.
     */
    public JacuzziHotTub() {
        this.temperature = 98.0; // Default temperature
        this.jetsOn = false;
        this.jetSpeed = 1; // Default jet speed
    }

    /**
     * Sets the temperature of the Jacuzzi hot tub.
     * 
     * @param temperature The desired temperature in degrees Fahrenheit.
     * @throws IllegalArgumentException If the temperature is out of range.
     */
    public void setTemperature(double temperature) {
        if (temperature < minTemperature || temperature > maxTemperature) {
            throw new IllegalArgumentException("Temperature must be between " + minTemperature + " and " + maxTemperature);
        }
        this.temperature = temperature;
    }

    /**
     * Gets the current temperature of the Jacuzzi hot tub.
     * 
     * @return The current temperature in degrees Fahrenheit.
     */
    public double getTemperature() {
        return temperature;
    }

    /**
     * Toggles the jets on or off.
     */
    public void toggleJets() {
        jetsOn = !jetsOn;
    }

    /**
     * Sets the speed of the jets.
     * 
     * @param speed The desired jet speed (1-5).
     * @throws IllegalArgumentException If the speed is out of range.
     */
    public void setJetSpeed(int speed) {
        if (speed < 1 || speed > 5) {
            throw new IllegalArgumentException("Jet speed must be between 1 and 5");
        }
        this.jetSpeed = speed;
    }

    /**
     * Gets the current jet speed.
     * 
     * @return The current jet speed (1-5).
     */
    public int getJetSpeed() {
        return jetSpeed;
    }

    /**
     * Checks if the jets are on.
     * 
     * @return True if the jets are on, false otherwise.
     */
    public boolean areJetsOn() {
        return jetsOn;
    }

    public static void main(String[] args) {
        JacuzziHotTub hotTub = new JacuzziHotTub();

        // Test temperature control
        System.out.println("Initial temperature: " + hotTub.getTemperature());
        hotTub.setTemperature(100.0);
        System.out.println("Temperature after setting to 100: " + hotTub.getTemperature());

        // Test jet settings
        System.out.println("Jets on: " + hotTub.areJetsOn());
        hotTub.toggleJets();
        System.out.println("Jets on after toggle: " + hotTub.areJetsOn());
        hotTub.setJetSpeed(3);
        System.out.println("Jet speed: " + hotTub.getJetSpeed());

        // Test error handling
        try {
            hotTub.setTemperature(105.0);
        } catch (IllegalArgumentException e) {
            System.out.println("Error: " + e.getMessage());
        }

        try {
            hotTub.setJetSpeed(6);
        } catch (IllegalArgumentException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
```
