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
#include <vector>
#include <cmath>
#include <stdexcept>
#include <limits>

/**
 * @brief Calculates the result of a simple pendulum experiment.
 * 
 * @param length Length of the pendulum in meters.
 * @param timePeriod Time period of oscillation in seconds.
 * @param gravity Acceleration due to gravity (default is 9.8 m/s^2).
 * @return double Calculated value of 'g' from the experiment.
 * @throws std::invalid_argument If length or timePeriod is non-positive.
 */
double simplePendulum(double length, double timePeriod, double gravity = 9.8) {
    if (length <= 0 || timePeriod <= 0) {
        throw std::invalid_argument("Length and time period must be positive.");
    }
    return (4 * M_PI * M_PI * length) / (timePeriod * timePeriod);
}

/**
 * @brief Calculates the resistivity of a wire using Ohm's Law.
 * 
 * @param resistance Resistance in ohms.
 * @param length Length of the wire in meters.
 * @param crossSectionArea Cross-sectional area in m^2.
 * @return double Resistivity in ohm-meter.
 * @throws std::invalid_argument If any parameter is non-positive.
 */
double resistivity(double resistance, double length, double crossSectionArea) {
    if (resistance <= 0 || length <= 0 || crossSectionArea <= 0) {
        throw std::invalid_argument("Resistance, length, and area must be positive.");
    }
    return (resistance * crossSectionArea) / length;
}

/**
 * @brief Calculates the focal length of a lens using the lens formula.
 * 
 * @param objectDistance Distance of the object from the lens in meters.
 * @param imageDistance Distance of the image from the lens in meters.
 * @return double Focal length in meters.
 * @throws std::invalid_argument If objectDistance or imageDistance is invalid.
 */
double lensFormula(double objectDistance, double imageDistance) {
    if (objectDistance <= 0 || imageDistance <= 0) {
        throw std::invalid_argument("Object and image distances must be positive.");
    }
    return (objectDistance * imageDistance) / (objectDistance + imageDistance);
}

/**
 * @brief Calculates the refractive index using Snell's Law.
 * 
 * @param angleOfIncidence Angle of incidence in degrees.
 * @param angleOfRefraction Angle of refraction in degrees.
 * @return double Refractive index.
 * @throws std::invalid_argument If angles are out of valid range.
 */
double snellsLaw(double angleOfIncidence, double angleOfRefraction) {
    if (angleOfIncidence <= 0 || angleOfIncidence >= 90 || 
        angleOfRefraction <= 0 || angleOfRefraction >= 90) {
        throw std::invalid_argument("Angles must be between 0 and 90 degrees.");
    }
    double sinI = sin(angleOfIncidence * M_PI / 180.0);
    double sinR = sin(angleOfRefraction * M_PI / 180.0);
    return sinI / sinR;
}

/**
 * @brief Main function to demonstrate physics experiment calculations.
 */
int main() {
    try {
        // Example 1: Simple Pendulum
        double g = simplePendulum(1.0, 2.0);
        std::cout << "Calculated 'g' from pendulum: " << g << " m/s^2" << std::endl;

        // Example 2: Resistivity
        double rho = resistivity(5.0, 2.0, 1e-6);
        std::cout << "Resistivity of wire: " << rho << " ohm-meter" << std::endl;

        // Example 3: Lens Formula
        double focalLength = lensFormula(0.3, 0.6);
        std::cout << "Focal length of lens: " << focalLength << " meters" << std::endl;

        // Example 4: Snell's Law
        double refractiveIndex = snellsLaw(45, 30);
        std::cout << "Refractive index: " << refractiveIndex << std::endl;

    } catch (const std::invalid_argument& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }

    return 0;
}
```
