"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethtokens.pages.dev
Prompt: Provide a step-by-step guide for implementing token staking logic for Ethena governance tokens using Solidity.
Generated: DETERMINISTIC_364f2a5311c5dea4
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

/**
 * @title Ethena Token Staking Contract
 * @dev A smart contract for staking Ethena governance tokens and earning rewards.
 * Implements basic staking logic with support for rewards distribution.
 */
contract EthenaTokenStaking {
    // State variables
    address public owner; // Contract owner
    IERC20 public governanceToken; // Governance token interface
    uint256 public rewardRate; // Reward rate per second
    uint256 public totalStaked; // Total staked tokens in the contract

    struct Stake {
        uint256 amount; // Staked token amount
        uint256 startTime; // Timestamp when staking started
        uint256 rewardEarned; // Accumulated reward
    }

    mapping(address => Stake) public stakes; // Mapping user addresses to their staking info

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor
    constructor(address _governanceToken, uint256 _rewardRate) {
        require(_governanceToken != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");

        owner = msg.sender;
        governanceToken = IERC20(_governanceToken);
        rewardRate = _rewardRate;
    }

    // Modifier to restrict access to contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Modifier to check staking amount validity
    modifier validStakeAmount(uint256 amount) {
        require(amount > 0, "Stake amount must be greater than zero");
        _;
    }

    /**
     * @dev Stake governance tokens into the contract.
     * @param amount The number of tokens to stake.
     */
    function stake(uint256 amount) external validStakeAmount(amount) {
        require(
            governanceToken.transferFrom(msg.sender, address(this), amount),
            "Token transfer failed"
        );

        // Calculate pending rewards if the user has already staked
        if (stakes[msg.sender].amount > 0) {
            stakes[msg.sender].rewardEarned += calculateReward(msg.sender);
        }

        // Update stake details
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].startTime = block.timestamp;

        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake tokens and optionally claim rewards.
     */
    function unstake() external {
        require(stakes[msg.sender].amount > 0, "No tokens staked");

        // Calculate rewards before unstaking
        uint256 rewards = calculateReward(msg.sender);
        uint256 stakedAmount = stakes[msg.sender].amount;

        // Reset user stake
        stakes[msg.sender].amount = 0;
        stakes[msg.sender].startTime = 0;
        stakes[msg.sender].rewardEarned = 0;

        totalStaked -= stakedAmount;

        // Return staked tokens to user
        require(
            governanceToken.transfer(msg.sender, stakedAmount),
            "Token transfer failed"
        );

        // Optional: Claim accumulated rewards
        if (rewards > 0) {
            require(
                governanceToken.transfer(msg.sender, rewards),
                "Reward transfer failed"
            );
        }

        emit Unstaked(msg.sender, stakedAmount);
        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Claim accumulated rewards without unstaking.
     */
    function claimRewards() external {
        uint256 rewards = calculateReward(msg.sender);
        require(rewards > 0, "No rewards to claim");

        // Reset reward calculation
        stakes[msg.sender].rewardEarned = 0;
        stakes[msg.sender].startTime = block.timestamp;

        // Transfer rewards to user
        require(
            governanceToken.transfer(msg.sender, rewards),
            "Reward transfer failed"
        );

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Calculate pending rewards for a given staker.
     * @param staker Address of the staker.
     * @return Reward amount.
     */
    function calculateReward(address staker) internal view returns (uint256) {
        Stake memory stakeInfo = stakes[staker];
        if (stakeInfo.amount == 0 || stakeInfo.startTime == 0) {
            return stakeInfo.rewardEarned;
        }

        uint256 stakingDuration = block.timestamp - stakeInfo.startTime;
        uint256 newRewards = stakingDuration * rewardRate * stakeInfo.amount / 1 ether;

        return stakeInfo.rewardEarned + newRewards;
    }

    /**
     * @dev Update the reward rate. Callable by the contract owner.
     * @param _rewardRate New reward rate per second.
     */
    function updateRewardRate(uint256 _rewardRate) external onlyOwner {
        require(_rewardRate > 0, "Reward rate must be greater than zero");
        rewardRate = _rewardRate;
    }
}

// IERC20 interface to interact with the governance token
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount)
        external
        returns (bool);
}
```
