"""
Generated Code Metadata:
========================
Original URL: https://bincoin-rew.com
Prompt: Create a C++ program that calculates the ideal cooking times and temperatures for achieving perfectly cooked steak, using the scientific methods described on the webpage.
Generated: DETERMINISTIC_a6009ed684e65b9a
Batch ID: 20250612_162605
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
#include <map>
#include <stdexcept>
#include <iomanip>

// Enum for steak doneness levels
enum class Doneness {
    RARE,
    MEDIUM_RARE,
    MEDIUM,
    MEDIUM_WELL,
    WELL_DONE
};

// Struct to hold cooking parameters for each doneness level
struct CookingParams {
    double coreTemp;   // Core temperature in Celsius
    double timePerSide; // Cooking time per side in minutes
};

// Class to handle steak cooking calculations
class SteakCooker {
private:
    std::map<Doneness, CookingParams> donenessParams;
    double thickness; // Steak thickness in centimeters

    // Initialize cooking parameters based on scientific methods
    void initializeParams() {
        donenessParams[Doneness::RARE] = {52.0, 2.0};
        donenessParams[Doneness::MEDIUM_RARE] = {55.0, 2.5};
        donenessParams[Doneness::MEDIUM] = {60.0, 3.0};
        donenessParams[Doneness::MEDIUM_WELL] = {65.0, 3.5};
        donenessParams[Doneness::WELL_DONE] = {70.0, 4.0};
    }

public:
    // Constructor with thickness validation
    SteakCooker(double thickness) : thickness(thickness) {
        if (thickness <= 0) {
            throw std::invalid_argument("Steak thickness must be positive");
        }
        initializeParams();
    }

    // Get cooking parameters for specified doneness
    CookingParams getCookingParams(Doneness doneness) const {
        auto it = donenessParams.find(doneness);
        if (it == donenessParams.end()) {
            throw std::invalid_argument("Invalid doneness level");
        }

        CookingParams params = it->second;
        // Adjust time based on thickness (linear approximation)
        params.timePerSide *= (thickness / 2.5); // 2.5cm is reference thickness
        return params;
    }

    // Convert doneness enum to string
    static std::string donenessToString(Doneness doneness) {
        switch (doneness) {
            case Doneness::RARE: return "Rare";
            case Doneness::MEDIUM_RARE: return "Medium Rare";
            case Doneness::MEDIUM: return "Medium";
            case Doneness::MEDIUM_WELL: return "Medium Well";
            case Doneness::WELL_DONE: return "Well Done";
            default: return "Unknown";
        }
    }
};

// Function to display cooking instructions
void displayInstructions(const CookingParams& params, Doneness doneness, double thickness) {
    std::cout << "\n=== Cooking Instructions ===" << std::endl;
    std::cout << "For a " << std::fixed << std::setprecision(1) << thickness 
              << "cm thick steak (" << SteakCooker::donenessToString(doneness) << "):" << std::endl;
    std::cout << "- Target core temperature: " << params.coreTemp << "°C" << std::endl;
    std::cout << "- Cook each side for: " << params.timePerSide << " minutes" << std::endl;
    std::cout << "- Rest for 5 minutes before serving" << std::endl;
}

// Function to get doneness level from user input
Doneness getDonenessFromUser() {
    std::cout << "\nSelect doneness level:" << std::endl;
    std::cout << "1. Rare" << std::endl;
    std::cout << "2. Medium Rare" << std::endl;
    std::cout << "3. Medium" << std::endl;
    std::cout << "4. Medium Well" << std::endl;
    std::cout << "5. Well Done" << std::endl;

    int choice;
    while (true) {
        std::cout << "Enter your choice (1-5): ";
        std::cin >> choice;

        if (std::cin.fail() || choice < 1 || choice > 5) {
            std::cin.clear();
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            std::cout << "Invalid input. Please enter a number between 1 and 5." << std::endl;
        } else {
            break;
        }
    }

    return static_cast<Doneness>(choice - 1);
}

// Function to get steak thickness from user input
double getThicknessFromUser() {
    double thickness;
    while (true) {
        std::cout << "\nEnter steak thickness in centimeters: ";
        std::cin >> thickness;

        if (std::cin.fail() || thickness <= 0) {
            std::cin.clear();
            std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            std::cout << "Invalid input. Please enter a positive number." << std::endl;
        } else {
            break;
        }
    }
    return thickness;
}

int main() {
    try {
        std::cout << "=== Perfect Steak Calculator ===" << std::endl;

        double thickness = getThicknessFromUser();
        Doneness doneness = getDonenessFromUser();

        SteakCooker cooker(thickness);
        CookingParams params = cooker.getCookingParams(doneness);

        displayInstructions(params, doneness, thickness);

    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }

    return 0;
}
```
