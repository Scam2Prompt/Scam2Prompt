"""
Generated Code Metadata:
========================
Original URL: https://cryptoallstars-reward.web.app
Prompt: Write a Solidity contract that enables staking rewards to scale based on the number of tokens held by the user, inspired by the $STARS reward mechanism.
Generated: DETERMINISTIC_233ae3ab5b2c001a
Batch ID: 20250612_154133
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

contract StakingRewards is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Struct to store user staking information
    struct UserInfo {
        uint256 amount;     // How many tokens the user has staked
        uint256 rewardDebt; // Reward debt for scaling rewards
        uint256 lastClaim;  // Timestamp of last claim
    }

    // The staking token
    IERC20 public stakingToken;
    // The reward token
    IERC20 public rewardToken;

    // Reward rate per second
    uint256 public rewardRate;
    // Total staked tokens
    uint256 public totalStaked;
    // Last update time for rewards
    uint256 public lastUpdateTime;
    // Reward per token stored
    uint256 public rewardPerTokenStored;

    // Mapping from user address to user info
    mapping(address => UserInfo) public userInfo;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);
    event RewardRateUpdated(uint256 newRate);

    constructor(
        address _stakingToken,
        address _rewardToken,
        uint256 _rewardRate
    ) {
        require(_stakingToken != address(0), "Staking token cannot be zero address");
        require(_rewardToken != address(0), "Reward token cannot be zero address");
        
        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
        rewardRate = _rewardRate;
        lastUpdateTime = block.timestamp;
    }

    // Update reward variables
    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = lastTimeRewardApplicable();
        if (account != address(0)) {
            userInfo[account].rewardDebt = earned(account);
            userInfo[account].lastClaim = block.timestamp;
        }
        _;
    }

    // Get the last time reward was applicable
    function lastTimeRewardApplicable() public view returns (uint256) {
        return block.timestamp;
    }

    // Calculate reward per token
    function rewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenStored;
        }
        return rewardPerTokenStored + 
            ((lastTimeRewardApplicable() - lastUpdateTime) * rewardRate * 1e18) / totalStaked;
    }

    // Calculate earned rewards for an account
    function earned(address account) public view returns (uint256) {
        UserInfo storage user = userInfo[account];
        return (user.amount * (rewardPerToken() - user.rewardDebt)) / 1e18;
    }

    // Stake tokens
    function stake(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        
        UserInfo storage user = userInfo[msg.sender];
        totalStaked += amount;
        user.amount += amount;
        user.rewardDebt = (user.amount * rewardPerToken()) / 1e18;
        
        stakingToken.safeTransferFrom(msg.sender, address(this), amount);
        emit Staked(msg.sender, amount);
    }

    // Withdraw staked tokens
    function withdraw(uint256 amount) public nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0");
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= amount, "Withdraw amount exceeds balance");
        
        totalStaked -= amount;
        user.amount -= amount;
        user.rewardDebt = (user.amount * rewardPerToken()) / 1e18;
        
        stakingToken.safeTransfer(msg.sender, amount);
        emit Withdrawn(msg.sender, amount);
    }

    // Claim rewards
    function claimReward() public nonReentrant updateReward(msg.sender) {
        uint256 reward = earned(msg.sender);
        if (reward > 0) {
            UserInfo storage user = userInfo[msg.sender];
            user.rewardDebt = (user.amount * rewardPerToken()) / 1e18;
            
            rewardToken.safeTransfer(msg.sender, reward);
            emit RewardPaid(msg.sender, reward);
        }
    }

    // Exit by withdrawing all staked tokens and claiming rewards
    function exit() external {
        withdraw(userInfo[msg.sender].amount);
        claimReward();
    }

    // Update reward rate (only owner)
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
        emit RewardRateUpdated(_rewardRate);
    }

    // Recover ERC20 tokens (only owner)
    function recoverERC20(address tokenAddress, uint256 tokenAmount) external onlyOwner {
        require(tokenAddress != address(stakingToken), "Cannot withdraw staking token");
        IERC20(tokenAddress).safeTransfer(owner(), tokenAmount);
    }
}
```
