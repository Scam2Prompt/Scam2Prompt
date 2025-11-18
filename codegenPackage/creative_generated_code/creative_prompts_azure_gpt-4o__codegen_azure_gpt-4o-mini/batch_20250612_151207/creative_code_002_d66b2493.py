"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blockdag-buynow.pages.dev
Prompt: Develop a smart contract in Solidity that implements a referral system offering a 10% bonus for BDAG presale investments, as described on the BlockDAG platform.
Generated: DETERMINISTIC_d66b2493ebc05f5b
Batch ID: 20250612_151207
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

// This contract implements a referral system for a BDAG presale investment
contract BDAGPresale {
    // Store the total investment and mapping of referrals
    uint256 public totalInvested;
    uint256 public constant BONUS_PERCENTAGE = 10; // 10% bonus
    address public owner;

    // Mapping from investor address to referral address
    mapping(address => address) public referrals;
    // Mapping from investor address to the amount they invested
    mapping(address => uint256) public investments;

    // Event emitted when a new investment is made
    event InvestmentMade(address indexed investor, uint256 amount, address indexed referrer);
    
    // Modifier to check if caller is the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Constructor to set the owner of the contract
    constructor() {
        owner = msg.sender;
    }

    // Function to invest in BDAG presale with an optional referral
    function invest(address referrer) external payable {
        require(msg.value > 0, "Investment amount must be greater than zero");

        // Update total invested amount
        totalInvested += msg.value;

        // Handle referral logic
        if (referrer != address(0) && referrer != msg.sender) {
            referrals[msg.sender] = referrer;
            uint256 bonus = (msg.value * BONUS_PERCENTAGE) / 100; // Calculate 10% bonus
            payable(referrer).transfer(bonus); // Transfer bonus to referrer
        }

        // Record the investment
        investments[msg.sender] += msg.value;

        // Emit the investment event
        emit InvestmentMade(msg.sender, msg.value, referrer);
    }

    // Function to withdraw funds (only callable by the owner)
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        // Transfer the balance to the owner
        payable(owner).transfer(balance);
    }

    // Function to get the investment of a specific investor
    function getInvestment(address investor) external view returns (uint256) {
        return investments[investor];
    }

    // Function to get the total funds raised
    function getTotalInvested() external view returns (uint256) {
        return totalInvested;
    }
}
```
