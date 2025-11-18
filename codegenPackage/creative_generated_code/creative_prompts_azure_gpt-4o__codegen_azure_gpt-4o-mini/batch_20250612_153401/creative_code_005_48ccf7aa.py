"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marketplace-jesse-3on.pages.dev
Prompt: Create a function in Solidity to calculate the number of tokens a buyer receives based on the tiered pricing structure outlined in the JESSE presale.
Generated: DETERMINISTIC_48ccf7aa2be4c30a
Batch ID: 20250612_153401
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

contract TokenSale {
    // Define the pricing tiers
    struct PricingTier {
        uint256 minAmount;  // Minimum amount to purchase for this tier
        uint256 maxAmount;  // Maximum amount to purchase for this tier
        uint256 tokenRate;  // Number of tokens per ether for this tier
    }

    // Array to store the pricing tiers
    PricingTier[] public pricingTiers;

    // Event to log the purchase
    event TokensPurchased(address buyer, uint256 amountSpent, uint256 tokensReceived);

    // Constructor to initialize pricing tiers
    constructor() {
        // Example tiers (modify as needed)
        pricingTiers.push(PricingTier(0 ether, 0.5 ether, 1000)); // Tier 1: 1000 tokens per ether
        pricingTiers.push(PricingTier(0.5 ether, 1 ether, 1200)); // Tier 2: 1200 tokens per ether
        pricingTiers.push(PricingTier(1 ether, type(uint256).max, 1500)); // Tier 3: 1500 tokens per ether
    }

    // Function to calculate the number of tokens received based on the amount spent
    function calculateTokens(uint256 amountSpent) public view returns (uint256) {
        // Ensure that the amount spent is greater than zero
        require(amountSpent > 0, "Amount spent must be greater than zero");

        uint256 totalTokens = 0;

        // Iterate through the pricing tiers to determine how many tokens to award
        for (uint256 i = 0; i < pricingTiers.length; i++) {
            PricingTier memory tier = pricingTiers[i];

            // Break the loop if the amount spent is less than the minimum for the current tier
            if (amountSpent < tier.minAmount) {
                break;
            }

            // Calculate the effective amount for the current tier
            uint256 effectiveAmount = amountSpent;

            // Adjust the effective amount if it exceeds the current tier's max
            if (amountSpent > tier.maxAmount) {
                effectiveAmount = tier.maxAmount;
            }

            // Calculate the tokens for the current tier
            uint256 tokensForTier = effectiveAmount * tier.tokenRate;

            // Add to the total tokens
            totalTokens += tokensForTier;

            // Subtract the effective amount from the amount spent
            amountSpent -= effectiveAmount;

            // Stop if there are no funds left to allocate
            if (amountSpent == 0) {
                break;
            }
        }

        return totalTokens;
    }

    // Fallback function to handle incoming ether
    receive() external payable {
        // Calculate the number of tokens for the amount sent
        uint256 tokens = calculateTokens(msg.value);
        require(tokens > 0, "No tokens could be purchased");

        // Emit event for the purchase
        emit TokensPurchased(msg.sender, msg.value, tokens);
    }
}
```
