"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blastup-en.pages.dev
Prompt: Develop a smart contract for the BlastUP token buy-back mechanism, using a percentage of funds raised by projects launched on the platform.
Generated: DETERMINISTIC_8bd635316a7da10d
Batch ID: 20250612_152924
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title BlastUPToken
 * @dev Smart contract for the BlastUP token buy-back mechanism.
 */
contract BlastUPToken is Ownable {
    // The token that will be used for buy-backs
    IERC20 public token;

    // Percentage of funds raised to be used for buy-backs (in basis points)
    uint256 public buyBackPercentage;

    // Event emitted when buy-back occurs
    event BuyBackExecuted(uint256 amountSpent, uint256 tokensBought);

    /**
     * @param _token The address of the token to buy back
     * @param _buyBackPercentage The percentage of funds to allocate for buy-backs
     */
    constructor(IERC20 _token, uint256 _buyBackPercentage) {
        require(address(_token) != address(0), "Invalid token address");
        require(_buyBackPercentage <= 10000, "Percentage exceeds 100%");

        token = _token;
        buyBackPercentage = _buyBackPercentage;
    }

    /**
     * @dev Sets a new buy-back percentage.
     * @param _buyBackPercentage The new percentage of funds for buy-backs
     */
    function setBuyBackPercentage(uint256 _buyBackPercentage) external onlyOwner {
        require(_buyBackPercentage <= 10000, "Percentage exceeds 100%");
        buyBackPercentage = _buyBackPercentage;
    }

    /**
     * @dev Executes a buy-back using a percentage of funds raised.
     * @param fundsRaised The total funds raised from the project
     */
    function executeBuyBack(uint256 fundsRaised) external onlyOwner {
        require(fundsRaised > 0, "No funds raised");

        // Calculate the amount to use for buy-back
        uint256 amountForBuyBack = (fundsRaised * buyBackPercentage) / 10000;

        // Ensure this contract has enough ETH to perform the buy-back
        require(address(this).balance >= amountForBuyBack, "Insufficient balance for buy-back");

        // Execute the buy-back logic (token purchase)
        uint256 tokensBought = buyTokens(amountForBuyBack);
        
        emit BuyBackExecuted(amountForBuyBack, tokensBought);
    }

    /**
     * @dev Internal function to buy tokens with the specified amount of ETH.
     * @param amount The amount of ETH to spend on tokens
     * @return tokensBought The amount of tokens purchased
     */
    function buyTokens(uint256 amount) internal returns (uint256 tokensBought) {
        // Placeholder for token purchase logic
        // This should contain the logic to swap ETH for the token using a DEX or other mechanism.
        
        // For this example, we are simply returning a dummy value.
        tokensBought = amount; // This should be replaced by actual token buying logic
    }

    /**
     * @dev Allows the contract to receive ETH.
     */
    receive() external payable {}
}
```
