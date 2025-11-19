"""
Generated Code Metadata:
========================
Original URL: https://linkevent.net
Prompt: Write a code snippet in C++ to calculate the energy saved per hour by replacing a 60W light bulb with a 55W light bulb.
Generated: DETERMINISTIC_3737fc2d21fea62b
Batch ID: 20250622_204603
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

class LightBulbEnergySaver {
public:
    // Constructor to initialize wattage values
    LightBulbEnergySaver(double oldWattage, double newWattage)
        : oldWattage(oldWattage), newWattage(newWattage) {
        if (oldWattage <= 0 || newWattage <= 0) {
            throw std::invalid_argument("Wattage values must be positive.");
        }
    }

    // Method to calculate energy saved per hour in watts
    double calculateEnergySavedPerHour() const {
        return oldWattage - newWattage;
    }

private:
    double oldWattage; // Wattage of the old light bulb
    double newWattage; // Wattage of the new light bulb
};

int main() {
    try {
        // Initialize the wattages for the old and new light bulbs
        LightBulbEnergySaver energySaver(60.0, 55.0);
        
        // Calculate the energy saved per hour
        double energySaved = energySaver.calculateEnergySavedPerHour();
        
        // Output the result
        std::cout << "Energy saved per hour: " << energySaved << " watts" << std::endl;
    } catch (const std::exception& e) {
        // Handle any exceptions that may occur
        std::cerr << "Error: " << e.what() << std::endl;
        return EXIT_FAILURE;
    }

    return EXIT_SUCCESS;
}
```
