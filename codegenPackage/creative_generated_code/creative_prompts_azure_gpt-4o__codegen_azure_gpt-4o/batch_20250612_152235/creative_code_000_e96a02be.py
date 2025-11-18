"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lopecoin-presale.pages.dev
Prompt: Write a smart contract in Solidity for a Binance Smart Chain (BSC) token presale, incorporating tiered pricing similar to LopeCoin's presale structure (Tier1: $0.00000009, Tier2: $0.00000010, etc.).
Generated: DETERMINISTIC_e96a02be39c19205
Batch ID: 20250612_152235
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
 * @dev Smart contract for tiered pricing token presale on Binance Smart Chain (BSC).
 */
contract TokenPresale {
    // Token details
    address public tokenAddress; // The token being sold
    address public owner; // Owner of the contract

    // Tiered pricing structure
    struct Tier {
        uint256 price; // Price per token in wei
        uint256 tokenLimit; // Max tokens available in this tier
        uint256 tokensSold; // Tokens already sold in this tier
    }

    Tier[] public tiers;

    // Funds collection
    uint256 public totalFundsCollected; // Total BNB collected
    uint256 public totalTokensSold; // Total tokens sold

    // Events
    event TokenPurchase(address indexed buyer, uint256 amount, uint256 value);
    event TierAdded(uint256 price, uint256 tokenLimit);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        tokenAddress = _tokenAddress;
        owner = msg.sender;
    }

    /**
     * @dev Add a new presale tier.
     * @param _price Price per token in wei.
     * @param _tokenLimit Maximum tokens available in this tier.
     */
    function addTier(uint256 _price, uint256 _tokenLimit) external onlyOwner {
        require(_price > 0, "Price must be greater than 0");
        require(_tokenLimit > 0, "Token limit must be greater than 0");
        tiers.push(Tier({price: _price, tokenLimit: _tokenLimit, tokensSold: 0}));
        emit TierAdded(_price, _tokenLimit);
    }

    /**
     * @dev Function to purchase tokens during the presale.
     */
    function buyTokens() external payable {
        require(msg.value > 0, "Value must be greater than 0");
        uint256 remainingAmount = msg.value; // Amount of BNB sent
        uint256 tokensToPurchase = 0;

        // Iterate through the tiers to determine how many tokens can be purchased
        for (uint256 i = 0; i < tiers.length && remainingAmount > 0; i++) {
            Tier storage tier = tiers[i];
            if (tier.tokensSold < tier.tokenLimit) {
                uint256 availableTokens = tier.tokenLimit - tier.tokensSold;
                uint256 tokensFromTier = remainingAmount / tier.price;

                if (tokensFromTier > availableTokens) {
                    tokensFromTier = availableTokens;
                }

                uint256 costForTier = tokensFromTier * tier.price;

                if (costForTier > remainingAmount) {
                    costForTier = remainingAmount;
                    tokensFromTier = costForTier / tier.price;
                }

                tier.tokensSold += tokensFromTier;
                tokensToPurchase += tokensFromTier;
                remainingAmount -= costForTier;
            }
        }

        require(tokensToPurchase > 0, "Insufficient value to purchase tokens");

        // Update total funds collected and tokens sold
        totalFundsCollected += msg.value - remainingAmount;
        totalTokensSold += tokensToPurchase;

        // Return excess amount if any
        if (remainingAmount > 0) {
            payable(msg.sender).transfer(remainingAmount);
        }

        // Transfer tokens to the buyer
        IERC20(tokenAddress).transfer(msg.sender, tokensToPurchase);

        emit TokenPurchase(msg.sender, tokensToPurchase, msg.value - remainingAmount);
    }

    /**
     * @dev Withdraw collected funds (BNB) by the owner.
     */
    function withdrawFunds() external onlyOwner {
        uint256 collected = address(this).balance;
        require(collected > 0, "No funds to withdraw");
        payable(owner).transfer(collected);
    }

    /**
     * @dev Withdraw unsold tokens by the owner after presale.
     */
    function withdrawUnsoldTokens() external onlyOwner {
        uint256 contractBalance = IERC20(tokenAddress).balanceOf(address(this));
        require(contractBalance > 0, "No tokens to withdraw");
        IERC20(tokenAddress).transfer(owner, contractBalance);
    }

    // Fallback function to accept BNB
    receive() external payable {}
}

/**
 * @dev Interface for the ERC20 token to interact with the presale contract.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
