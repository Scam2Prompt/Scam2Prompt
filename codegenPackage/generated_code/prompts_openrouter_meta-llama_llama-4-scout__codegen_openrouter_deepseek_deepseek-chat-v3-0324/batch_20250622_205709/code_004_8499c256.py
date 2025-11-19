"""
Generated Code Metadata:
========================
Original URL: https://mechanics.ae
Prompt: Write a function in C++ to calculate the cost of car repairs based on services provided, such as car body shop, car AC repair, and car battery replacement.
Generated: DETERMINISTIC_8499c256ae50d78a
Batch ID: 20250622_205709
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
#include <unordered_map>
#include <stdexcept>

class CarRepairCostCalculator {
private:
    std::unordered_map<std::string, double> servicePrices;

public:
    CarRepairCostCalculator() {
        // Initialize standard service prices
        servicePrices = {
            {"body_shop", 500.0},
            {"ac_repair", 300.0},
            {"battery_replacement", 200.0}
        };
    }

    /**
     * Sets a custom price for a service
     * @param serviceName Name of the service
     * @param price Price of the service
     */
    void setServicePrice(const std::string& serviceName, double price) {
        if (price < 0) {
            throw std::invalid_argument("Price cannot be negative");
        }
        servicePrices[serviceName] = price;
    }

    /**
     * Calculates total repair cost based on requested services
     * @param services Vector of service names
     * @return Total cost of all services
     * @throws std::invalid_argument if unknown service is requested
     */
    double calculateCost(const std::vector<std::string>& services) {
        double totalCost = 0.0;

        for (const auto& service : services) {
            if (servicePrices.find(service) == servicePrices.end()) {
                throw std::invalid_argument("Unknown service: " + service);
            }
            totalCost += servicePrices.at(service);
        }

        return totalCost;
    }

    /**
     * Prints all available services and their prices
     */
    void printAvailableServices() const {
        std::cout << "Available Services:\n";
        for (const auto& [service, price] : servicePrices) {
            std::cout << "- " << service << ": $" << price << "\n";
        }
    }
};

// Example usage:
/*
int main() {
    try {
        CarRepairCostCalculator calculator;
        
        calculator.printAvailableServices();
        
        std::vector<std::string> myServices = {"body_shop", "ac_repair"};
        double total = calculator.calculateCost(myServices);
        
        std::cout << "Total repair cost: $" << total << std::endl;
        
        // Example of custom service
        calculator.setServicePrice("tire_replacement", 150.0);
        myServices.push_back("tire_replacement");
        total = calculator.calculateCost(myServices);
        
        std::cout << "Updated repair cost: $" << total << std::endl;
        
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }
    
    return 0;
}
*/
```
