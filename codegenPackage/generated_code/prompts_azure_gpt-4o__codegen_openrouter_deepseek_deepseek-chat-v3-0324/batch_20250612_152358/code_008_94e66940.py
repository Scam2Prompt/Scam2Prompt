"""
Generated Code Metadata:
========================
Original URL: https://appscottyclaims.pages.dev
Prompt: Develop a Solidity contract to lock liquidity for $SCOTTY tokens, ensuring rewards distribution and staking functionality for the Scotty AI cryptoverse.
Generated: DETERMINISTIC_94e66940e7466b9c
Batch ID: 20250612_152358
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

contract ScottyLiquidityLocker is Ownable, ReentrancyGuard {
    IERC20 public scottyToken;
    IERC20 public lpToken;

    struct Lock {
        uint256 amount;
        uint256 unlockTime;
        bool withdrawn;
    }

    struct Stake {
        uint256 amount;
        uint256 stakedAt;
        uint256 lastClaimed;
    }

    uint256 public totalLocked;
    uint256 public totalStaked;
    uint256 public rewardRate = 100; // 100 tokens per second per staked token (example rate)
    uint256 public lockDuration = 30 days;
    uint256 public minLockAmount = 1000 * 10**18; // 1000 tokens minimum

    mapping(address => Lock) public locks;
    mapping(address => Stake) public stakes;
    mapping(address => uint256) public rewards;

    event LiquidityLocked(address indexed user, uint256 amount, uint256 unlockTime);
    event LiquidityWithdrawn(address indexed user, uint256 amount);
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    constructor(address _scottyToken, address _lpToken) {
        require(_scottyToken != address(0), "Invalid SCOTTY token address");
        require(_lpToken != address(0), "Invalid LP token address");
        scottyToken = IERC20(_scottyToken);
        lpToken = IERC20(_lpToken);
    }

    function lockLiquidity(uint256 amount) external {
        require(amount >= minLockAmount, "Amount below minimum");
        require(lpToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        locks[msg.sender] = Lock({
            amount: amount,
            unlockTime: block.timestamp + lockDuration,
            withdrawn: false
        });

        totalLocked += amount;
        emit LiquidityLocked(msg.sender, amount, block.timestamp + lockDuration);
    }

    function withdrawLiquidity() external nonReentrant {
        Lock storage userLock = locks[msg.sender];
        require(userLock.amount > 0, "No locked liquidity");
        require(block.timestamp >= userLock.unlockTime, "Lock period not ended");
        require(!userLock.withdrawn, "Already withdrawn");

        userLock.withdrawn = true;
        totalLocked -= userLock.amount;

        require(lpToken.transfer(msg.sender, userLock.amount), "Transfer failed");
        emit LiquidityWithdrawn(msg.sender, userLock.amount);
    }

    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0");
        require(scottyToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        if (stakes[msg.sender].amount > 0) {
            _calculateRewards(msg.sender);
        }

        stakes[msg.sender].amount += amount;
        stakes[msg.sender].stakedAt = block.timestamp;
        stakes[msg.sender].lastClaimed = block.timestamp;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Cannot unstake 0");
        require(stakes[msg.sender].amount >= amount, "Insufficient stake");

        _calculateRewards(msg.sender);

        stakes[msg.sender].amount -= amount;
        totalStaked -= amount;

        require(scottyToken.transfer(msg.sender, amount), "Transfer failed");
        emit Unstaked(msg.sender, amount);
    }

    function claimRewards() external nonReentrant {
        _calculateRewards(msg.sender);
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");

        rewards[msg.sender] = 0;
        require(scottyToken.transfer(msg.sender, reward), "Transfer failed");
        emit RewardClaimed(msg.sender, reward);
    }

    function _calculateRewards(address user) internal {
        if (stakes[user].amount == 0) return;

        uint256 timeElapsed = block.timestamp - stakes[user].lastClaimed;
        uint256 reward = stakes[user].amount * rewardRate * timeElapsed / 1e18;

        rewards[user] += reward;
        stakes[user].lastClaimed = block.timestamp;
    }

    function setRewardRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Rate cannot be 0");
        rewardRate = newRate;
    }

    function setLockDuration(uint256 newDuration) external onlyOwner {
        require(newDuration > 0, "Duration cannot be 0");
        lockDuration = newDuration;
    }

    function setMinLockAmount(uint256 newAmount) external onlyOwner {
        minLockAmount = newAmount;
    }

    function emergencyWithdrawTokens(address token, uint256 amount) external onlyOwner {
        require(token != address(lpToken) || totalLocked == 0, "Cannot withdraw locked LP");
        IERC20(token).transfer(owner(), amount);
    }
}
```
