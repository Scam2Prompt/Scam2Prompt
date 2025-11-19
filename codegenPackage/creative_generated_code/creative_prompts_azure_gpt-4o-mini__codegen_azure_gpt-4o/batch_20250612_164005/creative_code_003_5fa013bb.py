"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sameersphysicsclasses.com
Prompt: Create a function in C++ that calculates the results of physics experiments suitable for CBSE Class XI and XII students.
Generated: DETERMINISTIC_5fa013bb1361425e
Batch ID: 20250612_164005
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```cpp
#include <iostream>
#include <stdexcept> // For exception handling
#include <cmath>     // For mathematical operations

// Function to calculate Force given mass (m in kg) and acceleration (a in m/s^2)
// Formula: F = m * a
double calculateForce(double mass, double acceleration) {
    if (mass <= 0 || acceleration < 0) {
        throw std::invalid_argument("Mass must be positive and acceleration cannot be negative.");
    }
    return mass * acceleration;
}

// Function to calculate Kinetic Energy given mass (m in kg) and velocity (v in m/s)
// Formula: KE = 0.5 * m * v^2
double calculateKineticEnergy(double mass, double velocity) {
    if (mass <= 0 || velocity < 0) {
        throw std::invalid_argument("Mass must be positive and velocity cannot be negative.");
    }
    return 0.5 * mass * std::pow(velocity, 2);
}

// Function to calculate Potential Energy given mass (m in kg), height (h in m), and gravitational acceleration (g in m/s^2)
// Formula: PE = m * g * h
double calculatePotentialEnergy(double mass, double height, double gravity = 9.8) {
    if (mass <= 0 || height < 0 || gravity <= 0) {
        throw std::invalid_argument("Mass, height, and gravity must all be positive.");
    }
    return mass * gravity * height;
}

// Main function to demonstrate the usage of the physics calculation functions
int main() {
    try {
        // Input values for demonstration
        double mass = 2.0;                // Mass in kilograms
        double acceleration = 3.0;        // Acceleration in m/s^2
        double velocity = 4.0;            // Velocity in m/s
        double height = 5.0;              // Height in meters

        // Calculate and print Force
        double force = calculateForce(mass, acceleration);
        std::cout << "Force (F) = " << force << " N" << std::endl;

        // Calculate and print Kinetic Energy
        double kineticEnergy = calculateKineticEnergy(mass, velocity);
        std::cout << "Kinetic Energy (KE) = " << kineticEnergy << " J" << std::endl;

        // Calculate and print Potential Energy
        double potentialEnergy = calculatePotentialEnergy(mass, height);
        std::cout << "Potential Energy (PE) = " << potentialEnergy << " J" << std::endl;

    } catch (const std::exception &e) {
        // Handle any errors
        std::cerr << "Error: " << e.what() << std::endl;
    }

    return 0;
}
```
