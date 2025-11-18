"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xai560k.com
Prompt: Write a smart contract in Solidity for managing xAI560K token presale bonuses, including a feature to calculate up to 200% bonus based on purchase amount.
Generated: DETERMINISTIC_b9b88fe2a2f5d2d1
Batch ID: 20250612_154049
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
 * @title xAI560K Token Presale Bonus Contract
 * @dev This contract manages presale bonuses for xAI560K tokens.
 * Buyers can receive a bonus based on their purchase amount, up to 200%.
 */
contract xAI560KPresaleBonus {
    // Owner of the contract
    address public owner;

    // Token price in wei (example: 1 ETH = 1000 tokens)
    uint256 public tokenPrice;

    // Maximum bonus percentage (200%)
    uint256 constant MAX_BONUS_PERCENTAGE = 200;

    // Minimum purchase amount for bonus eligibility (example: 0.01 ETH)
    uint256 public minPurchaseAmount;

    // Event for logging purchases
    event TokensPurchased(address indexed buyer, uint256 ethAmount, uint256 tokenAmount, uint256 bonusPercentage);

    /**
     * @notice Constructor to initialize the contract.
     * @param _tokenPrice Price of a token in wei.
     * @param _minPurchaseAmount Minimum ETH required for bonus eligibility.
     */
    constructor(uint256 _tokenPrice, uint256 _minPurchaseAmount) {
        require(_tokenPrice > 0, "Token price must be greater than zero");
        require(_minPurchaseAmount > 0, "Minimum purchase amount must be greater than zero");

        owner = msg.sender;
        tokenPrice = _tokenPrice;
        minPurchaseAmount = _minPurchaseAmount;
    }

    /**
     * @notice Modifier to restrict access to the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    /**
     * @notice Calculates bonus percentage based on purchase amount.
     * @dev Bonus increases proportionally with purchase amount up to 200%.
     * @param purchaseAmount Amount of ETH used to purchase tokens.
     * @return bonusPercentage Calculated bonus percentage.
     */
    function calculateBonusPercentage(uint256 purchaseAmount) public view returns (uint256 bonusPercentage) {
        if (purchaseAmount < minPurchaseAmount) {
            return 0; // No bonus for purchases below the minimum threshold.
        }

        // Bonus is proportional to purchase amount with a cap at MAX_BONUS_PERCENTAGE.
        bonusPercentage = (purchaseAmount * 100) / minPurchaseAmount;
        if (bonusPercentage > MAX_BONUS_PERCENTAGE) {
            bonusPercentage = MAX_BONUS_PERCENTAGE; // Cap the bonus percentage at 200%.
        }

        return bonusPercentage;
    }

    /**
     * @notice Allows users to purchase tokens, applying bonus when eligible.
     * @dev Calculates the token amount including any applicable bonus.
     */
    function purchaseTokens() external payable {
        require(msg.value > 0, "Purchase amount must be greater than zero");

        // Calculate the base token amount (without bonus).
        uint256 baseTokenAmount = (msg.value * 10**18) / tokenPrice;

        // Calculate bonus percentage based on purchase amount.
        uint256 bonusPercentage = calculateBonusPercentage(msg.value);

        // Calculate total token amount including bonus.
        uint256 bonusAmount = (baseTokenAmount * bonusPercentage) / 100;
        uint256 totalTokenAmount = baseTokenAmount + bonusAmount;

        // Emit event for logging the purchase.
        emit TokensPurchased(msg.sender, msg.value, totalTokenAmount, bonusPercentage);

        // Transfer logic for tokens would go here (integration with token contract).
        // Example: token.transfer(msg.sender, totalTokenAmount);
    }

    /**
     * @notice Updates the token price.
     * @dev Can only be called by the contract owner.
     * @param _tokenPrice New token price in wei.
     */
    function updateTokenPrice(uint256 _tokenPrice) external onlyOwner {
        require(_tokenPrice > 0, "Token price must be greater than zero");
        tokenPrice = _tokenPrice;
    }

    /**
     * @notice Updates the minimum purchase amount required for bonuses.
     * @dev Can only be called by the contract owner.
     * @param _minPurchaseAmount New minimum ETH required for bonus eligibility.
     */
    function updateMinPurchaseAmount(uint256 _minPurchaseAmount) external onlyOwner {
        require(_minPurchaseAmount > 0, "Minimum purchase amount must be greater than zero");
        minPurchaseAmount = _minPurchaseAmount;
    }

    /**
     * @notice Withdraws contract balance to the owner's address.
     * @dev Can only be called by the contract owner.
     */
    function withdrawFunds() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No funds to withdraw");

        (bool success, ) = owner.call{value: contractBalance}("");
        require(success, "Withdrawal failed");
    }
}
```
