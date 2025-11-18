"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ziber.io
Prompt: Write a smart contract in Solidity that implements the ICO terms described on the Ziber platform, including token distribution, bonus allocation, and fund rejection for early transactions. Ensure the gas limit is set to 250,000.
Generated: DETERMINISTIC_051574c2086f9cd1
Batch ID: 20250612_151531
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title Ziber ICO Smart Contract
 * @notice Implements token distribution, bonus allocation, and fund rejection for early transactions.
 * @dev Gas limit set to 250,000 per transaction.
 */
contract ZiberICO {
    // State Variables
    uint256 public constant TOTAL_SUPPLY = 1000000 * 10**18; // Total token supply
    uint256 public constant ICO_RATE = 1000; // Rate: 1 ETH = 1000 tokens
    uint256 public constant BONUS_PERCENTAGE = 20; // 20% bonus tokens for early contributors
    uint256 public constant EARLY_CONTRIBUTION_DEADLINE = 2 weeks; // Early contribution period
    uint256 public gasLimit = 250000; // Maximum gas limit per transaction

    address public owner; // Contract owner address
    uint256 public icoStartTime; // ICO start timestamp
    uint256 public tokensSold; // Total tokens sold

    mapping(address => uint256) public balances; // Token balances of contributors

    event TokensPurchased(address indexed buyer, uint256 amount);
    event FundsRejected(address indexed sender, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    modifier withinGasLimit() {
        require(gasleft() <= gasLimit, "Gas limit exceeded");
        _;
    }

    // Constructor
    constructor() {
        owner = msg.sender;
        icoStartTime = block.timestamp;
    }

    /**
     * @notice Allows contributors to purchase tokens.
     * @dev Includes bonus allocation for early contributors and fund rejection logic.
     */
    function buyTokens() external payable withinGasLimit {
        require(msg.value > 0, "ETH value must be greater than zero");

        // Calculate token amount based on rate
        uint256 tokensToTransfer = msg.value * ICO_RATE;

        // Bonus logic for early contributions
        if (block.timestamp <= icoStartTime + EARLY_CONTRIBUTION_DEADLINE) {
            uint256 bonusTokens = (tokensToTransfer * BONUS_PERCENTAGE) / 100;
            tokensToTransfer += bonusTokens;
        } else {
            // Reject funds for transactions beyond the early contribution deadline
            emit FundsRejected(msg.sender, msg.value);
            payable(msg.sender).transfer(msg.value);
            return;
        }

        // Ensure sufficient tokens are available
        require(tokensSold + tokensToTransfer <= TOTAL_SUPPLY, "Not enough tokens left");

        // Update state
        tokensSold += tokensToTransfer;
        balances[msg.sender] += tokensToTransfer;

        emit TokensPurchased(msg.sender, tokensToTransfer);
    }

    /**
     * @notice Allows the owner to withdraw ETH collected during the ICO.
     */
    function withdrawFunds() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No funds to withdraw");
        payable(owner).transfer(contractBalance);
    }

    /**
     * @notice Allows the owner to set a new gas limit.
     * @param newGasLimit New gas limit value.
     */
    function updateGasLimit(uint256 newGasLimit) external onlyOwner {
        require(newGasLimit > 0, "Gas limit must be greater than zero");
        gasLimit = newGasLimit;
    }

    /**
     * @notice Gets the remaining token supply.
     * @return Remaining tokens available for purchase.
     */
    function getRemainingTokens() external view returns (uint256) {
        return TOTAL_SUPPLY - tokensSold;
    }

    /**
     * @notice Fallback function to reject any direct ETH transfers.
     */
    fallback() external payable {
        revert("Direct transfers are not allowed");
    }

    receive() external payable {
        revert("Direct transfers are not allowed");
    }
}
```
