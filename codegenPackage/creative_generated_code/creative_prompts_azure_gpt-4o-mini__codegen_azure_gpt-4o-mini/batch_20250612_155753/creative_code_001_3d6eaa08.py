"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minerdogs.icu
Prompt: Write a code snippet that implements a referral program in a smart contract, allowing for multiple commission levels as described on the MinerDog platform.
Generated: DETERMINISTIC_3d6eaa08061d6838
Batch ID: 20250612_155753
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

contract ReferralProgram {
    struct User {
        address referrer; // The address of the user's referrer
        uint256 earnings; // Total earnings from referrals
        uint256 level;    // Level of the referral
    }

    mapping(address => User) public users; // Mapping of addresses to User data
    mapping(uint256 => uint256) public commissionRates; // Commission rates for each level

    // Event emitted when a new user registers with a referrer
    event UserRegistered(address indexed user, address indexed referrer);
    
    // Event emitted when a commission is paid
    event CommissionPaid(address indexed referrer, uint256 amount);

    // Constructor to set initial commission rates
    constructor() {
        // Set commission rates for levels 1 to 3
        commissionRates[1] = 5; // 5% for level 1
        commissionRates[2] = 3; // 3% for level 2
        commissionRates[3] = 1; // 1% for level 3
    }

    // Function to register a user with a referrer
    function register(address _referrer) external {
        require(users[msg.sender].referrer == address(0), "User already registered");
        require(_referrer != msg.sender, "Cannot refer yourself");

        users[msg.sender].referrer = _referrer;
        users[msg.sender].level = 1; // Start at level 1

        emit UserRegistered(msg.sender, _referrer);
    }

    // Function to simulate a purchase that generates commissions
    // This would typically be called after a payment is made
    function makePurchase(uint256 amount) external {
        require(users[msg.sender].referrer != address(0), "User not registered");

        address referrer = users[msg.sender].referrer;

        // Calculate commission for level 1
        uint256 commission = (amount * commissionRates[users[referrer].level]) / 100;
        
        // Update referrer earnings
        users[referrer].earnings += commission;

        // Emit an event for the commission payment
        emit CommissionPaid(referrer, commission);

        // Handle multi-level commission payment
        payCommissionToUpperLevels(referrer, commission);
    }

    // Private function to pay commissions to upper levels
    function payCommissionToUpperLevels(address _referrer, uint256 _commission) private {
        for (uint256 i = 1; i <= 3; i++) {
            _referrer = users[_referrer].referrer; // Move up the referral chain

            if (_referrer == address(0)) break; // Stop if there is no referrer

            uint256 commission = (_commission * commissionRates[i]) / 100;
            users[_referrer].earnings += commission;

            emit CommissionPaid(_referrer, commission);
        }
    }

    // Function to withdraw earnings (for demonstration purposes)
    function withdrawEarnings() external {
        uint256 amount = users[msg.sender].earnings;
        require(amount > 0, "No earnings to withdraw");

        // Reset user's earnings before transfer
        users[msg.sender].earnings = 0;

        // Transfer earnings to user
        payable(msg.sender).transfer(amount);
    }

    // Fallback function to accept Ether
    receive() external payable {}
}
```
