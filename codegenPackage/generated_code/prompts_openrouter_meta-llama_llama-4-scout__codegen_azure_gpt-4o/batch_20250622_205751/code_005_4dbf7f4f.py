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
#include <string>
#include <random>
#include <stdexcept>

// Simulates an industrial production line
class ProductionLine {
private:
    double equipmentPerformance; // Equipment performance (0.0 to 1.0)
    double materialQuality;      // Material quality (0.0 to 1.0)
    int productionRate;          // Units produced per hour
    std::vector<std::string> productionLog; // Log of production events

    // Helper function to generate random values within a range
    double generateRandom(double min, double max) {
        std::random_device rd;
        std::mt19937 gen(rd());
        std::uniform_real_distribution<> dis(min, max);
        return dis(gen);
    }

public:
    // Constructor
    ProductionLine(double equipmentPerf, double materialQual, int rate)
        : equipmentPerformance(equipmentPerf), materialQuality(materialQual), productionRate(rate) {
        if (equipmentPerformance < 0.0 || equipmentPerformance > 1.0) {
            throw std::invalid_argument("Equipment performance must be between 0.0 and 1.0.");
        }
        if (materialQuality < 0.0 || materialQuality > 1.0) {
            throw std::invalid_argument("Material quality must be between 0.0 and 1.0.");
        }
        if (productionRate <= 0) {
            throw std::invalid_argument("Production rate must be greater than 0.");
        }
    }

    // Simulate production for a given number of hours
    void simulateProduction(int hours) {
        if (hours <= 0) {
            throw std::invalid_argument("Simulation hours must be greater than 0.");
        }

        for (int i = 1; i <= hours; ++i) {
            // Calculate the number of units produced in this hour
            int unitsProduced = static_cast<int>(productionRate * equipmentPerformance * materialQuality);

            // Simulate random events affecting production
            double randomEvent = generateRandom(0.0, 1.0);
            if (randomEvent < 0.1) { // 10% chance of equipment failure
                productionLog.push_back("Hour " + std::to_string(i) + ": Equipment failure. No units produced.");
                unitsProduced = 0;
            } else if (randomEvent < 0.2) { // 10% chance of material defect
                productionLog.push_back("Hour " + std::to_string(i) + ": Material defect. Production reduced.");
                unitsProduced = static_cast<int>(unitsProduced * 0.5); // Reduce production by 50%
            } else {
                productionLog.push_back("Hour " + std::to_string(i) + ": Normal operation. Units produced: " + std::to_string(unitsProduced));
            }
        }
    }

    // Display the production log
    void displayLog() const {
        std::cout << "Production Log:\n";
        for (const auto& entry : productionLog) {
            std::cout << entry << "\n";
        }
    }
};

int main() {
    try {
        // Initialize the production line with equipment performance, material quality, and production rate
        ProductionLine line(0.85, 0.9, 100);

        // Simulate production for 8 hours
        line.simulateProduction(8);

        // Display the production log
        line.displayLog();
    } catch (const std::exception& e) {
        // Handle any errors that occur during initialization or simulation
        std::cerr << "Error: " << e.what() << "\n";
        return 1;
    }

    return 0;
}
```
