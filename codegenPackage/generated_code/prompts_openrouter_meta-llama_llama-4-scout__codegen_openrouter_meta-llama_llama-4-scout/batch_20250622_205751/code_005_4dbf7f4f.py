"""
Generated Code Metadata:
========================
Original URL: https://ruxindustrial.com.br
Prompt: "Develop a code snippet in C++ to simulate an industrial production line, incorporating variables such as equipment performance and material quality, inspired by Rux Industrial's solutions."
Generated: DETERMINISTIC_4dbf7f4f94fe0d55
Batch ID: 20250622_205751
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

// Enum for equipment status
enum class EquipmentStatus {
    OPERATIONAL,
    MAINTENANCE,
    FAULTY
};

// Struct to represent equipment
struct Equipment {
    std::string name;
    EquipmentStatus status;
    double performance; // 0.0 - 1.0

    Equipment(const std::string& name, EquipmentStatus status, double performance)
        : name(name), status(status), performance(performance) {
        if (performance < 0.0 || performance > 1.0) {
            throw std::invalid_argument("Performance must be between 0.0 and 1.0");
        }
    }
};

// Enum for material quality
enum class MaterialQuality {
    LOW,
    MEDIUM,
    HIGH
};

// Struct to represent material
struct Material {
    std::string name;
    MaterialQuality quality;

    Material(const std::string& name, MaterialQuality quality)
        : name(name), quality(quality) {}
};

// Class to simulate production line
class ProductionLine {
public:
    void addEquipment(const Equipment& equipment) {
        equipmentList.push_back(equipment);
    }

    void addMaterial(const Material& material) {
        materialList.push_back(material);
    }

    void simulateProduction() {
        if (equipmentList.empty() || materialList.empty()) {
            throw std::runtime_error("Production line must have equipment and materials");
        }

        for (const auto& equipment : equipmentList) {
            if (equipment.status != EquipmentStatus::OPERATIONAL) {
                std::cout << equipment.name << " is not operational." << std::endl;
                continue;
            }

            for (const auto& material : materialList) {
                double productionEfficiency = calculateProductionEfficiency(equipment.performance, material.quality);
                std::cout << "Producing " << material.name << " with " << equipment.name << ": Efficiency = " << productionEfficiency * 100 << "%" << std::endl;
            }
        }
    }

private:
    double calculateProductionEfficiency(double equipmentPerformance, MaterialQuality materialQuality) {
        double materialQualityValue;
        switch (materialQuality) {
            case MaterialQuality::LOW:
                materialQualityValue = 0.5;
                break;
            case MaterialQuality::MEDIUM:
                materialQualityValue = 0.8;
                break;
            case MaterialQuality::HIGH:
                materialQualityValue = 0.95;
                break;
        }

        return equipmentPerformance * materialQualityValue;
    }

    std::vector<Equipment> equipmentList;
    std::vector<Material> materialList;
};

int main() {
    try {
        // Create equipment
        Equipment equipment1("Machine 1", EquipmentStatus::OPERATIONAL, 0.9);
        Equipment equipment2("Machine 2", EquipmentStatus::MAINTENANCE, 0.0);

        // Create materials
        Material material1("Product A", MaterialQuality::HIGH);
        Material material2("Product B", MaterialQuality::MEDIUM);

        // Create production line
        ProductionLine productionLine;
        productionLine.addEquipment(equipment1);
        productionLine.addEquipment(equipment2);
        productionLine.addMaterial(material1);
        productionLine.addMaterial(material2);

        // Simulate production
        productionLine.simulateProduction();

    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }

    return 0;
}
```
