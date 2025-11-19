"""
Generated Code Metadata:
========================
Original URL: https://moxie.social
Prompt: Generate a sample smart contract that utilizes Moxie’s bonding curves to emphasize utility over speculation in token distribution.
Generated: DETERMINISTIC_5a806bbc2952e4d6
Batch ID: 20250612_162854
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

// Importing OpenZeppelin's ERC20 implementation for token standards
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// MoxieBondingCurve contract that implements a bonding curve for token distribution
contract MoxieBondingCurve is ERC20, Ownable {
    // State variables
    uint256 public constant BASE_PRICE = 0.01 ether; // Base price for the first token
    uint256 public totalSupply; // Total tokens minted
    uint256 public totalInvestment; // Total ether invested in the contract

    // Event emitted when tokens are purchased
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 cost);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("MoxieToken", "MOK") {}

    // Function to calculate the price of tokens based on the bonding curve
    function calculatePrice(uint256 _amount) public view returns (uint256) {
        require(_amount > 0, "Amount must be greater than zero");
        // Price increases quadratically based on the amount of tokens already minted
        return BASE_PRICE * (_amount ** 2);
    }

    // Function to purchase tokens
    function purchaseTokens(uint256 _amount) external payable {
        uint256 cost = calculatePrice(_amount);
        require(msg.value >= cost, "Insufficient Ether sent");

        // Mint tokens to the buyer
        _mint(msg.sender, _amount);
        totalSupply += _amount;
        totalInvestment += msg.value;

        // Emit event for the purchase
        emit TokensPurchased(msg.sender, _amount, cost);

        // Refund any excess Ether sent
        if (msg.value > cost) {
            payable(msg.sender).transfer(msg.value - cost);
        }
    }

    // Function to withdraw funds from the contract (only owner can call)
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }

    // Function to get the current price of a single token
    function getCurrentPrice() external view returns (uint256) {
        return calculatePrice(1);
    }

    // Fallback function to prevent accidental Ether transfers
    receive() external payable {
        revert("Direct Ether transfers not allowed. Use purchaseTokens instead.");
    }
}
```
