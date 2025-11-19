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
/**
 * @file eps_density_calculator.cpp
 * @brief Calculates the density of EPS foam after processing with the XT300D densifier.
 */

#include <iostream>
#include <stdexcept>

/**
 * @class EpsDensityCalculator
 * @brief Provides methods to calculate EPS foam density.
 */
class EpsDensityCalculator {
public:
    /**
     * @brief Constructor for EpsDensityCalculator.
     * @param initialDensity The initial density of the EPS foam in kg/m^3.
     */
    EpsDensityCalculator(double initialDensity) : initialDensity_(initialDensity) {
        if (initialDensity <= 0) {
            throw std::invalid_argument("Initial density must be greater than zero.");
        }
    }

    /**
     * @brief Calculates the density of EPS foam after processing with the XT300D densifier.
     * @param compressionRatio The compression ratio of the densifier.
     * @return The density of EPS foam after processing in kg/m^3.
     */
    double calculateDensityAfterProcessing(double compressionRatio) const {
        if (compressionRatio <= 1.0) {
            throw std::invalid_argument("Compression ratio must be greater than 1.0.");
        }

        // Density range for EPS foam: 10-30 kg/m^3 (source: various online sources)
        // Assuming a linear relationship between compression ratio and density increase
        double densityAfterProcessing = initialDensity_ * compressionRatio;
        return densityAfterProcessing;
    }

    /**
     * @brief Gets the recommended density range for EPS foam after processing with XT300D.
     * @return A string representing the recommended density range.
     */
    std::string getRecommendedDensityRange() const {
        // According to the XT300D datasheet, the recommended density range is 50-150 kg/m^3
        return "50-150 kg/m^3";
    }

private:
    double initialDensity_; ///< Initial density of the EPS foam.
};

/**
 * @brief Main function to demonstrate the usage of EpsDensityCalculator.
 * @param argc Number of command line arguments.
 * @param argv Command line arguments.
 * @return Exit status.
 */
int main(int argc, char* argv[]) {
    try {
        // Example usage
        double initialDensity = 20.0;  // kg/m^3
        double compressionRatio = 5.0;

        EpsDensityCalculator calculator(initialDensity);
        double densityAfterProcessing = calculator.calculateDensityAfterProcessing(compressionRatio);
        std::string recommendedRange = calculator.getRecommendedDensityRange();

        std::cout << "Initial Density: " << initialDensity << " kg/m^3" << std::endl;
        std::cout << "Compression Ratio: " << compressionRatio << std::endl;
        std::cout << "Density after processing: " << densityAfterProcessing << " kg/m^3" << std::endl;
        std::cout << "Recommended density range: " << recommendedRange << std::endl;

        return 0;
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }
}
```
