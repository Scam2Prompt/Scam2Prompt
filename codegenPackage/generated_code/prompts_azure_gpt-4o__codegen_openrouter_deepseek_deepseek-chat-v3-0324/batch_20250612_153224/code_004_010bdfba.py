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

/**
 * @brief Calculates the density of EPS foam after processing with the XT300D densifier.
 * 
 * This program takes the initial density of EPS foam and calculates the final density
 * after processing with the XT300D densifier, which has a known compression ratio.
 */
class EPSDensifierCalculator {
public:
    /**
     * @brief Construct a new EPSDensifierCalculator object with default compression ratio.
     */
    EPSDensifierCalculator() : compression_ratio_(30.0) {}

    /**
     * @brief Set the compression ratio of the densifier.
     * @param ratio The compression ratio (must be positive).
     * @throws std::invalid_argument if ratio is not positive.
     */
    void setCompressionRatio(double ratio) {
        if (ratio <= 0) {
            throw std::invalid_argument("Compression ratio must be positive.");
        }
        compression_ratio_ = ratio;
    }

    /**
     * @brief Calculate the final density after processing.
     * @param initial_density The initial density of EPS foam (kg/m³).
     * @return double The final density after processing.
     * @throws std::invalid_argument if initial_density is not positive.
     */
    double calculateFinalDensity(double initial_density) const {
        if (initial_density <= 0) {
            throw std::invalid_argument("Initial density must be positive.");
        }
        return initial_density * compression_ratio_;
    }

private:
    double compression_ratio_;
};

/**
 * @brief Get valid double input from the user.
 * @param prompt The prompt to display to the user.
 * @return double The valid input value.
 */
double getValidDoubleInput(const std::string& prompt) {
    double value;
    while (true) {
        std::cout << prompt;
        if (std::cin >> value) {
            if (value > 0) {
                break;
            } else {
                std::cout << "Value must be positive. Please try again.\n";
            }
        } else {
            std::cout << "Invalid input. Please enter a numeric value.\n";
            std::cin.clear();
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        }
    }
    return value;
}

int main() {
    try {
        EPSDensifierCalculator calculator;

        std::cout << "EPS Foam Density Calculator for XT300D Densifier\n";
        std::cout << "------------------------------------------------\n";

        double initial_density = getValidDoubleInput(
            "Enter the initial density of EPS foam (kg/m³): ");
        
        double final_density = calculator.calculateFinalDensity(initial_density);

        std::cout << "Final density after processing: " << final_density 
                  << " kg/m³\n";
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }

    return 0;
}
```
