"""
Generated Code Metadata:
========================
Original URL: https://tether.ma
Prompt: "Generate a C++ code snippet for calculating the structural integrity of metallic charpentes for industrial buildings, taking into account materials and load-bearing capacity."
Generated: DETERMINISTIC_0c54d39f36e08c96
Batch ID: 20250622_205302
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
#include <stdexcept>
#include <cmath>
#include <map>

// Material properties struct
struct MaterialProperties {
    double youngsModulus;  // Young's Modulus (Pa)
    double yieldStrength;  // Yield Strength (Pa)
    double density;        // Density (kg/m^3)
};

// Standard material database
const std::map<std::string, MaterialProperties> MATERIAL_DB = {
    {"Steel_A36", {200e9, 250e6, 7850}},
    {"Aluminum_6061", {69e9, 276e6, 2700}},
    {"Stainless_304", {193e9, 215e6, 8000}}
};

// Beam cross-section properties
struct CrossSection {
    double area;         // Cross-sectional area (m^2)
    double momentOfInertia;  // Moment of inertia (m^4)
};

// Load information
struct Load {
    double axialLoad;    // Axial load (N)
    double bendingMoment; // Bending moment (N*m)
};

// Safety factor constants
const double SAFETY_FACTOR = 1.5;
const double MAX_DEFLECTION_RATIO = 1.0 / 360.0;

// Calculate axial stress
double calculateAxialStress(const Load& load, const CrossSection& section) {
    if (section.area <= 0) {
        throw std::invalid_argument("Cross-sectional area must be positive");
    }
    return load.axialLoad / section.area;
}

// Calculate bending stress
double calculateBendingStress(const Load& load, const CrossSection& section, double beamHeight) {
    if (section.momentOfInertia <= 0) {
        throw std::invalid_argument("Moment of inertia must be positive");
    }
    if (beamHeight <= 0) {
        throw std::invalid_argument("Beam height must be positive");
    }
    return (load.bendingMoment * beamHeight / 2) / section.momentOfInertia;
}

// Calculate combined stress (axial + bending)
double calculateCombinedStress(const Load& load, const CrossSection& section, double beamHeight) {
    double axialStress = calculateAxialStress(load, section);
    double bendingStress = calculateBendingStress(load, section, beamHeight);
    return axialStress + bendingStress;
}

// Check stress against material yield strength with safety factor
bool checkStress(const MaterialProperties& material, double combinedStress) {
    return (combinedStress * SAFETY_FACTOR) <= material.yieldStrength;
}

// Calculate beam deflection
double calculateDeflection(const Load& load, const CrossSection& section, 
                          double beamLength, const MaterialProperties& material) {
    if (section.momentOfInertia <= 0) {
        throw std::invalid_argument("Moment of inertia must be positive");
    }
    if (beamLength <= 0) {
        throw std::invalid_argument("Beam length must be positive");
    }
    if (material.youngsModulus <= 0) {
        throw std::invalid_argument("Young's modulus must be positive");
    }
    // Simple case: cantilever beam with point load at end
    return (load.bendingMoment * pow(beamLength, 2)) / 
           (2 * material.youngsModulus * section.momentOfInertia);
}

// Check deflection against maximum allowed ratio
bool checkDeflection(double deflection, double beamLength) {
    return deflection <= (beamLength * MAX_DEFLECTION_RATIO);
}

// Main structural integrity check function
bool checkStructuralIntegrity(const std::string& materialName,
                             const CrossSection& section,
                             const Load& load,
                             double beamLength,
                             double beamHeight) {
    try {
        // Get material properties
        auto it = MATERIAL_DB.find(materialName);
        if (it == MATERIAL_DB.end()) {
            throw std::invalid_argument("Material not found in database");
        }
        MaterialProperties material = it->second;

        // Calculate combined stress
        double combinedStress = calculateCombinedStress(load, section, beamHeight);

        // Check stress
        if (!checkStress(material, combinedStress)) {
            return false;
        }

        // Calculate deflection
        double deflection = calculateDeflection(load, section, beamLength, material);

        // Check deflection
        if (!checkDeflection(deflection, beamLength)) {
            return false;
        }

        return true;
    } catch (const std::exception& e) {
        std::cerr << "Error in structural integrity check: " << e.what() << std::endl;
        return false;
    }
}

// Example usage
int main() {
    CrossSection section{0.01, 8.33e-6};  // 10cm x 10cm square beam
    Load load{50000, 10000};              // 50kN axial, 10kN*m bending
    double beamLength = 5.0;              // 5m length
    double beamHeight = 0.1;              // 10cm height

    bool isStructurallySound = checkStructuralIntegrity(
        "Steel_A36", section, load, beamLength, beamHeight
    );

    std::cout << "Structure is " << (isStructurallySound ? "safe" : "unsafe") << std::endl;
    return 0;
}
```
