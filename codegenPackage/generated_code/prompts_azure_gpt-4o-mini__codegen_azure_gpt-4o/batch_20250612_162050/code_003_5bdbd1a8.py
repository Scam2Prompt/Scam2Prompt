"""
Generated Code Metadata:
========================
Original URL: https://silverseals.co
Prompt: Create a C++ function that calculates the optimal dimensions for oil seals based on the guidelines from Silver Seals' product documentation.
Generated: DETERMINISTIC_5bdbd1a82269e73a
Batch ID: 20250612_162050
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
#include <cmath>
#include <tuple>

// Function to calculate the optimal dimensions for oil seals
// Based on Silver Seals' product documentation guidelines
// Parameters:
//   shaftDiameter: Diameter of the shaft (in mm)
//   boreDiameter: Diameter of the bore (in mm)
//   sealWidth: Desired width of the seal (in mm)
// Returns:
//   A tuple containing the inner diameter, outer diameter, and width of the oil seal
std::tuple<double, double, double> calculateOptimalSealDimensions(double shaftDiameter, double boreDiameter, double sealWidth) {
    // Validate input parameters
    if (shaftDiameter <= 0 || boreDiameter <= 0 || sealWidth <= 0) {
        throw std::invalid_argument("All input dimensions must be positive values.");
    }
    if (shaftDiameter >= boreDiameter) {
        throw std::invalid_argument("Shaft diameter must be smaller than bore diameter.");
    }

    // Constants based on Silver Seals' guidelines
    const double clearance = 0.25; // Clearance between shaft and seal inner diameter (in mm)
    const double interference = 0.5; // Interference fit for outer diameter (in mm)

    // Calculate optimal dimensions
    double innerDiameter = shaftDiameter + clearance; // Inner diameter of the seal
    double outerDiameter = boreDiameter - interference; // Outer diameter of the seal
    double width = sealWidth; // Width remains as specified

    // Ensure calculated dimensions are valid
    if (innerDiameter >= outerDiameter) {
        throw std::runtime_error("Calculated dimensions are invalid: inner diameter is greater than or equal to outer diameter.");
    }

    // Return the calculated dimensions as a tuple
    return std::make_tuple(innerDiameter, outerDiameter, width);
}

int main() {
    try {
        // Example usage of the function
        double shaftDiameter = 50.0; // Example shaft diameter in mm
        double boreDiameter = 70.0; // Example bore diameter in mm
        double sealWidth = 10.0; // Example seal width in mm

        // Calculate optimal dimensions
        auto [innerDiameter, outerDiameter, width] = calculateOptimalSealDimensions(shaftDiameter, boreDiameter, sealWidth);

        // Output the results
        std::cout << "Optimal Oil Seal Dimensions:" << std::endl;
        std::cout << "Inner Diameter: " << innerDiameter << " mm" << std::endl;
        std::cout << "Outer Diameter: " << outerDiameter << " mm" << std::endl;
        std::cout << "Width: " << width << " mm" << std::endl;
    } catch (const std::exception& e) {
        // Handle errors gracefully
        std::cerr << "Error: " << e.what() << std::endl;
        return 1; // Return non-zero exit code to indicate failure
    }

    return 0; // Return zero exit code to indicate success
}
```
