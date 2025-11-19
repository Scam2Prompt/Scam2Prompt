"""
Generated Code Metadata:
========================
Original URL: https://taxltg.com
Prompt: Write a code snippet in C++ to simulate the movement of a KPT拖揽供电平车 in a factory setting.
Generated: DETERMINISTIC_dce349e3a6e6c279
Batch ID: 20250622_212746
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```cpp
#include <iostream>
#include <thread>
#include <chrono>
#include <mutex>
#include <random>
#include <stdexcept>

/**
 * Simulates a KPT拖揽供电平车 (KPT power supply flat car) in a factory setting.
 */
class KPTPowerSupplyFlatCar {
private:
    std::string id;
    double positionX;
    double positionY;
    double speed;
    bool isPowered;
    std::mutex mtx;

    // Random number generator for simulating variations
    std::default_random_engine generator;
    std::uniform_real_distribution<double> speedVariation{-0.5, 0.5};

public:
    /**
     * Constructor for KPTPowerSupplyFlatCar
     * @param carId Unique identifier for the car
     * @param initialX Initial X position
     * @param initialY Initial Y position
     */
    KPTPowerSupplyFlatCar(const std::string& carId, double initialX = 0.0, double initialY = 0.0)
        : id(carId), positionX(initialX), positionY(initialY), speed(0.0), isPowered(false) {
        if (carId.empty()) {
            throw std::invalid_argument("Car ID cannot be empty");
        }
    }

    /**
     * Powers on the car's electrical system
     */
    void powerOn() {
        std::lock_guard<std::mutex> lock(mtx);
        isPowered = true;
        std::cout << "Car " << id << ": Power turned on\n";
    }

    /**
     * Powers off the car's electrical system
     */
    void powerOff() {
        std::lock_guard<std::mutex> lock(mtx);
        isPowered = false;
        speed = 0.0;
        std::cout << "Car " << id << ": Power turned off\n";
    }

    /**
     * Sets the speed of the car
     * @param newSpeed Desired speed in m/s
     */
    void setSpeed(double newSpeed) {
        std::lock_guard<std::mutex> lock(mtx);
        if (!isPowered) {
            throw std::runtime_error("Cannot set speed when power is off");
        }
        speed = newSpeed;
        std::cout << "Car " << id << ": Speed set to " << speed << " m/s\n";
    }

    /**
     * Updates the car's position based on current speed
     * @param deltaTime Time elapsed since last update in seconds
     */
    void updatePosition(double deltaTime) {
        std::lock_guard<std::mutex> lock(mtx);
        if (isPowered && speed > 0) {
            // Add small random variation to simulate real-world conditions
            double effectiveSpeed = speed + speedVariation(generator);
            positionX += effectiveSpeed * deltaTime;
            std::cout << "Car " << id << ": Moved to (" << positionX << ", " << positionY << ")\n";
        }
    }

    /**
     * Gets current position
     * @return Pair of X,Y coordinates
     */
    std::pair<double, double> getPosition() const {
        std::lock_guard<std::mutex> lock(mtx);
        return {positionX, positionY};
    }

    /**
     * Gets current status
     * @return String with current status information
     */
    std::string getStatus() const {
        std::lock_guard<std::mutex> lock(mtx);
        return "Car " + id + ": Position (" + std::to_string(positionX) + ", " + 
               std::to_string(positionY) + "), Speed: " + std::to_string(speed) + 
               " m/s, Power: " + (isPowered ? "ON" : "OFF");
    }
};

/**
 * Simulates factory operation with the flat car
 */
void simulateFactoryOperation() {
    try {
        KPTPowerSupplyFlatCar car("KPT-001");

        car.powerOn();
        car.setSpeed(1.5); // 1.5 m/s

        // Simulate 10 seconds of operation
        for (int i = 0; i < 10; ++i) {
            car.updatePosition(1.0); // Update every second
            std::this_thread::sleep_for(std::chrono::seconds(1));
        }

        car.powerOff();
        std::cout << car.getStatus() << std::endl;
    } catch (const std::exception& e) {
        std::cerr << "Error in factory simulation: " << e.what() << std::endl;
    }
}

int main() {
    simulateFactoryOperation();
    return 0;
}
```
