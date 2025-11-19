"""
Generated Code Metadata:
========================
Original URL: https://filterwale.com
Prompt: Write a code snippet in C++ to simulate a shopping cart for industrial filters, including Mann Filters, Donaldson Filters, and Wix Filters.
Generated: DETERMINISTIC_ad899f1d8d3d4c59
Batch ID: 20250622_211449
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
#include <map>
#include <stdexcept>
#include <iomanip>

// Enum to represent different filter brands
enum class FilterBrand {
    MANN,
    DONALDSON,
    WIX
};

// Structure to represent a filter item
struct FilterItem {
    FilterBrand brand;
    std::string partNumber;
    std::string description;
    double price;
    int quantity;
};

// Shopping cart class to manage filter items
class ShoppingCart {
private:
    std::vector<FilterItem> items;
    std::map<FilterBrand, std::string> brandNames = {
        {FilterBrand::MANN, "Mann Filters"},
        {FilterBrand::DONALDSON, "Donaldson Filters"},
        {FilterBrand::WIX, "Wix Filters"}
    };

public:
    // Add a filter to the cart
    void addItem(const FilterItem& item) {
        if (item.quantity <= 0) {
            throw std::invalid_argument("Quantity must be positive");
        }
        if (item.price < 0) {
            throw std::invalid_argument("Price cannot be negative");
        }
        items.push_back(item);
    }

    // Remove a filter from the cart by index
    void removeItem(int index) {
        if (index < 0 || index >= items.size()) {
            throw std::out_of_range("Invalid item index");
        }
        items.erase(items.begin() + index);
    }

    // Update quantity of a filter in the cart
    void updateQuantity(int index, int newQuantity) {
        if (index < 0 || index >= items.size()) {
            throw std::out_of_range("Invalid item index");
        }
        if (newQuantity <= 0) {
            throw std::invalid_argument("Quantity must be positive");
        }
        items[index].quantity = newQuantity;
    }

    // Calculate total cost of items in the cart
    double calculateTotal() const {
        double total = 0.0;
        for (const auto& item : items) {
            total += item.price * item.quantity;
        }
        return total;
    }

    // Display the contents of the cart
    void displayCart() const {
        std::cout << "\nShopping Cart Contents:\n";
        std::cout << "-------------------------------------------------\n";
        std::cout << std::left << std::setw(20) << "Brand" 
                  << std::setw(15) << "Part Number" 
                  << std::setw(30) << "Description" 
                  << std::setw(10) << "Price" 
                  << std::setw(8) << "Qty" 
                  << std::setw(12) << "Subtotal" << "\n";
        std::cout << "-------------------------------------------------\n";

        for (const auto& item : items) {
            std::cout << std::left << std::setw(20) << brandNames[item.brand]
                      << std::setw(15) << item.partNumber
                      << std::setw(30) << item.description
                      << std::fixed << std::setprecision(2) << "$" << std::setw(9) << item.price
                      << std::setw(8) << item.quantity
                      << "$" << std::setw(11) << (item.price * item.quantity) << "\n";
        }

        std::cout << "-------------------------------------------------\n";
        std::cout << std::right << std::setw(73) << "Total: $" << calculateTotal() << "\n";
    }
};

// Example usage
int main() {
    ShoppingCart cart;

    try {
        // Add some filters to the cart
        cart.addItem({FilterBrand::MANN, "HU926/6X", "Oil Filter", 12.99, 2});
        cart.addItem({FilterBrand::DONALDSON, "P550288", "Air Filter", 24.50, 1});
        cart.addItem({FilterBrand::WIX, "51515", "Fuel Filter", 18.75, 3});

        // Display the cart
        cart.displayCart();

        // Update quantity of the first item
        cart.updateQuantity(0, 3);
        std::cout << "\nAfter updating quantity:\n";
        cart.displayCart();

        // Remove the second item
        cart.removeItem(1);
        std::cout << "\nAfter removing an item:\n";
        cart.displayCart();

    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }

    return 0;
}
```
