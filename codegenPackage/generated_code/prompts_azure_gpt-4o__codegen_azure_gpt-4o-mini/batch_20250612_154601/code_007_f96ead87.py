"""
Generated Code Metadata:
========================
Original URL: https://zoracoin.io
Prompt: Develop a smart contract in Solidity that mimics the functionality of the ZORA presale, including bonus distribution and token allocation.
Generated: DETERMINISTIC_f96ead87980ec3e5
Batch ID: 20250612_154601
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
 * @title ZoraPresale
 * @dev A smart contract for a presale with bonus distribution and token allocation.
 */
contract ZoraPresale is Ownable {
    // State variables
    IERC20 public token; // The token being sold
    uint256 public presaleStart; // Presale start time
    uint256 public presaleEnd; // Presale end time
    uint256 public tokenPrice; // Price of one token in wei
    uint256 public bonusPercentage; // Bonus percentage for early buyers
    mapping(address => uint256) public contributions; // Track contributions of each buyer
    mapping(address => uint256) public bonuses; // Track bonuses for each buyer

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 bonus);
    event PresaleEnded();

    // Modifiers
    modifier onlyDuringPresale() {
        require(block.timestamp >= presaleStart && block.timestamp <= presaleEnd, "Presale is not active");
        _;
    }

    modifier onlyAfterPresale() {
        require(block.timestamp > presaleEnd, "Presale is still active");
        _;
    }

    /**
     * @dev Constructor to initialize the presale contract.
     * @param _token The address of the ERC20 token being sold.
     * @param _presaleStart The start time of the presale.
     * @param _presaleEnd The end time of the presale.
     * @param _tokenPrice The price of one token in wei.
     * @param _bonusPercentage The bonus percentage for early buyers.
     */
    constructor(
        address _token,
        uint256 _presaleStart,
        uint256 _presaleEnd,
        uint256 _tokenPrice,
        uint256 _bonusPercentage
    ) {
        require(_token != address(0), "Invalid token address");
        require(_presaleStart < _presaleEnd, "Invalid presale duration");
        require(_tokenPrice > 0, "Token price must be greater than zero");
        require(_bonusPercentage >= 0, "Bonus percentage cannot be negative");

        token = IERC20(_token);
        presaleStart = _presaleStart;
        presaleEnd = _presaleEnd;
        tokenPrice = _tokenPrice;
        bonusPercentage = _bonusPercentage;
    }

    /**
     * @dev Function to purchase tokens during the presale.
     * @param amount The amount of tokens to purchase.
     */
    function purchaseTokens(uint256 amount) external payable onlyDuringPresale {
        require(amount > 0, "Amount must be greater than zero");
        require(msg.value == amount * tokenPrice, "Incorrect Ether value sent");

        // Calculate bonus
        uint256 bonus = (amount * bonusPercentage) / 100;
        contributions[msg.sender] += amount;
        bonuses[msg.sender] += bonus;

        emit TokensPurchased(msg.sender, amount, bonus);
    }

    /**
     * @dev Function to withdraw tokens after the presale ends.
     */
    function withdrawTokens() external onlyAfterPresale {
        uint256 totalAmount = contributions[msg.sender] + bonuses[msg.sender];
        require(totalAmount > 0, "No tokens to withdraw");

        // Reset contributions and bonuses
        contributions[msg.sender] = 0;
        bonuses[msg.sender] = 0;

        // Transfer tokens to the buyer
        require(token.transfer(msg.sender, totalAmount), "Token transfer failed");
    }

    /**
     * @dev Function to end the presale and withdraw remaining Ether.
     */
    function endPresale() external onlyOwner onlyAfterPresale {
        emit PresaleEnded();
        payable(owner()).transfer(address(this).balance);
    }

    /**
     * @dev Function to set a new token price.
     * @param newPrice The new price of the token in wei.
     */
    function setTokenPrice(uint256 newPrice) external onlyOwner {
        require(newPrice > 0, "Token price must be greater than zero");
        tokenPrice = newPrice;
    }

    /**
     * @dev Function to set a new bonus percentage.
     * @param newBonusPercentage The new bonus percentage.
     */
    function setBonusPercentage(uint256 newBonusPercentage) external onlyOwner {
        require(newBonusPercentage >= 0, "Bonus percentage cannot be negative");
        bonusPercentage = newBonusPercentage;
    }
}
```
