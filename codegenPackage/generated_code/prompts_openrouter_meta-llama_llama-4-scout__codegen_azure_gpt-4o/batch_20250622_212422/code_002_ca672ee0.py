"""
Generated Code Metadata:
========================
Original URL: https://zoranetwork.io
Prompt: Generate a smart contract code snippet in Solidity for a token presale platform, incorporating a time-limited bonus structure like the one described on the ZORA Network website.
Generated: DETERMINISTIC_ca672ee07d5f63d5
Batch ID: 20250622_212422
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
 * @title TokenPresale
 * @dev A smart contract for a token presale platform with a time-limited bonus structure.
 */
contract TokenPresale {
    // Token details
    address public tokenAddress;
    uint256 public tokenPrice; // Price per token in wei
    uint256 public presaleStartTime;
    uint256 public presaleEndTime;

    // Bonus structure
    uint256 public bonusEndTime; // Time until bonus is active
    uint256 public bonusPercentage; // Bonus percentage (e.g., 20 for 20%)

    // State variables
    address public owner;
    uint256 public totalTokensSold;

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 bonusTokens);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    modifier presaleActive() {
        require(block.timestamp >= presaleStartTime, "Presale has not started yet");
        require(block.timestamp <= presaleEndTime, "Presale has ended");
        _;
    }

    /**
     * @dev Constructor to initialize the presale contract.
     * @param _tokenAddress Address of the token being sold.
     * @param _tokenPrice Price per token in wei.
     * @param _presaleStartTime Start time of the presale (UNIX timestamp).
     * @param _presaleEndTime End time of the presale (UNIX timestamp).
     * @param _bonusEndTime End time for the bonus structure (UNIX timestamp).
     * @param _bonusPercentage Bonus percentage (e.g., 20 for 20%).
     */
    constructor(
        address _tokenAddress,
        uint256 _tokenPrice,
        uint256 _presaleStartTime,
        uint256 _presaleEndTime,
        uint256 _bonusEndTime,
        uint256 _bonusPercentage
    ) {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_tokenPrice > 0, "Token price must be greater than zero");
        require(_presaleStartTime < _presaleEndTime, "Presale start time must be before end time");
        require(_bonusEndTime <= _presaleEndTime, "Bonus end time must be within presale period");

        tokenAddress = _tokenAddress;
        tokenPrice = _tokenPrice;
        presaleStartTime = _presaleStartTime;
        presaleEndTime = _presaleEndTime;
        bonusEndTime = _bonusEndTime;
        bonusPercentage = _bonusPercentage;
        owner = msg.sender;
    }

    /**
     * @dev Function to purchase tokens during the presale.
     * @param _amount Number of tokens to purchase.
     */
    function purchaseTokens(uint256 _amount) external payable presaleActive {
        require(_amount > 0, "Amount must be greater than zero");
        uint256 totalCost = _amount * tokenPrice;
        require(msg.value >= totalCost, "Insufficient funds sent");

        uint256 bonusTokens = 0;

        // Apply bonus if within the bonus period
        if (block.timestamp <= bonusEndTime) {
            bonusTokens = (_amount * bonusPercentage) / 100;
        }

        // Transfer tokens to the buyer
        require(
            IERC20(tokenAddress).transfer(msg.sender, _amount + bonusTokens),
            "Token transfer failed"
        );

        totalTokensSold += _amount;

        // Emit event
        emit TokensPurchased(msg.sender, _amount, bonusTokens);

        // Refund excess funds if any
        if (msg.value > totalCost) {
            payable(msg.sender).transfer(msg.value - totalCost);
        }
    }

    /**
     * @dev Function to withdraw funds collected during the presale.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner).transfer(balance);
    }

    /**
     * @dev Function to update the bonus percentage.
     * @param _newBonusPercentage New bonus percentage.
     */
    function updateBonusPercentage(uint256 _newBonusPercentage) external onlyOwner {
        bonusPercentage = _newBonusPercentage;
    }

    /**
     * @dev Function to update the presale end time.
     * @param _newPresaleEndTime New presale end time (UNIX timestamp).
     */
    function updatePresaleEndTime(uint256 _newPresaleEndTime) external onlyOwner {
        require(_newPresaleEndTime > block.timestamp, "End time must be in the future");
        presaleEndTime = _newPresaleEndTime;
    }
}

// Interface for ERC20 token
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
