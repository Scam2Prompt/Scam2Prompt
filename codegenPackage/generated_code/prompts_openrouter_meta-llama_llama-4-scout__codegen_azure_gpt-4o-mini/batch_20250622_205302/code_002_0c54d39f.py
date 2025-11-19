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
#include <stdexcept>
#include <string>

// Class representing a metallic charpente (framework)
class MetallicCharpente {
public:
    // Constructor to initialize material properties and dimensions
    MetallicCharpente(const std::string& material, double length, double width, double height, double loadCapacity)
        : material(material), length(length), width(width), height(height), loadCapacity(loadCapacity) {
        if (length <= 0 || width <= 0 || height <= 0 || loadCapacity <= 0) {
            throw std::invalid_argument("Dimensions and load capacity must be positive values.");
        }
    }

    // Method to calculate the structural integrity based on load
    bool isStructurallySound(double appliedLoad) const {
        if (appliedLoad < 0) {
            throw std::invalid_argument("Applied load must be a non-negative value.");
        }
        return appliedLoad <= loadCapacity;
    }

    // Method to display the properties of the charpente
    void displayProperties() const {
        std::cout << "Material: " << material << std::endl;
        std::cout << "Dimensions (L x W x H): " << length << " x " << width << " x " << height << std::endl;
        std::cout << "Load Capacity: " << loadCapacity << " N" << std::endl;
    }

private:
    std::string material; // Material of the charpente
    double length;        // Length of the charpente in meters
    double width;         // Width of the charpente in meters
    double height;        // Height of the charpente in meters
    double loadCapacity;  // Maximum load capacity in Newtons
};

int main() {
    try {
        // Create a metallic charpente object
        MetallicCharpente charpente("Steel", 10.0, 5.0, 3.0, 50000.0);

        // Display the properties of the charpente
        charpente.displayProperties();

        // Example applied load
        double appliedLoad = 45000.0; // Load in Newtons

        // Check if the charpente is structurally sound
        if (charpente.isStructurallySound(appliedLoad)) {
            std::cout << "The charpente is structurally sound under the applied load of " << appliedLoad << " N." << std::endl;
        } else {
            std::cout << "Warning: The charpente is NOT structurally sound under the applied load of " << appliedLoad << " N." << std::endl;
        }
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return EXIT_FAILURE;
    }

    return EXIT_SUCCESS;
}
```
