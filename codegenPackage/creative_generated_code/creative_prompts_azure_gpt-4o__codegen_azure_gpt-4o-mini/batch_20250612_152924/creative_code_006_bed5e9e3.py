"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ututu.pages.dev
Prompt: Provide an example of a smart contract that includes a "BUY" function for purchasing SHROOM tokens during the presale, with the rate of 0.1 ETH = 99,500 SHROOM.
Generated: DETERMINISTIC_bed5e9e33d8b5cca
Batch ID: 20250612_152924
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

// Importing OpenZeppelin's ERC20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for SHROOM token presale
contract SHROOMPresale is Ownable {
    // The token being sold
    IERC20 public shroomToken;

    // Presale parameters
    uint256 public constant RATE = 99500; // 0.1 ETH = 99,500 SHROOM
    uint256 public constant MIN_PURCHASE = 0.1 ether; // Minimum purchase in ETH
    uint256 public totalSold;

    // Event for tracking purchases
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 cost);

    // Constructor to set the token address
    constructor(address _shroomToken) {
        require(_shroomToken != address(0), "Invalid token address");
        shroomToken = IERC20(_shroomToken);
    }

    // Function to buy SHROOM tokens
    function buyTokens() external payable {
        // Check if the sent value is at least the minimum purchase
        require(msg.value >= MIN_PURCHASE, "Insufficient ETH sent");

        // Calculate the amount of SHROOM tokens to purchase
        uint256 tokenAmount = (msg.value * RATE) / 1 ether;

        // Ensure the presale has enough tokens available
        require(shroomToken.balanceOf(address(this)) >= tokenAmount, "Not enough tokens in presale");

        // Transfer SHROOM tokens to the buyer
        shroomToken.transfer(msg.sender, tokenAmount);

        // Update total sold
        totalSold += tokenAmount;

        // Emit event for purchase
        emit TokensPurchased(msg.sender, tokenAmount, msg.value);
    }

    // Function to withdraw ETH from the contract (only owner)
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Function to withdraw unsold tokens after presale ends (only owner)
    function withdrawUnsoldTokens() external onlyOwner {
        uint256 unsoldTokens = shroomToken.balanceOf(address(this));
        require(unsoldTokens > 0, "No unsold tokens to withdraw");
        shroomToken.transfer(owner(), unsoldTokens);
    }

    // Fallback function to prevent ETH from being sent directly to the contract
    receive() external payable {
        revert("Direct ETH transfers not allowed; use buyTokens function.");
    }
}
```
