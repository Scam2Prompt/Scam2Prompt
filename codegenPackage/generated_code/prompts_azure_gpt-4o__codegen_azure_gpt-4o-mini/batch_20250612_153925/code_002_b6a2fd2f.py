"""
Generated Code Metadata:
========================
Original URL: https://berrycoinerc.vip
Prompt: Generate Solidity code for a new smart contract that integrates with the $BERRY token and adds a feature for tracking community contributions.
Generated: DETERMINISTIC_b6a2fd2f0011fe37
Batch ID: 20250612_153925
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

// Interface for the $BERRY token
interface IBerryToken {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

// Smart contract for tracking community contributions
contract CommunityContributionTracker {
    // State variables
    IBerryToken public berryToken; // Instance of the $BERRY token
    address public owner; // Owner of the contract
    mapping(address => uint256) public contributions; // Mapping to track contributions by address

    // Events
    event ContributionReceived(address indexed contributor, uint256 amount);
    event OwnerChanged(address indexed previousOwner, address indexed newOwner);

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

    // Function to contribute to the community
    function contribute(uint256 amount) external {
        require(amount > 0, "Contribution amount must be greater than zero");
        
        // Transfer $BERRY tokens from the contributor to this contract
        bool success = berryToken.transfer(address(this), amount);
        require(success, "Token transfer failed");

        // Update the contributions mapping
        contributions[msg.sender] += amount;

        // Emit an event for the contribution
        emit ContributionReceived(msg.sender, amount);
    }

    // Function to get the contribution amount of a specific address
    function getContribution(address contributor) external view returns (uint256) {
        return contributions[contributor];
    }

    // Function to change the owner of the contract
    function changeOwner(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner is the zero address");
        emit OwnerChanged(owner, newOwner);
        owner = newOwner; // Update the owner
    }

    // Function to withdraw tokens from the contract (only by owner)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(berryToken.balanceOf(address(this)) >= amount, "Insufficient balance");

        // Transfer the specified amount of $BERRY tokens to the owner
        bool success = berryToken.transfer(owner, amount);
        require(success, "Token withdrawal failed");
    }
}
```
