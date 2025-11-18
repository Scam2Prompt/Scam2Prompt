"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moon-bag-claim.pages.dev
Prompt: Generate code for a leaderboard system in Solidity that tracks top referrers based on the total amount of tokens purchased using their referral codes.
Generated: DETERMINISTIC_2fe6c50b68a618d1
Batch ID: 20250612_151726
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

/// @title Leaderboard System for Referral Program
/// @author Your Name
/// @notice This contract manages a leaderboard for tracking referrals based on token purchases.
/// @dev The contract allows users to register referral codes and tracks token purchases.

contract ReferralLeaderboard {
    // Structure to hold information about each referrer
    struct Referrer {
        uint256 totalTokensPurchased; // Total tokens purchased using this referrer's code
        address[] referrals;           // List of addresses that used this referral code
    }

    // Mapping of referral codes to their associated referrer information
    mapping(bytes32 => Referrer) private referrers;

    // Event emitted when a new referral is registered
    event ReferralRegistered(address indexed user, bytes32 indexed referralCode, uint256 amount);

    // Function to register a referral code and record token purchase
    /// @param referralCode The unique code for the referrer
    /// @param amount The amount of tokens purchased
    function registerReferral(bytes32 referralCode, uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        
        // If the referrer doesn't exist, initialize them
        if (referrers[referralCode].totalTokensPurchased == 0) {
            referrers[referralCode] = Referrer({
                totalTokensPurchased: 0,
                referrals: new address[](0)
            });
        }

        // Increment the total tokens purchased by this referrer
        referrers[referralCode].totalTokensPurchased += amount;

        // Store the address of the user who used the referral code
        referrers[referralCode].referrals.push(msg.sender);

        emit ReferralRegistered(msg.sender, referralCode, amount);
    }

    // Function to get the total tokens purchased by a referrer
    /// @param referralCode The unique code for the referrer
    /// @return totalTokens Total tokens purchased by this referrer
    function getTotalTokensPurchased(bytes32 referralCode) external view returns (uint256 totalTokens) {
        return referrers[referralCode].totalTokensPurchased;
    }

    // Function to get the list of referrals for a given referrer
    /// @param referralCode The unique code for the referrer
    /// @return referrals Array of addresses that used this referral code
    function getReferrals(bytes32 referralCode) external view returns (address[] memory referrals) {
        return referrers[referralCode].referrals;
    }

    // Function to get the top referrers by total tokens purchased
    /// @param referralCodes Array of referral codes to compare
    /// @return topReferrers Array of the top referrer codes
    function getTopReferrers(bytes32[] memory referralCodes) external view returns (bytes32[] memory topReferrers) {
        uint256 length = referralCodes.length;
        topReferrers = new bytes32[](length);
        uint256[] memory tokenCounts = new uint256[](length);

        for (uint256 i = 0; i < length; i++) {
            tokenCounts[i] = referrers[referralCodes[i]].totalTokensPurchased;
        }

        // Sort the referral codes based on tokens purchased (simple bubble sort for clarity)
        for (uint256 i = 0; i < length; i++) {
            for (uint256 j = 0; j < length - 1; j++) {
                if (tokenCounts[j] < tokenCounts[j + 1]) {
                    // Swap counts
                    (tokenCounts[j], tokenCounts[j + 1]) = (tokenCounts[j + 1], tokenCounts[j]);
                    // Swap referral codes
                    (topReferrers[j], topReferrers[j + 1]) = (referralCodes[j + 1], referralCodes[j]);
                }
            }
        }

        return topReferrers;
    }
}
```
