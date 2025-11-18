"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://grokxcoinai.com
Prompt: Generate a Solidity smart contract that incorporates KYC verification and prevents participation by whales, inspired by $GROK's presale strategy.
Generated: DETERMINISTIC_75406343f33aea85
Batch ID: 20250612_155102
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

/**
 * @title PresaleWithKYCAndAntiWhale
 * @dev Smart contract for a presale with KYC verification and anti-whale measures.
 */
contract PresaleWithKYCAndAntiWhale {
    // Owner of the contract
    address public owner;

    // Mapping to store KYC verification status of users
    mapping(address => bool) public isKYCVerified;

    // Maximum participation limit per address (anti-whale measure)
    uint256 public maxContribution;

    // Total amount contributed by each user
    mapping(address => uint256) public contributions;

    // Event for logging contributions
    event Contribution(address indexed user, uint256 amount);

    // Event for updating KYC verification
    event KYCVerified(address indexed user, bool status);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action");
        _;
    }

    // Constructor to initialize contract variables
    constructor(uint256 _maxContribution) {
        require(_maxContribution > 0, "Maximum contribution must be greater than 0");
        owner = msg.sender;
        maxContribution = _maxContribution;
    }

    /**
     * @dev Function to verify a user's KYC status. Only the owner can call this.
     * @param user Address of the user to verify
     * @param status KYC verification status (true for verified, false for not verified)
     */
    function verifyKYC(address user, bool status) external onlyOwner {
        require(user != address(0), "Invalid address");
        isKYCVerified[user] = status;
        emit KYCVerified(user, status);
    }

    /**
     * @dev Function for users to contribute to the presale.
     * Contribution is allowed only for KYC-verified users and below the maximum contribution limit.
     */
    function contribute() external payable {
        require(isKYCVerified[msg.sender], "KYC verification required to participate");
        require(msg.value > 0, "Contribution must be greater than 0");
        require(contributions[msg.sender] + msg.value <= maxContribution, "Contribution exceeds maximum limit");

        // Update user's contribution amount
        contributions[msg.sender] += msg.value;

        // Emit the contribution event
        emit Contribution(msg.sender, msg.value);
    }

    /**
     * @dev Function to withdraw funds. Only the owner can call this.
     */
    function withdrawFunds() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No funds to withdraw");

        // Transfer balance to the owner
        (bool success, ) = owner.call{value: contractBalance}("");
        require(success, "Withdrawal failed");
    }
}
```
