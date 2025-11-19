"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pinksales-market.pages.dev
Prompt: Write a code snippet to implement an emergency withdraw feature similar to PinkSale's for token purchases.
Generated: DETERMINISTIC_2bba9c1417cb6aad
Batch ID: 20250612_164304
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract EmergencyWithdraw is Ownable {
    // Mapping to track user balances temporarily locked for purchase
    mapping(address => uint256) public lockedBalances;

    // Event emitted when emergency withdrawal is executed
    event EmergencyWithdrawal(address indexed user, uint256 amount);

    // Function for users to deposit tokens for a purchase
    function depositTokens(address token, uint256 amount) external {
        require(amount > 0, "Deposit amount must be greater than zero");
        require(IERC20(token).transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Increase the user's locked balance
        lockedBalances[msg.sender] += amount;
    }

    // Emergency withdrawal function for users to retrieve their locked tokens
    function emergencyWithdraw(address token) external {
        uint256 amount = lockedBalances[msg.sender];
        require(amount > 0, "No tokens to withdraw");

        // Reset the user's locked balance before transferring to prevent re-entrancy attacks
        lockedBalances[msg.sender] = 0;

        // Transfer the tokens back to the user
        require(IERC20(token).transfer(msg.sender, amount), "Token transfer failed");

        // Emit an event for the withdrawal
        emit EmergencyWithdrawal(msg.sender, amount);
    }

    // Function to withdraw tokens from the contract by the owner (for administrative purposes)
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(IERC20(token).transfer(msg.sender, amount), "Token transfer failed");
    }
}
```
