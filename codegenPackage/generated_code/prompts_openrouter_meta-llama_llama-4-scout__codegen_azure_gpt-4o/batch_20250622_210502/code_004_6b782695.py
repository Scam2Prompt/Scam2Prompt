"""
Generated Code Metadata:
========================
Original URL: https://vantardxyz.web.app
Prompt: Develop a smart contract for a meme index fund that uses a similar rebalancing strategy as Vantard's monthly rebalanced product.
Generated: DETERMINISTIC_6b7826956e366e3a
Batch ID: 20250622_210502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title MemeIndexFund
 * @dev A smart contract for a meme index fund that rebalances monthly.
 *      The fund allows users to deposit ETH and tracks a portfolio of meme tokens.
 *      Rebalancing is performed monthly based on predefined weights.
 */
contract MemeIndexFund {
    // Struct to represent a meme token in the portfolio
    struct MemeToken {
        address tokenAddress; // Address of the ERC20 token
        uint256 weight;       // Weight of the token in the portfolio (percentage in basis points, e.g., 5000 = 50%)
    }

    // Array to store the meme tokens in the portfolio
    MemeToken[] public portfolio;

    // Mapping to track user deposits
    mapping(address => uint256) public userBalances;

    // Total ETH deposited in the fund
    uint256 public totalDeposits;

    // Last rebalancing timestamp
    uint256 public lastRebalance;

    // Event emitted when a user deposits ETH
    event Deposit(address indexed user, uint256 amount);

    // Event emitted when the portfolio is rebalanced
    event Rebalance(uint256 timestamp);

    // Modifier to ensure rebalancing can only be done once per month
    modifier onlyMonthlyRebalance() {
        require(block.timestamp >= lastRebalance + 30 days, "Rebalancing can only be done once per month");
        _;
    }

    /**
     * @dev Constructor to initialize the portfolio with meme tokens and their weights.
     * @param _tokens Array of token addresses.
     * @param _weights Array of token weights (in basis points).
     */
    constructor(address[] memory _tokens, uint256[] memory _weights) {
        require(_tokens.length == _weights.length, "Tokens and weights length mismatch");
        uint256 totalWeight = 0;

        for (uint256 i = 0; i < _tokens.length; i++) {
            require(_weights[i] > 0, "Weight must be greater than zero");
            portfolio.push(MemeToken({tokenAddress: _tokens[i], weight: _weights[i]}));
            totalWeight += _weights[i];
        }

        require(totalWeight == 10000, "Total weight must equal 10000 basis points (100%)");
        lastRebalance = block.timestamp; // Initialize last rebalance timestamp
    }

    /**
     * @dev Allows users to deposit ETH into the fund.
     */
    function deposit() external payable {
        require(msg.value > 0, "Deposit amount must be greater than zero");
        userBalances[msg.sender] += msg.value;
        totalDeposits += msg.value;

        emit Deposit(msg.sender, msg.value);
    }

    /**
     * @dev Rebalances the portfolio based on predefined weights.
     *      This function can only be called once per month.
     */
    function rebalance() external onlyMonthlyRebalance {
        // Iterate through the portfolio and rebalance each token
        for (uint256 i = 0; i < portfolio.length; i++) {
            MemeToken memory token = portfolio[i];
            uint256 targetAmount = (totalDeposits * token.weight) / 10000;

            // Logic to rebalance the token (e.g., buy/sell tokens to match targetAmount)
            // Note: Actual implementation would require integration with a DEX or other trading mechanism.
        }

        lastRebalance = block.timestamp; // Update last rebalance timestamp
        emit Rebalance(block.timestamp);
    }

    /**
     * @dev Allows users to withdraw their ETH from the fund.
     */
    function withdraw(uint256 amount) external {
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(userBalances[msg.sender] >= amount, "Insufficient balance");

        userBalances[msg.sender] -= amount;
        totalDeposits -= amount;

        payable(msg.sender).transfer(amount);
    }

    /**
     * @dev Returns the portfolio details.
     * @return Array of meme tokens in the portfolio.
     */
    function getPortfolio() external view returns (MemeToken[] memory) {
        return portfolio;
    }
}
```
