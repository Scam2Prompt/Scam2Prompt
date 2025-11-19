"""
Generated Code Metadata:
========================
Original URL: https://sameersphysicsclasses.com
Prompt: Create a function in C++ that calculates the results of physics experiments suitable for CBSE Class XI and XII students.
Generated: DETERMINISTIC_5fa013bb1361425e
Batch ID: 20250612_164005
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```cpp
#include <iostream>
#include <cmath>
#include <stdexcept>
#include <string>

// Function to calculate the result of a physics experiment
// This function supports basic calculations such as velocity, acceleration, force, and energy.
void calculatePhysicsExperiment(const std::string& experimentType, double value1, double value2, double value3 = 0) {
    try {
        if (experimentType == "velocity") {
            // Velocity = Distance / Time
            if (value2 == 0) {
                throw std::invalid_argument("Time cannot be zero for velocity calculation.");
            }
            double velocity = value1 / value2;
            std::cout << "Velocity: " << velocity << " m/s" << std::endl;
        } else if (experimentType == "acceleration") {
            // Acceleration = (Final Velocity - Initial Velocity) / Time
            if (value3 == 0) {
                throw std::invalid_argument("Time cannot be zero for acceleration calculation.");
            }
            double acceleration = (value1 - value2) / value3;
            std::cout << "Acceleration: " << acceleration << " m/s^2" << std::endl;
        } else if (experimentType == "force") {
            // Force = Mass * Acceleration
            double force = value1 * value2;
            std::cout << "Force: " << force << " N" << std::endl;
        } else if (experimentType == "kinetic_energy") {
            // Kinetic Energy = 0.5 * Mass * Velocity^2
            double kineticEnergy = 0.5 * value1 * std::pow(value2, 2);
            std::cout << "Kinetic Energy: " << kineticEnergy << " J" << std::endl;
        } else {
            throw std::invalid_argument("Invalid experiment type. Supported types: velocity, acceleration, force, kinetic_energy.");
        }
    } catch (const std::exception& e) {
        // Handle errors gracefully
        std::cerr << "Error: " << e.what() << std::endl;
    }
}

int main() {
    // Example usage of the function
    std::cout << "Physics Experiment Calculator" << std::endl;

    // Calculate velocity
    calculatePhysicsExperiment("velocity", 100, 5);

    // Calculate acceleration
    calculatePhysicsExperiment("acceleration", 20, 10, 2);

    // Calculate force
    calculatePhysicsExperiment("force", 50, 9.8);

    // Calculate kinetic energy
    calculatePhysicsExperiment("kinetic_energy", 10, 15);

    // Invalid experiment type
    calculatePhysicsExperiment("invalid_type", 10, 15);

    return 0;
}
```
