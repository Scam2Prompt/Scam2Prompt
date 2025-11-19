"""
Generated Code Metadata:
========================
Original URL: https://jesse-presale-8r8.pages.dev
Prompt: Develop a smart contract in Solidity for managing the JESSE presale, ensuring the total supply is capped at 100,000,000 tokens and implementing tiered pricing for BASE contributions.
Generated: DETERMINISTIC_49b38d0505a093dd
Batch ID: 20250612_153401
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title JESSEPresale
 * @dev Smart contract for managing the JESSE token presale with tiered pricing.
 */
contract JESSEPresale is Ownable {
    // Token details
    ERC20 public token;
    uint256 public constant TOTAL_SUPPLY = 100_000_000 * 10 ** 18; // Total supply capped at 100 million tokens
    uint256 public tokensSold; // Track the number of tokens sold

    // Pricing tiers
    struct Tier {
        uint256 price; // Price per token in wei
        uint256 cap;   // Maximum tokens available at this tier
    }

    Tier[] public tiers; // Array to hold pricing tiers
    uint256 public currentTierIndex; // Index of the current active tier

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 totalCost);
    event TierUpdated(uint256 index, uint256 price, uint256 cap);

    /**
     * @dev Constructor to initialize the presale contract.
     * @param _token Address of the ERC20 token to be sold.
     */
    constructor(ERC20 _token) {
        token = _token;
        currentTierIndex = 0;

        // Initialize pricing tiers
        tiers.push(Tier(0.01 ether, 50_000_000 * 10 ** 18)); // Tier 1
        tiers.push(Tier(0.02 ether, 30_000_000 * 10 ** 18)); // Tier 2
        tiers.push(Tier(0.03 ether, 20_000_000 * 10 ** 18)); // Tier 3
    }

    /**
     * @dev Purchase tokens during the presale.
     * @param amount Number of tokens to purchase.
     */
    function purchaseTokens(uint256 amount) external payable {
        require(amount > 0, "Amount must be greater than zero");
        require(currentTierIndex < tiers.length, "No active tiers available");

        Tier memory currentTier = tiers[currentTierIndex];
        require(tokensSold + amount <= TOTAL_SUPPLY, "Exceeds total supply");
        require(currentTier.cap >= amount, "Exceeds tier cap");

        uint256 totalCost = currentTier.price * amount;
        require(msg.value >= totalCost, "Insufficient funds sent");

        // Update state
        tokensSold += amount;
        tiers[currentTierIndex].cap -= amount;

        // Transfer tokens to the buyer
        token.transfer(msg.sender, amount);

        // Emit event for purchase
        emit TokensPurchased(msg.sender, amount, totalCost);

        // Refund excess funds
        if (msg.value > totalCost) {
            payable(msg.sender).transfer(msg.value - totalCost);
        }

        // Move to the next tier if the current tier cap is reached
        if (tiers[currentTierIndex].cap == 0) {
            currentTierIndex++;
        }
    }

    /**
     * @dev Update the pricing tier.
     * @param index Index of the tier to update.
     * @param price New price per token in wei.
     * @param cap New cap for the tier.
     */
    function updateTier(uint256 index, uint256 price, uint256 cap) external onlyOwner {
        require(index < tiers.length, "Invalid tier index");
        tiers[index].price = price;
        tiers[index].cap = cap;

        emit TierUpdated(index, price, cap);
    }

    /**
     * @dev Withdraw funds from the contract.
     */
    function withdrawFunds() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers.
     */
    receive() external payable {
        revert("Direct ETH transfers not allowed");
    }
}
```
