"""
Generated Code Metadata:
========================
Original URL: https://rocket-pool.xyz
Prompt: Write a smart contract in Solidity that integrates Rocket Pool's rETH token into a DeFi protocol, allowing users to stake rETH and earn rewards. Include functionality for calculating rETH/ETH exchange rates based on Rocket Pool's reward distribution mechanism.
Generated: DETERMINISTIC_06d5493fe64c50a2
Batch ID: 20250612_153821
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

interface IRocketTokenRETH {
    function getEthValue(uint256 _rethAmount) external view returns (uint256);
    function getRethValue(uint256 _ethAmount) external view returns (uint256);
    function balanceOf(address account) external view returns (uint256);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
}

contract RethStaking is ReentrancyGuard, Ownable {
    using SafeERC20 for IERC20;
    using SafeERC20 for IRocketTokenRETH;

    // State variables
    IRocketTokenRETH public immutable rETH;
    uint256 public totalStaked;
    uint256 public rewardRate;
    uint256 public lastUpdateTime;
    uint256 public rewardPerTokenStored;
    uint256 public rewardPeriodEnd;

    mapping(address => uint256) public userStaked;
    mapping(address => uint256) public userRewards;
    mapping(address => uint256) public userRewardPerTokenPaid;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);
    event RewardRateUpdated(uint256 newRate, uint256 duration);

    constructor(address _rETH) {
        rETH = IRocketTokenRETH(_rETH);
    }

    // Modifier to update reward for caller
    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = lastTimeRewardApplicable();
        if (account != address(0)) {
            userRewards[account] = earned(account);
            userRewardPerTokenPaid[account] = rewardPerTokenStored;
        }
        _;
    }

    // Returns the latest time reward is applicable
    function lastTimeRewardApplicable() public view returns (uint256) {
        return block.timestamp < rewardPeriodEnd ? block.timestamp : rewardPeriodEnd;
    }

    // Returns reward per token staked
    function rewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenStored;
        }
        return rewardPerTokenStored + (
            (lastTimeRewardApplicable() - lastUpdateTime) * rewardRate * 1e18 / totalStaked
        );
    }

    // Returns earned rewards for an account
    function earned(address account) public view returns (uint256) {
        return (userStaked[account] * (rewardPerToken() - userRewardPerTokenPaid[account]) / 1e18) + userRewards[account];
    }

    // Returns current rETH/ETH exchange rate from Rocket Pool
    function getEthValue(uint256 rEthAmount) public view returns (uint256) {
        return rETH.getEthValue(rEthAmount);
    }

    // Returns current ETH/rETH exchange rate from Rocket Pool
    function getRethValue(uint256 ethAmount) public view returns (uint256) {
        return rETH.getRethValue(ethAmount);
    }

    // Stake rETH tokens
    function stake(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        totalStaked += amount;
        userStaked[msg.sender] += amount;
        rETH.safeTransferFrom(msg.sender, address(this), amount);
        emit Staked(msg.sender, amount);
    }

    // Withdraw staked rETH tokens
    function withdraw(uint256 amount) public nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0");
        require(userStaked[msg.sender] >= amount, "Insufficient balance");
        totalStaked -= amount;
        userStaked[msg.sender] -= amount;
        rETH.safeTransfer(msg.sender, amount);
        emit Withdrawn(msg.sender, amount);
    }

    // Claim rewards
    function getReward() public nonReentrant updateReward(msg.sender) {
        uint256 reward = userRewards[msg.sender];
        if (reward > 0) {
            userRewards[msg.sender] = 0;
            // Transfer ETH rewards (convert from rETH if needed)
            (bool success, ) = msg.sender.call{value: reward}("");
            require(success, "Reward transfer failed");
            emit RewardPaid(msg.sender, reward);
        }
    }

    // Exit by withdrawing all and claiming rewards
    function exit() external {
        withdraw(userStaked[msg.sender]);
        getReward();
    }

    // Set reward rate (only owner)
    function setRewardRate(uint256 rate, uint256 duration) external onlyOwner {
        require(block.timestamp + duration >= rewardPeriodEnd, "Cannot reduce existing period");
        require(rate > 0, "Reward rate must be positive");

        // Update rewards before changing rate
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = block.timestamp;
        if (block.timestamp >= rewardPeriodEnd) {
            rewardRate = rate;
        } else {
            uint256 remaining = rewardPeriodEnd - block.timestamp;
            uint256 leftover = remaining * rewardRate;
            rewardRate = (leftover + rate * duration) / duration;
        }

        rewardPeriodEnd = block.timestamp + duration;
        emit RewardRateUpdated(rewardRate, duration);
    }

    // Allow contract to receive ETH (for rewards)
    receive() external payable {}
}
```
