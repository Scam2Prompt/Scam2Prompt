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
#include <vector>
#include <iomanip>
#include <limits>
#include <stdexcept>

class Product {
public:
    Product(int id, const std::string& name, double price) 
        : id(id), name(name), price(price) {}

    int getId() const { return id; }
    std::string getName() const { return name; }
    double getPrice() const { return price; }

private:
    int id;
    std::string name;
    double price;
};

class CashRegister {
public:
    void addProduct(const Product& product) {
        products.push_back(product);
    }

    void displayProducts() const {
        std::cout << "\nAvailable Products:\n";
        std::cout << "ID\tName\t\tPrice\n";
        std::cout << "--------------------------------\n";
        for (const auto& product : products) {
            std::cout << product.getId() << "\t" 
                      << std::left << std::setw(15) << product.getName() 
                      << "\t$" << std::fixed << std::setprecision(2) 
                      << product.getPrice() << "\n";
        }
    }

    void processTransaction() {
        std::vector<int> cart;
        double total = 0.0;
        int productId;
        char continueShopping;

        std::cout << "\nWelcome to Central Multi Computer\n";
        displayProducts();

        do {
            try {
                std::cout << "\nEnter product ID to add to cart: ";
                if (!(std::cin >> productId)) {
                    throw std::runtime_error("Invalid input. Please enter a number.");
                }

                bool found = false;
                for (const auto& product : products) {
                    if (product.getId() == productId) {
                        cart.push_back(productId);
                        total += product.getPrice();
                        std::cout << "Added " << product.getName() << " to cart.\n";
                        found = true;
                        break;
                    }
                }

                if (!found) {
                    std::cout << "Product not found.\n";
                }

                std::cout << "Continue shopping? (y/n): ";
                std::cin >> continueShopping;
                std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            } catch (const std::exception& e) {
                std::cerr << "Error: " << e.what() << "\n";
                std::cin.clear();
                std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
            }
        } while (continueShopping == 'y' || continueShopping == 'Y');

        printReceipt(cart, total);
    }

private:
    void printReceipt(const std::vector<int>& cart, double total) {
        std::cout << "\n\nCENTRAL MULTI COMPUTER - RECEIPT\n";
        std::cout << "--------------------------------\n";
        std::cout << "Items Purchased:\n";

        for (int id : cart) {
            for (const auto& product : products) {
                if (product.getId() == id) {
                    std::cout << "- " << product.getName() 
                              << " ($" << std::fixed << std::setprecision(2) 
                              << product.getPrice() << ")\n";
                    break;
                }
            }
        }

        std::cout << "--------------------------------\n";
        std::cout << "TOTAL: $" << std::fixed << std::setprecision(2) << total << "\n";
        std::cout << "Thank you for shopping with us!\n\n";
    }

    std::vector<Product> products;
};

int main() {
    CashRegister registerSystem;

    // Add sample products
    registerSystem.addProduct(Product(1, "Laptop", 999.99));
    registerSystem.addProduct(Product(2, "Mouse", 19.99));
    registerSystem.addProduct(Product(3, "Keyboard", 49.99));
    registerSystem.addProduct(Product(4, "Monitor", 199.99));
    registerSystem.addProduct(Product(5, "Headphones", 79.99));

    // Process transaction
    registerSystem.processTransaction();

    return 0;
}
```
