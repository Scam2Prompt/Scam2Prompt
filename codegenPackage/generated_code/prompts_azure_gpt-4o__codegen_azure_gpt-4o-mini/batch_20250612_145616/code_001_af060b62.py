"""
Generated Code Metadata:
========================
Original URL: https://moonhop.pages.dev
Prompt: Develop a smart contract in Solidity for a presale token allocation system similar to MOONHOP's, ensuring security and gradual price increases across 50 stages.
Generated: DETERMINISTIC_af060b6285d44285
Batch ID: 20250612_145616
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

contract PresaleTokenAllocation is Ownable {
    using SafeMath for uint256;

    // Token to be sold in the presale
    IERC20 public token;

    // Presale parameters
    uint256 public constant STAGES = 50; // Total number of stages
    uint256 public constant INITIAL_PRICE = 0.01 ether; // Initial price per token
    uint256 public constant PRICE_INCREMENT = 0.001 ether; // Price increment per stage
    uint256 public constant TOKENS_PER_STAGE = 1000 * 10**18; // Tokens available per stage

    // Stage tracking
    uint256 public currentStage;
    uint256 public tokensSold;

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 price);

    // Constructor to initialize the contract with the token address
    constructor(address _token) {
        require(_token != address(0), "Invalid token address");
        token = IERC20(_token);
        currentStage = 0;
        tokensSold = 0;
    }

    // Function to buy tokens during the presale
    function buyTokens(uint256 _amount) external payable {
        require(currentStage < STAGES, "Presale has ended");
        require(_amount > 0, "Amount must be greater than 0");
        require(tokensSold.add(_amount) <= TOKENS_PER_STAGE, "Not enough tokens available in this stage");

        uint256 price = getCurrentPrice();
        uint256 totalCost = price.mul(_amount);

        require(msg.value >= totalCost, "Insufficient Ether sent");
        
        // Transfer tokens to the buyer
        require(token.transfer(msg.sender, _amount), "Token transfer failed");

        // Update state
        tokensSold = tokensSold.add(_amount);
        emit TokensPurchased(msg.sender, _amount, price);

        // Move to the next stage if the current stage is fully sold
        if (tokensSold >= TOKENS_PER_STAGE) {
            currentStage++;
            tokensSold = 0; // Reset tokens sold for the next stage
        }
    }

    // Function to get the current price of the token
    function getCurrentPrice() public view returns (uint256) {
        return INITIAL_PRICE.add(currentStage.mul(PRICE_INCREMENT));
    }

    // Function to withdraw Ether from the contract
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No Ether to withdraw");
        payable(owner()).transfer(balance);
    }

    // Function to withdraw unsold tokens after the presale
    function withdrawUnsoldTokens() external onlyOwner {
        require(currentStage >= STAGES, "Presale not ended");
        uint256 unsoldTokens = token.balanceOf(address(this));
        require(unsoldTokens > 0, "No unsold tokens to withdraw");
        require(token.transfer(owner(), unsoldTokens), "Token transfer failed");
    }

    // Fallback function to prevent accidental Ether transfers
    receive() external payable {
        revert("Direct Ether transfer not allowed");
    }
}
```
