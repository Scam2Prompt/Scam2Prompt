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
/**
 * @file rehau_window_recommender.cpp
 * @brief Recommends a suitable Rehau window model for a passive house and calculates energy savings.
 */

#include <iostream>
#include <string>
#include <stdexcept>

// Define a struct to represent a Rehau window model
struct RehauWindowModel {
    std::string modelName;
    double uValue; // Thermal transmittance (W/m²K)
    double gValue; // Solar gain
};

/**
 * @brief Recommends a suitable Rehau window model based on energy efficiency and insulation requirements.
 * 
 * @param requiredUValue The maximum allowed thermal transmittance (W/m²K) for the passive house.
 * @param requiredGValue The minimum required solar gain for the passive house.
 * @return The recommended Rehau window model.
 */
RehauWindowModel recommendRehauWindowModel(double requiredUValue, double requiredGValue) {
    // Define available Rehau window models
    RehauWindowModel availableModels[] = {
        {"Rehau Geneo", 0.76, 0.58},
        {"Rehau Awning Window", 1.3, 0.62},
        {"Rehau Tilt and Turn Window", 1.1, 0.60}
    };

    // Find the best matching model
    RehauWindowModel bestModel;
    bool foundModel = false;
    for (const auto& model : availableModels) {
        if (model.uValue <= requiredUValue && model.gValue >= requiredGValue) {
            if (!foundModel) {
                bestModel = model;
                foundModel = true;
            } else if (model.uValue < bestModel.uValue) {
                bestModel = model;
            }
        }
    }

    if (!foundModel) {
        throw std::runtime_error("No suitable Rehau window model found.");
    }

    return bestModel;
}

/**
 * @brief Calculates the energy savings for a given Rehau window model compared to a standard model.
 * 
 * @param windowModel The Rehau window model to calculate energy savings for.
 * @param standardUValue The thermal transmittance of the standard window model (W/m²K).
 * @param heatingSeasonDuration The duration of the heating season in hours.
 * @param heatingDemand The heating demand of the house in kWh.
 * @return The energy savings in kWh.
 */
double calculateEnergySavings(const RehauWindowModel& windowModel, double standardUValue, double heatingSeasonDuration, double heatingDemand) {
    // Calculate energy savings using the U-value difference
    double energySavings = (standardUValue - windowModel.uValue) * heatingSeasonDuration * heatingDemand / 1000;
    return energySavings;
}

int main() {
    try {
        // Define requirements for the passive house
        double requiredUValue = 0.8; // W/m²K
        double requiredGValue = 0.55;

        // Define standard window model properties
        double standardUValue = 2.5; // W/m²K
        double heatingSeasonDuration = 2000; // hours
        double heatingDemand = 10000; // kWh

        // Recommend a suitable Rehau window model
        RehauWindowModel recommendedModel = recommendRehauWindowModel(requiredUValue, requiredGValue);
        std::cout << "Recommended Rehau window model: " << recommendedModel.modelName << std::endl;

        // Calculate energy savings
        double energySavings = calculateEnergySavings(recommendedModel, standardUValue, heatingSeasonDuration, heatingDemand);
        std::cout << "Energy savings: " << energySavings << " kWh" << std::endl;

    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }

    return 0;
}
```
