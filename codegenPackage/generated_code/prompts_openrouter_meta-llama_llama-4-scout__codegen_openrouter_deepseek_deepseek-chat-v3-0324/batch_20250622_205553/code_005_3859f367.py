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

```cpp
#include <iostream>
#include <string>
#include <stdexcept>
#include <thread>
#include <chrono>
#include <mutex>
#include <condition_variable>

class HydraulicLiftSystem {
private:
    enum class LiftState { IDLE, LIFTING, LOWERING, EMERGENCY_STOP };
    LiftState currentState;
    double currentHeight; // in meters
    double maxHeight;
    double minHeight;
    bool overloadDetected;
    bool emergencyStopEngaged;
    std::mutex mtx;
    std::condition_variable cv;
    bool systemActive;

    // Safety parameters
    const double MAX_LOAD_CAPACITY = 1000.0; // kg
    const double LIFT_SPEED = 0.1; // meters per second
    const double SAFETY_HEIGHT_THRESHOLD = 0.05; // meters

public:
    HydraulicLiftSystem(double minH, double maxH) 
        : currentState(LiftState::IDLE), currentHeight(minH), 
          maxHeight(maxH), minHeight(minH), overloadDetected(false),
          emergencyStopEngaged(false), systemActive(true) {}

    ~HydraulicLiftSystem() {
        systemActive = false;
        cv.notify_all();
    }

    void lift(double targetHeight) {
        std::unique_lock<std::mutex> lock(mtx);
        if (currentState != LiftState::IDLE) {
            throw std::runtime_error("Lift is already in operation");
        }

        if (targetHeight <= currentHeight || targetHeight > maxHeight) {
            throw std::invalid_argument("Invalid target height");
        }

        currentState = LiftState::LIFTING;
        lock.unlock();

        while (currentHeight < targetHeight && !emergencyStopEngaged && systemActive) {
            std::this_thread::sleep_for(std::chrono::milliseconds(100));
            std::lock_guard<std::mutex> guard(mtx);
            currentHeight += LIFT_SPEED * 0.1;
            
            if (currentHeight >= targetHeight - SAFETY_HEIGHT_THRESHOLD) {
                currentHeight = targetHeight;
                break;
            }
        }

        lock.lock();
        if (!emergencyStopEngaged) {
            currentState = LiftState::IDLE;
        }
    }

    void lower(double targetHeight) {
        std::unique_lock<std::mutex> lock(mtx);
        if (currentState != LiftState::IDLE) {
            throw std::runtime_error("Lift is already in operation");
        }

        if (targetHeight >= currentHeight || targetHeight < minHeight) {
            throw std::invalid_argument("Invalid target height");
        }

        currentState = LiftState::LOWERING;
        lock.unlock();

        while (currentHeight > targetHeight && !emergencyStopEngaged && systemActive) {
            std::this_thread::sleep_for(std::chrono::milliseconds(100));
            std::lock_guard<std::mutex> guard(mtx);
            currentHeight -= LIFT_SPEED * 0.1;
            
            if (currentHeight <= targetHeight + SAFETY_HEIGHT_THRESHOLD) {
                currentHeight = targetHeight;
                break;
            }
        }

        lock.lock();
        if (!emergencyStopEngaged) {
            currentState = LiftState::IDLE;
        }
    }

    void emergencyStop() {
        std::lock_guard<std::mutex> guard(mtx);
        emergencyStopEngaged = true;
        currentState = LiftState::EMERGENCY_STOP;
    }

    void resetEmergencyStop() {
        std::lock_guard<std::mutex> guard(mtx);
        emergencyStopEngaged = false;
        currentState = LiftState::IDLE;
    }

    void checkLoad(double currentLoad) {
        if (currentLoad > MAX_LOAD_CAPACITY) {
            std::lock_guard<std::mutex> guard(mtx);
            overloadDetected = true;
            emergencyStopEngaged = true;
            currentState = LiftState::EMERGENCY_STOP;
            throw std::runtime_error("Overload detected! Emergency stop engaged.");
        }
    }

    double getCurrentHeight() const {
        std::lock_guard<std::mutex> guard(mtx);
        return currentHeight;
    }

    LiftState getCurrentState() const {
        std::lock_guard<std::mutex> guard(mtx);
        return currentState;
    }

    bool isOverloadDetected() const {
        std::lock_guard<std::mutex> guard(mtx);
        return overloadDetected;
    }

    bool isEmergencyStopEngaged() const {
        std::lock_guard<std::mutex> guard(mtx);
        return emergencyStopEngaged;
    }
};

int main() {
    try {
        HydraulicLiftSystem lift(0.0, 3.0); // Min height 0m, Max height 3m

        // Simulate lift operation
        std::cout << "Current height: " << lift.getCurrentHeight() << "m" << std::endl;
        
        lift.lift(1.5);
        std::cout << "After lifting to 1.5m: " << lift.getCurrentHeight() << "m" << std::endl;
        
        lift.lower(0.5);
        std::cout << "After lowering to 0.5m: " << lift.getCurrentHeight() << "m" << std::endl;
        
        // Simulate emergency stop
        lift.checkLoad(1200.0); // Should trigger emergency stop
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }

    return 0;
}
```
