"""
Generated Code Metadata:
========================
Original URL: https://aayraint.com
Prompt: Write a code snippet in Java to control Aayra International Limited's microprocessor-controlled side sealing machine for plane and printed bags.
Generated: DETERMINISTIC_5692b1c1a81c88ec
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.util.concurrent.TimeUnit;

/**
 * Controller for Aayra International Limited's microprocessor-controlled side sealing machine.
 * This class provides methods to control the sealing process for both plane and printed bags.
 */
public class SideSealingMachineController {

    // Machine states
    private enum MachineState {
        IDLE, HEATING, SEALING, COOLING, ERROR
    }

    private MachineState currentState;
    private boolean isPrintedBagMode;
    private double temperature;
    private double pressure;
    private int sealingTimeMs;

    // Constants
    private static final double MIN_TEMPERATURE = 100.0;
    private static final double MAX_TEMPERATURE = 300.0;
    private static final double MIN_PRESSURE = 0.5;
    private static final double MAX_PRESSURE = 5.0;
    private static final int MIN_SEALING_TIME_MS = 500;
    private static final int MAX_SEALING_TIME_MS = 5000;

    /**
     * Initializes the sealing machine controller.
     */
    public SideSealingMachineController() {
        this.currentState = MachineState.IDLE;
        this.isPrintedBagMode = false;
        this.temperature = 150.0;
        this.pressure = 2.5;
        this.sealingTimeMs = 2000;
    }

    /**
     * Sets the machine to printed bag mode.
     * @param isPrintedBag true for printed bags, false for plane bags
     */
    public synchronized void setPrintedBagMode(boolean isPrintedBag) {
        if (currentState != MachineState.IDLE) {
            throw new IllegalStateException("Cannot change bag mode while machine is running");
        }
        this.isPrintedBagMode = isPrintedBag;
    }

    /**
     * Sets the sealing temperature.
     * @param temperature Temperature in degrees Celsius
     * @throws IllegalArgumentException if temperature is out of range
     */
    public synchronized void setTemperature(double temperature) {
        if (temperature < MIN_TEMPERATURE || temperature > MAX_TEMPERATURE) {
            throw new IllegalArgumentException("Temperature must be between " + MIN_TEMPERATURE + " and " + MAX_TEMPERATURE);
        }
        this.temperature = temperature;
    }

    /**
     * Sets the sealing pressure.
     * @param pressure Pressure in bar
     * @throws IllegalArgumentException if pressure is out of range
     */
    public synchronized void setPressure(double pressure) {
        if (pressure < MIN_PRESSURE || pressure > MAX_PRESSURE) {
            throw new IllegalArgumentException("Pressure must be between " + MIN_PRESSURE + " and " + MAX_PRESSURE);
        }
        this.pressure = pressure;
    }

    /**
     * Sets the sealing time.
     * @param sealingTimeMs Sealing time in milliseconds
     * @throws IllegalArgumentException if time is out of range
     */
    public synchronized void setSealingTime(int sealingTimeMs) {
        if (sealingTimeMs < MIN_SEALING_TIME_MS || sealingTimeMs > MAX_SEALING_TIME_MS) {
            throw new IllegalArgumentException("Sealing time must be between " + MIN_SEALING_TIME_MS + " and " + MAX_SEALING_TIME_MS + " ms");
        }
        this.sealingTimeMs = sealingTimeMs;
    }

    /**
     * Starts the sealing process.
     * @throws IllegalStateException if machine is not idle
     */
    public synchronized void startSealing() {
        if (currentState != MachineState.IDLE) {
            throw new IllegalStateException("Machine is not idle");
        }

        try {
            currentState = MachineState.HEATING;
            heatElements();

            currentState = MachineState.SEALING;
            applySeal();

            currentState = MachineState.COOLING;
            coolElements();

            currentState = MachineState.IDLE;
        } catch (Exception e) {
            currentState = MachineState.ERROR;
            throw new RuntimeException("Sealing process failed", e);
        }
    }

    /**
     * Emergency stops the machine.
     */
    public synchronized void emergencyStop() {
        currentState = MachineState.IDLE;
        // Implementation would include stopping all physical processes
    }

    /**
     * Gets the current machine state.
     * @return Current machine state
     */
    public synchronized MachineState getCurrentState() {
        return currentState;
    }

    private void heatElements() throws InterruptedException {
        // Simulate heating process
        System.out.println("Heating elements to " + temperature + "°C");
        TimeUnit.MILLISECONDS.sleep(1000);
    }

    private void applySeal() throws InterruptedException {
        // Simulate sealing process
        System.out.println("Applying seal with " + pressure + " bar pressure for " + sealingTimeMs + " ms");
        TimeUnit.MILLISECONDS.sleep(sealingTimeMs);
    }

    private void coolElements() throws InterruptedException {
        // Simulate cooling process
        System.out.println("Cooling elements");
        TimeUnit.MILLISECONDS.sleep(500);
    }
}
```
