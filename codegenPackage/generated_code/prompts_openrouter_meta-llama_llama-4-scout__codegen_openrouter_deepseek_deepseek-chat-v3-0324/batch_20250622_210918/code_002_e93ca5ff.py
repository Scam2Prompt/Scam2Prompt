"""
Generated Code Metadata:
========================
Original URL: https://fi-dapp-git-hotfix-pendle-zircuit-etherfi.vercel.app
Prompt: "Generate a smart contract function to facilitate (re)staking with eETH on the etherfi platform."
Generated: DETERMINISTIC_e93ca5ff5eade2b6
Batch ID: 20250622_210918
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

contract EtherFiStaking is ReentrancyGuard {
    using SafeERC20 for IERC20;

    IERC20 public eETH;
    address public etherFiTreasury;

    mapping(address => uint256) public stakedBalances;
    mapping(address => uint256) public rewardBalances;
    mapping(address => uint256) public lastStakeTime;

    uint256 public constant MIN_STAKE_AMOUNT = 0.01 ether;
    uint256 public constant LOCK_PERIOD = 30 days;
    uint256 public constant REWARD_RATE = 5; // 5% APY

    event Staked(address indexed user, uint256 amount);
    event Restaked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    constructor(address _eETH, address _treasury) {
        require(_eETH != address(0), "Invalid eETH address");
        require(_treasury != address(0), "Invalid treasury address");
        eETH = IERC20(_eETH);
        etherFiTreasury = _treasury;
    }

    function stake(uint256 amount) external nonReentrant {
        require(amount >= MIN_STAKE_AMOUNT, "Amount below minimum stake");
        require(eETH.balanceOf(msg.sender) >= amount, "Insufficient balance");

        _updateRewards(msg.sender);

        eETH.safeTransferFrom(msg.sender, address(this), amount);
        stakedBalances[msg.sender] += amount;
        lastStakeTime[msg.sender] = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    function restake() external nonReentrant {
        uint256 rewards = _calculateRewards(msg.sender);
        require(rewards > 0, "No rewards to restake");

        _updateRewards(msg.sender);
        stakedBalances[msg.sender] += rewards;
        lastStakeTime[msg.sender] = block.timestamp;

        emit Restaked(msg.sender, rewards);
    }

    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");
        require(
            block.timestamp >= lastStakeTime[msg.sender] + LOCK_PERIOD,
            "Funds are locked"
        );

        _updateRewards(msg.sender);

        stakedBalances[msg.sender] -= amount;
        eETH.safeTransfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    function claimRewards() external nonReentrant {
        uint256 rewards = _calculateRewards(msg.sender);
        require(rewards > 0, "No rewards to claim");

        _updateRewards(msg.sender);
        rewardBalances[msg.sender] = 0;
        eETH.safeTransferFrom(etherFiTreasury, msg.sender, rewards);

        emit RewardClaimed(msg.sender, rewards);
    }

    function _updateRewards(address user) internal {
        uint256 rewards = _calculateRewards(user);
        if (rewards > 0) {
            rewardBalances[user] += rewards;
        }
        lastStakeTime[user] = block.timestamp;
    }

    function _calculateRewards(address user) internal view returns (uint256) {
        if (stakedBalances[user] == 0) {
            return 0;
        }

        uint256 timeElapsed = block.timestamp - lastStakeTime[user];
        uint256 annualReward = (stakedBalances[user] * REWARD_RATE) / 100;
        uint256 reward = (annualReward * timeElapsed) / 365 days;

        return reward;
    }

    function getStakedBalance(address user) external view returns (uint256) {
        return stakedBalances[user];
    }

    function getPendingRewards(address user) external view returns (uint256) {
        return rewardBalances[user] + _calculateRewards(user);
    }
}
```
