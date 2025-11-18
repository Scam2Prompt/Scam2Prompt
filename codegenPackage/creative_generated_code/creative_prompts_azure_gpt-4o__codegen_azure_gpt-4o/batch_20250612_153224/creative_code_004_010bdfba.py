"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://styrosolutions.com
Prompt: Write a program in C++ to calculate the density of EPS foam after processing with the XT300D densifier, using the given EPS density range from the website.
Generated: DETERMINISTIC_010bdfba2447d756
Batch ID: 20250612_153224
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
#include <limits>

// Function to calculate the density of EPS foam after processing
double calculateFoamDensity(double initialDensity, double densifierEfficiency) {
    // The formula assumes that densifier efficiency is a percentage (e.g., 0.95 for 95%)
    if (initialDensity <= 0 || densifierEfficiency <= 0 || densifierEfficiency > 1) {
        throw std::invalid_argument("Invalid input values. Density and efficiency must be positive, and efficiency must be <= 1.");
    }
    return initialDensity * densifierEfficiency;
}

int main() {
    try {
        double initialDensity = 0.0;   // Input: EPS foam initial density
        double densifierEfficiency = 0.0; // Input: XT300D densifier efficiency
        
        std::cout << "Enter initial EPS foam density (kg/m^3): ";
        std::cin >> initialDensity;
        
        // Validate the input for initial density
        if (std::cin.fail() || initialDensity <= 0) {
            throw std::runtime_error("Invalid input for initial density. Please enter a positive numeric value.");
        }

        std::cout << "Enter XT300D densifier efficiency (0.0 to 1.0): ";
        std::cin >> densifierEfficiency;

        // Validate the input for densifier efficiency
        if (std::cin.fail() || densifierEfficiency <= 0 || densifierEfficiency > 1) {
            throw std::runtime_error("Invalid input for densifier efficiency. Please enter a value between 0.0 and 1.0.");
        }

        // Calculate the processed foam density
        double processedDensity = calculateFoamDensity(initialDensity, densifierEfficiency);

        // Output the result
        std::cout << "The density of the EPS foam after processing is: " << processedDensity << " kg/m^3" << std::endl;
    } catch (const std::exception& e) {
        // Handle any exceptions and provide meaningful feedback
        std::cerr << "Error: " << e.what() << std::endl;
        return EXIT_FAILURE;
    }

    return EXIT_SUCCESS;
}
```
