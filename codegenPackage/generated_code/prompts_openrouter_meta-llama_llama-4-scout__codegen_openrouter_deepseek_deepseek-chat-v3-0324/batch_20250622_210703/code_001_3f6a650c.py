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
#include <cmath>
#include <stdexcept>
#include <vector>
#include <map>

// Structure to store window properties
struct WindowModel {
    std::string name;
    double uValue;          // Thermal transmittance (W/m²K)
    double gValue;          // Solar heat gain coefficient
    double frameWidth;      // Frame width in mm
    bool tripleGlazing;     // Whether it has triple glazing
};

// Database of Rehau window models suitable for passive houses
const std::vector<WindowModel> REHAU_MODELS = {
    {"Rehau Geneo", 0.76, 0.5, 84.0, true},
    {"Rehau Delight", 0.85, 0.6, 78.0, true},
    {"Rehau Brillant-Design", 0.93, 0.62, 80.0, false}
};

// Function to calculate annual energy savings
double calculateEnergySavings(double area, double oldUValue, double newUValue, 
                             double heatingDegreeDays, double heatingCostPerKWh) {
    if (area <= 0 || oldUValue <= 0 || newUValue <= 0 || heatingDegreeDays <= 0 || heatingCostPerKWh <= 0) {
        throw std::invalid_argument("All parameters must be positive values");
    }
    
    // Energy savings formula: (oldU - newU) * area * heatingDegreeDays * 24 / 1000
    double energySavingsKWh = (oldUValue - newUValue) * area * heatingDegreeDays * 24.0 / 1000.0;
    return energySavingsKWh * heatingCostPerKWh;
}

// Function to recommend best window model based on U-value
const WindowModel& recommendWindowModel(double maxUValue = 0.8) {
    const WindowModel* bestModel = nullptr;
    
    for (const auto& model : REHAU_MODELS) {
        if (model.uValue <= maxUValue) {
            if (!bestModel || model.uValue < bestModel->uValue) {
                bestModel = &model;
            }
        }
    }
    
    if (!bestModel) {
        throw std::runtime_error("No suitable Rehau window model found for the given U-value requirement");
    }
    
    return *bestModel;
}

int main() {
    try {
        // Example usage
        const WindowModel& recommendedModel = recommendWindowModel(0.8);
        std::cout << "Recommended Rehau window model: " << recommendedModel.name << std::endl;
        std::cout << "U-value: " << recommendedModel.uValue << " W/m²K" << std::endl;
        
        // Calculate energy savings example
        double windowArea = 2.5; // m²
        double oldWindowUValue = 1.4; // W/m²K
        double heatingDegreeDays = 3500; // K·days/year
        double heatingCost = 0.15; // $/kWh
        
        double savings = calculateEnergySavings(
            windowArea, 
            oldWindowUValue, 
            recommendedModel.uValue, 
            heatingDegreeDays, 
            heatingCost
        );
        
        std::cout << "Annual energy savings: $" << savings << std::endl;
        
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }
    
    return 0;
}
```
