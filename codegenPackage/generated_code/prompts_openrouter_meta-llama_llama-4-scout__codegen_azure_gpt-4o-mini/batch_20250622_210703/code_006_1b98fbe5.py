"""
Generated Code Metadata:
========================
Original URL: https://duct-split.com
Prompt: "Write a code in C++ to simulate the performance of a Gree ducted split system, like model GUD36PHS, under different environmental conditions."
Generated: DETERMINISTIC_1b98fbe590713cd6
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
#include <stdexcept>
#include <vector>
#include <iomanip>

// Class to represent the Gree ducted split system
class GreeDuctedSplitSystem {
public:
    // Constructor to initialize the system with default parameters
    GreeDuctedSplitSystem(double coolingCapacity, double heatingCapacity)
        : coolingCapacity(coolingCapacity), heatingCapacity(heatingCapacity) {
        if (coolingCapacity <= 0 || heatingCapacity <= 0) {
            throw std::invalid_argument("Cooling and heating capacities must be positive values.");
        }
    }

    // Method to simulate performance under different environmental conditions
    void simulatePerformance(double outsideTemperature, double humidity) {
        if (outsideTemperature < -30 || outsideTemperature > 50) {
            throw std::out_of_range("Outside temperature must be between -30 and 50 degrees Celsius.");
        }
        if (humidity < 0 || humidity > 100) {
            throw std::out_of_range("Humidity must be between 0 and 100 percent.");
        }

        // Calculate performance based on outside temperature and humidity
        double coolingPerformance = calculateCoolingPerformance(outsideTemperature, humidity);
        double heatingPerformance = calculateHeatingPerformance(outsideTemperature, humidity);

        // Output the results
        std::cout << std::fixed << std::setprecision(2);
        std::cout << "Outside Temperature: " << outsideTemperature << " °C\n";
        std::cout << "Humidity: " << humidity << " %\n";
        std::cout << "Cooling Performance: " << coolingPerformance << " kW\n";
        std::cout << "Heating Performance: " << heatingPerformance << " kW\n";
    }

private:
    double coolingCapacity; // Cooling capacity in kW
    double heatingCapacity; // Heating capacity in kW

    // Private method to calculate cooling performance
    double calculateCoolingPerformance(double outsideTemperature, double humidity) {
        // Simplified model: performance decreases with higher outside temperature
        return coolingCapacity * (1 - (outsideTemperature - 20) * 0.02) * (1 - humidity * 0.01);
    }

    // Private method to calculate heating performance
    double calculateHeatingPerformance(double outsideTemperature, double humidity) {
        // Simplified model: performance decreases with lower outside temperature
        return heatingCapacity * (1 - (20 - outsideTemperature) * 0.02) * (1 - humidity * 0.01);
    }
};

int main() {
    try {
        // Create an instance of the Gree ducted split system with specified capacities
        GreeDuctedSplitSystem greeSystem(10.0, 12.0); // Cooling: 10 kW, Heating: 12 kW

        // Simulate performance under various conditions
        std::vector<std::pair<double, double>> testConditions = {
            {30.0, 60.0}, // Hot and humid
            {15.0, 40.0}, // Mild and dry
            {5.0, 80.0},  // Cold and humid
            {-5.0, 20.0}, // Very cold and dry
            {45.0, 50.0}  // Extreme hot and humid
        };

        for (const auto& condition : testConditions) {
            greeSystem.simulatePerformance(condition.first, condition.second);
            std::cout << "-----------------------------------\n";
        }
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return EXIT_FAILURE;
    }

    return EXIT_SUCCESS;
}
```
