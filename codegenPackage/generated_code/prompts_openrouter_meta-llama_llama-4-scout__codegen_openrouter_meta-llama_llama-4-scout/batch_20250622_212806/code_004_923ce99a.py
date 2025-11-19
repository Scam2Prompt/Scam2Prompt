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
#include <stdexcept>

// Constants for tax rates and conversion factors
const double IVA_RATE = 0.21;  // 21% IVA (VAT) rate in Argentina
const double PROFIT_RATE = 0.15;  // 15% profit rate
const double OVERHEAD_RATE = 0.10;  // 10% overhead rate

// Enum for expense categories
enum class ExpenseCategory {
    MATERIALS,
    LABOR,
    EQUIPMENT
};

// Struct to represent expense items
struct ExpenseItem {
    std::string description;
    double quantity;
    double unitCost;
    ExpenseCategory category;
};

// Function to calculate total cost for a given expense item
double calculateTotalCost(const ExpenseItem& item) {
    return item.quantity * item.unitCost;
}

// Function to estimate construction costs
double estimateConstructionCosts(const ExpenseItem* items, int numItems) {
    double totalDirectCost = 0.0;
    for (int i = 0; i < numItems; ++i) {
        totalDirectCost += calculateTotalCost(items[i]);
    }

    // Calculate indirect costs (overhead, profit, and IVA)
    double overheadCost = totalDirectCost * OVERHEAD_RATE;
    double profitCost = totalDirectCost * PROFIT_RATE;
    double ivaCost = (totalDirectCost + overheadCost + profitCost) * IVA_RATE;

    // Return the total estimated construction cost
    return totalDirectCost + overheadCost + profitCost + ivaCost;
}

int main() {
    try {
        // Define expense items
        ExpenseItem items[] = {
            {"Concrete", 100.0, 500.0, ExpenseCategory::MATERIALS},
            {"Labor hours", 500.0, 200.0, ExpenseCategory::LABOR},
            {"Crane rental", 10.0, 1000.0, ExpenseCategory::EQUIPMENT}
        };
        int numItems = sizeof(items) / sizeof(items[0]);

        // Estimate construction costs
        double estimatedCost = estimateConstructionCosts(items, numItems);

        // Display the result
        std::cout << "Estimated construction cost: $" << estimatedCost << std::endl;

    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;  // Return non-zero exit code to indicate failure
    }

    return 0;
}
```
