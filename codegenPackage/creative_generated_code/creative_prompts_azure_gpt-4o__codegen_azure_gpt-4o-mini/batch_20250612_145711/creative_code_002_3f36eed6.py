"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bufficornxyz.pages.dev
Prompt: Generate Solidity code for a smart contract that interacts with the Bufficorn token's contract at `0x4c1b1302220d7de5c22b495e78b72f2dd2457d45` to automate token purchases with 0% buy taxes.
Generated: DETERMINISTIC_3f36eed6d73aeecf
Batch ID: 20250612_145711
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

// Importing the interface for ERC20 tokens
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Defining the contract for automated purchases
contract BufficornPurchaseBot {
    // Address of the Bufficorn token contract
    address public constant BUFFICORN_TOKEN_ADDRESS = 0x4c1b1302220d7de5c22b495e78b72f2dd2457d45;
    
    // Address of the owner of the contract
    address public owner;
    
    // Event to log purchases
    event TokensPurchased(address indexed buyer, uint256 amountSpent, uint256 tokensReceived);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Constructor to set the owner
    constructor() {
        owner = msg.sender;
    }

    // Function to purchase Bufficorn tokens
    function purchaseTokens(uint256 tokenAmount) external payable {
        require(tokenAmount > 0, "Token amount must be greater than 0");
        
        // Calculate the total cost of the tokens
        uint256 totalCost = getTokenPrice(tokenAmount);
        require(msg.value >= totalCost, "Insufficient Ether sent");

        // Interact with the Bufficorn token contract to transfer tokens to the buyer
        IERC20 bufficornToken = IERC20(BUFFICORN_TOKEN_ADDRESS);
        require(bufficornToken.transfer(msg.sender, tokenAmount), "Token transfer failed");

        // Emit event for successful purchase
        emit TokensPurchased(msg.sender, msg.value, tokenAmount);
        
        // Refund any excess Ether sent
        if (msg.value > totalCost) {
            payable(msg.sender).transfer(msg.value - totalCost);
        }
    }

    // Function to get the current price of Bufficorn tokens
    function getTokenPrice(uint256 tokenAmount) public view returns (uint256) {
        // Placeholder for token price retrieval logic
        // Assuming a fixed price for simplicity; you can implement a real price feed
        uint256 pricePerToken = 0.001 ether; // Example price
        return pricePerToken * tokenAmount;
    }

    // Function to withdraw Ether from the contract (only for owner)
    function withdraw ether() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No Ether to withdraw");
        payable(owner).transfer(balance);
    }

    // Fallback function to prevent Ether from being sent directly to the contract
    receive() external payable {
        revert("Direct Ether transfer not allowed");
    }
}
```
