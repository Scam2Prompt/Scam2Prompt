"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elfworldvape.com
Prompt: Write a program in C++ to simulate the smart heating system used in Elfworld vape devices, optimizing for healthier vaping and natural-based taste.
Generated: DETERMINISTIC_db121f6938aeac75
Batch ID: 20250612_154400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```cpp
#include <iostream>
#include <stdexcept>
#include <vector>
#include <cmath>

// Class representing the Smart Heating System
class SmartHeatingSystem {
private:
    float targetTemperature; // Target temperature for vaping
    float currentTemperature; // Current temperature of the coil
    float heatingRate;        // Rate at which the system heats the coil
    float coolingRate;        // Rate at which the system cools down the coil
    bool systemActive;        // Indicates whether the system is active or not

public:
    // Constructor to initialize the heating system
    SmartHeatingSystem(float targetTemp, float heatingRate, float coolingRate)
        : targetTemperature(targetTemp), currentTemperature(25.0f), heatingRate(heatingRate), coolingRate(coolingRate), systemActive(false) {
        if (targetTemp <= 0 || heatingRate <= 0 || coolingRate <= 0) {
            throw std::invalid_argument("Invalid parameters for heating system initialization.");
        }
    }

    // Activate the heating system
    void activate() {
        systemActive = true;
        std::cout << "Smart Heating System activated.\n";
    }

    // Deactivate the heating system
    void deactivate() {
        systemActive = false;
        std::cout << "Smart Heating System deactivated.\n";
    }

    // Method to optimize temperature for healthier vaping
    void optimizeTemperature() {
        if (!systemActive) {
            throw std::runtime_error("Heating system is not active.");
        }

        // Adjust temperature to reach target temperature
        while (std::abs(targetTemperature - currentTemperature) > 0.1f) {
            if (currentTemperature < targetTemperature) {
                currentTemperature += heatingRate;
            } else if (currentTemperature > targetTemperature) {
                currentTemperature -= coolingRate;
            }
            std::cout << "Current Temperature: " << currentTemperature << "°C\n";
        }

        std::cout << "Target Temperature of " << targetTemperature << "°C reached.\n";
    }

    // Method for natural-based taste optimization
    void enhanceNaturalTaste() {
        if (!systemActive) {
            throw std::runtime_error("Heating system is not active.");
        }

        std::cout << "Enhancing natural-based taste using adaptive heating profiles...\n";
        // Simulate flavor adjustment logic
        std::cout << "Natural-based taste optimized at " << currentTemperature << "°C.\n";
    }

    // Get the current system status
    bool isActive() const {
        return systemActive;
    }

    // Get the current temperature
    float getCurrentTemperature() const {
        return currentTemperature;
    }

    // Get the target temperature
    float getTargetTemperature() const {
        return targetTemperature;
    }
};

int main() {
    try {
        // Initialize the Smart Heating System
        SmartHeatingSystem heatingSystem(200.0f, 5.0f, 3.0f);

        // Activate the system
        heatingSystem.activate();

        // Optimize temperature for healthier vaping
        heatingSystem.optimizeTemperature();

        // Enhance natural-based taste
        heatingSystem.enhanceNaturalTaste();

        // Deactivate the system
        heatingSystem.deactivate();

    } catch (const std::exception &e) {
        // Handle any errors during operation
        std::cerr << "Error: " << e.what() << "\n";
        return EXIT_FAILURE;
    }

    // Exit successfully
    return EXIT_SUCCESS;
}
```
