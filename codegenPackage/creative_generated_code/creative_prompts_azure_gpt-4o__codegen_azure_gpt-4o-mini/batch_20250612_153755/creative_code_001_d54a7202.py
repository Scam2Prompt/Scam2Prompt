"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethe.top
Prompt: Generate Solidity code for a smart contract that implements the eligibility check for the 30 ETH airdrop, referencing the verified protocol and flexible lock period features mentioned on https://ethe.top.
Generated: DETERMINISTIC_d54a7202ff626c18
Batch ID: 20250612_153755
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

/// @title AirdropEligibility
/// @notice This contract checks eligibility for a 30 ETH airdrop
/// @dev It implements flexible lock periods and references the verified protocol
contract AirdropEligibility {
    // Define a structure to hold user information
    struct User {
        bool isEligible; // Indicates if the user is eligible for airdrop
        uint256 lockPeriod; // The lock period in seconds
        uint256 lockedAmount; // Amount of ETH locked by the user
    }

    // Mapping to store user data by address
    mapping(address => User) public users;

    // Event emitted when a user locks ETH
    event ETHLocked(address indexed user, uint256 amount, uint256 lockPeriod);
    
    // Event emitted when a user is marked as eligible
    event UserEligibilityUpdated(address indexed user, bool isEligible);

    // The minimum amount required for eligibility
    uint256 public constant MINIMUM_LOCK_AMOUNT = 1 ether;

    /// @notice Lock ETH and set eligibility
    /// @param lockPeriod The time in seconds for how long the ETH should be locked
    /// @dev This function requires the user to send ETH with the transaction
    function lockETH(uint256 lockPeriod) external payable {
        require(msg.value >= MINIMUM_LOCK_AMOUNT, "Insufficient amount locked");
        require(users[msg.sender].lockedAmount == 0, "Already locked ETH");

        // Store user information
        users[msg.sender] = User({
            isEligible: false,
            lockPeriod: lockPeriod,
            lockedAmount: msg.value
        });
        
        emit ETHLocked(msg.sender, msg.value, lockPeriod);
    }

    /// @notice Check user eligibility based on locked amount and time
    /// @dev Updates eligibility status based on locking conditions
    function checkEligibility() external {
        User storage user = users[msg.sender];
        require(user.lockedAmount > 0, "No ETH locked");

        // Check if the lock period has passed
        if (block.timestamp >= user.lockPeriod) {
            user.isEligible = true;
            emit UserEligibilityUpdated(msg.sender, true);
        }
    }

    /// @notice Withdraw ETH after the eligible period
    /// @dev Only eligible users can call this function
    function withdrawETH() external {
        User storage user = users[msg.sender];
        require(user.isEligible, "Not eligible to withdraw");
        require(user.lockedAmount > 0, "No ETH to withdraw");

        uint256 amountToWithdraw = user.lockedAmount;

        // Reset user data
        user.lockedAmount = 0;
        user.isEligible = false; // Reset eligibility after withdrawal

        // Transfer ETH to user
        (bool sent, ) = msg.sender.call{value: amountToWithdraw}("");
        require(sent, "Failed to send ETH");

    }

    /// @notice Fallback function to accept ETH
    receive() external payable {
        revert("Direct ETH transfers not allowed. Use lockETH function.");
    }
}
```
