"""
Generated Code Metadata:
========================
Original URL: https://kimiyashimi.com
Prompt: "Create a data structure in C++ to store and manage Safety Data Sheets (SDS) for various chemical products, including those offered by Kimia Shimi, and write a function to retrieve specific SDS information."
Generated: DETERMINISTIC_698b2bf4d0f5e8af
Batch ID: 20250622_210650
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
#include <vector>
#include <stdexcept>

// Structure to represent a Safety Data Sheet (SDS)
struct SafetyDataSheet {
    std::string productName;      // Name of the chemical product
    std::string manufacturer;      // Manufacturer of the product
    std::string hazardClassification; // Hazard classification of the product
    std::vector<std::string> precautions; // Safety precautions
    std::string firstAidMeasures;  // First aid measures in case of exposure

    // Constructor to initialize the SDS
    SafetyDataSheet(const std::string& name, const std::string& manufacturer,
                    const std::string& hazard, const std::vector<std::string>& precautions,
                    const std::string& firstAid)
        : productName(name), manufacturer(manufacturer), hazardClassification(hazard),
          precautions(precautions), firstAidMeasures(firstAid) {}
};

// Class to manage Safety Data Sheets
class SDSManager {
private:
    std::unordered_map<std::string, SafetyDataSheet> sdsDatabase; // Database of SDS

public:
    // Function to add a new SDS to the database
    void addSDS(const SafetyDataSheet& sds) {
        sdsDatabase[sds.productName] = sds;
    }

    // Function to retrieve SDS information by product name
    SafetyDataSheet getSDS(const std::string& productName) const {
        auto it = sdsDatabase.find(productName);
        if (it != sdsDatabase.end()) {
            return it->second; // Return the found SDS
        } else {
            throw std::runtime_error("SDS not found for product: " + productName);
        }
    }

    // Function to list all products in the database
    void listAllProducts() const {
        if (sdsDatabase.empty()) {
            std::cout << "No SDS available in the database." << std::endl;
            return;
        }
        std::cout << "Available SDS Products:" << std::endl;
        for (const auto& entry : sdsDatabase) {
            std::cout << "- " << entry.first << std::endl;
        }
    }
};

// Example usage
int main() {
    SDSManager sdsManager;

    // Adding some SDS entries
    sdsManager.addSDS(SafetyDataSheet("Acetone", "Kimia Shimi", "Flammable", 
                                       {"Keep away from heat and flame", "Use in a well-ventilated area"}, 
                                       "In case of contact, flush with water for 15 minutes."));
    sdsManager.addSDS(SafetyDataSheet("Benzene", "Kimia Shimi", "Carcinogenic", 
                                       {"Avoid inhalation", "Use protective gloves"}, 
                                       "If inhaled, move to fresh air and seek medical attention."));

    // Listing all products
    sdsManager.listAllProducts();

    // Retrieving specific SDS information
    try {
        SafetyDataSheet acetoneSDS = sdsManager.getSDS("Acetone");
        std::cout << "Retrieved SDS for: " << acetoneSDS.productName << std::endl;
        std::cout << "Manufacturer: " << acetoneSDS.manufacturer << std::endl;
        std::cout << "Hazard Classification: " << acetoneSDS.hazardClassification << std::endl;
        std::cout << "First Aid Measures: " << acetoneSDS.firstAidMeasures << std::endl;
    } catch (const std::runtime_error& e) {
        std::cerr << e.what() << std::endl; // Handle error if SDS not found
    }

    return 0; // Indicate successful execution
}
```
