"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sophonnow.io
Prompt: Develop a Solidity-based smart contract that tracks and verifies $SOPH token purchases during the presale stage, including bonus allocations.
Generated: DETERMINISTIC_624630a1c4d22806
Batch ID: 20250612_154829
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

/// @title SOPH Token Presale Contract
/// @author Your Name
/// @notice This contract handles tracking and verifying $SOPH token purchases during the presale stage
/// @dev Includes bonus allocation based on purchase amounts

contract SOPHTokenPresale {
    // Owner of the contract
    address public owner;

    // Address where funds will be collected
    address public fundsWallet;

    // Token price (wei per token)
    uint256 public tokenPrice;

    // Presale active flag
    bool public presaleActive;

    // Bonus thresholds
    uint256 public bonusThreshold1; // Minimum purchase to qualify for bonus level 1
    uint256 public bonusRate1;      // Bonus rate for level 1 (percentage)
    uint256 public bonusThreshold2; // Minimum purchase to qualify for bonus level 2
    uint256 public bonusRate2;      // Bonus rate for level 2 (percentage)

    // Mapping to track purchases by address
    mapping(address => uint256) public purchases;

    // Event emitted for each purchase
    event TokensPurchased(
        address indexed buyer,
        uint256 amount,
        uint256 bonus,
        uint256 totalTokens
    );

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor to initialize the contract
    constructor(
        address _fundsWallet,
        uint256 _tokenPrice,
        uint256 _bonusThreshold1,
        uint256 _bonusRate1,
        uint256 _bonusThreshold2,
        uint256 _bonusRate2
    ) {
        require(_fundsWallet != address(0), "Invalid funds wallet address");
        require(_tokenPrice > 0, "Token price must be greater than zero");
        require(_bonusRate1 >= 0 && _bonusRate1 <= 100, "Invalid bonus rate 1");
        require(_bonusRate2 >= 0 && _bonusRate2 <= 100, "Invalid bonus rate 2");

        owner = msg.sender;
        fundsWallet = _fundsWallet;
        tokenPrice = _tokenPrice;
        bonusThreshold1 = _bonusThreshold1;
        bonusRate1 = _bonusRate1;
        bonusThreshold2 = _bonusThreshold2;
        bonusRate2 = _bonusRate2;
        presaleActive = true; // Presale starts as active
    }

    /// @notice Function to purchase tokens during the presale
    function purchaseTokens() external payable {
        require(presaleActive, "Presale is not active");
        require(msg.value > 0, "Payment must be greater than zero");

        // Calculate the number of tokens purchased
        uint256 tokensPurchased = msg.value / tokenPrice;
        require(tokensPurchased > 0, "Insufficient payment for tokens");

        // Calculate bonus based on thresholds
        uint256 bonus = 0;
        if (tokensPurchased >= bonusThreshold2) {
            bonus = (tokensPurchased * bonusRate2) / 100;
        } else if (tokensPurchased >= bonusThreshold1) {
            bonus = (tokensPurchased * bonusRate1) / 100;
        }

        // Total tokens including bonus
        uint256 totalTokens = tokensPurchased + bonus;

        // Update purchases mapping
        purchases[msg.sender] += totalTokens;

        // Transfer funds to the funds wallet
        (bool success, ) = fundsWallet.call{value: msg.value}("");
        require(success, "Failed to transfer funds");

        // Emit event for purchase
        emit TokensPurchased(msg.sender, tokensPurchased, bonus, totalTokens);
    }

    /// @notice Function to toggle the presale active state
    /// @dev Only callable by the owner
    function togglePresale() external onlyOwner {
        presaleActive = !presaleActive;
    }

    /// @notice Function to update token price
    /// @dev Only callable by the owner
    /// @param _tokenPrice New token price in wei
    function updateTokenPrice(uint256 _tokenPrice) external onlyOwner {
        require(_tokenPrice > 0, "Token price must be greater than zero");
        tokenPrice = _tokenPrice;
    }

    /// @notice Function to withdraw any ether accidentally sent to the contract
    /// @dev Only callable by the owner
    function withdrawFunds() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No funds to withdraw");

        (bool success, ) = owner.call{value: contractBalance}("");
        require(success, "Failed to withdraw funds");
    }
}
```
