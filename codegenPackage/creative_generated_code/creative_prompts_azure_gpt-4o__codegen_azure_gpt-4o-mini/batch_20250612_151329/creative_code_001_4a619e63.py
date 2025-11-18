"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-astraworld.pages.dev
Prompt: Create a smart contract in Solidity that integrates with Astra Nova's $RVV token system, allowing users to securely purchase tokens using ETH and track their balances.
Generated: DETERMINISTIC_4a619e630cf57168
Batch ID: 20250612_151329
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

// Importing the interface for the RVV token
interface IRVVToken {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract RVVTokenSale {
    // Address of the RVV token contract
    IRVVToken public rvvToken;
    
    // Price of RVV token in wei (ETH)
    uint256 public tokenPrice;

    // Mapping to track user purchases
    mapping(address => uint256) public balances;

    // Event to log token purchases
    event TokensPurchased(address indexed buyer, uint256 amount);

    // Constructor to initialize the contract with the RVV token address and the token price
    constructor(address _rvvTokenAddress, uint256 _tokenPrice) {
        require(_rvvTokenAddress != address(0), "Invalid token address");
        require(_tokenPrice > 0, "Token price must be greater than zero");

        rvvToken = IRVVToken(_rvvTokenAddress);
        tokenPrice = _tokenPrice;
    }

    // Function to purchase RVV tokens with Ether
    function purchaseTokens(uint256 _amount) external payable {
        require(_amount > 0, "Amount must be greater than zero");
        require(msg.value == _amount * tokenPrice, "Incorrect ETH amount sent");

        // Calculate total tokens to purchase
        uint256 totalCost = _amount * tokenPrice;

        // Update user's balance
        balances[msg.sender] += _amount;

        // Transfer RVV tokens to the buyer
        bool success = rvvToken.transfer(msg.sender, _amount);
        require(success, "Token transfer failed");

        // Emit an event for the purchase
        emit TokensPurchased(msg.sender, _amount);
    }

    // Function to withdraw Ether from the contract (only owner can call this)
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No ether to withdraw");

        // Transfer the contract's Ether balance to the owner
        payable(msg.sender).transfer(balance);
    }

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        // Placeholder for owner address
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Function to check the RVV token balance of a user
    function checkBalance(address user) external view returns (uint256) {
        return rvvToken.balanceOf(user);
    }
}
```
