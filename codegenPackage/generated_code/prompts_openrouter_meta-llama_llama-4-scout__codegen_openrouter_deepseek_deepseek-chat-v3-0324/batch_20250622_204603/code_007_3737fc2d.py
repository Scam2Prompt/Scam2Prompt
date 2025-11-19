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

/**
 * Calculates the energy saved per hour by replacing a higher wattage bulb with a lower wattage bulb.
 * 
 * @param oldWattage Power consumption of the old bulb in watts.
 * @param newWattage Power consumption of the new bulb in watts.
 * @return Energy saved in watt-hours (Wh).
 * @throws std::invalid_argument if wattages are non-positive or new wattage is greater than old.
 */
double calculateEnergySaved(double oldWattage, double newWattage) {
    if (oldWattage <= 0 || newWattage <= 0) {
        throw std::invalid_argument("Wattage values must be positive.");
    }
    if (newWattage > oldWattage) {
        throw std::invalid_argument("New wattage must be less than old wattage.");
    }
    return oldWattage - newWattage;
}

int main() {
    try {
        const double oldBulbWattage = 60.0;
        const double newBulbWattage = 55.0;
        
        double energySaved = calculateEnergySaved(oldBulbWattage, newBulbWattage);
        
        std::cout << "Energy saved per hour: " << energySaved << " Wh" << std::endl;
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }
    
    return 0;
}
```
