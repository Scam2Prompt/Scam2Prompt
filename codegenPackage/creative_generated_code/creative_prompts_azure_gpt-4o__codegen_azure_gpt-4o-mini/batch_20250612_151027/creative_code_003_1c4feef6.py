"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minucoindapp.pages.dev
Prompt: Create a function in Solidity to implement a referral system similar to Minu's, where referrers earn 12% of the BNB used by invited users to hire miners.
Generated: DETERMINISTIC_1c4feef6a95278db
Batch ID: 20250612_151027
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

contract ReferralSystem {
    // Structure to hold information about each user
    struct User {
        address referrer; // Address of the referrer
        uint256 referralEarnings; // Total earnings from referrals
        bool isRegistered; // Flag to check if user is registered
    }

    // Mapping to store user information
    mapping(address => User) public users;

    // Event to log referral earnings
    event ReferralEarnings(address indexed referrer, address indexed referred, uint256 amount);

    // Modifier to check if the user is registered
    modifier onlyRegistered() {
        require(users[msg.sender].isRegistered, "User is not registered.");
        _;
    }

    // Function to register a user with an optional referrer
    function register(address _referrer) external {
        require(!users[msg.sender].isRegistered, "User is already registered.");
        
        // Check if referrer is valid and not the user themselves
        if (_referrer != address(0) && _referrer != msg.sender) {
            users[msg.sender].referrer = _referrer;
        }

        // Mark the user as registered
        users[msg.sender].isRegistered = true;
    }

    // Function to hire miners
    function hireMiners() external payable onlyRegistered {
        require(msg.value > 0, "Amount must be greater than zero.");

        // Calculate referral commission
        address referrer = users[msg.sender].referrer;
        uint256 referralCommission = (msg.value * 12) / 100;

        // Transfer the referral commission to the referrer if exists
        if (referrer != address(0)) {
            users[referrer].referralEarnings += referralCommission;
            emit ReferralEarnings(referrer, msg.sender, referralCommission);
            payable(referrer).transfer(referralCommission);
        }
    }

    // Function to withdraw referral earnings
    function withdrawEarnings() external onlyRegistered {
        uint256 earnings = users[msg.sender].referralEarnings;
        require(earnings > 0, "No earnings to withdraw.");

        // Reset the user's earnings before transferring to prevent reentrancy attacks
        users[msg.sender].referralEarnings = 0;

        // Transfer earnings to the user
        payable(msg.sender).transfer(earnings);
    }

    // Fallback function to receive BNB
    receive() external payable {}
    
    // Function to get referral earnings of a user
    function getReferralEarnings() external view returns (uint256) {
        return users[msg.sender].referralEarnings;
    }
}
```
