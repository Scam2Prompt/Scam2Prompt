"""
Generated Code Metadata:
========================
Original URL: https://claires.pages.dev
Prompt: Design a use case for Symbiotic's restaking logic in a decentralized finance (DeFi) application, such as a lending protocol or a stablecoin.
Generated: DETERMINISTIC_cfc5c8c5878891c7
Batch ID: 20250622_212712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title SymbioticRestaking
 * @dev A contract that implements restaking logic for DeFi protocols, allowing users
 * to restake their rewards to maximize yield while maintaining security.
 */
contract SymbioticRestaking is ReentrancyGuard, Ownable {
    IERC20 public stakingToken;
    IERC20 public rewardToken;

    uint256 public totalStaked;
    uint256 public rewardRate;
    uint256 public lastUpdateTime;
    uint256 public rewardPerTokenStored;

    mapping(address => uint256) public userStaked;
    mapping(address => uint256) public userRewards;
    mapping(address => uint256) public userRewardPerTokenPaid;

    event Staked(address indexed user, uint256 amount);
    event Restaked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);
    event RewardRateUpdated(uint256 newRate);

    /**
     * @dev Constructor initializes the staking and reward tokens
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
     * @dev Updates the reward for a given user
     * @param account The address of the user to update rewards for
     */
    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = block.timestamp;
        if (account != address(0)) {
            userRewards[account] = earned(account);
            userRewardPerTokenPaid[account] = rewardPerTokenStored;
        }
        _;
    }

    /**
     * @dev Calculates the current reward per token
     * @return The updated reward per token
     */
    function rewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenStored;
        }
        return rewardPerTokenStored + (
            (block.timestamp - lastUpdateTime) * rewardRate * 1e18 / totalStaked
        );
    }

    /**
     * @dev Calculates the earned rewards for a user
     * @param account The address of the user
     * @return The amount of rewards earned
     */
    function earned(address account) public view returns (uint256) {
        return userStaked[account] * (
            rewardPerToken() - userRewardPerTokenPaid[account]
        ) / 1e18 + userRewards[account];
    }

    /**
     * @dev Stake tokens into the contract
     * @param amount The amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        
        totalStaked += amount;
        userStaked[msg.sender] += amount;
        
        require(
            stakingToken.transferFrom(msg.sender, address(this), amount),
            "Staking transfer failed"
        );
        
        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Restake earned rewards
     */
    function restake() external nonReentrant updateReward(msg.sender) {
        uint256 reward = userRewards[msg.sender];
        require(reward > 0, "No rewards to restake");
        
        userRewards[msg.sender] = 0;
        totalStaked += reward;
        userStaked[msg.sender] += reward;
        
        emit Restaked(msg.sender, reward);
    }

    /**
     * @dev Withdraw staked tokens
     * @param amount The amount of tokens to withdraw
     */
    function withdraw(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0");
        require(userStaked[msg.sender] >= amount, "Insufficient balance");
        
        totalStaked -= amount;
        userStaked[msg.sender] -= amount;
        
        require(
            stakingToken.transfer(msg.sender, amount),
            "Withdrawal transfer failed"
        );
        
        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Claim earned rewards
     */
    function claimReward() external nonReentrant updateReward(msg.sender) {
        uint256 reward = userRewards[msg.sender];
        require(reward > 0, "No rewards to claim");
        
        userRewards[msg.sender] = 0;
        
        require(
            rewardToken.transfer(msg.sender, reward),
            "Reward transfer failed"
        );
        
        emit RewardPaid(msg.sender, reward);
    }

    /**
     * @dev Update the reward rate (only callable by owner)
     * @param newRate The new reward rate per second
     */
    function updateRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
        emit RewardRateUpdated(newRate);
    }

    /**
     * @dev Emergency withdraw all staked tokens without claiming rewards
     */
    function emergencyWithdraw() external nonReentrant {
        uint256 amount = userStaked[msg.sender];
        require(amount > 0, "No tokens to withdraw");
        
        totalStaked -= amount;
        userStaked[msg.sender] = 0;
        userRewards[msg.sender] = 0;
        
        require(
            stakingToken.transfer(msg.sender, amount),
            "Emergency withdrawal failed"
        );
        
        emit Withdrawn(msg.sender, amount);
    }
}
```
