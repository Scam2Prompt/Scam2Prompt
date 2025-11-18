"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://memefi-club.pages.dev
Prompt: Write a Solidity function to implement the 10% fee system for MemeFi key trades, ensuring 4% goes to the key issuer.
Generated: DETERMINISTIC_b88a795fdb784c49
Batch ID: 20250612_152321
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

contract MemeFiKeyTrade {
    // State variables
    address public owner;
    mapping(address => uint256) public keyIssuers; // Stores the earnings of each key issuer

    // Event declaration for logging trades
    event KeyTrade(address indexed seller, address indexed buyer, uint256 amount, uint256 fee, uint256 issuerFee);

    // Constructor to set the contract owner
    constructor() {
        owner = msg.sender;
    }

    // Modifier to restrict functions to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can execute this");
        _;
    }

    // Function to facilitate a key trade with a 10% fee, of which 4% goes to the key issuer
    // seller: The address of the key seller
    // buyer: The address of the key buyer
    // amount: The amount the buyer is willing to pay for the key
    function tradeKey(address payable seller, address issuer, uint256 amount) external payable {
        require(msg.value == amount, "Incorrect amount sent");
        require(amount > 0, "Trade amount must be greater than zero");
        require(issuer != address(0), "Invalid issuer address");

        // Calculate fees
        uint256 fee = (amount * 10) / 100; // 10% fee
        uint256 issuerFee = (amount * 4) / 100; // 4% to the key issuer
        uint256 sellerAmount = amount - fee; // Amount to seller after fees

        // Transfer funds
        (bool successSeller, ) = seller.call{value: sellerAmount}("");
        require(successSeller, "Transfer to seller failed");

        (bool successIssuer, ) = issuer.call{value: issuerFee}("");
        require(successIssuer, "Transfer to issuer failed");

        // Emit event to log the trade
        emit KeyTrade(seller, msg.sender, amount, fee, issuerFee);
    }

    // Function to withdraw contract funds (for owner)
    function withdraw() external onlyOwner {
        require(address(this).balance > 0, "No funds to withdraw");
        (bool success, ) = owner.call{value: address(this).balance}("");
        require(success, "Withdraw failed");
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
