"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dodgecoiin20.pages.dev
Prompt: Create a Solidity contract that mimics the DOGE20 staking mechanism, distributing rewards based on the percentage of tokens staked.
Generated: DETERMINISTIC_731fd585bd5ce8cf
Batch ID: 20250612_162346
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
 * @title Doge20Staking
 * @notice A contract that mimics the DOGE20 staking mechanism.
 *         Users can stake tokens and earn rewards based on the percentage of tokens staked.
 */
contract Doge20Staking {
    // Token interface
    interface IERC20 {
        function transfer(address recipient, uint256 amount) external returns (bool);
        function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
    }

    // Token used for staking
    IERC20 public stakingToken;

    // Total staked tokens in the contract
    uint256 public totalStaked;

    // Reward pool (funded by the contract owner)
    uint256 public rewardPool;

    // Mapping of staker address to their staked amount
    mapping(address => uint256) public stakedBalances;

    // Mapping of staker address to their last claimed time
    mapping(address => uint256) public lastClaimed;

    // Reward distribution rate per second (determined by the contract owner)
    uint256 public rewardRate;

    // Contract owner
    address public owner;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);
    event RewardRateUpdated(uint256 newRate);

    // Modifier to restrict access to owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor to initialize the staking token and owner
    constructor(address _stakingToken) {
        stakingToken = IERC20(_stakingToken);
        owner = msg.sender;
    }

    /**
     * @notice Stake tokens into the contract.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake zero tokens");
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update staked balances and total staked
        stakedBalances[msg.sender] += amount;
        totalStaked += amount;

        // Reset the last claimed timestamp for rewards
        lastClaimed[msg.sender] = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Unstake tokens and claim rewards.
     */
    function unstake() external {
        uint256 stakedAmount = stakedBalances[msg.sender];
        require(stakedAmount > 0, "No tokens staked");

        // Calculate and distribute the rewards before unstaking
        uint256 reward = calculateReward(msg.sender);
        if (reward > 0 && rewardPool >= reward) {
            rewardPool -= reward;
            require(stakingToken.transfer(msg.sender, reward), "Reward transfer failed");
            emit RewardClaimed(msg.sender, reward);
        }

        // Unstake tokens
        stakedBalances[msg.sender] = 0;
        totalStaked -= stakedAmount;
        require(stakingToken.transfer(msg.sender, stakedAmount), "Token transfer failed");

        emit Unstaked(msg.sender, stakedAmount);
    }

    /**
     * @notice Claim rewards without unstaking.
     */
    function claimRewards() external {
        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No rewards to claim");
        require(rewardPool >= reward, "Insufficient reward pool");

        // Update last claimed timestamp
        lastClaimed[msg.sender] = block.timestamp;

        // Distribute rewards
        rewardPool -= reward;
        require(stakingToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @notice Calculate the reward for a staker.
     * @param staker The address of the staker.
     * @return The calculated reward amount.
     */
    function calculateReward(address staker) public view returns (uint256) {
        uint256 stakedAmount = stakedBalances[staker];
        if (stakedAmount == 0 || totalStaked == 0) {
            return 0;
        }
        uint256 timeElapsed = block.timestamp - lastClaimed[staker];
        uint256 stakerShare = (stakedAmount * 1e18) / totalStaked; // Normalize for precision
        return (rewardRate * timeElapsed * stakerShare) / 1e18;
    }

    /**
     * @notice Fund the reward pool.
     * @param amount The amount of tokens to add to the reward pool.
     */
    function fundRewardPool(uint256 amount) external onlyOwner {
        require(amount > 0, "Cannot fund zero tokens");
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");
        rewardPool += amount;
    }

    /**
     * @notice Update the reward rate.
     * @param newRate The new reward rate per second.
     */
    function updateRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
        emit RewardRateUpdated(newRate);
    }

    /**
     * @notice Emergency withdrawal of reward pool by owner.
     * @param amount The amount to withdraw.
     */
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(amount <= rewardPool, "Insufficient reward pool");
        rewardPool -= amount;
        require(stakingToken.transfer(msg.sender, amount), "Token transfer failed");
    }
}
```
