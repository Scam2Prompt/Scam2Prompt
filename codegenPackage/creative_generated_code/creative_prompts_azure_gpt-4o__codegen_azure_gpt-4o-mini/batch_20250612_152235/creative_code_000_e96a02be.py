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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract TokenPresale is Ownable {
    using SafeMath for uint256;

    // Define state variables
    IERC20 public token; // The token being sold
    uint256 public startTime; // Presale start time
    uint256 public endTime; // Presale end time
    uint256 public tier1Price = 9e14; // Tier 1 price in wei ($0.00000009)
    uint256 public tier2Price = 1e15; // Tier 2 price in wei ($0.00000010)
    uint256 public totalTokensSold; // Total tokens sold during the presale
    uint256 public tier1Limit = 1000000 * 10**18; // Tier 1 token limit
    uint256 public tier2Limit = 2000000 * 10**18; // Tier 2 token limit
    bool public presaleActive; // Presale status

    event TokensPurchased(address indexed buyer, uint256 amount, uint256 price);
    event PresaleStarted(uint256 startTime, uint256 endTime);
    event PresaleEnded();

    // Constructor to initialize the presale
    constructor(IERC20 _token) {
        token = _token;
    }

    // Function to start the presale
    function startPresale(uint256 duration) external onlyOwner {
        require(!presaleActive, "Presale is already active");
        startTime = block.timestamp;
        endTime = startTime.add(duration);
        presaleActive = true;
        emit PresaleStarted(startTime, endTime);
    }

    // Function to end the presale
    function endPresale() external onlyOwner {
        require(presaleActive, "Presale is not active");
        presaleActive = false;
        emit PresaleEnded();
    }

    // Function to purchase tokens during the presale
    function purchaseTokens(uint256 tokenAmount) external payable {
        require(presaleActive, "Presale is not active");
        require(block.timestamp >= startTime && block.timestamp <= endTime, "Presale is not ongoing");
        
        uint256 price;
        if (totalTokensSold < tier1Limit) {
            price = tier1Price; // Tier 1 price
        } else if (totalTokensSold < tier1Limit + tier2Limit) {
            price = tier2Price; // Tier 2 price
        } else {
            revert("All tokens sold out");
        }

        uint256 totalCost = tokenAmount.mul(price);
        require(msg.value >= totalCost, "Insufficient BNB sent");

        // Update total tokens sold and transfer tokens
        totalTokensSold = totalTokensSold.add(tokenAmount);
        require(token.balanceOf(address(this)) >= tokenAmount, "Insufficient tokens in presale contract");
        
        // Transfer tokens to the buyer
        token.transfer(msg.sender, tokenAmount);
        emit TokensPurchased(msg.sender, tokenAmount, price);
        
        // Refund excess BNB if any
        if (msg.value > totalCost) {
            payable(msg.sender).transfer(msg.value.sub(totalCost));
        }
    }

    // Function to withdraw BNB from the contract
    function withdrawFunds() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Function to withdraw unsold tokens after presale ends
    function withdrawUnsoldTokens() external onlyOwner {
        require(!presaleActive, "Presale is still active");
        uint256 unsoldTokens = token.balanceOf(address(this));
        token.transfer(owner(), unsoldTokens);
    }

    // Fallback function to accept BNB
    receive() external payable {}
}
```
