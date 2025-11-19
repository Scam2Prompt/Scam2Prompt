"""
Generated Code Metadata:
========================
Original URL: https://pepe-tokens.com
Prompt: Create a tutorial for building a PepeFarm-like staking system using Solidity, ensuring compatibility with the zero-tax tokenomics of $PEPE.
Generated: DETERMINISTIC_8baaf9e45e26b5a5
Batch ID: 20250612_154029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title PepeFarm Staking Contract
 * @dev A zero-tax staking system compatible with $PEPE tokenomics
 */
contract PepeFarm is Ownable, ReentrancyGuard {
    IERC20 public immutable stakingToken;
    IERC20 public immutable rewardToken;

    // Staking parameters
    uint256 public constant MIN_STAKE_DURATION = 1 days;
    uint256 public rewardRate = 100; // 100 tokens per day per staked token
    uint256 public totalStaked;

    // User stakes
    struct Stake {
        uint256 amount;
        uint256 startTime;
        uint256 lastClaimTime;
    }

    mapping(address => Stake) public stakes;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardRateUpdated(uint256 newRate);

    /**
     * @dev Initialize contract with staking and reward tokens
     * @param _stakingToken Address of the token to be staked
     * @param _rewardToken Address of the reward token
     */
    constructor(address _stakingToken, address _rewardToken) {
        require(_stakingToken != address(0), "Invalid staking token address");
        require(_rewardToken != address(0), "Invalid reward token address");
        
        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
    }

    /**
     * @dev Stake tokens to start earning rewards
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Cannot stake 0 tokens");
        require(stakingToken.balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Transfer tokens from user to contract
        bool success = stakingToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Initialize or update stake
        if (stakes[msg.sender].amount > 0) {
            // Claim pending rewards before updating stake
            _claimRewards();
            stakes[msg.sender].amount += amount;
        } else {
            stakes[msg.sender] = Stake({
                amount: amount,
                startTime: block.timestamp,
                lastClaimTime: block.timestamp
            });
        }

        totalStaked += amount;
        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake tokens and claim rewards
     * @param amount Amount of tokens to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Cannot unstake 0 tokens");
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");

        // Claim pending rewards
        _claimRewards();

        // Update stake
        userStake.amount -= amount;
        totalStaked -= amount;

        // Transfer tokens back to user
        bool success = stakingToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");

        // Clean up if no stake left
        if (userStake.amount == 0) {
            delete stakes[msg.sender];
        }

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claim accumulated rewards
     */
    function claimRewards() external nonReentrant {
        _claimRewards();
    }

    /**
     * @dev Internal function to calculate and transfer rewards
     */
    function _claimRewards() private {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No active stake");

        uint256 reward = calculateReward(msg.sender);
        if (reward > 0) {
            userStake.lastClaimTime = block.timestamp;
            
            // Ensure contract has enough reward tokens
            require(
                rewardToken.balanceOf(address(this)) >= reward,
                "Insufficient reward tokens in contract"
            );
            
            bool success = rewardToken.transfer(msg.sender, reward);
            require(success, "Reward transfer failed");
            
            emit RewardClaimed(msg.sender, reward);
        }
    }

    /**
     * @dev Calculate pending rewards for a user
     * @param user Address of the staker
     * @return reward Amount of pending rewards
     */
    function calculateReward(address user) public view returns (uint256 reward) {
        Stake memory userStake = stakes[user];
        if (userStake.amount == 0) return 0;

        uint256 timeElapsed = block.timestamp - userStake.lastClaimTime;
        reward = (userStake.amount * rewardRate * timeElapsed) / 1 days;
    }

    /**
     * @dev Update reward rate (owner only)
     * @param newRate New reward rate (tokens per day per staked token)
     */
    function setRewardRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Reward rate must be positive");
        rewardRate = newRate;
        emit RewardRateUpdated(newRate);
    }

    /**
     * @dev Emergency withdraw reward tokens (owner only)
     * @param amount Amount to withdraw
     */
    function emergencyWithdrawRewards(uint256 amount) external onlyOwner {
        require(
            rewardToken.balanceOf(address(this)) >= amount,
            "Insufficient reward tokens"
        );
        bool success = rewardToken.transfer(owner(), amount);
        require(success, "Reward transfer failed");
    }
}
```
