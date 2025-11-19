"""
Generated Code Metadata:
========================
Original URL: https://babywif-io.pages.dev
Prompt: Generate a Solidity smart contract for a token presale that aligns with the tokenomics of Baby WIF ($BIF), including a 5% tax split into 1% liquidity pool, 2% marketing, and 2% development.
Generated: DETERMINISTIC_4feb493dcead7be3
Batch ID: 20250612_153517
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract BabyWIFPresale is Ownable {
    using SafeMath for uint256;

    // Token to be sold in the presale
    IERC20 public token;

    // Presale parameters
    uint256 public presaleStartTime;
    uint256 public presaleEndTime;
    uint256 public tokenPrice; // Price per token in wei
    uint256 public totalTokensForSale;
    uint256 public tokensSold;

    // Tax distribution
    uint256 public constant TAX_PERCENTAGE = 5;
    uint256 public constant LIQUIDITY_PERCENTAGE = 1;
    uint256 public constant MARKETING_PERCENTAGE = 2;
    uint256 public constant DEVELOPMENT_PERCENTAGE = 2;

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);
    event PresaleEnded();

    // Constructor to initialize the presale
    constructor(
        address _tokenAddress,
        uint256 _presaleStartTime,
        uint256 _presaleEndTime,
        uint256 _tokenPrice,
        uint256 _totalTokensForSale
    ) {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_presaleStartTime < _presaleEndTime, "Invalid presale time");
        require(_tokenPrice > 0, "Token price must be greater than 0");
        require(_totalTokensForSale > 0, "Total tokens must be greater than 0");

        token = IERC20(_tokenAddress);
        presaleStartTime = _presaleStartTime;
        presaleEndTime = _presaleEndTime;
        tokenPrice = _tokenPrice;
        totalTokensForSale = _totalTokensForSale;
        tokensSold = 0;
    }

    // Modifier to check if presale is active
    modifier isPresaleActive() {
        require(block.timestamp >= presaleStartTime && block.timestamp <= presaleEndTime, "Presale is not active");
        _;
    }

    // Function to purchase tokens during the presale
    function purchaseTokens(uint256 _amount) external payable isPresaleActive {
        require(msg.value == _amount.mul(tokenPrice), "Incorrect Ether value sent");
        require(tokensSold.add(_amount) <= totalTokensForSale, "Not enough tokens available");

        // Calculate tax distribution
        uint256 taxAmount = _amount.mul(TAX_PERCENTAGE).div(100);
        uint256 liquidityAmount = taxAmount.mul(LIQUIDITY_PERCENTAGE).div(TAX_PERCENTAGE);
        uint256 marketingAmount = taxAmount.mul(MARKETING_PERCENTAGE).div(TAX_PERCENTAGE);
        uint256 developmentAmount = taxAmount.mul(DEVELOPMENT_PERCENTAGE).div(TAX_PERCENTAGE);

        // Transfer tokens to the buyer
        tokensSold = tokensSold.add(_amount);
        token.transfer(msg.sender, _amount);

        // Handle tax distribution (this is a placeholder, implement actual distribution logic)
        // For example, you could send the amounts to respective addresses

        emit TokensPurchased(msg.sender, _amount);
    }

    // Function to end the presale
    function endPresale() external onlyOwner {
        require(block.timestamp > presaleEndTime, "Presale is still active");
        emit PresaleEnded();
        // Transfer remaining tokens back to owner or handle as needed
    }

    // Function to withdraw Ether from the contract
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Function to withdraw unsold tokens after presale
    function withdrawUnsoldTokens() external onlyOwner {
        uint256 unsoldTokens = totalTokensForSale.sub(tokensSold);
        require(unsoldTokens > 0, "No unsold tokens to withdraw");
        token.transfer(owner(), unsoldTokens);
    }
}
```
