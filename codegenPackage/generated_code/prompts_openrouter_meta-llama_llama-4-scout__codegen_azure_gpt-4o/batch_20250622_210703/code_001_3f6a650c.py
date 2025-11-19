"""
Generated Code Metadata:
========================
Original URL: https://www.ablakvaros.hu
Prompt: "Recommend a suitable Rehau window model for a passive house, taking into account the requirements for energy efficiency and insulation, and provide a code snippet in C++ to calculate the energy savings."
Generated: DETERMINISTIC_3f6a650cf3c3e827
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```cpp
#include <iostream>
#include <string>
#include <stdexcept>

// Function to recommend a Rehau window model based on passive house requirements
std::string recommendWindowModel(double uValue, double insulationRating) {
    // Passive house requirements: U-value <= 0.8 W/m²K and high insulation rating
    if (uValue <= 0.8 && insulationRating >= 9.0) {
        return "Rehau Geneo PHZ (Passive House Certified)";
    } else if (uValue <= 0.8) {
        return "Rehau Synego";
    } else {
        return "Rehau Euro-Design 70 (Consider upgrading insulation)";
    }
}

// Function to calculate energy savings based on window U-value and area
double calculateEnergySavings(double uValueOld, double uValueNew, double area, double heatingCostPerKWh, double hoursPerYear) {
    if (uValueOld <= 0 || uValueNew <= 0 || area <= 0 || heatingCostPerKWh <= 0 || hoursPerYear <= 0) {
        throw std::invalid_argument("All input values must be positive.");
    }

    // Energy savings formula: ΔU * Area * Hours * Heating Cost
    double deltaU = uValueOld - uValueNew;
    double energySavings = deltaU * area * hoursPerYear * heatingCostPerKWh;

    return energySavings;
}

int main() {
    try {
        // Example inputs
        double uValueOld = 1.4; // U-value of old windows (W/m²K)
        double uValueNew = 0.8; // U-value of new windows (W/m²K)
        double area = 20.0;     // Total window area (m²)
        double heatingCostPerKWh = 0.12; // Heating cost per kWh ($)
        double hoursPerYear = 2000;      // Heating hours per year

        // Recommend a window model
        double insulationRating = 9.5; // Example insulation rating
        std::string recommendedModel = recommendWindowModel(uValueNew, insulationRating);
        std::cout << "Recommended Rehau Window Model: " << recommendedModel << std::endl;

        // Calculate energy savings
        double energySavings = calculateEnergySavings(uValueOld, uValueNew, area, heatingCostPerKWh, hoursPerYear);
        std::cout << "Estimated Annual Energy Savings: $" << energySavings << std::endl;
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1; // Return non-zero exit code for error
    }

    return 0; // Successful execution
}
```
