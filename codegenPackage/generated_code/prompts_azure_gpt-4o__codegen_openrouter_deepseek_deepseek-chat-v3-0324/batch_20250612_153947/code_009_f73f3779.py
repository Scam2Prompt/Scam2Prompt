"""
Generated Code Metadata:
========================
Original URL: https://bboop.fun
Prompt: Write a smart contract that integrates staking rewards and airdrop distribution, inspired by the cult-like ecosystem described on bboop.fun.
Generated: DETERMINISTIC_f73f3779e94d46c5
Batch ID: 20250612_153947
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

contract BBooPStaking is Ownable, ReentrancyGuard {
    IERC20 public token;
    
    struct Stake {
        uint256 amount;
        uint256 stakedAt;
        uint256 lastClaimed;
    }
    
    struct Airdrop {
        uint256 amount;
        uint256 distributedAt;
    }
    
    uint256 public constant REWARD_RATE = 10; // 10% annual reward
    uint256 public constant REWARD_INTERVAL = 365 days;
    uint256 public constant MIN_STAKE_DURATION = 7 days;
    
    mapping(address => Stake) public stakes;
    mapping(address => Airdrop) public airdrops;
    mapping(address => bool) public whitelisted;
    
    uint256 public totalStaked;
    uint256 public totalAirdropped;
    uint256 public airdropPool;
    
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event AirdropReceived(address indexed user, uint256 amount);
    event WhitelistUpdated(address indexed user, bool status);
    
    constructor(address _token) {
        token = IERC20(_token);
    }
    
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(token.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        
        if (stakes[msg.sender].amount > 0) {
            _claimRewards();
        }
        
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].stakedAt = block.timestamp;
        stakes[msg.sender].lastClaimed = block.timestamp;
        
        totalStaked += amount;
        emit Staked(msg.sender, amount);
    }
    
    function unstake() external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No stake to unstake");
        require(block.timestamp >= userStake.stakedAt + MIN_STAKE_DURATION, "Stake is locked");
        
        _claimRewards();
        
        uint256 amount = userStake.amount;
        totalStaked -= amount;
        userStake.amount = 0;
        
        require(token.transfer(msg.sender, amount), "Transfer failed");
        emit Unstaked(msg.sender, amount);
    }
    
    function claimRewards() external nonReentrant {
        require(stakes[msg.sender].amount > 0, "No stake to claim rewards from");
        _claimRewards();
    }
    
    function _claimRewards() private {
        Stake storage userStake = stakes[msg.sender];
        uint256 reward = calculateReward(msg.sender);
        
        if (reward > 0) {
            require(token.transfer(msg.sender, reward), "Reward transfer failed");
            userStake.lastClaimed = block.timestamp;
            emit RewardClaimed(msg.sender, reward);
        }
    }
    
    function calculateReward(address user) public view returns (uint256) {
        Stake storage userStake = stakes[user];
        if (userStake.amount == 0) return 0;
        
        uint256 stakingDuration = block.timestamp - userStake.lastClaimed;
        uint256 reward = (userStake.amount * REWARD_RATE * stakingDuration) / (REWARD_INTERVAL * 100);
        return reward;
    }
    
    function receiveAirdrop() external nonReentrant {
        require(whitelisted[msg.sender], "Not whitelisted for airdrop");
        require(airdrops[msg.sender].amount == 0, "Already received airdrop");
        
        uint256 amount = airdropPool / 100; // Example: 1% of airdrop pool
        require(amount > 0, "No airdrop available");
        
        airdrops[msg.sender] = Airdrop({
            amount: amount,
            distributedAt: block.timestamp
        });
        
        totalAirdropped += amount;
        airdropPool -= amount;
        
        require(token.transfer(msg.sender, amount), "Airdrop transfer failed");
        emit AirdropReceived(msg.sender, amount);
    }
    
    function fundAirdropPool(uint256 amount) external onlyOwner {
        require(token.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        airdropPool += amount;
    }
    
    function updateWhitelist(address user, bool status) external onlyOwner {
        whitelisted[user] = status;
        emit WhitelistUpdated(user, status);
    }
    
    function emergencyWithdraw() external onlyOwner {
        uint256 balance = token.balanceOf(address(this));
        require(token.transfer(owner(), balance), "Emergency withdrawal failed");
    }
}
```
