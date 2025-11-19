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
#include <iomanip>
#include <vector>
#include <string>
#include <stdexcept>

using namespace std;

// Struct to represent an item in the store
struct Item {
    string name;
    double price;
};

// Class to represent the cash register system
class CashRegister {
private:
    vector<Item> items; // List of items available in the store
    vector<Item> cart;  // Items added to the customer's cart
    double total;       // Total cost of items in the cart

public:
    // Constructor
    CashRegister() : total(0.0) {}

    // Add an item to the store inventory
    void addItemToInventory(const string& name, double price) {
        if (price < 0) {
            throw invalid_argument("Price cannot be negative.");
        }
        items.push_back({name, price});
    }

    // Display the store inventory
    void displayInventory() const {
        cout << "Store Inventory:\n";
        cout << setw(5) << "ID" << setw(20) << "Item Name" << setw(10) << "Price\n";
        cout << "---------------------------------------------\n";
        for (size_t i = 0; i < items.size(); ++i) {
            cout << setw(5) << i + 1 << setw(20) << items[i].name << setw(10) << fixed << setprecision(2) << items[i].price << "\n";
        }
    }

    // Add an item to the customer's cart
    void addItemToCart(int itemId) {
        if (itemId < 1 || itemId > static_cast<int>(items.size())) {
            throw out_of_range("Invalid item ID.");
        }
        cart.push_back(items[itemId - 1]);
        total += items[itemId - 1].price;
    }

    // Display the customer's cart
    void displayCart() const {
        cout << "Customer's Cart:\n";
        cout << setw(5) << "ID" << setw(20) << "Item Name" << setw(10) << "Price\n";
        cout << "---------------------------------------------\n";
        for (size_t i = 0; i < cart.size(); ++i) {
            cout << setw(5) << i + 1 << setw(20) << cart[i].name << setw(10) << fixed << setprecision(2) << cart[i].price << "\n";
        }
        cout << "---------------------------------------------\n";
        cout << setw(25) << "Total: " << setw(10) << fixed << setprecision(2) << total << "\n";
    }

    // Checkout and display the final bill
    void checkout() {
        if (cart.empty()) {
            throw runtime_error("Cart is empty. Cannot proceed to checkout.");
        }
        cout << "Final Bill:\n";
        displayCart();
        cout << "Thank you for shopping with us!\n";
        // Reset cart and total for the next customer
        cart.clear();
        total = 0.0;
    }
};

int main() {
    try {
        CashRegister registerSystem;

        // Add items to the store inventory
        registerSystem.addItemToInventory("Laptop", 999.99);
        registerSystem.addItemToInventory("Mouse", 19.99);
        registerSystem.addItemToInventory("Keyboard", 49.99);
        registerSystem.addItemToInventory("Monitor", 199.99);

        // Display the inventory
        registerSystem.displayInventory();

        // Simulate adding items to the cart
        registerSystem.addItemToCart(1); // Add Laptop
        registerSystem.addItemToCart(3); // Add Keyboard

        // Display the cart
        registerSystem.displayCart();

        // Checkout
        registerSystem.checkout();
    } catch (const exception& e) {
        cerr << "Error: " << e.what() << endl;
    }

    return 0;
}
```
