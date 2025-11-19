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
#include <cmath>
#include <stdexcept>

// PhysicsExperiment class to encapsulate methods for various physics calculations
class PhysicsExperiment {
public:
    // Function to calculate the speed of an object
    // speed = distance / time
    static double calculateSpeed(double distance, double time) {
        if (time <= 0) {
            throw std::invalid_argument("Time must be greater than zero.");
        }
        return distance / time;
    }

    // Function to calculate the force applied on an object
    // force = mass * acceleration
    static double calculateForce(double mass, double acceleration) {
        if (mass < 0 || acceleration < 0) {
            throw std::invalid_argument("Mass and acceleration must be non-negative.");
        }
        return mass * acceleration;
    }

    // Function to calculate work done
    // work = force * distance
    static double calculateWork(double force, double distance) {
        if (force < 0 || distance < 0) {
            throw std::invalid_argument("Force and distance must be non-negative.");
        }
        return force * distance;
    }

    // Function to calculate potential energy
    // potentialEnergy = mass * gravity * height
    static double calculatePotentialEnergy(double mass, double height, double gravity = 9.81) {
        if (mass < 0 || height < 0) {
            throw std::invalid_argument("Mass and height must be non-negative.");
        }
        return mass * gravity * height;
    }

    // Function to calculate kinetic energy
    // kineticEnergy = 0.5 * mass * velocity^2
    static double calculateKineticEnergy(double mass, double velocity) {
        if (mass < 0 || velocity < 0) {
            throw std::invalid_argument("Mass and velocity must be non-negative.");
        }
        return 0.5 * mass * std::pow(velocity, 2);
    }
};

// Main function to demonstrate the use of the PhysicsExperiment class
int main() {
    try {
        // Example calculations
        double speed = PhysicsExperiment::calculateSpeed(100.0, 2.0);
        std::cout << "Speed: " << speed << " m/s" << std::endl;

        double force = PhysicsExperiment::calculateForce(10.0, 9.8);
        std::cout << "Force: " << force << " N" << std::endl;

        double work = PhysicsExperiment::calculateWork(force, 5.0);
        std::cout << "Work: " << work << " J" << std::endl;

        double potentialEnergy = PhysicsExperiment::calculatePotentialEnergy(5.0, 10.0);
        std::cout << "Potential Energy: " << potentialEnergy << " J" << std::endl;

        double kineticEnergy = PhysicsExperiment::calculateKineticEnergy(5.0, 20.0);
        std::cout << "Kinetic Energy: " << kineticEnergy << " J" << std::endl;

    } catch (const std::invalid_argument &e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return EXIT_FAILURE;
    }

    return EXIT_SUCCESS;
}
```
