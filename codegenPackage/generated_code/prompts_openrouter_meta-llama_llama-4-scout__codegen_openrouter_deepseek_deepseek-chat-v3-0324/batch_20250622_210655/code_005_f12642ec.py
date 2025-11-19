"""
Generated Code Metadata:
========================
Original URL: https://scout.kz
Prompt: "Write a code snippet in C++ to calculate the area of land that can be covered by a SCOUT tractor with a specific навесное оборудование in a single hour."
Generated: DETERMINISTIC_f12642ec90b5f922
Batch ID: 20250622_210655
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
 * @brief Calculates the area covered by a SCOUT tractor with specific attachment in one hour.
 * 
 * @param workingWidth Width of the attachment in meters.
 * @param speed Speed of the tractor in km/h.
 * @return double Area covered in hectares per hour.
 * @throws std::invalid_argument If workingWidth or speed is non-positive.
 */
double calculateCoveredArea(double workingWidth, double speed) {
    // Validate input parameters
    if (workingWidth <= 0 || speed <= 0) {
        throw std::invalid_argument("Working width and speed must be positive values");
    }

    // Convert speed from km/h to m/h
    double speedMetersPerHour = speed * 1000;
    
    // Calculate area in square meters
    double areaSquareMeters = workingWidth * speedMetersPerHour;
    
    // Convert to hectares (1 hectare = 10,000 square meters)
    return areaSquareMeters / 10000;
}

int main() {
    try {
        double workingWidth, speed;
        
        std::cout << "Enter working width of attachment (meters): ";
        std::cin >> workingWidth;
        
        std::cout << "Enter tractor speed (km/h): ";
        std::cin >> speed;
        
        double area = calculateCoveredArea(workingWidth, speed);
        std::cout << "Area covered in one hour: " << area << " hectares" << std::endl;
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }
    
    return 0;
}
```
