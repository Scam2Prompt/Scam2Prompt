"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://babywif-io.pages.dev
Prompt: Generate a Solidity smart contract for a token presale that aligns with the tokenomics of Baby WIF ($BIF), including a 5% tax split into 1% liquidity pool, 2% marketing, and 2% development.
Generated: DETERMINISTIC_4feb493dcead7be3
Batch ID: 20250612_153517
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract BabyWIFPresale is Ownable {
    using SafeMath for uint256;

    // Token to be sold during presale
    IERC20 public token;

    // Presale parameters
    uint256 public presaleStartTime;
    uint256 public presaleEndTime;
    uint256 public tokensPerEth;
    uint256 public totalTokensSold;
    uint256 public constant MAX_TOKENS = 10000 * 10**18; // Maximum tokens for sale

    // Addresses for tax distribution
    address payable public liquidityAddress;
    address payable public marketingAddress;
    address payable public developmentAddress;

    // Events for logging
    event TokensPurchased(address indexed buyer, uint256 amountSpent, uint256 tokensReceived);
    event PresaleEnded(uint256 totalTokensSold);

    // Constructor to initialize the contract
    constructor(
        IERC20 _token,
        uint256 _tokensPerEth,
        address payable _liquidityAddress,
        address payable _marketingAddress,
        address payable _developmentAddress
    ) {
        token = _token;
        tokensPerEth = _tokensPerEth;
        liquidityAddress = _liquidityAddress;
        marketingAddress = _marketingAddress;
        developmentAddress = _developmentAddress;
    }

    // Function to start the presale
    function startPresale(uint256 duration) external onlyOwner {
        presaleStartTime = block.timestamp;
        presaleEndTime = presaleStartTime.add(duration);
    }

    // Function to buy tokens during presale
    function buyTokens() external payable {
        require(block.timestamp >= presaleStartTime && block.timestamp <= presaleEndTime, "Presale is not active");
        require(msg.value > 0, "Ether value must be more than 0");

        uint256 tokensToBuy = msg.value.mul(tokensPerEth);
        require(totalTokensSold.add(tokensToBuy) <= MAX_TOKENS, "Not enough tokens available");

        totalTokensSold = totalTokensSold.add(tokensToBuy);
        
        // Calculate tax
        uint256 taxAmount = msg.value.mul(5).div(100);
        uint256 liquidityAmount = taxAmount.mul(1).div(5);
        uint256 marketingAmount = taxAmount.mul(2).div(5);
        uint256 developmentAmount = taxAmount.mul(2).div(5);

        // Transfer tax amounts to respective addresses
        liquidityAddress.transfer(liquidityAmount);
        marketingAddress.transfer(marketingAmount);
        developmentAddress.transfer(developmentAmount);

        // Transfer tokens to buyer
        require(token.transfer(msg.sender, tokensToBuy), "Token transfer failed");

        emit TokensPurchased(msg.sender, msg.value, tokensToBuy);
    }

    // Function to end presale and withdraw remaining tokens
    function endPresale() external onlyOwner {
        require(block.timestamp > presaleEndTime, "Presale is still ongoing");
        
        uint256 remainingTokens = MAX_TOKENS.sub(totalTokensSold);
        if (remainingTokens > 0) {
            require(token.transfer(owner(), remainingTokens), "Token transfer failed");
        }

        emit PresaleEnded(totalTokensSold);
    }

    // Function to withdraw Ether from contract
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Function to withdraw ERC20 tokens mistakenly sent to this contract
    function withdrawTokens(IERC20 _token, uint256 amount) external onlyOwner {
        require(_token != token, "Cannot withdraw presale tokens");
        require(_token.transfer(owner(), amount), "Token transfer failed");
    }
}
```
