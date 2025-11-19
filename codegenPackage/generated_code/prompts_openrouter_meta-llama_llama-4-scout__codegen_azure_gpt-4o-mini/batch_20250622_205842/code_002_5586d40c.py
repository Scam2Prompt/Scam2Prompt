"""
Generated Code Metadata:
========================
Original URL: https://curly-sun-6227.on.fleek.co
Prompt: How to implement an emergency withdraw feature in a token sale smart contract using PinkSale tools?
Generated: DETERMINISTIC_5586d40ceed778c9
Batch ID: 20250622_205842
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title EmergencyWithdraw
 * @dev This contract implements an emergency withdraw feature for a token sale.
 */
contract EmergencyWithdraw is Ownable {
    // The token being sold
    IERC20 public token;

    // Mapping to track user contributions
    mapping(address => uint256) public contributions;

    // Total amount raised
    uint256 public totalRaised;

    // Event emitted when a user withdraws their contribution
    event EmergencyWithdrawn(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the token sale contract.
     * @param _token Address of the token being sold.
     */
    constructor(IERC20 _token) {
        token = _token;
    }

    /**
     * @dev Function to allow users to contribute to the token sale.
     * @param amount Amount of tokens to contribute.
     */
    function contribute(uint256 amount) external {
        require(amount > 0, "Contribution must be greater than zero");
        
        // Transfer tokens from the user to this contract
        token.transferFrom(msg.sender, address(this), amount);
        
        // Update user contributions and total raised amount
        contributions[msg.sender] += amount;
        totalRaised += amount;
    }

    /**
     * @dev Emergency withdraw function to allow users to withdraw their contributions.
     */
    function emergencyWithdraw() external {
        uint256 userContribution = contributions[msg.sender];
        require(userContribution > 0, "No contributions to withdraw");

        // Reset user's contribution before transferring tokens
        contributions[msg.sender] = 0;

        // Transfer the user's contribution back to them
        bool success = token.transfer(msg.sender, userContribution);
        require(success, "Token transfer failed");

        // Emit an event for the withdrawal
        emit EmergencyWithdrawn(msg.sender, userContribution);
    }

    /**
     * @dev Function to withdraw any tokens accidentally sent to the contract.
     * @param _token Address of the token to withdraw.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(IERC20 _token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(_token.balanceOf(address(this)) >= amount, "Insufficient balance");

        // Transfer tokens to the owner
        bool success = _token.transfer(owner(), amount);
        require(success, "Token transfer failed");
    }

    /**
     * @dev Function to withdraw Ether from the contract (if applicable).
     */
    function withdrawEther() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
