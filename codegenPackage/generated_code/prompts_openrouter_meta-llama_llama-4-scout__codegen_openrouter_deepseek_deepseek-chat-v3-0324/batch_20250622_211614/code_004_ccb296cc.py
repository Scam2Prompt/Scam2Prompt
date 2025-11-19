"""
Generated Code Metadata:
========================
Original URL: https://godcoin.world
Prompt: Develop a simple staking program for God Token using Solidity and OpenZeppelin libraries.
Generated: DETERMINISTIC_ccb296cc6de63b14
Batch ID: 20250622_211614
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
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title GodTokenStaking
 * @dev A simple staking contract for God Token that allows users to stake tokens
 * and earn rewards over time. Uses OpenZeppelin libraries for security and best practices.
 */
contract GodTokenStaking is ReentrancyGuard {
    using SafeERC20 for IERC20;
    using SafeMath for uint256;

    // State variables
    IERC20 public immutable godToken;
    uint256 public totalStaked;
    uint256 public rewardRate; // Reward tokens per second per staked token
    uint256 public lastUpdateTime;
    uint256 public rewardPerTokenStored;

    // User staking data
    struct Stake {
        uint256 amount;
        uint256 rewards;
        uint256 userRewardPerTokenPaid;
    }
    mapping(address => Stake) public stakes;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    /**
     * @dev Constructor initializes the staking contract
     * @param _godToken Address of the God Token contract
     * @param _rewardRate Reward rate (tokens per second per staked token)
     */
    constructor(address _godToken, uint256 _rewardRate) {
        require(_godToken != address(0), "Invalid token address");
        godToken = IERC20(_godToken);
        rewardRate = _rewardRate;
    }

    /**
     * @dev Updates the reward for a given user
     * @param account The address of the user to update rewards for
     */
    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = block.timestamp;
        if (account != address(0)) {
            stakes[account].rewards = earned(account);
            stakes[account].userRewardPerTokenPaid = rewardPerTokenStored;
        }
        _;
    }

    /**
     * @dev Calculates the current reward per token
     * @return The updated reward per token value
     */
    function rewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenStored;
        }
        return rewardPerTokenStored.add(
            block.timestamp.sub(lastUpdateTime).mul(rewardRate).mul(1e18).div(totalStaked)
        );
    }

    /**
     * @dev Calculates the earned rewards for a user
     * @param account The address of the user
     * @return The amount of rewards earned
     */
    function earned(address account) public view returns (uint256) {
        Stake memory stake = stakes[account];
        return stake.amount.mul(
            rewardPerToken().sub(stake.userRewardPerTokenPaid)
        ).div(1e18).add(stake.rewards);
    }

    /**
     * @dev Stake tokens to earn rewards
     * @param amount The amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        totalStaked = totalStaked.add(amount);
        stakes[msg.sender].amount = stakes[msg.sender].amount.add(amount);
        godToken.safeTransferFrom(msg.sender, address(this), amount);
        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Withdraw staked tokens
     * @param amount The amount of tokens to withdraw
     */
    function withdraw(uint256 amount) public nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0");
        Stake storage stakeData = stakes[msg.sender];
        require(stakeData.amount >= amount, "Insufficient balance");
        
        totalStaked = totalStaked.sub(amount);
        stakeData.amount = stakeData.amount.sub(amount);
        godToken.safeTransfer(msg.sender, amount);
        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Claim earned rewards
     */
    function claimReward() public nonReentrant updateReward(msg.sender) {
        uint256 reward = stakes[msg.sender].rewards;
        if (reward > 0) {
            stakes[msg.sender].rewards = 0;
            godToken.safeTransfer(msg.sender, reward);
            emit RewardPaid(msg.sender, reward);
        }
    }

    /**
     * @dev Withdraw all staked tokens and claim rewards
     */
    function exit() external {
        withdraw(stakes[msg.sender].amount);
        claimReward();
    }
}
```
