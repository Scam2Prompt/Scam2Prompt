"""
Generated Code Metadata:
========================
Original URL: https://theoldcastle.pages.dev
Prompt: Create a referral system in Solidity that records referrals directly on the blockchain, ensuring permanent tracking of referred users and distributing 10% of commissions to the referrer, as outlined in TOCD's referral mechanism.
Generated: DETERMINISTIC_6a4976c2c43d8f3e
Batch ID: 20250612_151100
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

/**
 * @title TOCDReferralSystem
 * @dev A smart contract for tracking referrals and distributing commissions
 */
contract TOCDReferralSystem {
    // Struct to store referral information
    struct Referral {
        address referrer;
        uint256 totalReferred;
        uint256 totalCommission;
    }

    // Mapping from user address to their referral data
    mapping(address => Referral) public referrals;

    // Mapping to track if an address has been referred (to prevent double counting)
    mapping(address => bool) public hasBeenReferred;

    // Commission percentage (10%)
    uint256 public constant COMMISSION_PERCENTAGE = 10;

    // Events
    event ReferralRecorded(address indexed referrer, address indexed referee);
    event CommissionDistributed(address indexed referrer, uint256 amount);

    /**
     * @dev Record a referral and distribute commission
     * @param _referrer The address of the referrer
     * @param _referee The address of the person being referred
     * @param _amount The transaction amount to calculate commission from
     */
    function recordReferral(
        address _referrer,
        address _referee,
        uint256 _amount
    ) external {
        require(_referrer != address(0), "Invalid referrer address");
        require(_referee != address(0), "Invalid referee address");
        require(_referrer != _referee, "Cannot refer yourself");
        require(!hasBeenReferred[_referee], "Address already referred");

        // Calculate commission (10% of the amount)
        uint256 commission = (_amount * COMMISSION_PERCENTAGE) / 100;

        // Update referral data
        referrals[_referrer].totalReferred += 1;
        referrals[_referrer].totalCommission += commission;
        hasBeenReferred[_referee] = true;

        // Emit events
        emit ReferralRecorded(_referrer, _referee);
        emit CommissionDistributed(_referrer, commission);
    }

    /**
     * @dev Get referral information for a specific address
     * @param _address The address to query
     * @return referrerData The referral data for the address
     */
    function getReferralInfo(address _address)
        external
        view
        returns (Referral memory referrerData)
    {
        return referrals[_address];
    }

    /**
     * @dev Check if an address has been referred
     * @param _address The address to check
     * @return True if the address has been referred, false otherwise
     */
    function checkIfReferred(address _address) external view returns (bool) {
        return hasBeenReferred[_address];
    }
}
```
