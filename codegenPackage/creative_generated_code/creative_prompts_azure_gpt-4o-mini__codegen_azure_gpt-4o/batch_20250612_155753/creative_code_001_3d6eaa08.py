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

/**
 * @title Multi-Level Referral Program Contract
 * @dev Implements a referral program with multiple commission levels.
 */
contract ReferralProgram {
    // Referral structure to track commissions
    struct Referral {
        address referrer;
        uint256 totalRewards;
    }

    // Mapping of user addresses to their referral information
    mapping(address => Referral) public referrals;

    // Mapping to track balances for users
    mapping(address => uint256) public balances;

    // Event to log rewards distributed
    event RewardDistributed(address indexed referrer, address indexed referee, uint256 reward, uint256 level);

    // Levels of commission and their respective percentage (e.g., 10%, 5%, 2% for level 1, 2, 3)
    uint256[] public commissionLevels = [10, 5, 2];

    // Modifier to ensure a valid referrer
    modifier validReferrer(address referrer) {
        require(referrer != msg.sender, "Self-referral is not allowed");
        require(referrer != address(0), "Referrer cannot be the zero address");
        _;
    }

    /**
     * @dev Initialize referral relationship when a user registers using a referrer code.
     * @param referrer The address of the referrer.
     */
    function registerReferral(address referrer) external validReferrer(referrer) {
        // Ensure the user does not already have a referrer
        require(referrals[msg.sender].referrer == address(0), "Referral already exists");
        
        // Assign referrer to the user
        referrals[msg.sender] = Referral({referrer: referrer, totalRewards: 0});
    }

    /**
     * @dev Distribute rewards to referrers based on commission levels.
     * @param amount The amount used to calculate commission rewards.
     */
    function distributeRewards(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        address currentReferrer = referrals[msg.sender].referrer;

        // Iterate through commission levels and distribute rewards
        for (uint256 level = 0; level < commissionLevels.length; level++) {
            if (currentReferrer == address(0)) {
                break; // Stop if there's no referrer at this level
            }

            // Calculate reward for this level
            uint256 reward = (amount * commissionLevels[level]) / 100;
            
            // Update referrer's balance and total rewards
            balances[currentReferrer] += reward;
            referrals[currentReferrer].totalRewards += reward;

            // Emit event for tracking reward distribution
            emit RewardDistributed(currentReferrer, msg.sender, reward, level + 1);

            // Move to the next referrer in the hierarchy
            currentReferrer = referrals[currentReferrer].referrer;
        }
    }

    /**
     * @dev Withdraw earned rewards.
     */
    function withdrawRewards() external {
        uint256 balance = balances[msg.sender];
        require(balance > 0, "No rewards available for withdrawal");

        // Reset balance before transferring to prevent re-entrancy attack
        balances[msg.sender] = 0;

        // Transfer rewards to the sender
        (bool success, ) = msg.sender.call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Fallback function to receive Ether.
     */
    receive() external payable {}
}
```
