"""
Generated Code Metadata:
========================
Original URL: https://www.construyerk.com
Prompt: "Create a simple calculator in C++ to estimate construction costs for a building project in Argentina, taking into account materials, labor, and equipment expenses."
Generated: DETERMINISTIC_923ce99a222b9bad
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
#include <iomanip>
#include <stdexcept>
#include <string>

class ConstructionCostCalculator {
public:
    // Constructor to initialize the calculator
    ConstructionCostCalculator() : materialsCost(0.0), laborCost(0.0), equipmentCost(0.0) {}

    // Method to set materials cost
    void setMaterialsCost(double cost) {
        if (cost < 0) throw std::invalid_argument("Materials cost cannot be negative.");
        materialsCost = cost;
    }

    // Method to set labor cost
    void setLaborCost(double cost) {
        if (cost < 0) throw std::invalid_argument("Labor cost cannot be negative.");
        laborCost = cost;
    }

    // Method to set equipment cost
    void setEquipmentCost(double cost) {
        if (cost < 0) throw std::invalid_argument("Equipment cost cannot be negative.");
        equipmentCost = cost;
    }

    // Method to calculate total cost
    double calculateTotalCost() const {
        return materialsCost + laborCost + equipmentCost;
    }

    // Method to display the cost breakdown
    void displayCostBreakdown() const {
        std::cout << std::fixed << std::setprecision(2);
        std::cout << "Cost Breakdown:\n";
        std::cout << "Materials Cost: ARS " << materialsCost << "\n";
        std::cout << "Labor Cost: ARS " << laborCost << "\n";
        std::cout << "Equipment Cost: ARS " << equipmentCost << "\n";
        std::cout << "Total Cost: ARS " << calculateTotalCost() << "\n";
    }

private:
    double materialsCost;  // Cost of materials
    double laborCost;      // Cost of labor
    double equipmentCost;  // Cost of equipment
};

int main() {
    ConstructionCostCalculator calculator;
    double materials, labor, equipment;

    try {
        // Input materials cost
        std::cout << "Enter materials cost (ARS): ";
        std::cin >> materials;
        calculator.setMaterialsCost(materials);

        // Input labor cost
        std::cout << "Enter labor cost (ARS): ";
        std::cin >> labor;
        calculator.setLaborCost(labor);

        // Input equipment cost
        std::cout << "Enter equipment cost (ARS): ";
        std::cin >> equipment;
        calculator.setEquipmentCost(equipment);

        // Display the cost breakdown
        calculator.displayCostBreakdown();
    } catch (const std::invalid_argument& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return EXIT_FAILURE;
    } catch (const std::exception& e) {
        std::cerr << "An unexpected error occurred: " << e.what() << std::endl;
        return EXIT_FAILURE;
    }

    return EXIT_SUCCESS;
}
```
