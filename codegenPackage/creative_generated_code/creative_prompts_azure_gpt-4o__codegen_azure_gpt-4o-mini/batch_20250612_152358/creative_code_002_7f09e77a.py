"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zeek.social
Prompt: Generate a smart contract in Solidity for managing referral codes and rewards distribution, inspired by Zeek Network's SocialFi model.
Generated: DETERMINISTIC_7f09e77a92dfcac4
Batch ID: 20250612_152358
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
    // Struct to store referral information
    struct Referral {
        address referrer;  // The address of the referrer
        uint256 reward;    // Total rewards earned by the referred user
        uint256 referralsCount; // Number of referrals made
    }

    // Mapping to hold referral details for each user
    mapping(address => Referral) public referrals;

    // Event emitted when a new referral is created
    event NewReferral(address indexed referee, address indexed referrer);

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed referrer, uint256 amount);

    // Function to register a new referral
    // Only callable if the referee has not been referred already
    function refer(address _referrer) external {
        require(_referrer != address(0), "Referrer address cannot be zero");
        require(referrals[msg.sender].referrer == address(0), "User already referred");

        // Set the referrer for the sender
        referrals[msg.sender].referrer = _referrer;
        referrals[_referrer].referralsCount += 1; // Increment the referrer's count

        emit NewReferral(msg.sender, _referrer);
    }

    // Function to distribute rewards to referrers
    // Can be called by anyone to distribute rewards
    function distributeRewards(address[] calldata _referrers, uint256[] calldata _amounts) external {
        require(_referrers.length == _amounts.length, "Referrers and amounts length mismatch");

        for (uint256 i = 0; i < _referrers.length; i++) {
            address referrer = _referrers[i];
            uint256 amount = _amounts[i];

            // Ensure the referrer has made referrals
            require(referrals[referrer].referralsCount > 0, "Referrer has no referrals");

            // Update the total rewards for the referrer
            referrals[referrer].reward += amount;

            emit RewardsDistributed(referrer, amount);
        }
    }

    // Function to withdraw rewards by the referrer
    function withdrawRewards() external {
        uint256 amount = referrals[msg.sender].reward;
        require(amount > 0, "No rewards to withdraw");

        // Reset the reward balance to prevent re-entrancy
        referrals[msg.sender].reward = 0;

        // Transfer the rewards (assumes the contract has sufficient ETH)
        payable(msg.sender).transfer(amount);
    }

    // Fallback function to accept ETH
    receive() external payable {}

    // Function to get the reward balance of a user
    function getRewardBalance(address _user) external view returns (uint256) {
        return referrals[_user].reward;
    }

    // Function to get the referral information of a user
    function getReferralInfo(address _user) external view returns (address, uint256, uint256) {
        Referral memory referral = referrals[_user];
        return (referral.referrer, referral.reward, referral.referralsCount);
    }
}
```
