"""
Generated Code Metadata:
========================
Original URL: https://dogecoin20-en.web.app
Prompt: Develop a smart contract in Solidity to distribute staking rewards to DOGE20 token holders over a 2-year period.
Generated: DETERMINISTIC_9b9b0f47c18804d0
Batch ID: 20250622_210216
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract DOGE20StakingRewards is Ownable {
    using SafeMath for uint256;

    IERC20 public token;
    uint256 public totalRewards;
    uint256 public startTime;
    uint256 public endTime;
    uint256 public totalDistributed;
    uint256 public constant DURATION = 730 days; // 2 years in days

    mapping(address => uint256) public balances;
    mapping(address => uint256) public claimedRewards;

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardsDeposited(uint256 amount);

    constructor(address _token) {
        require(_token != address(0), "Invalid token address");
        token = IERC20(_token);
    }

    function depositRewards(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(token.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        totalRewards = totalRewards.add(amount);
        startTime = block.timestamp;
        endTime = startTime.add(DURATION);

        emit RewardsDeposited(amount);
    }

    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(token.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        balances[msg.sender] = balances[msg.sender].add(amount);
        emit Staked(msg.sender, amount);
    }

    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        claimReward();

        balances[msg.sender] = balances[msg.sender].sub(amount);
        require(token.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    function claimReward() public {
        uint256 reward = calculateReward(msg.sender);
        if (reward > 0) {
            claimedRewards[msg.sender] = claimedRewards[msg.sender].add(reward);
            totalDistributed = totalDistributed.add(reward);
            require(token.transfer(msg.sender, reward), "Transfer failed");
            emit RewardClaimed(msg.sender, reward);
        }
    }

    function calculateReward(address user) public view returns (uint256) {
        if (balances[user] == 0 || totalRewards == 0 || block.timestamp < startTime) {
            return 0;
        }

        uint256 currentTime = block.timestamp > endTime ? endTime : block.timestamp;
        uint256 timeElapsed = currentTime.sub(startTime);
        uint256 totalStaked = token.balanceOf(address(this)).add(totalDistributed).sub(totalRewards);

        if (totalStaked == 0) {
            return 0;
        }

        uint256 totalReward = totalRewards.mul(timeElapsed).div(DURATION);
        uint256 pendingReward = totalReward.sub(totalDistributed);
        uint256 userReward = pendingReward.mul(balances[user]).div(totalStaked);

        return userReward;
    }

    function getStakedBalance(address user) external view returns (uint256) {
        return balances[user];
    }

    function getClaimedRewards(address user) external view returns (uint256) {
        return claimedRewards[user];
    }

    function getPendingReward(address user) external view returns (uint256) {
        return calculateReward(user);
    }

    function emergencyWithdraw() external onlyOwner {
        uint256 balance = token.balanceOf(address(this));
        require(token.transfer(owner(), balance), "Transfer failed");
    }
}
```
