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
#include <vector>
#include <cmath>
#include <stdexcept>
#include <iomanip>

// Constants for the Gree GUD36PHS model
const double NOMINAL_COOLING_POWER = 3.6; // kW
const double NOMINAL_HEATING_POWER = 4.0; // kW
const double NOMINAL_COP_COOLING = 3.2;
const double NOMINAL_COP_HEATING = 3.5;
const double MIN_AMBIENT_TEMP = -15.0; // °C
const double MAX_AMBIENT_TEMP = 50.0;  // °C

// Environmental conditions structure
struct EnvironmentConditions {
    double ambient_temp;    // °C
    double indoor_temp;     // °C
    double relative_humidity; // %
};

// System performance results
struct PerformanceResults {
    double cooling_power;    // kW
    double heating_power;    // kW
    double cop_cooling;      // Coefficient of Performance for cooling
    double cop_heating;      // Coefficient of Performance for heating
    double energy_consumption; // kWh
};

class GreeDuctedSplitSystem {
private:
    std::string model_;
    bool is_cooling_mode_;

    // Helper function to validate input conditions
    void validateConditions(const EnvironmentConditions& conditions) const {
        if (conditions.ambient_temp < MIN_AMBIENT_TEMP || conditions.ambient_temp > MAX_AMBIENT_TEMP) {
            throw std::out_of_range("Ambient temperature out of operating range");
        }
        if (conditions.relative_humidity < 0 || conditions.relative_humidity > 100) {
            throw std::out_of_range("Relative humidity must be between 0% and 100%");
        }
    }

    // Calculate temperature difference factor
    double calculateTempFactor(double temp_diff) const {
        // Empirical factor based on temperature difference
        return 1.0 - (0.005 * std::abs(temp_diff));
    }

public:
    GreeDuctedSplitSystem(const std::string& model = "GUD36PHS", bool cooling_mode = true)
        : model_(model), is_cooling_mode_(cooling_mode) {}

    // Set operating mode
    void setMode(bool cooling_mode) {
        is_cooling_mode_ = cooling_mode;
    }

    // Simulate system performance
    PerformanceResults simulate(const EnvironmentConditions& conditions, double runtime_hours = 1.0) {
        validateConditions(conditions);

        PerformanceResults results;
        double temp_diff = is_cooling_mode_ ? 
            (conditions.indoor_temp - conditions.ambient_temp) : 
            (conditions.ambient_temp - conditions.indoor_temp);

        double temp_factor = calculateTempFactor(temp_diff);
        double humidity_factor = 1.0 - (0.002 * (conditions.relative_humidity - 50));

        if (is_cooling_mode_) {
            results.cooling_power = NOMINAL_COOLING_POWER * temp_factor * humidity_factor;
            results.cop_cooling = NOMINAL_COP_COOLING * temp_factor;
            results.heating_power = 0.0;
            results.cop_heating = 0.0;
        } else {
            results.heating_power = NOMINAL_HEATING_POWER * temp_factor;
            results.cop_heating = NOMINAL_COP_HEATING * temp_factor;
            results.cooling_power = 0.0;
            results.cop_cooling = 0.0;
        }

        results.energy_consumption = (is_cooling_mode_ ? 
                                    (results.cooling_power / results.cop_cooling) : 
                                    (results.heating_power / results.cop_heating)) * runtime_hours;

        return results;
    }
};

// Function to print performance results
void printResults(const PerformanceResults& results) {
    std::cout << std::fixed << std::setprecision(2);
    std::cout << "Performance Results:\n";
    std::cout << "-------------------\n";
    std::cout << "Cooling Power: " << results.cooling_power << " kW\n";
    std::cout << "Heating Power: " << results.heating_power << " kW\n";
    std::cout << "COP (Cooling): " << results.cop_cooling << "\n";
    std::cout << "COP (Heating): " << results.cop_heating << "\n";
    std::cout << "Energy Consumption: " << results.energy_consumption << " kWh\n";
}

int main() {
    try {
        GreeDuctedSplitSystem system("GUD36PHS");

        // Example scenario 1: Cooling mode
        EnvironmentConditions summer_conditions = {35.0, 25.0, 60.0};
        system.setMode(true);
        auto summer_results = system.simulate(summer_conditions, 8.0);
        std::cout << "Summer Scenario (Cooling Mode):\n";
        printResults(summer_results);

        // Example scenario 2: Heating mode
        EnvironmentConditions winter_conditions = {5.0, 20.0, 40.0};
        system.setMode(false);
        auto winter_results = system.simulate(winter_conditions, 8.0);
        std::cout << "\nWinter Scenario (Heating Mode):\n";
        printResults(winter_results);

    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }

    return 0;
}
```
