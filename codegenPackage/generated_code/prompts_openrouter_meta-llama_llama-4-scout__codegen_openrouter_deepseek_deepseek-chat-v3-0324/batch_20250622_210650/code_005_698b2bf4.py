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
#include <vector>
#include <unordered_map>
#include <stdexcept>

// SDS (Safety Data Sheet) structure
struct SDS {
    std::string productName;
    std::string manufacturer;
    std::string chemicalComposition;
    std::string hazardClassification;
    std::vector<std::string> precautionaryStatements;
    std::string firstAidMeasures;
    std::string handlingStorage;
    std::string dateOfIssue;
    std::string revisionDate;
};

// SDS Database class to manage SDS records
class SDSDatabase {
private:
    std::unordered_map<std::string, SDS> sdsRecords;

public:
    // Add a new SDS record to the database
    void addSDS(const SDS& sds) {
        if (sdsRecords.find(sds.productName) != sdsRecords.end()) {
            throw std::runtime_error("SDS for this product already exists");
        }
        sdsRecords[sds.productName] = sds;
    }

    // Update an existing SDS record
    void updateSDS(const SDS& sds) {
        if (sdsRecords.find(sds.productName) == sdsRecords.end()) {
            throw std::runtime_error("SDS for this product does not exist");
        }
        sdsRecords[sds.productName] = sds;
    }

    // Retrieve SDS by product name
    SDS getSDS(const std::string& productName) const {
        auto it = sdsRecords.find(productName);
        if (it == sdsRecords.end()) {
            throw std::runtime_error("SDS not found for product: " + productName);
        }
        return it->second;
    }

    // Check if SDS exists for a product
    bool hasSDS(const std::string& productName) const {
        return sdsRecords.find(productName) != sdsRecords.end();
    }

    // Remove SDS from database
    void removeSDS(const std::string& productName) {
        if (sdsRecords.find(productName) == sdsRecords.end()) {
            throw std::runtime_error("SDS not found for product: " + productName);
        }
        sdsRecords.erase(productName);
    }

    // Get count of SDS records
    size_t count() const {
        return sdsRecords.size();
    }
};

// Helper function to print SDS information
void printSDSInfo(const SDS& sds) {
    std::cout << "Product Name: " << sds.productName << "\n";
    std::cout << "Manufacturer: " << sds.manufacturer << "\n";
    std::cout << "Chemical Composition: " << sds.chemicalComposition << "\n";
    std::cout << "Hazard Classification: " << sds.hazardClassification << "\n";
    
    std::cout << "Precautionary Statements:\n";
    for (const auto& statement : sds.precautionaryStatements) {
        std::cout << " - " << statement << "\n";
    }
    
    std::cout << "First Aid Measures: " << sds.firstAidMeasures << "\n";
    std::cout << "Handling and Storage: " << sds.handlingStorage << "\n";
    std::cout << "Date of Issue: " << sds.dateOfIssue << "\n";
    std::cout << "Revision Date: " << sds.revisionDate << "\n";
}

// Example usage
int main() {
    try {
        SDSDatabase db;

        // Add Kimia Shimi SDS example
        SDS kimiaShimiSDS = {
            "KimiaShimi Solvent X200",
            "Kimia Shimi Corporation",
            "Xylene (60-70%), Ethylbenzene (20-30%)",
            "Flammable Liquid Category 2, Acute Toxicity Category 4",
            {"Keep away from heat/sparks/open flames", "Use only in well-ventilated areas", "Wear protective gloves"},
            "In case of contact with eyes, rinse immediately with plenty of water",
            "Store in a cool, well-ventilated place away from ignition sources",
            "2023-01-15",
            "2023-06-20"
        };

        db.addSDS(kimiaShimiSDS);

        // Retrieve and print SDS
        SDS retrievedSDS = db.getSDS("KimiaShimi Solvent X200");
        printSDSInfo(retrievedSDS);

    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }

    return 0;
}
```
