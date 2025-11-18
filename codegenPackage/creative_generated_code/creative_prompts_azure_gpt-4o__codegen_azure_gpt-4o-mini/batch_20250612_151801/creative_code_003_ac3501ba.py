"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://binnance.app
Prompt: Write a Solidity smart contract that verifies wallet connections and allows users to claim a gift between $100 and $500 in the $ZEUS ecosystem.
Generated: DETERMINISTIC_ac3501ba2054c1e9
Batch ID: 20250612_151801
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

contract ZeusGift {
    // State variables
    address public owner; // Contract owner
    mapping(address => bool) public claimed; // Track if the user has claimed their gift
    mapping(address => uint256) public userBalances; // Track user balances for gift amounts

    // Event to emit when a user claims a gift
    event GiftClaimed(address indexed user, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can execute this function");
        _;
    }

    // Constructor to set the contract owner
    constructor() {
        owner = msg.sender;
    }

    // Function to claim a gift
    function claimGift(uint256 amount) external {
        // Check if the gift has already been claimed
        require(!claimed[msg.sender], "Gift already claimed");
        // Validate the gift amount is between $100 and $500 (assuming 18 decimals)
        require(amount >= 100 * 10**18 && amount <= 500 * 10**18, "Invalid gift amount");

        // Mark the gift as claimed
        claimed[msg.sender] = true;

        // Update user balance
        userBalances[msg.sender] = amount;

        // Emit an event for claiming the gift
        emit GiftClaimed(msg.sender, amount);
    }

    // Function to withdraw the claimed gift (only callable by the owner for security reasons)
    function withdraw(address payable recipient) external onlyOwner {
        require(address(this).balance > 0, "No funds to withdraw");
        recipient.transfer(address(this).balance);
    }

    // Fallback function to accept Ether payments
    receive() external payable {}

    // Function to check the contract balance
    function contractBalance() external view returns (uint256) {
        return address(this).balance;
    }

    // Utility function to check if a user has claimed their gift
    function hasClaimed(address user) external view returns (bool) {
        return claimed[user];
    }
}
```
