"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepeunchained-io.pages.dev
Prompt: Write a smart contract in Solidity for staking $PEPU tokens on the Pepe Unchained Layer 2 blockchain, ensuring double staking rewards functionality.
Generated: DETERMINISTIC_3f28537827c35bee
Batch ID: 20250612_150226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

/**
 * @title PEPU Staking Smart Contract
 * @dev This contract allows for staking of $PEPU tokens with double staking rewards functionality.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract PEPUStaking {
    // Address of the $PEPU token contract
    IERC20 public immutable pepuToken;

    // Annual percentage rate for rewards (e.g., 10 for 10%)
    uint256 public immutable baseRewardRate;
    uint256 public immutable doubleRewardRate;

    // Minimum staking period in seconds
    uint256 public immutable minimumStakingPeriod;

    // Struct to store staker information
    struct StakeInfo {
        uint256 amount; // Amount of tokens staked
        uint256 startTime; // Timestamp when staking started
        bool claimedDoubleRewards; // Whether double rewards have been claimed
    }

    // Mapping of stakers to their stake information
    mapping(address => StakeInfo) public stakes;

    // Event emitted when tokens are staked
    event Staked(address indexed staker, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed staker, uint256 rewards);

    // Event emitted when double rewards are claimed
    event DoubleRewardsClaimed(address indexed staker, uint256 rewards);

    // Constructor to initialize the contract
    constructor(
        address _pepuToken,
        uint256 _baseRewardRate,
        uint256 _doubleRewardRate,
        uint256 _minimumStakingPeriod
    ) {
        require(_pepuToken != address(0), "Invalid token address");
        require(_baseRewardRate > 0, "Base reward rate must be > 0");
        require(_doubleRewardRate > _baseRewardRate, "Double reward rate must be > base reward rate");
        require(_minimumStakingPeriod > 0, "Minimum staking period must be > 0");

        pepuToken = IERC20(_pepuToken);
        baseRewardRate = _baseRewardRate;
        doubleRewardRate = _doubleRewardRate;
        minimumStakingPeriod = _minimumStakingPeriod;
    }

    /**
     * @dev Stake $PEPU tokens in the contract.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be > 0");

        // Transfer $PEPU tokens to the contract
        bool success = pepuToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Update stake information
        StakeInfo storage stakeInfo = stakes[msg.sender];
        stakeInfo.amount += amount;
        stakeInfo.startTime = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Claim regular staking rewards.
     */
    function claimRewards() external {
        StakeInfo storage stakeInfo = stakes[msg.sender];
        require(stakeInfo.amount > 0, "No tokens staked");

        uint256 stakingDuration = block.timestamp - stakeInfo.startTime;
        require(stakingDuration >= minimumStakingPeriod, "Staking period not met");

        // Calculate rewards based on base reward rate
        uint256 rewards = (stakeInfo.amount * baseRewardRate * stakingDuration) / (365 days * 100);

        // Transfer rewards to the staker
        bool success = pepuToken.transfer(msg.sender, rewards);
        require(success, "Reward transfer failed");

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Claim double rewards for eligible stakers.
     */
    function claimDoubleRewards() external {
        StakeInfo storage stakeInfo = stakes[msg.sender];
        require(stakeInfo.amount > 0, "No tokens staked");
        require(!stakeInfo.claimedDoubleRewards, "Double rewards already claimed");

        uint256 stakingDuration = block.timestamp - stakeInfo.startTime;
        require(stakingDuration >= minimumStakingPeriod, "Staking period not met");

        // Calculate double rewards
        uint256 doubleRewards = (stakeInfo.amount * doubleRewardRate * stakingDuration) / (365 days * 100);

        // Mark double rewards as claimed
        stakeInfo.claimedDoubleRewards = true;

        // Transfer rewards to the staker
        bool success = pepuToken.transfer(msg.sender, doubleRewards);
        require(success, "Double reward transfer failed");

        emit DoubleRewardsClaimed(msg.sender, doubleRewards);
    }

    /**
     * @dev View function to check staked amount for a user.
     * @param staker Address of the staker.
     * @return The amount of tokens staked by the user.
     */
    function getStakedAmount(address staker) external view returns (uint256) {
        return stakes[staker].amount;
    }

    /**
     * @dev View function to check staking start time for a user.
     * @param staker Address of the staker.
     * @return The staking start timestamp.
     */
    function getStakingStartTime(address staker) external view returns (uint256) {
        return stakes[staker].startTime;
    }

    /**
     * @dev View function to check if double rewards have been claimed.
     * @param staker Address of the staker.
     * @return True if double rewards have been claimed, false otherwise.
     */
    function hasClaimedDoubleRewards(address staker) external view returns (bool) {
        return stakes[staker].claimedDoubleRewards;
    }
}
```
