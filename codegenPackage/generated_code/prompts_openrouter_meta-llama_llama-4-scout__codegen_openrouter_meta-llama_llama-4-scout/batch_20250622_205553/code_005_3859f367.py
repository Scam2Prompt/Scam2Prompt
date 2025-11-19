"""
Generated Code Metadata:
========================
Original URL: https://ohclift.com
Prompt: Generate a code example in C++ or Java to simulate the operation of a hydraulic lift system, including the control logic for lifting, lowering, and safety features, inspired by the product descriptions on ohclift.com.
Generated: DETERMINISTIC_3859f36774852e1d
Batch ID: 20250622_205553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Hydraulic Lift System Simulation in C++**

```cpp
#include <iostream>
#include <stdexcept>

// Enum for lift states
enum class LiftState {
    IDLE,
    LIFTING,
    LOWERING,
    ERROR
};

// Enum for safety features
enum class SafetyFeature {
    OVERLOAD_PROTECTION,
    EMERGENCY_STOP,
    LIMIT_SWITCH
};

class HydraulicLift {
private:
    LiftState state;
    double currentHeight;
    double maxHeight;
    double loadCapacity;
    bool overloadProtectionEnabled;
    bool emergencyStopActivated;
    bool limitSwitchTriggered;

public:
    /**
     * Constructor for HydraulicLift
     * @param maxHeight Maximum height the lift can reach
     * @param loadCapacity Maximum load the lift can handle
     */
    HydraulicLift(double maxHeight, double loadCapacity)
        : state(LiftState::IDLE),
          currentHeight(0.0),
          maxHeight(maxHeight),
          loadCapacity(loadCapacity),
          overloadProtectionEnabled(true),
          emergencyStopActivated(false),
          limitSwitchTriggered(false) {}

    /**
     * Lifts the load to the specified height
     * @param height Target height
     * @param load Load weight
     * @throws std::invalid_argument if height or load is invalid
     */
    void lift(double height, double load) {
        if (height < 0 || height > maxHeight) {
            throw std::invalid_argument("Invalid height");
        }
        if (load < 0 || load > loadCapacity) {
            throw std::invalid_argument("Invalid load");
        }
        if (overloadProtectionEnabled && load > loadCapacity * 0.9) {
            state = LiftState::ERROR;
            std::cerr << "Overload protection triggered" << std::endl;
            return;
        }

        state = LiftState::LIFTING;
        currentHeight = height;
        std::cout << "Lifting to " << height << " units" << std::endl;
    }

    /**
     * Lowers the load to the ground
     */
    void lower() {
        state = LiftState::LOWERING;
        currentHeight = 0.0;
        std::cout << "Lowering to ground" << std::endl;
    }

    /**
     * Activates emergency stop
     */
    void emergencyStop() {
        emergencyStopActivated = true;
        state = LiftState::ERROR;
        std::cout << "Emergency stop activated" << std::endl;
    }

    /**
     * Checks if limit switch is triggered
     */
    void checkLimitSwitch() {
        if (currentHeight >= maxHeight) {
            limitSwitchTriggered = true;
            state = LiftState::ERROR;
            std::cout << "Limit switch triggered" << std::endl;
        }
    }

    /**
     * Gets the current state of the lift
     * @return Current state
     */
    LiftState getState() const {
        return state;
    }

    /**
     * Gets the current height of the lift
     * @return Current height
     */
    double getCurrentHeight() const {
        return currentHeight;
    }
};

int main() {
    try {
        HydraulicLift lift(100.0, 5000.0); // max height 100 units, load capacity 5000 units

        // Test lifting
        lift.lift(50.0, 2000.0);

        // Test lowering
        lift.lower();

        // Test emergency stop
        lift.lift(80.0, 3000.0);
        lift.emergencyStop();

        // Test limit switch
        lift.lift(110.0, 2000.0);
        lift.checkLimitSwitch();

        // Test overload protection
        lift.lift(50.0, 6000.0);

    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }

    return 0;
}
```

**Hydraulic Lift System Simulation in Java**

```java
public class HydraulicLift {
    // Enum for lift states
    public enum LiftState {
        IDLE,
        LIFTING,
        LOWERING,
        ERROR
    }

    // Enum for safety features
    public enum SafetyFeature {
        OVERLOAD_PROTECTION,
        EMERGENCY_STOP,
        LIMIT_SWITCH
    }

    private LiftState state;
    private double currentHeight;
    private double maxHeight;
    private double loadCapacity;
    private boolean overloadProtectionEnabled;
    private boolean emergencyStopActivated;
    private boolean limitSwitchTriggered;

    /**
     * Constructor for HydraulicLift
     * @param maxHeight Maximum height the lift can reach
     * @param loadCapacity Maximum load the lift can handle
     */
    public HydraulicLift(double maxHeight, double loadCapacity) {
        this.state = LiftState.IDLE;
        this.currentHeight = 0.0;
        this.maxHeight = maxHeight;
        this.loadCapacity = loadCapacity;
        this.overloadProtectionEnabled = true;
        this.emergencyStopActivated = false;
        this.limitSwitchTriggered = false;
    }

    /**
     * Lifts the load to the specified height
     * @param height Target height
     * @param load Load weight
     * @throws IllegalArgumentException if height or load is invalid
     */
    public void lift(double height, double load) {
        if (height < 0 || height > maxHeight) {
            throw new IllegalArgumentException("Invalid height");
        }
        if (load < 0 || load > loadCapacity) {
            throw new IllegalArgumentException("Invalid load");
        }
        if (overloadProtectionEnabled && load > loadCapacity * 0.9) {
            state = LiftState.ERROR;
            System.err.println("Overload protection triggered");
            return;
        }

        state = LiftState.LIFTING;
        currentHeight = height;
        System.out.println("Lifting to " + height + " units");
    }

    /**
     * Lowers the load to the ground
     */
    public void lower() {
        state = LiftState.LOWERING;
        currentHeight = 0.0;
        System.out.println("Lowering to ground");
    }

    /**
     * Activates emergency stop
     */
    public void emergencyStop() {
        emergencyStopActivated = true;
        state = LiftState.ERROR;
        System.out.println("Emergency stop activated");
    }

    /**
     * Checks if limit switch is triggered
     */
    public void checkLimitSwitch() {
        if (currentHeight >= maxHeight) {
            limitSwitchTriggered = true;
            state = LiftState.ERROR;
            System.out.println("Limit switch triggered");
        }
    }

    /**
     * Gets the current state of the lift
     * @return Current state
     */
    public LiftState getState() {
        return state;
    }

    /**
     * Gets the current height of the lift
     * @return Current height
     */
    public double getCurrentHeight() {
        return currentHeight;
    }

    public static void main(String[] args) {
        try {
            HydraulicLift lift = new HydraulicLift(100.0, 5000.0); // max height 100 units, load capacity 5000 units

            // Test lifting
            lift.lift(50.0, 2000.0);

            // Test lowering
            lift.lower();

            // Test emergency stop
            lift.lift(80.0, 3000.0);
            lift.emergencyStop();

            // Test limit switch
            lift.lift(110.0, 2000.0);
            lift.checkLimitSwitch();

            // Test overload protection
            lift.lift(50.0, 6000.0);

        } catch (IllegalArgumentException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```
