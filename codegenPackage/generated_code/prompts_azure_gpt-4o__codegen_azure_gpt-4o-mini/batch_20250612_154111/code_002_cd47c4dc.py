"""
Generated Code Metadata:
========================
Original URL: https://minerdogs.icu
Prompt: Generate a Solidity function that calculates and distributes referral commissions across four levels, using the structure provided in the MinerDog contract.
Generated: DETERMINISTIC_cd47c4dce9684d29
Batch ID: 20250612_154111
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

contract MinerDog {
    // Structure to hold user information
    struct User {
        address referrer; // Address of the referrer
        uint256 totalEarnings; // Total earnings from referrals
        uint256[] referrals; // List of referrals
    }

    // Mapping to store user information
    mapping(address => User) public users;

    // Event to log commission distribution
    event CommissionDistributed(address indexed user, uint256 amount);

    // Function to calculate and distribute referral commissions
    function distributeReferralCommission(address _user, uint256 _amount) external {
        require(_user != address(0), "Invalid user address");
        require(_amount > 0, "Amount must be greater than zero");

        // Initialize commission percentages for each level
        uint256[4] memory commissionRates = [10, 5, 3, 2]; // 10%, 5%, 3%, 2%
        address currentReferrer = users[_user].referrer;

        // Loop through the levels to distribute commissions
        for (uint256 i = 0; i < commissionRates.length; i++) {
            if (currentReferrer == address(0)) {
                break; // Stop if there are no more referrers
            }

            // Calculate commission for the current level
            uint256 commission = (_amount * commissionRates[i]) / 100;

            // Update the referrer's total earnings
            users[currentReferrer].totalEarnings += commission;

            // Emit an event for the commission distribution
            emit CommissionDistributed(currentReferrer, commission);

            // Move to the next referrer in the hierarchy
            currentReferrer = users[currentReferrer].referrer;
        }
    }

    // Function to register a user with a referrer
    function registerUser(address _referrer) external {
        require(users[msg.sender].referrer == address(0), "User already registered");
        require(_referrer != msg.sender, "Cannot refer yourself");
        require(users[_referrer].referrer != address(0) || _referrer == address(0), "Referrer must be registered");

        // Register the user with the referrer
        users[msg.sender].referrer = _referrer;
        users[_referrer].referrals.push(uint256(uint160(msg.sender))); // Store the referral
    }
}
```
