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
/**
 * @file binary_trade_calculator.cpp
 * @brief Calculates potential winnings for a binary trade on CoChilli SportsBook.
 */

#include <iostream>
#include <stdexcept>

/**
 * @enum TradeType
 * @brief Enum for trade types.
 */
enum class TradeType {
    BACK,
    LAY
};

/**
 * @class BinaryTradeCalculator
 * @brief Calculates potential winnings for a binary trade.
 */
class BinaryTradeCalculator {
public:
    /**
     * @brief Constructor.
     */
    BinaryTradeCalculator() = default;

    /**
     * @brief Calculates potential winnings.
     * 
     * @param tradeType Type of trade (BACK or LAY).
     * @param odds Odds of the trade.
     * @param amountInvested Amount invested in the trade.
     * @return Potential winnings.
     */
    double calculateWinnings(TradeType tradeType, double odds, double amountInvested) {
        if (odds <= 1.0) {
            throw std::invalid_argument("Odds must be greater than 1.0");
        }

        if (amountInvested <= 0.0) {
            throw std::invalid_argument("Amount invested must be greater than 0.0");
        }

        double winnings;
        switch (tradeType) {
            case TradeType::BACK:
                // For BACK trades, winnings = (odds * amountInvested) - amountInvested
                winnings = (odds * amountInvested) - amountInvested;
                break;
            case TradeType::LAY:
                // For LAY trades, winnings = amountInvested
                // However, if the trade loses, the loss is (amountInvested * (odds - 1))
                // Here we only calculate the potential winnings if the trade wins
                winnings = amountInvested;
                break;
            default:
                throw std::invalid_argument("Invalid trade type");
        }

        return winnings;
    }
};

int main() {
    try {
        BinaryTradeCalculator calculator;
        double odds = 2.5;
        double amountInvested = 10.0;

        double backWinnings = calculator.calculateWinnings(TradeType::BACK, odds, amountInvested);
        double layWinnings = calculator.calculateWinnings(TradeType::LAY, odds, amountInvested);

        std::cout << "Potential BACK winnings: " << backWinnings << std::endl;
        std::cout << "Potential LAY winnings: " << layWinnings << std::endl;

    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }

    return 0;
}
```
