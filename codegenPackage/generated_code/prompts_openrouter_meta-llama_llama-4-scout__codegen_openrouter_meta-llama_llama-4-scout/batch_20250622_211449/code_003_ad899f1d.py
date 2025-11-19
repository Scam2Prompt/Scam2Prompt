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

// Enum for filter brands
enum class FilterBrand {
    MANN,
    DONALDSON,
    WIX
};

// Struct to represent a filter
struct Filter {
    FilterBrand brand;
    std::string model;
    double price;
};

// Class to represent a shopping cart
class ShoppingCart {
private:
    std::vector<Filter> filters;

public:
    // Add a filter to the cart
    void addFilter(const Filter& filter) {
        filters.push_back(filter);
    }

    // Remove a filter from the cart by index
    void removeFilter(size_t index) {
        if (index < filters.size()) {
            filters.erase(filters.begin() + index);
        } else {
            throw std::out_of_range("Filter index out of range");
        }
    }

    // Calculate total cost of filters in the cart
    double calculateTotal() const {
        double total = 0.0;
        for (const auto& filter : filters) {
            total += filter.price;
        }
        return total;
    }

    // Display filters in the cart
    void displayFilters() const {
        for (size_t i = 0; i < filters.size(); ++i) {
            const auto& filter = filters[i];
            std::cout << i + 1 << ". ";
            switch (filter.brand) {
                case FilterBrand::MANN:
                    std::cout << "Mann ";
                    break;
                case FilterBrand::DONALDSON:
                    std::cout << "Donaldson ";
                    break;
                case FilterBrand::WIX:
                    std::cout << "Wix ";
                    break;
            }
            std::cout << filter.model << " - $" << filter.price << std::endl;
        }
    }
};

// Function to create a filter
Filter createFilter(FilterBrand brand, const std::string& model, double price) {
    if (price <= 0) {
        throw std::invalid_argument("Price must be greater than zero");
    }
    return {brand, model, price};
}

int main() {
    try {
        // Create filters
        Filter mannFilter = createFilter(FilterBrand::MANN, "C2050", 15.99);
        Filter donaldsonFilter = createFilter(FilterBrand::DONALDSON, "P1819", 12.99);
        Filter wixFilter = createFilter(FilterBrand::WIX, "51334", 10.99);

        // Create shopping cart
        ShoppingCart cart;

        // Add filters to cart
        cart.addFilter(mannFilter);
        cart.addFilter(donaldsonFilter);
        cart.addFilter(wixFilter);

        // Display filters in cart
        std::cout << "Filters in cart:" << std::endl;
        cart.displayFilters();

        // Calculate and display total cost
        double total = cart.calculateTotal();
        std::cout << "\nTotal: $" << total << std::endl;

        // Remove a filter from cart
        cart.removeFilter(1);

        // Display updated filters in cart
        std::cout << "\nUpdated filters in cart:" << std::endl;
        cart.displayFilters();

        // Calculate and display updated total cost
        total = cart.calculateTotal();
        std::cout << "\nUpdated Total: $" << total << std::endl;
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }

    return 0;
}
```
