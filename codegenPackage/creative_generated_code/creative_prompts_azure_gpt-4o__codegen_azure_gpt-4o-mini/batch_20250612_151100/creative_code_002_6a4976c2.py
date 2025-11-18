"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theoldcastle.pages.dev
Prompt: Create a referral system in Solidity that records referrals directly on the blockchain, ensuring permanent tracking of referred users and distributing 10% of commissions to the referrer, as outlined in TOCD's referral mechanism.
Generated: DETERMINISTIC_6a4976c2c43d8f3e
Batch ID: 20250612_151100
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

/// @title Referral System for TOCD
/// @author Your Name
/// @notice This contract implements a referral system that tracks user referrals and distributes commissions.
contract ReferralSystem {
    // Struct to store referral information
    struct Referral {
        address referrer;
        uint256 commissionEarned;
    }

    // Mapping from user address to their referral information
    mapping(address => Referral) public referrals;

    // Event emitted when a new referral is created
    event NewReferral(address indexed user, address indexed referrer);

    // Event emitted when commission is paid to referrer
    event CommissionPaid(address indexed referrer, uint256 amount);

    // The total commission pool
    uint256 public totalCommissionPool;

    /// @notice Allows a user to register a referral
    /// @param referrer Address of the referrer
    /// @dev Only one referrer can be assigned per user
    function registerReferral(address referrer) external {
        require(referrer != address(0), "Referrer address cannot be zero");
        require(referrals[msg.sender].referrer == address(0), "User already referred");
        
        // Store the referral information
        referrals[msg.sender] = Referral({
            referrer: referrer,
            commissionEarned: 0
        });

        emit NewReferral(msg.sender, referrer);
    }

    /// @notice This function simulates a transaction that generates commission
    /// @param amount The amount of commission generated
    /// @dev This should be linked to your payment processing logic
    function generateCommission(uint256 amount) external {
        require(amount > 0, "Commission amount must be greater than zero");

        // Calculate 10% for the referrer
        uint256 commissionForReferrer = (amount * 10) / 100;

        // Update the total commission pool
        totalCommissionPool += commissionForReferrer;

        // Update the commission earned by the referrer
        if (referrals[msg.sender].referrer != address(0)) {
            referrals[referrals[msg.sender].referrer].commissionEarned += commissionForReferrer;
            emit CommissionPaid(referrals[msg.sender].referrer, commissionForReferrer);
        }
    }

    /// @notice Allows the referrer to withdraw their earned commissions
    function withdrawCommission() external {
        uint256 earned = referrals[msg.sender].commissionEarned;
        require(earned > 0, "No commission to withdraw");

        // Reset the earned commissions to prevent re-entrancy
        referrals[msg.sender].commissionEarned = 0;

        // Transfer the commission to the referrer
        (bool success, ) = msg.sender.call{value: earned}("");
        require(success, "Transfer failed");

        // Emit an event for withdrawal
        emit CommissionPaid(msg.sender, earned);
    }

    /// @notice Fallback function to accept Ether
    receive() external payable {}
}
```
