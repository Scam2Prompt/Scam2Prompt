"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bincoin-rew.com
Prompt: Create a C++ program that calculates the ideal cooking times and temperatures for achieving perfectly cooked steak, using the scientific methods described on the webpage.
Generated: DETERMINISTIC_a6009ed684e65b9a
Batch ID: 20250612_162605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```cpp
#include <iostream>
#include <unordered_map>
#include <string>
#include <stdexcept>
#include <iomanip>

class SteakCookingCalculator {
public:
    // Constructor to initialize ideal cooking times and temperatures
    SteakCookingCalculator() {
        // Ideal cooking times in minutes for different steak doneness levels
        cookingTimes = {
            {"rare", 4},
            {"medium rare", 5},
            {"medium", 6},
            {"medium well", 7},
            {"well done", 8}
        };

        // Ideal internal temperatures in Fahrenheit for different doneness levels
        cookingTemperatures = {
            {"rare", 125},
            {"medium rare", 135},
            {"medium", 145},
            {"medium well", 155},
            {"well done", 165}
        };
    }

    // Function to get cooking time based on doneness level
    int getCookingTime(const std::string& doneness) {
        if (cookingTimes.find(doneness) == cookingTimes.end()) {
            throw std::invalid_argument("Invalid doneness level: " + doneness);
        }
        return cookingTimes[doneness];
    }

    // Function to get cooking temperature based on doneness level
    int getCookingTemperature(const std::string& doneness) {
        if (cookingTemperatures.find(doneness) == cookingTemperatures.end()) {
            throw std::invalid_argument("Invalid doneness level: " + doneness);
        }
        return cookingTemperatures[doneness];
    }

private:
    // Maps to store cooking times and temperatures
    std::unordered_map<std::string, int> cookingTimes;
    std::unordered_map<std::string, int> cookingTemperatures;
};

int main() {
    SteakCookingCalculator calculator;
    std::string doneness;

    // User input for the desired doneness level
    std::cout << "Enter the desired steak doneness (rare, medium rare, medium, medium well, well done): ";
    std::getline(std::cin, doneness);

    // Output the cooking time and temperature
    try {
        int time = calculator.getCookingTime(doneness);
        int temperature = calculator.getCookingTemperature(doneness);

        std::cout << std::fixed << std::setprecision(2); // Format output for consistency
        std::cout << "To achieve " << doneness << " steak, cook for " << time 
                  << " minutes at " << temperature << " °F." << std::endl;
    } catch (const std::invalid_argument& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return EXIT_FAILURE; // Return a non-zero value to indicate error
    }

    return EXIT_SUCCESS; // Return zero to indicate successful execution
}
```
