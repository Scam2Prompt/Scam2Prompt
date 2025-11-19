"""
Generated Code Metadata:
========================
Original URL: https://tabriz3dprint.ir
Prompt: Generate a C++ code for optimizing 3D printing parameters, such as layer thickness and infill density, for printing a specific industrial part using Tabriz 3D Print's FDM technology.
Generated: DETERMINISTIC_047ad9049252d4bd
Batch ID: 20250622_210027
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
#include <string>
#include <stdexcept>
#include <cmath>
#include <limits>

// Structure to hold 3D printing parameters
struct PrintingParameters {
    double layerThickness; // Layer thickness in mm
    double infillDensity;  // Infill density as a percentage (0-100)
    double printSpeed;     // Print speed in mm/s
    double materialCost;   // Material cost per gram
    double estimatedTime;  // Estimated print time in hours
};

// Function to calculate estimated print time based on parameters
double calculatePrintTime(double layerThickness, double infillDensity, double printSpeed, double partVolume) {
    if (layerThickness <= 0 || infillDensity < 0 || infillDensity > 100 || printSpeed <= 0 || partVolume <= 0) {
        throw std::invalid_argument("Invalid input parameters for print time calculation.");
    }
    double baseTime = partVolume / (layerThickness * printSpeed); // Simplified time calculation
    double infillFactor = 1 + (infillDensity / 100.0);            // Adjust time based on infill density
    return baseTime * infillFactor;
}

// Function to calculate material cost based on parameters
double calculateMaterialCost(double infillDensity, double partVolume, double materialCostPerGram) {
    if (infillDensity < 0 || infillDensity > 100 || partVolume <= 0 || materialCostPerGram <= 0) {
        throw std::invalid_argument("Invalid input parameters for material cost calculation.");
    }
    double materialVolume = partVolume * (infillDensity / 100.0); // Volume of material used
    double materialWeight = materialVolume * 1.25;               // Assume density of material is 1.25 g/cm³
    return materialWeight * materialCostPerGram;
}

// Function to optimize 3D printing parameters
PrintingParameters optimizeParameters(double partVolume, double materialCostPerGram, double maxPrintTime) {
    if (partVolume <= 0 || materialCostPerGram <= 0 || maxPrintTime <= 0) {
        throw std::invalid_argument("Invalid input parameters for optimization.");
    }

    PrintingParameters bestParameters;
    double minCost = std::numeric_limits<double>::max();

    // Iterate over possible layer thickness and infill density values
    for (double layerThickness = 0.1; layerThickness <= 0.3; layerThickness += 0.05) {
        for (double infillDensity = 10; infillDensity <= 100; infillDensity += 10) {
            double printSpeed = 50.0; // Fixed print speed for simplicity
            double estimatedTime = calculatePrintTime(layerThickness, infillDensity, printSpeed, partVolume);

            if (estimatedTime <= maxPrintTime) {
                double materialCost = calculateMaterialCost(infillDensity, partVolume, materialCostPerGram);

                // Update best parameters if cost is lower
                if (materialCost < minCost) {
                    minCost = materialCost;
                    bestParameters = {layerThickness, infillDensity, printSpeed, materialCost, estimatedTime};
                }
            }
        }
    }

    if (minCost == std::numeric_limits<double>::max()) {
        throw std::runtime_error("No feasible parameters found within the given constraints.");
    }

    return bestParameters;
}

int main() {
    try {
        // Input parameters
        double partVolume = 500.0;          // Volume of the part in cm³
        double materialCostPerGram = 0.05; // Cost of material per gram
        double maxPrintTime = 10.0;        // Maximum allowable print time in hours

        // Optimize parameters
        PrintingParameters optimizedParams = optimizeParameters(partVolume, materialCostPerGram, maxPrintTime);

        // Output optimized parameters
        std::cout << "Optimized 3D Printing Parameters:\n";
        std::cout << "Layer Thickness: " << optimizedParams.layerThickness << " mm\n";
        std::cout << "Infill Density: " << optimizedParams.infillDensity << " %\n";
        std::cout << "Print Speed: " << optimizedParams.printSpeed << " mm/s\n";
        std::cout << "Material Cost: $" << optimizedParams.materialCost << "\n";
        std::cout << "Estimated Print Time: " << optimizedParams.estimatedTime << " hours\n";
    } catch (const std::exception &e) {
        std::cerr << "Error: " << e.what() << '\n';
        return 1;
    }

    return 0;
}
```
