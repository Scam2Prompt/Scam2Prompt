"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hamster-ico.pages.dev
Prompt: Write a smart contract in Solidity to implement a token sale for $HMSTR tokens, including a pricing mechanism of $0.00001 per token and a wallet connection feature.
Generated: DETERMINISTIC_fd5b86569ac3ebf8
Batch ID: 20250612_152240
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

// Importing OpenZeppelin's ERC20 interface for token standard compliance
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Address.sol";

// Token Sale Contract for $HMSTR tokens
contract TokenSale is Ownable {
    using Address for address;

    // State variables
    IERC20 public token; // Token being sold
    uint256 public pricePerToken; // Price per token in wei

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);

    // Constructor to initialize the token sale
    constructor(address _tokenAddress) {
        require(_tokenAddress.isContract(), "Token address must be a contract");
        token = IERC20(_tokenAddress);
        pricePerToken = 0.00001 ether; // Set token price to $0.00001 (in wei)
    }

    // Function to buy tokens
    function buyTokens(uint256 _numTokens) external payable {
        require(_numTokens > 0, "Must purchase at least one token");
        require(msg.value == _numTokens * pricePerToken, "Incorrect Ether value sent");

        uint256 totalCost = _numTokens * pricePerToken;
        require(token.balanceOf(address(this)) >= _numTokens, "Not enough tokens in the reserve");

        // Transfer tokens to buyer
        token.transfer(msg.sender, _numTokens);
        
        // Emit an event for the purchase
        emit TokensPurchased(msg.sender, _numTokens);
    }

    // Function to withdraw Ether from the contract
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No Ether to withdraw");

        // Transfer Ether to owner
        payable(owner()).transfer(balance);
    }

    // Function to update the token price (only owner)
    function setTokenPrice(uint256 _newPrice) external onlyOwner {
        require(_newPrice > 0, "Price must be greater than zero");
        pricePerToken = _newPrice;
    }

    // Fallback function to prevent Ether from being sent directly to the contract
    receive() external payable {
        revert("Direct Ether transfer not allowed");
    }
}
```
