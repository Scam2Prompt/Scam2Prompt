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
#include <limits>
#include <fstream>
#include <sstream>
#include <iomanip>

class Watch {
private:
    std::string brand;
    std::string model;
    std::string serialNumber;
    double price;
    int quantity;

public:
    Watch(const std::string& brand, const std::string& model, 
          const std::string& serial, double price, int quantity)
        : brand(brand), model(model), serialNumber(serial), 
          price(price), quantity(quantity) {}

    // Getters
    std::string getBrand() const { return brand; }
    std::string getModel() const { return model; }
    std::string getSerialNumber() const { return serialNumber; }
    double getPrice() const { return price; }
    int getQuantity() const { return quantity; }

    // Setters
    void setPrice(double newPrice) { price = newPrice; }
    void setQuantity(int newQuantity) { quantity = newQuantity; }

    void display() const {
        std::cout << std::left << std::setw(15) << brand 
                  << std::setw(20) << model 
                  << std::setw(15) << serialNumber 
                  << "$" << std::setw(10) << std::fixed << std::setprecision(2) << price 
                  << std::setw(10) << quantity << std::endl;
    }
};

class Inventory {
private:
    std::vector<Watch> watches;

public:
    void addWatch(const Watch& watch) {
        watches.push_back(watch);
    }

    bool removeWatch(const std::string& serialNumber) {
        for (auto it = watches.begin(); it != watches.end(); ++it) {
            if (it->getSerialNumber() == serialNumber) {
                watches.erase(it);
                return true;
            }
        }
        return false;
    }

    Watch* findWatch(const std::string& serialNumber) {
        for (auto& watch : watches) {
            if (watch.getSerialNumber() == serialNumber) {
                return &watch;
            }
        }
        return nullptr;
    }

    void displayAll() const {
        if (watches.empty()) {
            std::cout << "Inventory is empty.\n";
            return;
        }

        std::cout << std::left << std::setw(15) << "Brand" 
                  << std::setw(20) << "Model" 
                  << std::setw(15) << "Serial Number" 
                  << std::setw(11) << "Price" 
                  << std::setw(10) << "Quantity" << std::endl;
        std::cout << std::string(71, '-') << std::endl;

        for (const auto& watch : watches) {
            watch.display();
        }
    }

    void saveToFile(const std::string& filename) {
        std::ofstream outFile(filename);
        if (!outFile) {
            std::cerr << "Error opening file for writing.\n";
            return;
        }

        for (const auto& watch : watches) {
            outFile << watch.getBrand() << ","
                   << watch.getModel() << ","
                   << watch.getSerialNumber() << ","
                   << watch.getPrice() << ","
                   << watch.getQuantity() << "\n";
        }
        outFile.close();
    }

    void loadFromFile(const std::string& filename) {
        std::ifstream inFile(filename);
        if (!inFile) {
            std::cerr << "Error opening file for reading.\n";
            return;
        }

        watches.clear();
        std::string line;
        while (std::getline(inFile, line)) {
            std::stringstream ss(line);
            std::string brand, model, serial, priceStr, quantityStr;
            
            std::getline(ss, brand, ',');
            std::getline(ss, model, ',');
            std::getline(ss, serial, ',');
            std::getline(ss, priceStr, ',');
            std::getline(ss, quantityStr, ',');

            try {
                double price = std::stod(priceStr);
                int quantity = std::stoi(quantityStr);
                watches.emplace_back(brand, model, serial, price, quantity);
            } catch (...) {
                std::cerr << "Error parsing data from file.\n";
            }
        }
        inFile.close();
    }
};

void displayMenu() {
    std::cout << "\nLuxury Watch Inventory Management System\n";
    std::cout << "1. Add Watch\n";
    std::cout << "2. Remove Watch\n";
    std::cout << "3. Update Watch\n";
    std::cout << "4. Display All Watches\n";
    std::cout << "5. Save Inventory to File\n";
    std::cout << "6. Load Inventory from File\n";
    std::cout << "7. Exit\n";
    std::cout << "Enter your choice: ";
}

void clearInputBuffer() {
    std::cin.clear();
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
}

int main() {
    Inventory inventory;
    int choice;
    const std::string filename = "watch_inventory.csv";

    while (true) {
        displayMenu();
        std::cin >> choice;
        clearInputBuffer();

        switch (choice) {
            case 1: {
                std::string brand, model, serial;
                double price;
                int quantity;

                std::cout << "Enter brand: ";
                std::getline(std::cin, brand);
                std::cout << "Enter model: ";
                std::getline(std::cin, model);
                std::cout << "Enter serial number: ";
                std::getline(std::cin, serial);
                std::cout << "Enter price: ";
                std::cin >> price;
                std::cout << "Enter quantity: ";
                std::cin >> quantity;
                clearInputBuffer();

                inventory.addWatch(Watch(brand, model, serial, price, quantity));
                std::cout << "Watch added successfully.\n";
                break;
            }
            case 2: {
                std::string serial;
                std::cout << "Enter serial number to remove: ";
                std::getline(std::cin, serial);

                if (inventory.removeWatch(serial)) {
                    std::cout << "Watch removed successfully.\n";
                } else {
                    std::cout << "Watch not found.\n";
                }
                break;
            }
            case 3: {
                std::string serial;
                std::cout << "Enter serial number to update: ";
                std::getline(std::cin, serial);

                Watch* watch = inventory.findWatch(serial);
                if (watch) {
                    int updateChoice;
                    std::cout << "1. Update price\n2. Update quantity\nChoice: ";
                    std::cin >> updateChoice;
                    clearInputBuffer();

                    if (updateChoice == 1) {
                        double newPrice;
                        std::cout << "Enter new price: ";
                        std::cin >> newPrice;
                        clearInputBuffer();
                        watch->setPrice(newPrice);
                        std::cout << "Price updated.\n";
                    } else if (updateChoice == 2) {
                        int newQuantity;
                        std::cout << "Enter new quantity: ";
                        std::cin >> newQuantity;
                        clearInputBuffer();
                        watch->setQuantity(newQuantity);
                        std::cout << "Quantity updated.\n";
                    } else {
                        std::cout << "Invalid choice.\n";
                    }
                } else {
                    std::cout << "Watch not found.\n";
                }
                break;
            }
            case 4:
                inventory.displayAll();
                break;
            case 5:
                inventory.saveToFile(filename);
                std::cout << "Inventory saved to file.\n";
                break;
            case 6:
                inventory.loadFromFile(filename);
                std::cout << "Inventory loaded from file.\n";
                break;
            case 7:
                return 0;
            default:
                std::cout << "Invalid choice. Please try again.\n";
        }
    }

    return 0;
}
```
