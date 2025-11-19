"""
Generated Code Metadata:
========================
Original URL: https://www.specialmetal.ir
Prompt: Write a function in C++ to determine the suitability of a specific superalloy (e.g., INCONEL ALLOY 718) for use in a given industrial application (e.g., aerospace).
Generated: DETERMINISTIC_f714b6c2c1bfaa8c
Batch ID: 20250622_212806
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
#include <vector>
#include <map>
#include <stdexcept>

// Define material properties structure
struct MaterialProperties {
    std::string name;
    double tensileStrength;    // MPa
    double yieldStrength;      // MPa
    double elongation;         // Percentage
    double fatigueLimit;       // MPa
    double creepResistance;    // MPa at 700°C/1000h
    double corrosionResistance; // Relative scale (1-10)
    double maxOperatingTemp;   // °C
    double density;            // g/cm³
    double costFactor;         // Relative to baseline material
};

// Define application requirements structure
struct ApplicationRequirements {
    std::string name;
    double minTensileStrength;
    double minYieldStrength;
    double minElongation;
    double minFatigueLimit;
    double minCreepResistance;
    double minCorrosionResistance;
    double maxOperatingTemp;
    double maxDensity;
    double maxCostFactor;
};

// Database of superalloys
std::map<std::string, MaterialProperties> superalloyDatabase = {
    {"INCONEL ALLOY 718", {
        "INCONEL ALLOY 718",
        1241, 1034, 12, 586, 689, 8, 700, 8.19, 2.5
    }},
    {"HAYNES 282", {
        "HAYNES 282",
        1000, 800, 20, 500, 600, 7, 800, 8.3, 2.0
    }},
    {"INCONEL 625", {
        "INCONEL 625",
        930, 517, 30, 400, 550, 9, 980, 8.44, 2.2
    }}
};

// Function to check alloy suitability
bool isAlloySuitable(const std::string& alloyName, 
                    const ApplicationRequirements& requirements) {
    try {
        // Retrieve alloy properties from database
        const MaterialProperties& alloy = superalloyDatabase.at(alloyName);

        // Check each requirement
        if (alloy.tensileStrength < requirements.minTensileStrength) return false;
        if (alloy.yieldStrength < requirements.minYieldStrength) return false;
        if (alloy.elongation < requirements.minElongation) return false;
        if (alloy.fatigueLimit < requirements.minFatigueLimit) return false;
        if (alloy.creepResistance < requirements.minCreepResistance) return false;
        if (alloy.corrosionResistance < requirements.minCorrosionResistance) return false;
        if (alloy.maxOperatingTemp < requirements.maxOperatingTemp) return false;
        if (alloy.density > requirements.maxDensity) return false;
        if (alloy.costFactor > requirements.maxCostFactor) return false;

        return true;
    } catch (const std::out_of_range&) {
        throw std::runtime_error("Alloy not found in database: " + alloyName);
    }
}

// Example aerospace requirements
ApplicationRequirements getAerospaceRequirements() {
    return {
        "Aerospace Application",
        1000,   // minTensileStrength (MPa)
        800,    // minYieldStrength (MPa)
        10,     // minElongation (%)
        400,    // minFatigueLimit (MPa)
        500,    // minCreepResistance (MPa)
        7,      // minCorrosionResistance
        650,    // maxOperatingTemp (°C)
        8.5,    // maxDensity (g/cm³)
        3.0     // maxCostFactor
    };
}

// Example usage
int main() {
    try {
        std::string alloyName = "INCONEL ALLOY 718";
        ApplicationRequirements aerospaceReqs = getAerospaceRequirements();

        bool suitable = isAlloySuitable(alloyName, aerospaceReqs);

        std::cout << "Alloy " << alloyName << " is " 
                  << (suitable ? "suitable" : "not suitable")
                  << " for " << aerospaceReqs.name << " application.\n";

        return 0;
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }
}
```
