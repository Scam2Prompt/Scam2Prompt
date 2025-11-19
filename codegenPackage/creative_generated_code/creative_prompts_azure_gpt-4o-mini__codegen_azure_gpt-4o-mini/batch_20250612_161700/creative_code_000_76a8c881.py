"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ututu.pages.dev
Prompt: Generate a smart contract in Solidity for a token presale with a cap of 1000 ETH and a conversion rate of 0.1 ETH for 99,500 SHROOM tokens.
Generated: DETERMINISTIC_76a8c88115d33809
Batch ID: 20250612_161700
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

/**
 * @title TokenPresale
 * @dev Smart contract for a token presale with a cap and fixed conversion rate.
 */
contract TokenPresale is Ownable {
    // Declaring state variables
    IERC20 public token;                // The token being sold in the presale
    uint256 public constant CAP = 1000 ether; // Maximum amount of ETH that can be raised
    uint256 public constant RATE = 99500; // Number of tokens per 0.1 ETH
    uint256 public totalRaised;         // Total amount of ETH raised
    bool public presaleActive;          // Status of the presale

    // Events for logging purposes
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 cost);
    event PresaleStatusChanged(bool active);

    // Constructor to initialize the token
    constructor(IERC20 _token) {
        token = _token;
        presaleActive = false; // Presale starts off inactive
    }

    // Function to start or stop the presale
    function setPresaleStatus(bool _active) external onlyOwner {
        presaleActive = _active;
        emit PresaleStatusChanged(_active);
    }

    // Function to buy tokens during the presale
    function buyTokens() external payable {
        require(presaleActive, "Presale is not active");
        require(msg.value > 0, "Must send ETH to purchase tokens");
        
        uint256 tokensToPurchase = (msg.value * RATE) / 0.1 ether;

        // Check if the new total raised would exceed the cap
        require(totalRaised + msg.value <= CAP, "Cap exceeded");

        // Update the total raised
        totalRaised += msg.value;

        // Transfer tokens to the buyer
        require(token.balanceOf(address(this)) >= tokensToPurchase, "Not enough tokens in contract");
        token.transfer(msg.sender, tokensToPurchase);

        emit TokensPurchased(msg.sender, tokensToPurchase, msg.value);
    }

    // Function to withdraw the raised ETH to the owner's address
    function withdrawFunds() external onlyOwner {
        require(address(this).balance > 0, "No funds to withdraw");
        payable(owner()).transfer(address(this).balance);
    }

    // Function to withdraw unsold tokens back to the owner
    function withdrawUnsoldTokens() external onlyOwner {
        uint256 unsoldTokens = token.balanceOf(address(this));
        require(unsoldTokens > 0, "No tokens to withdraw");
        token.transfer(owner(), unsoldTokens);
    }

    // Fallback function to prevent accidental ETH transfers
    receive() external payable {
        revert("Direct ETH transfers not allowed. Use buyTokens function.");
    }
}
```
