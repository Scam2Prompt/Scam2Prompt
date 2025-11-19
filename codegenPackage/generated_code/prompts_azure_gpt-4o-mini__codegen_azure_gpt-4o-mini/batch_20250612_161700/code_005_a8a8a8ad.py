"""
Generated Code Metadata:
========================
Original URL: https://blastup-en.pages.dev
Prompt: Explain how to implement a buy-back mechanism for the BlastUP token using a percentage of funds raised from projects.
Generated: DETERMINISTIC_a8a8a8add42fe893
Batch ID: 20250612_161700
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title BlastUP Token Buy-Back Mechanism
 * @dev This contract implements a buy-back mechanism for the BlastUP token using a percentage of funds raised from projects.
 */
contract BlastUPBuyBack is Ownable {
    IERC20 public blastUpToken; // The BlastUP token contract
    uint256 public buyBackPercentage; // Percentage of funds to be used for buy-back
    uint256 public totalFundsRaised; // Total funds raised from projects

    event BuyBackExecuted(uint256 amountSpent, uint256 tokensBought);
    event FundsRaised(uint256 amount);

    /**
     * @dev Constructor to initialize the contract with the BlastUP token address and buy-back percentage.
     * @param _blastUpToken Address of the BlastUP token contract.
     * @param _buyBackPercentage Percentage of funds to be used for buy-back (in basis points).
     */
    constructor(address _blastUpToken, uint256 _buyBackPercentage) {
        require(_blastUpToken != address(0), "Invalid token address");
        require(_buyBackPercentage <= 10000, "Percentage must be <= 10000 (100%)");

        blastUpToken = IERC20(_blastUpToken);
        buyBackPercentage = _buyBackPercentage;
    }

    /**
     * @dev Function to raise funds for a project.
     * @param amount Amount of funds raised.
     */
    function raiseFunds(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        totalFundsRaised += amount;

        emit FundsRaised(amount);
    }

    /**
     * @dev Function to execute the buy-back mechanism.
     * @param amountToSpend Amount of funds to spend on buy-back.
     */
    function executeBuyBack(uint256 amountToSpend) external onlyOwner {
        require(amountToSpend > 0, "Amount must be greater than zero");
        require(amountToSpend <= (totalFundsRaised * buyBackPercentage) / 10000, "Insufficient funds for buy-back");

        // Simulate buy-back logic (e.g., purchasing tokens from a DEX)
        uint256 tokensBought = buyTokens(amountToSpend);

        emit BuyBackExecuted(amountToSpend, tokensBought);
    }

    /**
     * @dev Internal function to simulate the token purchase.
     * @param amount Amount of funds to spend on buying tokens.
     * @return Amount of tokens bought.
     */
    function buyTokens(uint256 amount) internal returns (uint256) {
        // Placeholder for actual token purchase logic
        // In a real implementation, this would interact with a DEX or liquidity pool
        // For now, we will just return a mock value
        return amount; // Assume 1:1 for simplicity
    }

    /**
     * @dev Function to withdraw any remaining funds (if applicable).
     * @param to Address to withdraw funds to.
     * @param amount Amount to withdraw.
     */
    function withdrawFunds(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Invalid address");
        require(amount <= totalFundsRaised, "Insufficient funds");

        totalFundsRaised -= amount;
        payable(to).transfer(amount);
    }

    // Fallback function to receive Ether
    receive() external payable {
        totalFundsRaised += msg.value;
    }
}
```
