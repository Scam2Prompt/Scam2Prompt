"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-i.pages.dev
Prompt: How can I implement a staking mechanism for an ERC-20 token like DOGE20 to distribute rewards over two years?
Generated: DETERMINISTIC_563b38c451832a87
Batch ID: 20250612_162504
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
 * @dev A staking mechanism for an ERC-20 token to distribute rewards over two years.
 * Users can stake tokens and receive rewards proportionally over the staking period.
 */
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract StakingContract is Ownable {
    // ERC-20 token to be staked
    IERC20 public stakingToken;

    // Reward distribution constant (two years in seconds)
    uint256 public constant REWARD_DURATION = 2 * 365 * 24 * 60 * 60;

    uint256 public rewardPool; // Total reward pool for distribution
    uint256 public totalStaked; // Total staked tokens
    uint256 public stakingStartTime; // Timestamp for when staking started

    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Rewards already claimed
    }

    mapping(address => Stake) public stakes;

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardPoolFunded(uint256 amount);

    constructor(address _stakingToken) {
        stakingToken = IERC20(_stakingToken);
    }

    /**
     * @dev Fund the reward pool with tokens for distribution.
     * @param _amount The amount of tokens to add to the reward pool.
     */
    function fundRewardPool(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than zero");
        stakingToken.transferFrom(msg.sender, address(this), _amount);

        rewardPool += _amount;

        emit RewardPoolFunded(_amount);
    }

    /**
     * @dev Start the staking mechanism. Can only be called once.
     */
    function startStaking() external onlyOwner {
        require(stakingStartTime == 0, "Staking has already started");
        stakingStartTime = block.timestamp;
    }

    /**
     * @dev Stake a specific amount of tokens.
     * @param _amount The amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(stakingStartTime > 0, "Staking has not started yet");

        // Transfer tokens to the contract
        stakingToken.transferFrom(msg.sender, address(this), _amount);

        // Update user stake
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += _amount;

        // Update total staked tokens
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake tokens and claim any pending rewards.
     */
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens to unstake");

        // Calculate pending rewards
        uint256 rewards = calculateReward(msg.sender);

        // Transfer staked tokens back to the user
        uint256 stakedAmount = userStake.amount;
        stakingToken.transfer(msg.sender, stakedAmount);

        // Reset user's stake
        userStake.amount = 0;
        userStake.rewardDebt += rewards;

        // Transfer rewards to the user
        if (rewards > 0) {
            stakingToken.transfer(msg.sender, rewards);
            rewardPool -= rewards;

            emit RewardClaimed(msg.sender, rewards);
        }

        emit Unstaked(msg.sender, stakedAmount);
    }

    /**
     * @dev View function to calculate pending rewards for a user.
     * @param _user The address of the user.
     * @return The amount of pending rewards.
     */
    function calculateReward(address _user) public view returns (uint256) {
        Stake memory userStake = stakes[_user];

        if (stakingStartTime == 0 || totalStaked == 0) {
            return 0;
        }

        // Calculate the elapsed time since staking started
        uint256 elapsedTime = block.timestamp - stakingStartTime;

        // Cap elapsed time to the reward duration
        if (elapsedTime > REWARD_DURATION) {
            elapsedTime = REWARD_DURATION;
        }

        // Calculate reward amount
        uint256 userShare = (userStake.amount * elapsedTime) / REWARD_DURATION;
        uint256 totalReward = (rewardPool * userShare) / totalStaked;

        // Subtract already claimed rewards
        return totalReward - userStake.rewardDebt;
    }

    /**
     * @dev Emergency withdrawal of any remaining tokens.
     * Only callable by the contract owner.
     */
    function emergencyWithdraw() external onlyOwner {
        uint256 balance = stakingToken.balanceOf(address(this));
        stakingToken.transfer(owner(), balance);
    }
}
```
