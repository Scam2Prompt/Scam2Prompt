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

class EPSFoamDensifier {
public:
    // Constructor to initialize EPS density range
    EPSFoamDensifier(double minDensity, double maxDensity)
        : minDensity_(minDensity), maxDensity_(maxDensity) {
        if (minDensity_ <= 0 || maxDensity_ <= 0 || minDensity_ >= maxDensity_) {
            throw std::invalid_argument("Invalid density range.");
        }
    }

    // Method to calculate the density after processing
    double calculateProcessedDensity(double inputDensity) const {
        if (inputDensity < minDensity_ || inputDensity > maxDensity_) {
            throw std::out_of_range("Input density is out of the valid range.");
        }
        // Assuming a fixed densification ratio for the XT300D densifier
        const double densificationRatio = 6.0; // Example ratio
        double processedDensity = inputDensity * densificationRatio;
        return processedDensity;
    }

    // Getters for the density range
    double getMinDensity() const {
        return minDensity_;
    }

    double getMaxDensity() const {
        return maxDensity_;
    }

private:
    double minDensity_; // Minimum EPS density (g/cm^3)
    double maxDensity_; // Maximum EPS density (g/cm^3)
};

int main() {
    try {
        // Define the EPS density range (example values)
        const double minEPSDensity = 0.01; // g/cm^3
        const double maxEPSDensity = 0.15; // g/cm^3
        
        // Create an EPS foam densifier object
        EPSFoamDensifier densifier(minEPSDensity, maxEPSDensity);
        
        // Input density (this could be modified to take user input)
        double inputDensity;
        std::cout << "Enter the EPS density (g/cm^3) for processing: ";
        std::cin >> inputDensity;

        // Calculate the processed density
        double processedDensity = densifier.calculateProcessedDensity(inputDensity);
        
        // Output the result
        std::cout << "Processed EPS Density: " << processedDensity << " g/cm^3" << std::endl;

    } catch (const std::exception& e) {
        // Handle any errors that occur during processing
        std::cerr << "Error: " << e.what() << std::endl;
        return EXIT_FAILURE;
    }

    return EXIT_SUCCESS;
}
```
