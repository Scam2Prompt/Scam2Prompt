"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethermail.pages.dev
Prompt: Develop a smart contract that interacts with EtherMail's PayWall feature, allowing users to define content preferences and earn EMC rewards for promotional emails.
Generated: DETERMINISTIC_f2e4ea00aa08fe3b
Batch ID: 20250612_152249
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

// Interface for the EtherMail contract
interface IEtherMail {
    function setContentPreferences(string calldata preferences) external;
    function earnEMCRewards(uint256 amount) external;
}

// Smart contract for interacting with EtherMail's PayWall feature
contract EtherMailInteraction {
    // State variables
    IEtherMail public etherMail; // Instance of the EtherMail contract
    address public owner; // Contract owner

    // Event emitted when preferences are set
    event PreferencesSet(address indexed user, string preferences);
    
    // Event emitted when rewards are earned
    event RewardsEarned(address indexed user, uint256 amount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Constructor to initialize the contract with the EtherMail address
    constructor(address _etherMail) {
        etherMail = IEtherMail(_etherMail);
        owner = msg.sender; // Set the deployer as the owner
    }

    // Function to set content preferences for the user
    // It requires the user to provide a string of preferences
    function setPreferences(string calldata preferences) external {
        require(bytes(preferences).length > 0, "Preferences cannot be empty");
        
        // Call the EtherMail contract to set preferences
        etherMail.setContentPreferences(preferences);
        
        // Emit an event for logging purposes
        emit PreferencesSet(msg.sender, preferences);
    }

    // Function to earn EMC rewards for promotional emails
    // It requires the user to specify the amount of rewards to earn
    function earnRewards(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        
        // Call the EtherMail contract to earn rewards
        etherMail.earnEMCRewards(amount);
        
        // Emit an event for logging purposes
        emit RewardsEarned(msg.sender, amount);
    }

    // Function to withdraw ownership of the contract
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be the zero address");
        owner = newOwner; // Transfer ownership to new address
    }
}
```
