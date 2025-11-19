"""
Generated Code Metadata:
========================
Original URL: https://mirayaelectricsac.com
Prompt: "Develop a code snippet in C++ to simulate the operation of an electric motor control system using products from Miraya Electric S.A.C."
Generated: DETERMINISTIC_df137264d2f2ef29
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```cpp
#include <iostream>
#include <stdexcept>

// Enum for motor status
enum class MotorStatus {
    STARTED,
    STOPPED,
    FAULTY
};

// Class representing an electric motor
class ElectricMotor {
private:
    MotorStatus status;
    double voltage;
    double current;

public:
    /**
     * Constructor for ElectricMotor
     * @param voltage Initial voltage
     * @param current Initial current
     */
    ElectricMotor(double voltage = 0.0, double current = 0.0)
        : status(MotorStatus::STOPPED), voltage(voltage), current(current) {}

    /**
     * Starts the electric motor
     */
    void start() {
        if (status != MotorStatus::STARTED) {
            status = MotorStatus::STARTED;
            std::cout << "Motor started successfully." << std::endl;
        } else {
            std::cout << "Motor is already started." << std::endl;
        }
    }

    /**
     * Stops the electric motor
     */
    void stop() {
        if (status != MotorStatus::STOPPED) {
            status = MotorStatus::STOPPED;
            std::cout << "Motor stopped successfully." << std::endl;
        } else {
            std::cout << "Motor is already stopped." << std::endl;
        }
    }

    /**
     * Sets the voltage of the electric motor
     * @param voltage New voltage value
     */
    void setVoltage(double voltage) {
        if (voltage >= 0) {
            this->voltage = voltage;
            std::cout << "Voltage set to " << voltage << "V." << std::endl;
        } else {
            throw std::invalid_argument("Voltage cannot be negative.");
        }
    }

    /**
     * Sets the current of the electric motor
     * @param current New current value
     */
    void setCurrent(double current) {
        if (current >= 0) {
            this->current = current;
            std::cout << "Current set to " << current << "A." << std::endl;
        } else {
            throw std::invalid_argument("Current cannot be negative.");
        }
    }

    /**
     * Gets the status of the electric motor
     * @return Current motor status
     */
    MotorStatus getStatus() const {
        return status;
    }

    /**
     * Gets the voltage of the electric motor
     * @return Current voltage
     */
    double getVoltage() const {
        return voltage;
    }

    /**
     * Gets the current of the electric motor
     * @return Current current
     */
    double getCurrent() const {
        return current;
    }
};

// Class representing a motor control system
class MotorControlSystem {
private:
    ElectricMotor motor;

public:
    /**
     * Constructor for MotorControlSystem
     */
    MotorControlSystem() = default;

    /**
     * Starts the motor control system
     */
    void startSystem() {
        motor.start();
    }

    /**
     * Stops the motor control system
     */
    void stopSystem() {
        motor.stop();
    }

    /**
     * Sets the voltage for the motor control system
     * @param voltage New voltage value
     */
    void setVoltage(double voltage) {
        try {
            motor.setVoltage(voltage);
        } catch (const std::exception& e) {
            std::cerr << "Error: " << e.what() << std::endl;
        }
    }

    /**
     * Sets the current for the motor control system
     * @param current New current value
     */
    void setCurrent(double current) {
        try {
            motor.setCurrent(current);
        } catch (const std::exception& e) {
            std::cerr << "Error: " << e.what() << std::endl;
        }
    }

    /**
     * Displays the motor control system status
     */
    void displayStatus() const {
        std::cout << "Motor Status: ";
        switch (motor.getStatus()) {
            case MotorStatus::STARTED:
                std::cout << "Started" << std::endl;
                break;
            case MotorStatus::STOPPED:
                std::cout << "Stopped" << std::endl;
                break;
            case MotorStatus::FAULTY:
                std::cout << "Faulty" << std::endl;
                break;
        }
        std::cout << "Voltage: " << motor.getVoltage() << "V" << std::endl;
        std::cout << "Current: " << motor.getCurrent() << "A" << std::endl;
    }
};

int main() {
    MotorControlSystem mcs;
    mcs.startSystem();
    mcs.setVoltage(230.0);
    mcs.setCurrent(10.5);
    mcs.displayStatus();
    mcs.stopSystem();
    return 0;
}
```
