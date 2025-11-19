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
#include <vector>
#include <string>
#include <stdexcept>

// Class representing a luxury watch
class Watch {
public:
    Watch(const std::string& name, double price, int quantity)
        : name(name), price(price), quantity(quantity) {
        if (price < 0 || quantity < 0) {
            throw std::invalid_argument("Price and quantity must be non-negative.");
        }
    }

    // Getters for watch properties
    std::string getName() const { return name; }
    double getPrice() const { return price; }
    int getQuantity() const { return quantity; }

    // Method to update the quantity of the watch
    void updateQuantity(int amount) {
        if (quantity + amount < 0) {
            throw std::out_of_range("Insufficient quantity in stock.");
        }
        quantity += amount;
    }

private:
    std::string name; // Name of the watch
    double price;     // Price of the watch
    int quantity;     // Quantity in stock
};

// Class representing the inventory management system
class Inventory {
public:
    // Method to add a watch to the inventory
    void addWatch(const Watch& watch) {
        inventory.push_back(watch);
    }

    // Method to display all watches in the inventory
    void displayInventory() const {
        std::cout << "Inventory:\n";
        for (const auto& watch : inventory) {
            std::cout << "Name: " << watch.getName()
                      << ", Price: $" << watch.getPrice()
                      << ", Quantity: " << watch.getQuantity() << "\n";
        }
    }

    // Method to update the quantity of a specific watch
    void updateWatchQuantity(const std::string& name, int amount) {
        for (auto& watch : inventory) {
            if (watch.getName() == name) {
                watch.updateQuantity(amount);
                return;
            }
        }
        throw std::invalid_argument("Watch not found in inventory.");
    }

private:
    std::vector<Watch> inventory; // Vector to store watches
};

// Main function to demonstrate the inventory management system
int main() {
    try {
        Inventory inventory;

        // Adding watches to the inventory
        inventory.addWatch(Watch("Rolex Submariner", 8500.00, 5));
        inventory.addWatch(Watch("Omega Seamaster", 5000.00, 3));
        inventory.addWatch(Watch("Tag Heuer Carrera", 4000.00, 2));

        // Displaying the current inventory
        inventory.displayInventory();

        // Updating the quantity of a watch
        inventory.updateWatchQuantity("Rolex Submariner", -1); // Sell one watch
        std::cout << "\nAfter selling one Rolex Submariner:\n";
        inventory.displayInventory();

        // Attempting to update a non-existent watch
        inventory.updateWatchQuantity("Nonexistent Watch", 1);
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }

    return 0; // Indicate successful execution
}
```
