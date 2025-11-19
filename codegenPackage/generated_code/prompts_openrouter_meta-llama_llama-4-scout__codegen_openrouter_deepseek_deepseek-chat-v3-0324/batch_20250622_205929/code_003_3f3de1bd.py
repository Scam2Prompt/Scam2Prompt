"""
Generated Code Metadata:
========================
Original URL: https://wdymdapp.pages.dev
Prompt: Create a decentralized application (DApp) interface for users to stake, unstake, and claim rewards for a token, incorporating security measures such as a maximum penalty restriction and safeguard measures.
Generated: DETERMINISTIC_3f3de1bd6066372d
Batch ID: 20250622_205929
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

contract StakingDApp is Ownable, ReentrancyGuard {
    IERC20 public stakingToken;
    IERC20 public rewardToken;

    uint256 public constant MAX_PENALTY = 20; // 20% maximum penalty
    uint256 public penaltyRate = 10; // Default 10% penalty
    uint256 public rewardRate = 100; // 100 tokens per second per staked token
    uint256 public lastUpdateTime;
    uint256 public rewardPerTokenStored;

    mapping(address => uint256) public userRewardPerTokenPaid;
    mapping(address => uint256) public rewards;
    mapping(address => uint256) public balances;
    mapping(address => uint256) public stakedTimestamps;

    uint256 private _totalSupply;

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event PenaltyRateUpdated(uint256 newRate);

    constructor(address _stakingToken, address _rewardToken) {
        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
    }

    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = block.timestamp;
        if (account != address(0)) {
            rewards[account] = earned(account);
            userRewardPerTokenPaid[account] = rewardPerTokenStored;
        }
        _;
    }

    function rewardPerToken() public view returns (uint256) {
        if (_totalSupply == 0) {
            return rewardPerTokenStored;
        }
        return
            rewardPerTokenStored +
            (((block.timestamp - lastUpdateTime) * rewardRate * 1e18) / _totalSupply);
    }

    function earned(address account) public view returns (uint256) {
        return
            ((balances[account] *
                (rewardPerToken() - userRewardPerTokenPaid[account])) / 1e18) +
            rewards[account];
    }

    function stake(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot stake 0");
        stakingToken.transferFrom(msg.sender, address(this), amount);
        _totalSupply += amount;
        balances[msg.sender] += amount;
        stakedTimestamps[msg.sender] = block.timestamp;
        emit Staked(msg.sender, amount);
    }

    function unstake(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot unstake 0");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        uint256 penalty = calculatePenalty(msg.sender, amount);
        uint256 amountAfterPenalty = amount - penalty;

        _totalSupply -= amount;
        balances[msg.sender] -= amount;

        stakingToken.transfer(msg.sender, amountAfterPenalty);
        if (penalty > 0) {
            stakingToken.transfer(owner(), penalty);
        }

        emit Unstaked(msg.sender, amount);
    }

    function claimReward() external nonReentrant updateReward(msg.sender) {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");
        rewards[msg.sender] = 0;
        rewardToken.transfer(msg.sender, reward);
        emit RewardClaimed(msg.sender, reward);
    }

    function calculatePenalty(address user, uint256 amount) public view returns (uint256) {
        uint256 stakedTime = block.timestamp - stakedTimestamps[user];
        if (stakedTime >= 7 days) {
            return 0;
        }
        uint256 penalty = (amount * penaltyRate) / 100;
        return penalty > (amount * MAX_PENALTY) / 100 ? (amount * MAX_PENALTY) / 100 : penalty;
    }

    function setPenaltyRate(uint256 newRate) external onlyOwner {
        require(newRate <= MAX_PENALTY, "Penalty rate exceeds maximum");
        penaltyRate = newRate;
        emit PenaltyRateUpdated(newRate);
    }

    function setRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
        lastUpdateTime = block.timestamp;
    }

    function withdrawRewardTokens(uint256 amount) external onlyOwner {
        rewardToken.transfer(owner(), amount);
    }

    function emergencyWithdraw() external nonReentrant {
        uint256 amount = balances[msg.sender];
        require(amount > 0, "No tokens staked");
        _totalSupply -= amount;
        balances[msg.sender] = 0;
        stakingToken.transfer(msg.sender, amount);
    }
}
```
