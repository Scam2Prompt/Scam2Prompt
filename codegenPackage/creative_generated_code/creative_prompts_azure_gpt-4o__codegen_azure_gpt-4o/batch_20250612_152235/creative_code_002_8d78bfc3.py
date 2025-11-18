"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://siduspad.xyz
Prompt: Create a Solidity function that calculates and distributes compounding staking rewards based on APY and lock term, as described in the SidusPad staking pools.
Generated: DETERMINISTIC_8d78bfc38179ff78
Batch ID: 20250612_152235
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
 * @title StakingRewards
 * @dev Contract to calculate and distribute compounding staking rewards based on APY and lock term.
 */
contract StakingRewards {
    // State variables for staking
    struct Stake {
        uint256 amount; // Staked amount
        uint256 startTime; // Timestamp when the staking started
        uint256 lockTerm; // Lock term in seconds
        uint256 APY; // Annual Percentage Yield in basis points (e.g., 500 = 5%)
        bool isWithdrawn; // Status of withdrawal
    }

    mapping(address => Stake) public stakes; // Mapping of staker addresses to their Stake
    uint256 public constant BASIS_POINTS = 10000; // Basis points for percentage calculations

    // Events
    event Staked(address indexed user, uint256 amount, uint256 lockTerm, uint256 APY);
    event RewardsClaimed(address indexed user, uint256 reward, uint256 totalAmount);

    /**
     * @dev Stake tokens and initialize staking parameters.
     * @param _amount The amount of tokens staked.
     * @param _lockTerm The lock term duration in seconds.
     * @param _APY The Annual Percentage Yield in basis points.
     */
    function stake(uint256 _amount, uint256 _lockTerm, uint256 _APY) external {
        require(_amount > 0, "Staking amount must be greater than zero");
        require(stakes[msg.sender].amount == 0, "Already staking");
        
        // Update user's stake
        stakes[msg.sender] = Stake({
            amount: _amount,
            startTime: block.timestamp,
            lockTerm: _lockTerm,
            APY: _APY,
            isWithdrawn: false
        });

        emit Staked(msg.sender, _amount, _lockTerm, _APY);
    }

    /**
     * @dev Calculate staking rewards and withdraw the full balance (initial + compounded rewards).
     */
    function claimRewards() external {
        Stake storage userStake = stakes[msg.sender];

        require(userStake.amount > 0, "No active stake found");
        require(!userStake.isWithdrawn, "Rewards already claimed");
        require(block.timestamp >= userStake.startTime + userStake.lockTerm, "Lock term not yet completed");

        // Calculate compounded rewards
        uint256 reward = _calculateCompoundedReward(
            userStake.amount,
            userStake.APY,
            userStake.lockTerm
        );

        // Total amount to transfer (initial + rewards)
        uint256 totalAmount = userStake.amount + reward;

        // Mark stake as withdrawn
        userStake.isWithdrawn = true;

        // Transfer the total amount (mock transfer for demonstration purposes)
        // In production, ensure the reward is transferred using an ERC20 token contract.
        // Example: IERC20(tokenAddress).transfer(msg.sender, totalAmount);

        emit RewardsClaimed(msg.sender, reward, totalAmount);
    }

    /**
     * @dev Internal function to calculate compounded staking rewards.
     * @param principal The initial staked amount.
     * @param apy Annual Percentage Yield in basis points.
     * @param duration Lock term duration in seconds.
     * @return The compounded reward amount.
     */
    function _calculateCompoundedReward(
        uint256 principal,
        uint256 apy,
        uint256 duration
    ) internal pure returns (uint256) {
        // Number of compounding periods per year (e.g., daily compounding is 365)
        uint256 periodsPerYear = 365;

        // Duration in years (rounded to nearest full day)
        uint256 durationInYears = duration / (365 days);

        // Effective interest rate per period (in basis points)
        uint256 ratePerPeriod = apy / periodsPerYear;

        // Compound interest formula: A = P * (1 + r/n)^(nt)
        uint256 compoundedAmount = principal;

        for (uint256 i = 0; i < periodsPerYear * durationInYears; i++) {
            compoundedAmount += (compoundedAmount * ratePerPeriod) / BASIS_POINTS;
        }

        // Reward is total compounded amount minus the principal
        return compoundedAmount - principal;
    }
}
```
