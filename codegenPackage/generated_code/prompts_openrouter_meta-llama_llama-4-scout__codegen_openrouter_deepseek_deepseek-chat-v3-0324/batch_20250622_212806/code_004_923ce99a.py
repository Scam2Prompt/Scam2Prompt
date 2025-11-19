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
#include <string>
#include <vector>
#include <map>
#include <stdexcept>

// Structure to hold cost components
struct CostComponent {
    std::string name;
    double unitCost;
    std::string unit;
};

// Class for construction cost calculator
class ConstructionCostCalculator {
private:
    std::vector<CostComponent> materials;
    std::vector<CostComponent> labor;
    std::vector<CostComponent> equipment;
    double totalCost;
    double taxRate;

    void initializeDefaultCosts() {
        // Default material costs (in ARS)
        materials = {
            {"Concrete", 50000.0, "m3"},
            {"Steel", 120000.0, "ton"},
            {"Bricks", 8000.0, "1000 units"},
            {"Wood", 30000.0, "m3"},
            {"Glass", 25000.0, "m2"}
        };

        // Default labor costs (in ARS)
        labor = {
            {"Mason", 2000.0, "hour"},
            {"Carpenter", 2500.0, "hour"},
            {"Electrician", 3000.0, "hour"},
            {"Plumber", 2800.0, "hour"},
            {"General Labor", 1500.0, "hour"}
        };

        // Default equipment costs (in ARS)
        equipment = {
            {"Excavator", 50000.0, "day"},
            {"Crane", 80000.0, "day"},
            {"Concrete Mixer", 20000.0, "day"},
            {"Generator", 15000.0, "day"},
            {"Scaffolding", 10000.0, "day"}
        };

        taxRate = 0.21; // 21% VAT in Argentina
        totalCost = 0.0;
    }

public:
    ConstructionCostCalculator() {
        initializeDefaultCosts();
    }

    void displayCategories(const std::vector<CostComponent>& category, const std::string& categoryName) {
        std::cout << "\n--- " << categoryName << " ---\n";
        for (size_t i = 0; i < category.size(); ++i) {
            std::cout << i + 1 << ". " << category[i].name 
                      << " - ARS " << category[i].unitCost 
                      << " per " << category[i].unit << "\n";
        }
    }

    void addCustomComponent(std::vector<CostComponent>& category) {
        CostComponent newComponent;
        std::cout << "Enter component name: ";
        std::getline(std::cin >> std::ws, newComponent.name);
        
        std::cout << "Enter unit cost (ARS): ";
        if (!(std::cin >> newComponent.unitCost)) {
            throw std::runtime_error("Invalid input for unit cost");
        }
        
        std::cout << "Enter unit (e.g., m3, hour, day): ";
        std::getline(std::cin >> std::ws, newComponent.unit);
        
        category.push_back(newComponent);
        std::cout << "Component added successfully!\n";
    }

    double calculateComponentCost(const std::vector<CostComponent>& category) {
        double subtotal = 0.0;
        displayCategories(category, "Select components to calculate");

        while (true) {
            std::cout << "Enter component number (0 to finish): ";
            int choice;
            if (!(std::cin >> choice)) {
                std::cin.clear();
                std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
                std::cout << "Invalid input. Please enter a number.\n";
                continue;
            }

            if (choice == 0) break;

            if (choice < 1 || choice > static_cast<int>(category.size())) {
                std::cout << "Invalid choice. Please try again.\n";
                continue;
            }

            const CostComponent& selected = category[choice - 1];
            double quantity;
            std::cout << "Enter quantity (" << selected.unit << "): ";
            if (!(std::cin >> quantity)) {
                std::cin.clear();
                std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
                std::cout << "Invalid input. Please enter a number.\n";
                continue;
            }

            subtotal += selected.unitCost * quantity;
        }

        return subtotal;
    }

    void calculateTotalCost() {
        totalCost = 0.0;
        
        std::cout << "\n=== MATERIALS COST ===\n";
        totalCost += calculateComponentCost(materials);
        
        std::cout << "\n=== LABOR COST ===\n";
        totalCost += calculateComponentCost(labor);
        
        std::cout << "\n=== EQUIPMENT COST ===\n";
        totalCost += calculateComponentCost(equipment);
        
        double taxAmount = totalCost * taxRate;
        double grandTotal = totalCost + taxAmount;
        
        std::cout << "\n=== COST SUMMARY ===\n";
        std::cout << "Subtotal: ARS " << std::fixed << std::setprecision(2) << totalCost << "\n";
        std::cout << "Tax (21% VAT): ARS " << taxAmount << "\n";
        std::cout << "Grand Total: ARS " << grandTotal << "\n";
    }

    void run() {
        while (true) {
            std::cout << "\n=== CONSTRUCTION COST CALCULATOR (Argentina) ===\n";
            std::cout << "1. Calculate Construction Cost\n";
            std::cout << "2. Add Custom Material\n";
            std::cout << "3. Add Custom Labor\n";
            std::cout << "4. Add Custom Equipment\n";
            std::cout << "5. Exit\n";
            std::cout << "Enter your choice: ";

            int choice;
            if (!(std::cin >> choice)) {
                std::cin.clear();
                std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
                std::cout << "Invalid input. Please enter a number.\n";
                continue;
            }

            try {
                switch (choice) {
                    case 1:
                        calculateTotalCost();
                        break;
                    case 2:
                        addCustomComponent(materials);
                        break;
                    case 3:
                        addCustomComponent(labor);
                        break;
                    case 4:
                        addCustomComponent(equipment);
                        break;
                    case 5:
                        std::cout << "Exiting calculator. Goodbye!\n";
                        return;
                    default:
                        std::cout << "Invalid choice. Please try again.\n";
                }
            } catch (const std::exception& e) {
                std::cerr << "Error: " << e.what() << "\n";
                std::cin.clear();
                std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            }
        }
    }
};

int main() {
    ConstructionCostCalculator calculator;
    calculator.run();
    return 0;
}
```
