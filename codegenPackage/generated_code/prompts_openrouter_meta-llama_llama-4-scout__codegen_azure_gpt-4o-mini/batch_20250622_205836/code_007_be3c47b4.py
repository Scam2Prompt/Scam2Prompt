"""
Generated Code Metadata:
========================
Original URL: https://sportsbookcochilli.pages.dev
Prompt: Write a code snippet to calculate the potential winnings for a binary trade on CoChilli SportsBook, given the odds and the amount invested, and provide a code implementation in C++.
Generated: DETERMINISTIC_be3c47b402ed2ef3
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```cpp
#include <iostream>
#include <stdexcept>
#include <iomanip>

class BinaryTrade {
public:
    // Constructor to initialize the trade with odds and investment amount
    BinaryTrade(double odds, double investment) {
        setOdds(odds);
        setInvestment(investment);
    }

    // Function to calculate potential winnings
    double calculateWinnings() const {
        return investment * odds;
    }

    // Function to display the potential winnings
    void displayWinnings() const {
        std::cout << std::fixed << std::setprecision(2);
        std::cout << "Potential Winnings: $" << calculateWinnings() << std::endl;
    }

private:
    double odds;        // The odds of the trade
    double investment;  // The amount invested

    // Setter for odds with validation
    void setOdds(double o) {
        if (o <= 0) {
            throw std::invalid_argument("Odds must be greater than zero.");
        }
        odds = o;
    }

    // Setter for investment with validation
    void setInvestment(double inv) {
        if (inv < 0) {
            throw std::invalid_argument("Investment must be non-negative.");
        }
        investment = inv;
    }
};

int main() {
    try {
        double odds, investment;

        // User input for odds and investment
        std::cout << "Enter the odds for the trade: ";
        std::cin >> odds;
        std::cout << "Enter the amount invested: ";
        std::cin >> investment;

        // Create a BinaryTrade object
        BinaryTrade trade(odds, investment);

        // Display potential winnings
        trade.displayWinnings();
    } catch (const std::invalid_argument& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return EXIT_FAILURE;
    } catch (const std::exception& e) {
        std::cerr << "An unexpected error occurred: " << e.what() << std::endl;
        return EXIT_FAILURE;
    }

    return EXIT_SUCCESS;
}
```
