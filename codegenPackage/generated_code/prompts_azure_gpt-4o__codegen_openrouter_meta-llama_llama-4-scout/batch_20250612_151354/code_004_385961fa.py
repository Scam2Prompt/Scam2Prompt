"""
Generated Code Metadata:
========================
Original URL: https://shiba-3.web.app
Prompt: Create a Solidity function that calculates the number of Shiba 3.0 tokens a user receives based on the Ethereum amount sent during the ICO sale.
Generated: DETERMINISTIC_385961fa5d927e3d
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
pragma solidity ^0.8.0;

/**
 * @title Shiba3TokenSale
 * @author [Your Name]
 * @notice Contract for Shiba 3.0 token sale
 */
contract Shiba3TokenSale {
    // Mapping of token exchange rate (1 ETH = x Shiba 3.0 tokens)
    uint256 public exchangeRate;

    // Mapping of total tokens sold
    uint256 public totalTokensSold;

    // Mapping of user balances
    mapping (address => uint256) public userBalances;

    /**
     * @dev Constructor for Shiba3TokenSale contract
     * @param _exchangeRate Exchange rate for 1 ETH to Shiba 3.0 tokens
     */
    constructor(uint256 _exchangeRate) {
        require(_exchangeRate > 0, "Exchange rate must be greater than 0");
        exchangeRate = _exchangeRate;
        totalTokensSold = 0;
    }

    /**
     * @dev Calculates the number of Shiba 3.0 tokens a user receives based on the Ethereum amount sent
     * @param _ethAmount Amount of Ethereum sent by the user
     * @return uint256 Number of Shiba 3.0 tokens the user receives
     */
    function calculateTokens(uint256 _ethAmount) public view returns (uint256) {
        // Validate input
        require(_ethAmount > 0, "Ethereum amount must be greater than 0");

        // Calculate tokens
        uint256 tokens = _ethAmount * exchangeRate;
        return tokens;
    }

    /**
     * @dev Buys Shiba 3.0 tokens with Ethereum
     */
    function buyTokens() public payable {
        // Validate input
        require(msg.value > 0, "Ethereum amount must be greater than 0");

        // Calculate tokens
        uint256 tokens = calculateTokens(msg.value);

        // Update user balance
        userBalances[msg.sender] += tokens;

        // Update total tokens sold
        totalTokensSold += tokens;

        // Emit event
        emit TokensPurchased(msg.sender, tokens);
    }

    /**
     * @dev Event emitted when tokens are purchased
     * @param buyer Address of the buyer
     * @param tokens Number of tokens purchased
     */
    event TokensPurchased(address indexed buyer, uint256 tokens);
}
```
