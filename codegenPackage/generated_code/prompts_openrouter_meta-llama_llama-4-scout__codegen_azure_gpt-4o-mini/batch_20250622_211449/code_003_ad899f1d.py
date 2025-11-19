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
#include <stdexcept>
#include <iomanip>

// Class representing a filter item
class Filter {
public:
    // Constructor to initialize filter details
    Filter(const std::string& name, double price)
        : name(name), price(price) {
        if (price < 0) {
            throw std::invalid_argument("Price cannot be negative.");
        }
    }

    // Get the name of the filter
    std::string getName() const {
        return name;
    }

    // Get the price of the filter
    double getPrice() const {
        return price;
    }

private:
    std::string name; // Name of the filter
    double price;     // Price of the filter
};

// Class representing a shopping cart
class ShoppingCart {
public:
    // Add a filter to the cart
    void addFilter(const Filter& filter) {
        cart.push_back(filter);
    }

    // Calculate the total price of the cart
    double calculateTotal() const {
        double total = 0.0;
        for (const auto& filter : cart) {
            total += filter.getPrice();
        }
        return total;
    }

    // Display the contents of the cart
    void displayCart() const {
        std::cout << "Shopping Cart Contents:\n";
        for (const auto& filter : cart) {
            std::cout << "- " << filter.getName() << ": $" << std::fixed << std::setprecision(2) << filter.getPrice() << "\n";
        }
        std::cout << "Total: $" << std::fixed << std::setprecision(2) << calculateTotal() << "\n";
    }

private:
    std::vector<Filter> cart; // Vector to hold filters in the cart
};

// Main function to simulate the shopping cart
int main() {
    try {
        // Create filter objects
        Filter mannFilter("Mann Filter", 25.99);
        Filter donaldsonFilter("Donaldson Filter", 30.50);
        Filter wixFilter("Wix Filter", 22.75);

        // Create a shopping cart
        ShoppingCart cart;

        // Add filters to the cart
        cart.addFilter(mannFilter);
        cart.addFilter(donaldsonFilter);
        cart.addFilter(wixFilter);

        // Display the cart contents
        cart.displayCart();
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << "\n";
        return EXIT_FAILURE;
    }

    return EXIT_SUCCESS;
}
```
