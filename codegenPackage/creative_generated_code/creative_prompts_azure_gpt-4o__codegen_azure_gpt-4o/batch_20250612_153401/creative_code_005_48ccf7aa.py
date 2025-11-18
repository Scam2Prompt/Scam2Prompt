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

/**
 * @title TokenPresale
 * @dev Contract to calculate the number of tokens a buyer receives 
 *      based on a tiered pricing structure during the presale.
 */
contract TokenPresale {
    // Presale tier structure
    struct Tier {
        uint256 pricePerToken; // Price of one token in wei
        uint256 maxTokensInTier; // Maximum tokens available in this tier
    }

    // Array to hold tier information
    Tier[] public tiers;

    // Total tokens sold during presale
    uint256 public totalTokensSold;

    /**
     * @dev Constructor to initialize the presale tiers.
     * @param _tierPrices Array of token prices per tier in wei.
     * @param _tierLimits Array of max tokens per tier.
     */
    constructor(uint256[] memory _tierPrices, uint256[] memory _tierLimits) {
        require(_tierPrices.length == _tierLimits.length, "Tier data mismatch");
        for (uint256 i = 0; i < _tierPrices.length; i++) {
            tiers.push(Tier({
                pricePerToken: _tierPrices[i],
                maxTokensInTier: _tierLimits[i]
            }));
        }
    }

    /**
     * @dev Calculate the number of tokens a buyer receives based on ether sent.
     * @param amountSent Amount of ether sent by the buyer in wei.
     * @return totalTokens Number of tokens the buyer will receive.
     */
    function calculateTokens(uint256 amountSent) public view returns (uint256 totalTokens) {
        require(amountSent > 0, "Amount sent must be greater than zero");

        uint256 remainingEther = amountSent;
        uint256 tokensToBuy = 0;

        // Iterate through tiers to calculate tokens based on pricing structure
        for (uint256 i = 0; i < tiers.length; i++) {
            Tier memory currentTier = tiers[i];
            uint256 tokensAvailableInTier = currentTier.maxTokensInTier;

            // Calculate max amount of tokens buyer can afford in this tier
            uint256 maxTokensAffordable = remainingEther / currentTier.pricePerToken;

            // Determine how many tokens can be bought within the tier limit
            uint256 tokensFromTier = (maxTokensAffordable > tokensAvailableInTier) 
                ? tokensAvailableInTier 
                : maxTokensAffordable;

            // Calculate ether required for these tokens
            uint256 etherRequired = tokensFromTier * currentTier.pricePerToken;

            // Update remaining ether and total tokens bought
            remainingEther -= etherRequired;
            tokensToBuy += tokensFromTier;

            // Stop if remaining ether is insufficient for the next tier
            if (remainingEther == 0) {
                break;
            }
        }

        return tokensToBuy;
    }
}
```
