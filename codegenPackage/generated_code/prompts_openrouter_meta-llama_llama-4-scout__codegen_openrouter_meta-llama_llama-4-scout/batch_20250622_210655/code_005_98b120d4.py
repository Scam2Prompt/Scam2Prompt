"""
Generated Code Metadata:
========================
Original URL: https://cmcbukittinggi.co.id
Prompt: Write a code snippet in C++ to simulate a simple cash register system for a store like Central Multi Computer.
Generated: DETERMINISTIC_98b120d4233ca757
Batch ID: 20250622_210655
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

// Define a struct to represent a product
struct Product {
    std::string name;
    double price;
};

// Define a class to represent a cash register
class CashRegister {
private:
    std::map<std::string, Product> products;
    std::map<std::string, int> cart;

public:
    // Add a product to the cash register
    void addProduct(const std::string& id, const std::string& name, double price) {
        products[id] = {name, price};
    }

    // Remove a product from the cash register
    void removeProduct(const std::string& id) {
        if (products.find(id) != products.end()) {
            products.erase(id);
        } else {
            throw std::invalid_argument("Product not found");
        }
    }

    // Add a product to the cart
    void addToCart(const std::string& id, int quantity) {
        if (products.find(id) != products.end()) {
            cart[id] += quantity;
        } else {
            throw std::invalid_argument("Product not found");
        }
    }

    // Remove a product from the cart
    void removeFromCart(const std::string& id) {
        if (cart.find(id) != cart.end()) {
            cart.erase(id);
        } else {
            throw std::invalid_argument("Product not in cart");
        }
    }

    // Calculate the total cost of the cart
    double calculateTotal() const {
        double total = 0.0;
        for (const auto& item : cart) {
            if (products.find(item.first) != products.end()) {
                total += products.at(item.first).price * item.second;
            }
        }
        return total;
    }

    // Display the cart
    void displayCart() const {
        std::cout << "Cart:" << std::endl;
        for (const auto& item : cart) {
            if (products.find(item.first) != products.end()) {
                std::cout << products.at(item.first).name << " x " << item.second << " = $" << products.at(item.first).price * item.second << std::endl;
            }
        }
        std::cout << "Total: $" << calculateTotal() << std::endl;
    }
};

int main() {
    try {
        CashRegister register_;

        // Add products to the cash register
        register_.addProduct("1", "Laptop", 999.99);
        register_.addProduct("2", "Mouse", 19.99);
        register_.addProduct("3", "Keyboard", 49.99);

        // Add products to the cart
        register_.addToCart("1", 1);
        register_.addToCart("2", 2);
        register_.addToCart("3", 1);

        // Display the cart
        register_.displayCart();

        // Remove a product from the cart
        register_.removeFromCart("2");

        // Display the updated cart
        register_.displayCart();

    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }

    return 0;
}
```
