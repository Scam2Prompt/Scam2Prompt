"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://token-oriviumio.pages.dev
Prompt: Create a Solidity smart contract for staking ORI tokens on the Orivium platform, incorporating the “Play & Earn” model.
Generated: DETERMINISTIC_cb1321ba4191a6ca
Batch ID: 20250612_162325
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
 * @title ORI Token Staking Contract
 * @dev Implements staking functionality for ORI tokens with a "Play & Earn" model.
 */
contract ORITokenStaking {
    // Address of the ORI token contract
    IERC20 public oriToken;

    // Struct to track staker information
    struct Stake {
        uint256 amount; // Amount of ORI tokens staked
        uint256 timestamp; // Timestamp when tokens were staked
        uint256 rewardsEarned; // Rewards earned through "Play & Earn"
    }

    // Mapping to store staking information per user
    mapping(address => Stake) private stakes;

    // Event logs
    event TokensStaked(address indexed staker, uint256 amount);
    event TokensUnstaked(address indexed staker, uint256 amount);
    event RewardsClaimed(address indexed staker, uint256 rewards);

    // Constructor to initialize token contract reference
    constructor(address _oriTokenAddress) {
        require(_oriTokenAddress != address(0), "Invalid ORI token address");
        oriToken = IERC20(_oriTokenAddress);
    }

    /**
     * @dev Stake ORI tokens into the contract.
     * @param _amount The number of ORI tokens to stake.
     */
    function stakeTokens(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");

        // Transfer ORI tokens from user to contract
        require(
            oriToken.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        // Update staking information
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += _amount;
        userStake.timestamp = block.timestamp;

        emit TokensStaked(msg.sender, _amount);
    }

    /**
     * @dev Unstake ORI tokens from the contract.
     * @param _amount The number of ORI tokens to unstake.
     */
    function unstakeTokens(uint256 _amount) external {
        require(_amount > 0, "Unstake amount must be greater than zero");

        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= _amount, "Insufficient staked amount");

        // Update staking information
        userStake.amount -= _amount;

        // Transfer ORI tokens back to user
        require(oriToken.transfer(msg.sender, _amount), "Token transfer failed");

        emit TokensUnstaked(msg.sender, _amount);
    }

    /**
     * @dev Claim earned rewards based on the "Play & Earn" model.
     */
    function claimRewards() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No staked tokens");

        // Calculate rewards (placeholder logic, replace with actual reward logic)
        uint256 rewards = calculateRewards(msg.sender);

        require(rewards > 0, "No rewards available");

        // Update rewards earned
        userStake.rewardsEarned += rewards;

        // Transfer rewards (ORI tokens) to the user
        require(oriToken.transfer(msg.sender, rewards), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev View function to fetch staking details for a user.
     * @param _staker The address of the staker.
     * @return amount Amount of tokens staked.
     * @return timestamp Timestamp of last staking activity.
     * @return rewardsEarned Total rewards earned.
     */
    function getStakingDetails(address _staker)
        external
        view
        returns (
            uint256 amount,
            uint256 timestamp,
            uint256 rewardsEarned
        )
    {
        Stake memory userStake = stakes[_staker];
        return (userStake.amount, userStake.timestamp, userStake.rewardsEarned);
    }

    /**
     * @dev Internal function to calculate rewards.
     * @param _staker The address of the staker.
     * @return rewards Calculated rewards.
     */
    function calculateRewards(address _staker) internal view returns (uint256) {
        Stake memory userStake = stakes[_staker];

        // Placeholder logic: rewards = staked amount * (time elapsed in seconds) / 1000
        // Replace with your specific reward calculation mechanism
        uint256 timeElapsed = block.timestamp - userStake.timestamp;
        return (userStake.amount * timeElapsed) / 1000;
    }
}

// Interface for the ERC20 token standard
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount)
        external
        returns (bool);

    function balanceOf(address account) external view returns (uint256);
}
```
