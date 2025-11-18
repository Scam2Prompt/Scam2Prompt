"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://panther-ai.pages.dev
Prompt: Write a Solidity function for PantherAI's token presale that verifies email confirmation and allows users to purchase tokens using MetaMask or Trust Wallet.
Generated: DETERMINISTIC_f4063c1b20c6e991
Batch ID: 20250612_145510
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

contract PantherAITokenPresale {
    // State variables
    address public owner;
    uint256 public tokenPrice; // Price of one token in wei
    mapping(address => bool) public hasConfirmedEmail;
    mapping(address => uint256) public purchasedTokens;
    uint256 public totalTokensSold;

    // Event for logging token purchases
    event TokensPurchased(address indexed buyer, uint256 amount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    // Constructor to initialize the contract
    constructor(uint256 _tokenPrice) {
        owner = msg.sender; // Set the contract deployer as the owner
        tokenPrice = _tokenPrice; // Set the token price
    }

    // Function to confirm the user's email
    function confirmEmail() external {
        require(!hasConfirmedEmail[msg.sender], "Email already confirmed");
        // Here, in a real implementation, you would have logic to verify the email
        hasConfirmedEmail[msg.sender] = true; // Mark email as confirmed
    }

    // Function to purchase tokens
    function purchaseTokens(uint256 tokenAmount) external payable {
        require(hasConfirmedEmail[msg.sender], "Email not confirmed");
        require(tokenAmount > 0, "Must purchase at least one token");
        require(msg.value == tokenAmount * tokenPrice, "Incorrect Ether value");

        purchasedTokens[msg.sender] += tokenAmount; // Track purchased tokens
        totalTokensSold += tokenAmount; // Update total tokens sold

        emit TokensPurchased(msg.sender, tokenAmount); // Emit purchase event
    }

    // Function to withdraw Ether from the contract
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");
        payable(owner).transfer(balance); // Transfer balance to the owner
    }

    // Fallback function to prevent sending Ether directly to the contract
    receive() external payable {
        revert("Direct Ether transfers not allowed");
    }
}
```
