"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonbag-claiming.pages.dev
Prompt: Provide an example of a smart contract function that calculates and distributes referral incentives based on the total amount purchased using referral codes, as described in MoonBag's referral system.
Generated: DETERMINISTIC_f2e6d7020b226cbe
Batch ID: 20250612_145625
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

/// @title Referral Incentive Smart Contract
/// @author Your Name
/// @notice This contract manages referral incentives based on purchases made using referral codes
contract ReferralSystem {
    // Structure to hold referral information
    struct Referral {
        address referrer; // Address of the referrer
        uint256 totalReferralEarnings; // Total earnings accumulated from referrals
    }

    // Mapping to keep track of referrals by user address
    mapping(address => Referral) public referrals;

    // Mapping to keep track of purchase amounts for each referral code
    mapping(string => uint256) public referralPurchases;

    // Event to log referral earnings distribution
    event ReferralEarningsDistributed(address indexed referrer, uint256 amount);

    // Function to calculate and distribute referral incentives
    /// @param referralCode The code used for referral
    /// @param purchaseAmount The total amount of the purchase
    function distributeReferralIncentives(string memory referralCode, uint256 purchaseAmount) external payable {
        // Validate purchase amount
        require(purchaseAmount > 0, "Purchase amount must be greater than zero");

        // Ensure the referral code is valid
        require(bytes(referralCode).length > 0, "Invalid referral code");

        // Update total purchases associated with the referral code
        referralPurchases[referralCode] += purchaseAmount;

        // Calculate incentive (e.g., 10% of the purchase amount)
        uint256 incentive = (purchaseAmount * 10) / 100;

        // Find the referrer using the referral code - assuming a separate mapping exists
        address referrer = getReferrer(referralCode);
        require(referrer != address(0), "Referrer not found");

        // Update referrer's total earnings
        referrals[referrer].totalReferralEarnings += incentive;

        // Emit event to notify about the incentive distribution
        emit ReferralEarningsDistributed(referrer, incentive);
    }

    // Function to retrieve the referrer based on the referral code
    /// @param referralCode The referral code to lookup
    /// @return address of the referrer
    function getReferrer(string memory referralCode) internal view returns (address) {
        // TODO: Implement logic to retrieve the referrer address based on the referral code
        // This is a placeholder return value for demonstration purposes
        return address(0); // Replace with actual logic
    }

    // Function to withdraw earned incentives (to be called by the referrer)
    function withdrawEarnings() external {
        uint256 earnings = referrals[msg.sender].totalReferralEarnings;
        require(earnings > 0, "No earnings to withdraw");

        // Reset the referrer's earnings after withdrawal
        referrals[msg.sender].totalReferralEarnings = 0;

        // Transfer the earnings to the referrer
        (bool success, ) = msg.sender.call{value: earnings}("");
        require(success, "Transfer failed");
    }

    // Function to receive Ether.
    receive() external payable {}
}
```
