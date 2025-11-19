"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sspanel.biz
Prompt: Create a C++ program that simulates a cryptocurrency transaction, inspired by the discussions on cryptocurrency investments found on sspanel.
Generated: DETERMINISTIC_a869c7e13e4b17f0
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```cpp
#include <iostream>
#include <string>
#include <stdexcept>
#include <vector>
#include <iomanip>

// Class representing a cryptocurrency wallet
class Wallet {
private:
    std::string owner;
    double balance; // Balance in cryptocurrency

public:
    // Constructor to initialize wallet with owner name and initial balance
    Wallet(const std::string& owner, double initialBalance) : owner(owner), balance(initialBalance) {
        if (initialBalance < 0) {
            throw std::invalid_argument("Initial balance cannot be negative");
        }
    }

    // Method to get the current balance
    double getBalance() const {
        return balance;
    }

    // Method to perform a transaction
    void transact(double amount) {
        if (amount == 0) {
            throw std::invalid_argument("Transaction amount cannot be zero");
        }
        if (balance + amount < 0) {
            throw std::runtime_error("Insufficient balance for this transaction");
        }
        balance += amount;
    }

    // Method to display wallet information
    void display() const {
        std::cout << "Wallet Owner: " << owner << "\n"
                  << "Current Balance: " << std::fixed << std::setprecision(8) << balance << " BTC" << std::endl;
    }
};

// Main function to simulate cryptocurrency transactions
int main() {
    try {
        // Create a new wallet with initial balance
        Wallet myWallet("Alice", 1.5);

        // Display current wallet information
        myWallet.display();

        // Simulate a deposit
        std::cout << "Depositing 0.5 BTC..." << std::endl;
        myWallet.transact(0.5);
        myWallet.display();

        // Simulate a withdrawal
        std::cout << "Withdrawing 0.3 BTC..." << std::endl;
        myWallet.transact(-0.3);
        myWallet.display();

        // Attempt to withdraw more than the balance
        std::cout << "Attempting to withdraw 2.0 BTC..." << std::endl;
        myWallet.transact(-2.0);
        myWallet.display();

    } catch (const std::exception& e) {
        // Handle exceptions by displaying an error message
        std::cerr << "Error: " << e.what() << std::endl;
    }

    return 0; // Indicate successful program execution
}
```
