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
/**
 * @file scout_tractor_area_calculator.cpp
 * @brief Calculates the area of land that can be covered by a SCOUT tractor
 *        with a specific навесное оборудование in a single hour.
 */

#include <iostream>
#include <stdexcept>

/**
 * @struct TractorAttachment
 * @brief Represents a навесное оборудование (tractor attachment) with its properties.
 */
struct TractorAttachment {
    std::string name;         ///< Name of the attachment
    double workingWidth;      ///< Working width of the attachment in meters
};

/**
 * @class ScoutTractor
 * @brief Represents a SCOUT tractor with its properties and behavior.
 */
class ScoutTractor {
public:
    /**
     * @brief Constructs a ScoutTractor object with a specific attachment.
     * @param attachment The навесное оборудование (tractor attachment) to use.
     * @param speed The speed of the tractor in km/h.
     */
    ScoutTractor(const TractorAttachment& attachment, double speed)
        : attachment_(attachment), speed_(speed) {
        if (speed <= 0) {
            throw std::invalid_argument("Speed must be greater than zero.");
        }
    }

    /**
     * @brief Calculates the area of land that can be covered in a single hour.
     * @return The area in hectares.
     */
    double calculateAreaPerHour() const {
        // Convert speed from km/h to m/h
        const double speedInMetersPerHour = speed_ * 1000;

        // Calculate area in square meters
        const double areaInSquareMeters = speedInMetersPerHour * attachment_.workingWidth;

        // Convert area from square meters to hectares
        const double areaInHectares = areaInSquareMeters / 10000;

        return areaInHectares;
    }

private:
    TractorAttachment attachment_; ///< The навесное оборудование (tractor attachment) in use.
    double speed_;                  ///< The speed of the tractor in km/h.
};

int main() {
    try {
        // Define a tractor attachment
        TractorAttachment attachment = {" Rotary Cultivator", 2.5}; // 2.5 meters working width

        // Create a SCOUT tractor with the attachment and a speed of 5 km/h
        ScoutTractor tractor(attachment, 5.0);

        // Calculate and display the area that can be covered in a single hour
        const double areaPerHour = tractor.calculateAreaPerHour();
        std::cout << "The SCOUT tractor with " << attachment.name << " can cover "
                  << areaPerHour << " hectares in a single hour." << std::endl;

    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1; // Return non-zero exit code to indicate failure
    }

    return 0;
}
```
