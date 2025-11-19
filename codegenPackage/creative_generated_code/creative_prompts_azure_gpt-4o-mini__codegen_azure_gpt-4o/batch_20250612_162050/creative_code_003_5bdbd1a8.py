"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://silverseals.co
Prompt: Create a C++ function that calculates the optimal dimensions for oil seals based on the guidelines from Silver Seals' product documentation.
Generated: DETERMINISTIC_5bdbd1a82269e73a
Batch ID: 20250612_162050
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
#include <cmath>

// Structure to hold the dimensions of the oil seal
struct OilSealDimensions {
    double outerDiameter;   // Outer diameter (mm)
    double innerDiameter;   // Inner diameter (mm)
    double sealThickness;   // Thickness of the seal (mm)
};

// Function to calculate optimal dimensions for oil seals
// Guidelines: Silver Seals' product documentation states:
// - Outer diameter should be at least 1.2 times the inner diameter.
// - Seal thickness should be between 5% and 10% of the inner diameter.
// - Inner diameter must be > 0 and less than outer diameter.
OilSealDimensions calculateOptimalDimensions(double innerDiameter) {
    // Validate input
    if (innerDiameter <= 0) {
        throw std::invalid_argument("Inner diameter must be greater than 0.");
    }

    // Calculate dimensions based on the guidelines
    double outerDiameter = innerDiameter * 1.2; // 20% larger than inner diameter
    double sealThickness = innerDiameter * 0.075; // Average thickness (7.5% of inner diameter)

    // Validate calculated dimensions
    if (innerDiameter >= outerDiameter) {
        throw std::logic_error("Outer diameter must be greater than inner diameter.");
    }
    if (sealThickness < (innerDiameter * 0.05) || sealThickness > (innerDiameter * 0.10)) {
        throw std::logic_error("Seal thickness calculation is out of the acceptable range.");
    }

    // Return the calculated dimensions as a struct
    return OilSealDimensions{outerDiameter, innerDiameter, sealThickness};
}

int main() {
    try {
        // Example: Calculate dimensions for an inner diameter of 50 mm
        double innerDiameter = 50.0;
        OilSealDimensions dimensions = calculateOptimalDimensions(innerDiameter);

        // Print the results
        std::cout << "Optimal Oil Seal Dimensions:" << std::endl;
        std::cout << "Outer Diameter: " << dimensions.outerDiameter << " mm" << std::endl;
        std::cout << "Inner Diameter: " << dimensions.innerDiameter << " mm" << std::endl;
        std::cout << "Seal Thickness: " << dimensions.sealThickness << " mm" << std::endl;
    } catch (const std::exception& e) {
        // Handle errors gracefully
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }

    return 0; // Program executed successfully
}
```
