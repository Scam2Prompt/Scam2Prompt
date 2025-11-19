"""
Generated Code Metadata:
========================
Original URL: https://berryeth.vip
Prompt: Generate Solidity code for a smart contract that integrates with the $BERRY token, allowing users to claim tokens based on specific conditions.
Generated: DETERMINISTIC_fa58975309de691f
Batch ID: 20250612_153947
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

// Interface for the ERC20 token standard
interface IBerryToken {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

// Smart contract for claiming $BERRY tokens
contract BerryClaim {
    // State variables
    IBerryToken public berryToken; // Instance of the $BERRY token contract
    address public owner; // Owner of the contract
    mapping(address => uint256) public claims; // Track claims for each user

    // Events
    event TokensClaimed(address indexed user, uint256 amount);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Constructor to initialize the contract with the $BERRY token address
    constructor(address _berryToken) {
        require(_berryToken != address(0), "Invalid token address");
        berryToken = IBerryToken(_berryToken);
        owner = msg.sender; // Set the contract deployer as the owner
    }

    // Function to claim $BERRY tokens based on specific conditions
    function claimTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(claims[msg.sender] + amount <= 100 * 10**18, "Claim limit exceeded"); // Example condition

        // Update the user's claim amount
        claims[msg.sender] += amount;

        // Transfer $BERRY tokens to the user
        require(berryToken.transfer(msg.sender, amount), "Token transfer failed");

        // Emit an event for the claim
        emit TokensClaimed(msg.sender, amount);
    }

    // Function to withdraw tokens from the contract (only owner)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(berryToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");
        require(berryToken.transfer(owner, amount), "Token transfer failed");
    }

    // Function to transfer ownership of the contract
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner is the zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    // Function to check the contract's balance of $BERRY tokens
    function contractBalance() external view returns (uint256) {
        return berryToken.balanceOf(address(this));
    }
}
```
