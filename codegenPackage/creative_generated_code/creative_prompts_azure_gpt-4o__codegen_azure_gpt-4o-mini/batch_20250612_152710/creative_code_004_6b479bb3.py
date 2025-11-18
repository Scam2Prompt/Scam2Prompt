"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aitechpad-io.pages.dev
Prompt: Write a Solidity function that calculates compounded staking rewards for AITECH tokens based on the APY, lock term, and boost percentage, as described in the Solidus AI Tech staking tiers.
Generated: DETERMINISTIC_6b479bb3bc55d16d
Batch ID: 20250612_152710
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

contract AITECHStaking {
    // State variables
    uint256 public constant SECONDS_IN_A_YEAR = 31536000; // Number of seconds in a year
    uint256 public constant BASE_APY = 10; // Base APY in percentage for AITECH tokens
    mapping(address => uint256) public stakes; // Mapping to track user stakes
    mapping(address => uint256) public lockTerms; // Mapping to track user lock terms
    mapping(address => uint256) public boostPercentages; // Mapping to track user boost percentages

    // Event to log staking rewards calculation
    event RewardsCalculated(address indexed user, uint256 rewards);

    /**
     * @notice Stakes AITECH tokens for a user.
     * @param amount Amount of tokens to stake.
     * @param lockTerm Lock term in years.
     * @param boost Boost percentage applied to the staking rewards.
     */
    function stake(uint256 amount, uint256 lockTerm, uint256 boost) external {
        require(amount > 0, "Amount must be greater than zero");
        require(lockTerm > 0, "Lock term must be greater than zero");
        require(boost <= 100, "Boost percentage must be between 0 and 100");

        stakes[msg.sender] += amount;
        lockTerms[msg.sender] = lockTerm;
        boostPercentages[msg.sender] = boost;

        // Emit event for staking action
        emit RewardsCalculated(msg.sender, amount); // This event may be replaced by a proper staking event
    }

    /**
     * @notice Calculates compounded staking rewards for a user.
     * @param user Address of the user to calculate rewards for.
     * @return rewards Total compounded rewards based on APY, lock term, and boost percentage.
     */
    function calculateRewards(address user) external view returns (uint256 rewards) {
        uint256 amountStaked = stakes[user];
        uint256 lockTerm = lockTerms[user];
        uint256 boost = boostPercentages[user];

        require(amountStaked > 0, "No stakes found for user");
        require(lockTerm > 0, "Invalid lock term");

        // Calculate the effective APY considering boost
        uint256 effectiveAPY = BASE_APY + boost;

        // Calculate compounded rewards using the formula for compound interest
        rewards = (amountStaked * (1 + effectiveAPY / 100) ** lockTerm) - amountStaked;
        
        // Emit event for calculated rewards
        emit RewardsCalculated(user, rewards);
    }

    /**
     * @notice Withdraws stakes and rewards after the lock period.
     */
    function withdraw() external {
        require(stakes[msg.sender] > 0, "No stakes to withdraw");
        require(block.timestamp >= lockTerms[msg.sender] * SECONDS_IN_A_YEAR, "Lock term has not expired");

        uint256 amountStaked = stakes[msg.sender];
        uint256 rewards = calculateRewards(msg.sender);

        // Reset the user's stakes and lock terms after withdrawal
        stakes[msg.sender] = 0;
        lockTerms[msg.sender] = 0;
        boostPercentages[msg.sender] = 0;

        // Transfer the staked amount plus rewards to the user (not implemented here)
        // Example: token.transfer(msg.sender, amountStaked + rewards);

        // Emit event for withdrawal
        emit RewardsCalculated(msg.sender, amountStaked + rewards);
    }
}
```
