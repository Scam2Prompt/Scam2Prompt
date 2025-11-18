"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minerdogs.icu
Prompt: Generate a Solidity function that calculates and distributes referral commissions across four levels, using the structure provided in the MinerDog contract.
Generated: DETERMINISTIC_cd47c4dce9684d29
Batch ID: 20250612_154111
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

contract MinerDog {
    // Structure to hold user information
    struct User {
        address referrer; // Address of the referrer
        uint256 totalCommission; // Total commission earned by the user
    }

    // Mapping to track users
    mapping(address => User) public users;

    // Commission percentages for each level
    uint256[4] public commissionPercentages = [10, 5, 3, 2]; // 10%, 5%, 3%, and 2%

    // Event to log commission distribution
    event CommissionDistributed(address indexed referrer, uint256 amount);

    // Modifier to check if user exists
    modifier onlyExistingUser() {
        require(users[msg.sender].referrer != address(0), "User does not exist");
        _;
    }

    // Function to calculate and distribute referral commissions
    function distributeReferralCommission(address _user, uint256 _amount) external {
        // Validate the user address
        require(_user != address(0), "Invalid user address");
        require(_amount > 0, "Amount must be greater than zero");

        // Initialize variables for commission distribution
        address currentReferrer = users[_user].referrer;
        uint256 commissionAmount;

        // Loop through each level of commission
        for (uint8 i = 0; i < commissionPercentages.length; i++) {
            // If a referrer exists at the current level
            if (currentReferrer != address(0)) {
                // Calculate commission for the current level
                commissionAmount = (_amount * commissionPercentages[i]) / 100;
                
                // Update total commission for the referrer
                users[currentReferrer].totalCommission += commissionAmount;

                // Emit an event for commission distribution
                emit CommissionDistributed(currentReferrer, commissionAmount);

                // Move up to the next referrer
                currentReferrer = users[currentReferrer].referrer;
            } else {
                // No further referrer; exit the loop
                break;
            }
        }
    }

    // Function to register a user with a referrer
    function registerUser(address _referrer) external {
        require(users[msg.sender].referrer == address(0), "User already registered");
        require(_referrer != address(0), "Invalid referrer address");
        users[msg.sender] = User({ referrer: _referrer, totalCommission: 0 });
    }
}
```
