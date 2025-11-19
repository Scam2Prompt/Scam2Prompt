"""
Generated Code Metadata:
========================
Original URL: https://pepearab.pages.dev
Prompt: Generate code to integrate the PepeArab staking functionality into a decentralized application (dApp), allowing users to stake $PEAB tokens and calculate rewards based on APY.
Generated: DETERMINISTIC_0e762e334a78457b
Batch ID: 20250612_145730
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
import "@openzeppelin/contracts/access/Ownable.sol";

contract PepeArabStaking is ReentrancyGuard, Ownable {
    using SafeERC20 for IERC20;

    // Staking token
    IERC20 public immutable stakingToken;

    // Reward parameters
    uint256 public constant REWARD_PRECISION = 1e18;
    uint256 public apy; // Annual Percentage Yield (e.g., 1000 = 10%)
    uint256 public rewardRate;
    uint256 public lastUpdateTime;
    uint256 public rewardPerTokenStored;

    // User staking data
    struct UserStake {
        uint256 balance;
        uint256 rewards;
        uint256 userRewardPerTokenPaid;
    }
    mapping(address => UserStake) public userStakes;

    // Total staked amount
    uint256 private _totalStaked;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);
    event APYUpdated(uint256 newAPY);

    constructor(address _stakingToken, uint256 _apy) {
        stakingToken = IERC20(_stakingToken);
        apy = _apy;
        _updateRewardRate();
    }

    // Update APY and recalculate reward rate
    function setAPY(uint256 _apy) external onlyOwner {
        apy = _apy;
        _updateRewardRate();
        emit APYUpdated(_apy);
    }

    // Calculate current reward rate based on APY
    function _updateRewardRate() private {
        rewardRate = (apy * REWARD_PRECISION) / (365 days * 100);
    }

    // Update reward calculations
    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = block.timestamp;
        if (account != address(0)) {
            userStakes[account].rewards = earned(account);
            userStakes[account].userRewardPerTokenPaid = rewardPerTokenStored;
        }
        _;
    }

    // Calculate reward per token
    function rewardPerToken() public view returns (uint256) {
        if (_totalStaked == 0) {
            return rewardPerTokenStored;
        }
        return
            rewardPerTokenStored +
            (((block.timestamp - lastUpdateTime) * rewardRate * REWARD_PRECISION) / _totalStaked);
    }

    // Calculate earned rewards for an account
    function earned(address account) public view returns (uint256) {
        UserStake memory user = userStakes[account];
        return
            ((user.balance * (rewardPerToken() - user.userRewardPerTokenPaid)) / REWARD_PRECISION) +
            user.rewards;
    }

    // Stake tokens
    function stake(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        
        UserStake storage user = userStakes[msg.sender];
        _totalStaked += amount;
        user.balance += amount;
        
        stakingToken.safeTransferFrom(msg.sender, address(this), amount);
        emit Staked(msg.sender, amount);
    }

    // Withdraw staked tokens
    function withdraw(uint256 amount) public nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0");
        
        UserStake storage user = userStakes[msg.sender];
        require(user.balance >= amount, "Insufficient balance");
        
        _totalStaked -= amount;
        user.balance -= amount;
        
        stakingToken.safeTransfer(msg.sender, amount);
        emit Withdrawn(msg.sender, amount);
    }

    // Claim rewards
    function getReward() public nonReentrant updateReward(msg.sender) {
        uint256 reward = userStakes[msg.sender].rewards;
        if (reward > 0) {
            userStakes[msg.sender].rewards = 0;
            stakingToken.safeTransfer(msg.sender, reward);
            emit RewardPaid(msg.sender, reward);
        }
    }

    // Exit staking (withdraw all and claim rewards)
    function exit() external {
        withdraw(userStakes[msg.sender].balance);
        getReward();
    }

    // Get total staked amount
    function totalStaked() external view returns (uint256) {
        return _totalStaked;
    }

    // Get user staked amount
    function balanceOf(address account) external view returns (uint256) {
        return userStakes[account].balance;
    }

    // Recover ERC20 tokens (emergency only)
    function recoverERC20(address tokenAddress, uint256 tokenAmount) external onlyOwner {
        require(tokenAddress != address(stakingToken), "Cannot withdraw staking token");
        IERC20(tokenAddress).safeTransfer(owner(), tokenAmount);
    }
}
```
