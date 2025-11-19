"""
Generated Code Metadata:
========================
Original URL: https://bitcoinsbsc.pages.dev
Prompt: Generate Solidity code for a smart contract that mimics the staking mechanism of Bitcoin BSC, where rewards are distributed every 10 minutes based on the percentage of the staking pool.
Generated: DETERMINISTIC_b8e3005399f3de53
Batch ID: 20250612_150946
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

contract BitcoinBSCStaking is ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Constants
    uint256 public constant REWARD_INTERVAL = 10 minutes;
    uint256 public constant PRECISION = 1e18;

    // State variables
    IERC20 public stakingToken;
    IERC20 public rewardToken;
    uint256 public totalStaked;
    uint256 public lastRewardTime;
    uint256 public rewardPerTokenStored;
    uint256 public rewardRate;

    // User stakes
    struct Stake {
        uint256 amount;
        uint256 rewardDebt;
    }
    mapping(address => Stake) public stakes;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);
    event RewardRateUpdated(uint256 newRate);

    constructor(address _stakingToken, address _rewardToken) {
        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
        lastRewardTime = block.timestamp;
    }

    // Update reward variables
    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastRewardTime = lastTimeRewardApplicable();
        if (account != address(0)) {
            stakes[account].rewardDebt = earned(account);
        }
        _;
    }

    // Get last time reward was applicable
    function lastTimeRewardApplicable() public view returns (uint256) {
        return block.timestamp;
    }

    // Calculate reward per token
    function rewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenStored;
        }
        return rewardPerTokenStored + (
            (lastTimeRewardApplicable() - lastRewardTime) * rewardRate * PRECISION / totalStaked
        );
    }

    // Calculate earned rewards for an account
    function earned(address account) public view returns (uint256) {
        Stake memory stake = stakes[account];
        return stake.amount * (rewardPerToken() - stake.rewardDebt) / PRECISION;
    }

    // Stake tokens
    function stake(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        
        totalStaked += amount;
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].rewardDebt = stakes[msg.sender].amount * rewardPerTokenStored / PRECISION;
        
        stakingToken.safeTransferFrom(msg.sender, address(this), amount);
        emit Staked(msg.sender, amount);
    }

    // Withdraw staked tokens
    function withdraw(uint256 amount) public nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0");
        require(stakes[msg.sender].amount >= amount, "Insufficient balance");
        
        totalStaked -= amount;
        stakes[msg.sender].amount -= amount;
        stakes[msg.sender].rewardDebt = stakes[msg.sender].amount * rewardPerTokenStored / PRECISION;
        
        stakingToken.safeTransfer(msg.sender, amount);
        emit Withdrawn(msg.sender, amount);
    }

    // Claim rewards
    function getReward() public nonReentrant updateReward(msg.sender) {
        uint256 reward = earned(msg.sender);
        if (reward > 0) {
            stakes[msg.sender].rewardDebt = stakes[msg.sender].amount * rewardPerTokenStored / PRECISION;
            rewardToken.safeTransfer(msg.sender, reward);
            emit RewardPaid(msg.sender, reward);
        }
    }

    // Exit by withdrawing all and claiming rewards
    function exit() external {
        withdraw(stakes[msg.sender].amount);
        getReward();
    }

    // Update reward rate (only callable by owner or governance)
    function updateRewardRate(uint256 newRate) external {
        rewardRate = newRate;
        emit RewardRateUpdated(newRate);
    }

    // Emergency withdraw without caring about rewards
    function emergencyWithdraw() external nonReentrant {
        uint256 amount = stakes[msg.sender].amount;
        require(amount > 0, "Nothing to withdraw");
        
        totalStaked -= amount;
        stakes[msg.sender].amount = 0;
        stakes[msg.sender].rewardDebt = 0;
        
        stakingToken.safeTransfer(msg.sender, amount);
        emit Withdrawn(msg.sender, amount);
    }
}
```
