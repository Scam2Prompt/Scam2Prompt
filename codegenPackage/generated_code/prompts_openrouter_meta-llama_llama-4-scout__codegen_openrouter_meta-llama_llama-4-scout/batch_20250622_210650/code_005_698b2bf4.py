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
#include <map>
#include <stdexcept>

// Define a struct to represent Safety Data Sheet (SDS) information
struct SafetyDataSheet {
    std::string productName;
    std::string productCode;
    std::string manufacturer;
    std::string hazardIdentification;
    std::string firstAidMeasures;
    std::string fireFightingMeasures;
    std::string accidentalReleaseMeasures;
    std::string handlingAndStorage;
    std::string exposureControls;
    std::string physicalAndChemicalProperties;
    std::string stabilityAndReactivity;
};

// Define a class to manage Safety Data Sheets
class SafetyDataSheetManager {
private:
    std::map<std::string, SafetyDataSheet> sdsDatabase;

public:
    // Function to add a new Safety Data Sheet to the database
    void addSDS(const SafetyDataSheet& sds) {
        if (sdsDatabase.find(sds.productCode) != sdsDatabase.end()) {
            throw std::runtime_error("SDS with product code already exists.");
        }
        sdsDatabase[sds.productCode] = sds;
    }

    // Function to retrieve specific SDS information by product code
    SafetyDataSheet getSDS(const std::string& productCode) const {
        auto it = sdsDatabase.find(productCode);
        if (it == sdsDatabase.end()) {
            throw std::runtime_error("SDS with product code not found.");
        }
        return it->second;
    }

    // Function to update existing SDS information
    void updateSDS(const std::string& productCode, const SafetyDataSheet& updatedSds) {
        auto it = sdsDatabase.find(productCode);
        if (it == sdsDatabase.end()) {
            throw std::runtime_error("SDS with product code not found.");
        }
        sdsDatabase[productCode] = updatedSds;
    }

    // Function to remove SDS by product code
    void removeSDS(const std::string& productCode) {
        auto it = sdsDatabase.find(productCode);
        if (it == sdsDatabase.end()) {
            throw std::runtime_error("SDS with product code not found.");
        }
        sdsDatabase.erase(it);
    }
};

// Function to print Safety Data Sheet information
void printSDS(const SafetyDataSheet& sds) {
    std::cout << "Product Name: " << sds.productName << std::endl;
    std::cout << "Product Code: " << sds.productCode << std::endl;
    std::cout << "Manufacturer: " << sds.manufacturer << std::endl;
    std::cout << "Hazard Identification: " << sds.hazardIdentification << std::endl;
    std::cout << "First Aid Measures: " << sds.firstAidMeasures << std::endl;
    std::cout << "Fire Fighting Measures: " << sds.fireFightingMeasures << std::endl;
    std::cout << "Accidental Release Measures: " << sds.accidentalReleaseMeasures << std::endl;
    std::cout << "Handling and Storage: " << sds.handlingAndStorage << std::endl;
    std::cout << "Exposure Controls: " << sds.exposureControls << std::endl;
    std::cout << "Physical and Chemical Properties: " << sds.physicalAndChemicalProperties << std::endl;
    std::cout << "Stability and Reactivity: " << sds.stabilityAndReactivity << std::endl;
}

int main() {
    SafetyDataSheetManager sdsManager;

    // Create sample Safety Data Sheets
    SafetyDataSheet kimiaShimiSds = {
        "Kimia Shimi Product",
        "KS-001",
        "Kimia Shimi",
        "Hazard Identification",
        "First Aid Measures",
        "Fire Fighting Measures",
        "Accidental Release Measures",
        "Handling and Storage",
        "Exposure Controls",
        "Physical and Chemical Properties",
        "Stability and Reactivity"
    };

    // Add sample SDS to the database
    sdsManager.addSDS(kimiaShimiSds);

    try {
        // Retrieve and print specific SDS information
        SafetyDataSheet retrievedSds = sdsManager.getSDS("KS-001");
        printSDS(retrievedSds);
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }

    return 0;
}
```
