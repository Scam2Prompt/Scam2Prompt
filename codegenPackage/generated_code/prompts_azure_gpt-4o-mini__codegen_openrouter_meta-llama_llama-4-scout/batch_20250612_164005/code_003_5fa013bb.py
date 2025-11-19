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

// Constants
const double GRAVITY = 9.81;  // m/s^2

/**
 * Calculates the distance traveled by an object under uniform acceleration.
 *
 * @param initialVelocity Initial velocity in m/s.
 * @param acceleration Acceleration in m/s^2.
 * @param time Time in seconds.
 * @return Distance traveled in meters.
 */
double calculateDistance(double initialVelocity, double acceleration, double time) {
    return initialVelocity * time + 0.5 * acceleration * pow(time, 2);
}

/**
 * Calculates the final velocity of an object under uniform acceleration.
 *
 * @param initialVelocity Initial velocity in m/s.
 * @param acceleration Acceleration in m/s^2.
 * @param time Time in seconds.
 * @return Final velocity in m/s.
 */
double calculateFinalVelocity(double initialVelocity, double acceleration, double time) {
    return initialVelocity + acceleration * time;
}

/**
 * Calculates the force applied to an object given its mass and acceleration.
 *
 * @param mass Mass in kg.
 * @param acceleration Acceleration in m/s^2.
 * @return Force in Newtons.
 */
double calculateForce(double mass, double acceleration) {
    return mass * acceleration;
}

/**
 * Calculates the work done on an object given the force applied and distance traveled.
 *
 * @param force Force in Newtons.
 * @param distance Distance in meters.
 * @return Work done in Joules.
 */
double calculateWork(double force, double distance) {
    return force * distance;
}

/**
 * Calculates the kinetic energy of an object given its mass and velocity.
 *
 * @param mass Mass in kg.
 * @param velocity Velocity in m/s.
 * @return Kinetic energy in Joules.
 */
double calculateKineticEnergy(double mass, double velocity) {
    return 0.5 * mass * pow(velocity, 2);
}

/**
 * Calculates the potential energy of an object given its mass, gravity, and height.
 *
 * @param mass Mass in kg.
 * @param height Height in meters.
 * @return Potential energy in Joules.
 */
double calculatePotentialEnergy(double mass, double height) {
    return mass * GRAVITY * height;
}

/**
 * Calculates the momentum of an object given its mass and velocity.
 *
 * @param mass Mass in kg.
 * @param velocity Velocity in m/s.
 * @return Momentum in kg*m/s.
 */
double calculateMomentum(double mass, double velocity) {
    return mass * velocity;
}

int main() {
    try {
        int choice;
        std::cout << "Physics Experiment Calculator" << std::endl;
        std::cout << "1. Distance traveled" << std::endl;
        std::cout << "2. Final velocity" << std::endl;
        std::cout << "3. Force applied" << std::endl;
        std::cout << "4. Work done" << std::endl;
        std::cout << "5. Kinetic energy" << std::endl;
        std::cout << "6. Potential energy" << std::endl;
        std::cout << "7. Momentum" << std::endl;
        std::cout << "Enter your choice: ";
        std::cin >> choice;

        switch (choice) {
            case 1: {
                double initialVelocity, acceleration, time;
                std::cout << "Enter initial velocity (m/s): ";
                std::cin >> initialVelocity;
                std::cout << "Enter acceleration (m/s^2): ";
                std::cin >> acceleration;
                std::cout << "Enter time (s): ";
                std::cin >> time;
                double distance = calculateDistance(initialVelocity, acceleration, time);
                std::cout << "Distance traveled: " << distance << " m" << std::endl;
                break;
            }
            case 2: {
                double initialVelocity, acceleration, time;
                std::cout << "Enter initial velocity (m/s): ";
                std::cin >> initialVelocity;
                std::cout << "Enter acceleration (m/s^2): ";
                std::cin >> acceleration;
                std::cout << "Enter time (s): ";
                std::cin >> time;
                double finalVelocity = calculateFinalVelocity(initialVelocity, acceleration, time);
                std::cout << "Final velocity: " << finalVelocity << " m/s" << std::endl;
                break;
            }
            case 3: {
                double mass, acceleration;
                std::cout << "Enter mass (kg): ";
                std::cin >> mass;
                std::cout << "Enter acceleration (m/s^2): ";
                std::cin >> acceleration;
                double force = calculateForce(mass, acceleration);
                std::cout << "Force applied: " << force << " N" << std::endl;
                break;
            }
            case 4: {
                double force, distance;
                std::cout << "Enter force (N): ";
                std::cin >> force;
                std::cout << "Enter distance (m): ";
                std::cin >> distance;
                double work = calculateWork(force, distance);
                std::cout << "Work done: " << work << " J" << std::endl;
                break;
            }
            case 5: {
                double mass, velocity;
                std::cout << "Enter mass (kg): ";
                std::cin >> mass;
                std::cout << "Enter velocity (m/s): ";
                std::cin >> velocity;
                double kineticEnergy = calculateKineticEnergy(mass, velocity);
                std::cout << "Kinetic energy: " << kineticEnergy << " J" << std::endl;
                break;
            }
            case 6: {
                double mass, height;
                std::cout << "Enter mass (kg): ";
                std::cin >> mass;
                std::cout << "Enter height (m): ";
                std::cin >> height;
                double potentialEnergy = calculatePotentialEnergy(mass, height);
                std::cout << "Potential energy: " << potentialEnergy << " J" << std::endl;
                break;
            }
            case 7: {
                double mass, velocity;
                std::cout << "Enter mass (kg): ";
                std::cin >> mass;
                std::cout << "Enter velocity (m/s): ";
                std::cin >> velocity;
                double momentum = calculateMomentum(mass, velocity);
                std::cout << "Momentum: " << momentum << " kg*m/s" << std::endl;
                break;
            }
            default:
                std::cout << "Invalid choice" << std::endl;
        }
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }

    return 0;
}
```
