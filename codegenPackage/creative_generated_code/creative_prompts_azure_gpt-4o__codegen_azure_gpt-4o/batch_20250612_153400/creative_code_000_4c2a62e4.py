"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://param-35r.pages.dev
Prompt: Write a smart contract in Solidity for a staking mechanism that aligns with the tokenomics described in the Param Network platform.
Generated: DETERMINISTIC_4c2a62e49a03d413
Batch ID: 20250612_153400
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
 * @title StakingContract
 * @dev A smart contract for staking tokens, designed to align with Param Network tokenomics.
 * Users can stake tokens, earn rewards, and withdraw their staked tokens.
 */
contract StakingContract {
    // ERC20 token interface
    interface IERC20 {
        function transfer(address recipient, uint256 amount) external returns (bool);
        function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
    }

    // State variables
    IERC20 public stakingToken; // Token that will be staked
    uint256 public rewardRate; // Reward rate per second
    uint256 public totalStaked; // Total amount of staked tokens

    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 lastUpdated; // Timestamp of last update
        uint256 rewards; // Accumulated rewards
    }

    mapping(address => Stake) public stakes; // Mapping of user address to stake details

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the staking contract.
     * @param _stakingToken Address of the token to be staked.
     * @param _rewardRate Reward rate per second (in token units).
     */
    constructor(IERC20 _stakingToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Modifier to update the rewards of a user before executing a function.
     */
    modifier updateRewards(address user) {
        if (stakes[user].amount > 0) {
            stakes[user].rewards += pendingRewards(user);
        }
        stakes[user].lastUpdated = block.timestamp;
        _;
    }

    /**
     * @dev Function to calculate pending rewards for a user.
     * @param user Address of the user.
     * @return Total pending rewards.
     */
    function pendingRewards(address user) public view returns (uint256) {
        Stake memory stakeDetails = stakes[user];
        if (stakeDetails.amount == 0) {
            return stakeDetails.rewards;
        }
        uint256 timeElapsed = block.timestamp - stakeDetails.lastUpdated;
        uint256 additionalRewards = timeElapsed * stakeDetails.amount * rewardRate;
        return stakeDetails.rewards + additionalRewards;
    }

    /**
     * @dev Function to allow users to stake tokens.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external updateRewards(msg.sender) {
        require(amount > 0, "Cannot stake zero tokens");
        require(
            stakingToken.transferFrom(msg.sender, address(this), amount),
            "Token transfer failed"
        );

        stakes[msg.sender].amount += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Function to allow users to withdraw staked tokens.
     * @param amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 amount) external updateRewards(msg.sender) {
        require(amount > 0, "Cannot withdraw zero tokens");
        require(stakes[msg.sender].amount >= amount, "Insufficient staked balance");

        stakes[msg.sender].amount -= amount;
        totalStaked -= amount;

        require(
            stakingToken.transfer(msg.sender, amount),
            "Token transfer failed"
        );

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Function to allow users to claim their rewards.
     */
    function claimRewards() external updateRewards(msg.sender) {
        uint256 rewards = stakes[msg.sender].rewards;
        require(rewards > 0, "No rewards available");

        stakes[msg.sender].rewards = 0; // Reset reward balance
        require(
            stakingToken.transfer(msg.sender, rewards),
            "Token transfer failed"
        );

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Function to get the total staked amount for a user.
     * @param user Address of the user.
     * @return Amount of tokens staked by the user.
     */
    function getStakedAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }

    /**
     * @dev Function to get the total pending rewards for a user.
     * @param user Address of the user.
     * @return Amount of pending rewards for the user.
     */
    function getPendingRewards(address user) external view returns (uint256) {
        return pendingRewards(user);
    }

    /**
     * @dev Function to get the total staked tokens in the contract.
     * @return Total staked tokens.
     */
    function getTotalStaked() external view returns (uint256) {
        return totalStaked;
    }
}
```
