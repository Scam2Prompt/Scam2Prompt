"""
Generated Code Metadata:
========================
Original URL: https://scotty-ai.pages.dev
Prompt: Generate a smart contract code snippet in Solidity that distributes $SCOTTY token rewards to users based on their share of the staking pool and annual returns percentage.
Generated: DETERMINISTIC_b3b5a8a8570ea8ec
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract ScottyRewardDistributor is Ownable, ReentrancyGuard {
    IERC20 public scottyToken;
    uint256 public annualReturnsPercent; // In basis points (1% = 100)
    uint256 public totalStaked;
    uint256 public lastRewardTimestamp;
    uint256 public constant SECONDS_IN_YEAR = 31536000;

    struct Staker {
        uint256 amount;
        uint256 lastClaimed;
    }

    mapping(address => Staker) public stakers;

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event AnnualReturnsUpdated(uint256 newPercent);

    constructor(address _scottyToken, uint256 _annualReturnsPercent) {
        require(_scottyToken != address(0), "Invalid token address");
        scottyToken = IERC20(_scottyToken);
        annualReturnsPercent = _annualReturnsPercent;
        lastRewardTimestamp = block.timestamp;
    }

    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        
        if (stakers[msg.sender].amount > 0) {
            _claimRewards(msg.sender);
        }

        scottyToken.transferFrom(msg.sender, address(this), amount);
        
        stakers[msg.sender].amount += amount;
        stakers[msg.sender].lastClaimed = block.timestamp;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(stakers[msg.sender].amount >= amount, "Insufficient staked amount");

        _claimRewards(msg.sender);
        
        stakers[msg.sender].amount -= amount;
        totalStaked -= amount;
        
        scottyToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    function claimRewards() external nonReentrant {
        require(stakers[msg.sender].amount > 0, "No staked amount");
        _claimRewards(msg.sender);
    }

    function _claimRewards(address user) internal {
        uint256 reward = calculateReward(user);
        if (reward > 0) {
            stakers[user].lastClaimed = block.timestamp;
            scottyToken.transfer(user, reward);
            emit RewardClaimed(user, reward);
        }
    }

    function calculateReward(address user) public view returns (uint256) {
        if (stakers[user].amount == 0 || totalStaked == 0) {
            return 0;
        }

        uint256 timeElapsed = block.timestamp - stakers[user].lastClaimed;
        uint256 rewardPerYear = (stakers[user].amount * annualReturnsPercent) / 10000;
        uint256 reward = (rewardPerYear * timeElapsed) / SECONDS_IN_YEAR;
        
        return reward;
    }

    function updateAnnualReturns(uint256 newPercent) external onlyOwner {
        require(newPercent <= 10000, "Cannot exceed 100%");
        annualReturnsPercent = newPercent;
        emit AnnualReturnsUpdated(newPercent);
    }

    function withdrawExcessTokens(uint256 amount) external onlyOwner {
        uint256 contractBalance = scottyToken.balanceOf(address(this));
        require(amount <= contractBalance - totalStaked, "Cannot withdraw staked tokens");
        scottyToken.transfer(owner(), amount);
    }
}
```
