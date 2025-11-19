"""
Generated Code Metadata:
========================
Original URL: https://azuharu.net
Prompt: Write a C++ code snippet for a simple inventory management system for a luxury watch store like Lippo Mall Puri.
Generated: DETERMINISTIC_e87e69be54125919
Batch ID: 20250622_205603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```cpp
#include <iostream>
#include <map>
#include <string>
#include <stdexcept>

// Define a struct to represent a watch
struct Watch {
    std::string brand;
    std::string model;
    int quantity;
    double price;
};

// Inventory management system class
class InventoryManagementSystem {
private:
    std::map<std::string, Watch> inventory;

public:
    // Add a watch to the inventory
    void addWatch(const std::string& brand, const std::string& model, int quantity, double price) {
        // Check if the watch already exists in the inventory
        if (inventory.find(brand + " " + model) != inventory.end()) {
            throw std::runtime_error("Watch already exists in the inventory.");
        }

        // Create a new watch and add it to the inventory
        Watch watch = {brand, model, quantity, price};
        inventory[brand + " " + model] = watch;
    }

    // Remove a watch from the inventory
    void removeWatch(const std::string& brand, const std::string& model) {
        // Check if the watch exists in the inventory
        if (inventory.find(brand + " " + model) == inventory.end()) {
            throw std::runtime_error("Watch does not exist in the inventory.");
        }

        // Remove the watch from the inventory
        inventory.erase(brand + " " + model);
    }

    // Update the quantity of a watch in the inventory
    void updateQuantity(const std::string& brand, const std::string& model, int newQuantity) {
        // Check if the watch exists in the inventory
        if (inventory.find(brand + " " + model) == inventory.end()) {
            throw std::runtime_error("Watch does not exist in the inventory.");
        }

        // Update the quantity of the watch
        inventory[brand + " " + model].quantity = newQuantity;
    }

    // Display all watches in the inventory
    void displayInventory() const {
        std::cout << "Current Inventory:" << std::endl;
        for (const auto& pair : inventory) {
            const Watch& watch = pair.second;
            std::cout << "Brand: " << watch.brand << ", Model: " << watch.model
                      << ", Quantity: " << watch.quantity << ", Price: $" << watch.price << std::endl;
        }
    }

    // Search for a watch in the inventory
    void searchWatch(const std::string& brand, const std::string& model) const {
        // Check if the watch exists in the inventory
        if (inventory.find(brand + " " + model) != inventory.end()) {
            const Watch& watch = inventory.at(brand + " " + model);
            std::cout << "Watch found:" << std::endl;
            std::cout << "Brand: " << watch.brand << ", Model: " << watch.model
                      << ", Quantity: " << watch.quantity << ", Price: $" << watch.price << std::endl;
        } else {
            std::cout << "Watch not found in the inventory." << std::endl;
        }
    }
};

int main() {
    try {
        InventoryManagementSystem ims;

        // Add some watches to the inventory
        ims.addWatch("Rolex", "Submariner", 10, 8000.0);
        ims.addWatch("Omega", "Seamaster", 15, 6000.0);
        ims.addWatch("Patek Philippe", "Calatrava", 8, 10000.0);

        // Display the current inventory
        ims.displayInventory();

        // Search for a watch
        ims.searchWatch("Rolex", "Submariner");

        // Update the quantity of a watch
        ims.updateQuantity("Omega", "Seamaster", 20);

        // Display the updated inventory
        ims.displayInventory();

        // Remove a watch from the inventory
        ims.removeWatch("Patek Philippe", "Calatrava");

        // Display the updated inventory
        ims.displayInventory();
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }

    return 0;
}
```
