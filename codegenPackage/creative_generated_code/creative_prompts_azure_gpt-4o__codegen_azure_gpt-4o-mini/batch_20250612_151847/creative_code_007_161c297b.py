"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trust-coin.org
Prompt: Write a smart contract in Solidity for managing referral commissions and profit distribution, based on Trust-coin's investment plans.
Generated: DETERMINISTIC_161c297bf5768bdd
Batch ID: 20250612_151847
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

contract TrustCoinReferral {
    // Struct to hold user information
    struct User {
        address userAddress;
        uint256 totalInvested;
        uint256 totalCommissionEarned;
        address referrer;
        uint256 referralCount;
    }

    // Mapping to track users
    mapping(address => User) public users;

    // Events for logging activities
    event Registered(address indexed user, address indexed referrer);
    event Invested(address indexed user, uint256 amount);
    event CommissionPaid(address indexed referrer, uint256 amount);
    
    // Commission rate per referral
    uint256 public constant COMMISSION_RATE = 10; // 10%

    // Function to register a user with an optional referrer
    function register(address _referrer) external {
        require(users[msg.sender].userAddress == address(0), "User already registered");
        
        if (_referrer != address(0) && _referrer != msg.sender) {
            users[msg.sender].referrer = _referrer;
            users[_referrer].referralCount++;
            emit Registered(msg.sender, _referrer);
        }
        users[msg.sender].userAddress = msg.sender;
    }

    // Function to invest in TrustCoin
    function invest() external payable {
        require(msg.value > 0, "Investment must be greater than 0");
        
        users[msg.sender].totalInvested += msg.value;
        emit Invested(msg.sender, msg.value);

        // Pay commission to referrer
        payCommission(msg.value);
    }

    // Internal function to handle commission payments
    function payCommission(uint256 investmentAmount) internal {
        address referrer = users[msg.sender].referrer;
        if (referrer != address(0)) {
            uint256 commission = (investmentAmount * COMMISSION_RATE) / 100;
            users[referrer].totalCommissionEarned += commission;

            // Transfer commission to referrer
            (bool success, ) = referrer.call{value: commission}("");
            require(success, "Commission transfer failed");

            emit CommissionPaid(referrer, commission);
        }
    }

    // Function to withdraw user commissions
    function withdrawCommission() external {
        uint256 commission = users[msg.sender].totalCommissionEarned;
        require(commission > 0, "No commissions to withdraw");

        users[msg.sender].totalCommissionEarned = 0;

        // Transfer commission to user
        (bool success, ) = msg.sender.call{value: commission}("");
        require(success, "Withdrawal failed");
    }

    // Fallback function to allow Ether transfers to the contract
    receive() external payable {}

    // Function to check user details
    function getUserDetails(address userAddress) external view returns (User memory) {
        return users[userAddress];
    }
}
```
