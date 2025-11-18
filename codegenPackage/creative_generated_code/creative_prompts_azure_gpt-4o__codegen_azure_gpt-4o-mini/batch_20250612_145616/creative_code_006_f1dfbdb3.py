"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonhop.pages.dev
Prompt: Create a Solidity smart contract that implements a referral program similar to MOONHOP's, allowing users to generate referral codes and track rewards.
Generated: DETERMINISTIC_f1dfbdb3fc332712
Batch ID: 20250612_145616
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
    // Struct to represent a referral
    struct Referral {
        address referrer; // Address of the referrer
        uint256 reward;   // Total rewards earned by the referral
        uint256 referralsCount; // Number of referrals made
    }

    // Mapping to store each user's referral details
    mapping(address => Referral) public referrals;

    // Mapping to store referral codes to addresses
    mapping(string => address) private referralCodes;

    // Event emitted when a new referral code is created
    event ReferralCodeCreated(address indexed user, string code);
    
    // Event emitted when rewards are updated
    event RewardsUpdated(address indexed user, uint256 totalReward);
    
    // Function to create a referral code
    function createReferralCode(string memory code) public {
        require(referralCodes[code] == address(0), "Referral code already exists.");
        require(bytes(code).length > 0, "Code cannot be empty.");
        
        // Assign the referral code to the caller's address
        referralCodes[code] = msg.sender;

        // Emit the event
        emit ReferralCodeCreated(msg.sender, code);
    }

    // Function to refer a new user with the referral code
    function referWithCode(string memory code) public {
        require(referralCodes[code] != address(0), "Invalid referral code.");
        
        address referrer = referralCodes[code];
        
        // Increment the referrer's referral count
        referrals[referrer].referralsCount++;

        // Update the referrer's rewards (implement your rewards logic)
        uint256 reward = calculateReward(referrals[referrer].referralsCount);
        referrals[referrer].reward += reward;

        // Emit the event for reward update
        emit RewardsUpdated(referrer, referrals[referrer].reward);
    }

    // Function to calculate rewards based on the number of referrals
    // This is a placeholder; adjust logic as needed
    function calculateReward(uint256 referralsCount) internal pure returns (uint256) {
        return referralsCount * 0.01 ether; // Example: 0.01 ETH per referral
    }

    // Function to withdraw rewards (only for the referrer)
    function withdrawRewards() public {
        uint256 reward = referrals[msg.sender].reward;
        require(reward > 0, "No rewards to withdraw.");

        // Reset rewards to zero before transferring
        referrals[msg.sender].reward = 0;

        // Transfer the reward
        payable(msg.sender).transfer(reward);
    }

    // Fallback function to accept ether transfers
    receive() external payable {}

    // Function to get the total rewards of a user
    function getTotalRewards(address user) public view returns (uint256) {
        return referrals[user].reward;
    }

    // Function to get the number of referrals made by a user
    function getReferralsCount(address user) public view returns (uint256) {
        return referrals[user].referralsCount;
    }
}
```
