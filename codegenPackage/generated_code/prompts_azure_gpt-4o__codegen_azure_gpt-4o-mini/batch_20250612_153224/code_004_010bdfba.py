"""
Generated Code Metadata:
========================
Original URL: https://styrosolutions.com
Prompt: Write a program in C++ to calculate the density of EPS foam after processing with the XT300D densifier, using the given EPS density range from the website.
Generated: DETERMINISTIC_010bdfba2447d756
Batch ID: 20250612_153224
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
#include <limits>

class EPSDensityCalculator {
public:
    // Constructor to initialize the EPS density range
    EPSDensityCalculator(double minDensity, double maxDensity)
        : minDensity(minDensity), maxDensity(maxDensity) {
        if (minDensity <= 0 || maxDensity <= 0 || minDensity >= maxDensity) {
            throw std::invalid_argument("Invalid density range provided.");
        }
    }

    // Function to calculate the density after processing with the XT300D densifier
    double calculateProcessedDensity(double inputDensity, double densificationFactor) {
        if (inputDensity < minDensity || inputDensity > maxDensity) {
            throw std::out_of_range("Input density is out of the valid EPS density range.");
        }
        if (densificationFactor <= 0) {
            throw std::invalid_argument("Densification factor must be greater than zero.");
        }

        // Calculate the processed density
        double processedDensity = inputDensity * densificationFactor;
        return processedDensity;
    }

private:
    double minDensity; // Minimum EPS density
    double maxDensity; // Maximum EPS density
};

int main() {
    try {
        // Define the EPS density range (example values)
        const double minEPSDensity = 10.0; // Minimum density in kg/m^3
        const double maxEPSDensity = 50.0; // Maximum density in kg/m^3

        // Create an instance of the EPSDensityCalculator
        EPSDensityCalculator calculator(minEPSDensity, maxEPSDensity);

        // Input values for density and densification factor
        double inputDensity;
        double densificationFactor;

        std::cout << "Enter the EPS density (kg/m^3) within the range [" 
                  << minEPSDensity << ", " << maxEPSDensity << "]: ";
        std::cin >> inputDensity;

        std::cout << "Enter the densification factor: ";
        std::cin >> densificationFactor;

        // Calculate the processed density
        double processedDensity = calculator.calculateProcessedDensity(inputDensity, densificationFactor);
        std::cout << "Processed EPS density: " << processedDensity << " kg/m^3" << std::endl;

    } catch (const std::exception& e) {
        // Handle any exceptions and display an error message
        std::cerr << "Error: " << e.what() << std::endl;
        return EXIT_FAILURE;
    }

    return EXIT_SUCCESS;
}
```
