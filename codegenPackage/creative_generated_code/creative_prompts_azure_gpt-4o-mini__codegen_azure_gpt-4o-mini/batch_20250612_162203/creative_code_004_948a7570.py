"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ccatctactatcatc.pages.dev
Prompt: Illustrate how to implement a buy function for Catcoin ($CAT) using Solidity smart contracts with no tax implications.
Generated: DETERMINISTIC_948a7570e0ae1728
Batch ID: 20250612_162203
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

// Import OpenZeppelin's ERC20 token implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Catcoin contract inheriting from ERC20 and Ownable
contract Catcoin is ERC20, Ownable {
    
    // Events for logging purchases
    event BuyCatcoin(address indexed buyer, uint256 amountSpent, uint256 amountReceived);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("Catcoin", "CAT") {
        // Mint initial supply to the contract owner
        _mint(msg.sender, 1000000 * 10 ** decimals()); // 1 million tokens
    }

    // Function to buy Catcoin
    // Accepts Ether and calculates the amount of CAT to mint
    function buyCatcoin() external payable {
        require(msg.value > 0, "You must send Ether to buy Catcoin");

        // Set a fixed exchange rate (e.g., 1 ETH = 1000 CAT)
        uint256 exchangeRate = 1000;
        uint256 amountToMint = msg.value * exchangeRate;

        // Check if the contract has enough tokens to sell
        require(balanceOf(owner()) >= amountToMint, "Not enough tokens available for sale");

        // Transfer the CAT tokens from the owner to the buyer
        _transfer(owner(), msg.sender, amountToMint);

        // Emit event for the purchase
        emit BuyCatcoin(msg.sender, msg.value, amountToMint);
    }

    // Function to withdraw contract balance to the owner
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No Ether to withdraw");
        
        // Transfer Ether to the owner
        payable(owner()).transfer(balance);
    }

    // Fallback function to accept Ether
    receive() external payable {
        buyCatcoin();
    }

    // Fallback function to handle unexpected calls
    fallback() external payable {
        revert("Invalid function call");
    }
}
```
