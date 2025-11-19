"""
Generated Code Metadata:
========================
Original URL: https://trust-coin.org
Prompt: Write a smart contract in Solidity for managing referral commissions and profit distribution, based on Trust-coin's investment plans.
Generated: DETERMINISTIC_161c297bf5768bdd
Batch ID: 20250612_151847
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

contract TrustCoinReferral {
    // Struct to hold user information
    struct User {
        address referrer; // Address of the referrer
        uint256 totalInvested; // Total amount invested by the user
        uint256 referralEarnings; // Total earnings from referrals
    }

    // Mapping to store user information
    mapping(address => User) public users;

    // Event to log referral earnings
    event ReferralEarnings(address indexed referrer, address indexed referee, uint256 amount);

    // Commission percentage for referrals (e.g., 10%)
    uint256 public referralCommissionPercentage = 10;

    // Function to invest and set referrer
    function invest(address _referrer) external payable {
        require(msg.value > 0, "Investment must be greater than 0");
        require(_referrer != msg.sender, "You cannot refer yourself");
        
        // Update user investment
        users[msg.sender].totalInvested += msg.value;

        // Set referrer if not already set
        if (users[msg.sender].referrer == address(0)) {
            users[msg.sender].referrer = _referrer;
        }

        // Calculate referral commission
        uint256 commission = (msg.value * referralCommissionPercentage) / 100;

        // Update referrer's earnings
        if (users[_referrer].referrer != address(0)) {
            users[_referrer].referralEarnings += commission;
            emit ReferralEarnings(_referrer, msg.sender, commission);
        }
    }

    // Function to withdraw referral earnings
    function withdrawEarnings() external {
        uint256 earnings = users[msg.sender].referralEarnings;
        require(earnings > 0, "No earnings to withdraw");

        // Reset earnings to zero before transfer to prevent re-entrancy
        users[msg.sender].referralEarnings = 0;

        // Transfer earnings to the user
        (bool success, ) = msg.sender.call{value: earnings}("");
        require(success, "Transfer failed");
    }

    // Function to get user information
    function getUserInfo(address _user) external view returns (User memory) {
        return users[_user];
    }

    // Function to update referral commission percentage (only owner can call)
    address public owner;

    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    constructor() {
        owner = msg.sender; // Set the contract deployer as the owner
    }

    function updateReferralCommissionPercentage(uint256 _newPercentage) external onlyOwner {
        require(_newPercentage <= 100, "Percentage must be between 0 and 100");
        referralCommissionPercentage = _newPercentage;
    }

    // Fallback function to accept Ether
    receive() external payable {}
}
```
