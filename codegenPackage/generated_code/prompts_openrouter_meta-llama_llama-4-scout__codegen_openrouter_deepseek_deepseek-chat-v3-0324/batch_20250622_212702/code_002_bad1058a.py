"""
Generated Code Metadata:
========================
Original URL: https://virtuals-race.pages.dev
Prompt: Generate a smart contract code for a decentralized platform that enables users to buy, sell, and claim airdrops of cryptocurrency tokens, with integration to a staking pool and wallet services.
Generated: DETERMINISTIC_bad1058a4f54aa56
Batch ID: 20250622_212702
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract TokenPlatform is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    struct Airdrop {
        uint256 amount;
        uint256 claimableAfter;
        bool claimed;
    }

    struct Stake {
        uint256 amount;
        uint256 stakedAt;
        uint256 unlockTime;
    }

    IERC20 public token;
    uint256 public stakingAPY; // APY percentage (e.g., 1000 = 10%)
    uint256 public minStakeDuration; // in seconds
    uint256 public totalStaked;

    mapping(address => Airdrop) public airdrops;
    mapping(address => Stake[]) public stakes;
    mapping(address => uint256) public stakingRewards;

    event TokensPurchased(address indexed buyer, uint256 amount);
    event TokensSold(address indexed seller, uint256 amount);
    event AirdropClaimed(address indexed recipient, uint256 amount);
    event TokensStaked(address indexed staker, uint256 amount, uint256 duration);
    event TokensUnstaked(address indexed staker, uint256 amount, uint256 reward);
    event RewardClaimed(address indexed staker, uint256 amount);

    constructor(address _token, uint256 _stakingAPY, uint256 _minStakeDuration) {
        token = IERC20(_token);
        stakingAPY = _stakingAPY;
        minStakeDuration = _minStakeDuration;
    }

    function buyTokens(uint256 amount) external payable nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        // In a real implementation, you would handle the payment here
        // This is a simplified version
        token.safeTransfer(msg.sender, amount);
        emit TokensPurchased(msg.sender, amount);
    }

    function sellTokens(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(token.balanceOf(msg.sender) >= amount, "Insufficient balance");
        
        token.safeTransferFrom(msg.sender, address(this), amount);
        // In a real implementation, you would send payment to the seller here
        emit TokensSold(msg.sender, amount);
    }

    function registerAirdrop(address recipient, uint256 amount, uint256 claimDelay) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(airdrops[recipient].amount == 0, "Airdrop already registered");

        airdrops[recipient] = Airdrop({
            amount: amount,
            claimableAfter: block.timestamp + claimDelay,
            claimed: false
        });
    }

    function claimAirdrop() external nonReentrant {
        Airdrop storage airdrop = airdrops[msg.sender];
        require(airdrop.amount > 0, "No airdrop available");
        require(!airdrop.claimed, "Airdrop already claimed");
        require(block.timestamp >= airdrop.claimableAfter, "Airdrop not yet claimable");

        airdrop.claimed = true;
        token.safeTransfer(msg.sender, airdrop.amount);
        emit AirdropClaimed(msg.sender, airdrop.amount);
    }

    function stakeTokens(uint256 amount, uint256 duration) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(duration >= minStakeDuration, "Stake duration too short");
        require(token.balanceOf(msg.sender) >= amount, "Insufficient balance");

        token.safeTransferFrom(msg.sender, address(this), amount);
        
        stakes[msg.sender].push(Stake({
            amount: amount,
            stakedAt: block.timestamp,
            unlockTime: block.timestamp + duration
        }));

        totalStaked += amount;
        emit TokensStaked(msg.sender, amount, duration);
    }

    function unstakeTokens(uint256 stakeIndex) external nonReentrant {
        require(stakeIndex < stakes[msg.sender].length, "Invalid stake index");
        Stake storage stake = stakes[msg.sender][stakeIndex];
        require(block.timestamp >= stake.unlockTime, "Stake not yet unlocked");

        uint256 stakedAmount = stake.amount;
        uint256 reward = calculateReward(stake);
        
        // Remove the stake
        stakes[msg.sender][stakeIndex] = stakes[msg.sender][stakes[msg.sender].length - 1];
        stakes[msg.sender].pop();

        totalStaked -= stakedAmount;
        stakingRewards[msg.sender] += reward;
        
        token.safeTransfer(msg.sender, stakedAmount);
        emit TokensUnstaked(msg.sender, stakedAmount, reward);
    }

    function claimRewards() external nonReentrant {
        uint256 reward = stakingRewards[msg.sender];
        require(reward > 0, "No rewards to claim");

        stakingRewards[msg.sender] = 0;
        token.safeTransfer(msg.sender, reward);
        emit RewardClaimed(msg.sender, reward);
    }

    function calculateReward(Stake memory stake) internal view returns (uint256) {
        uint256 duration = stake.unlockTime - stake.stakedAt;
        uint256 reward = (stake.amount * stakingAPY * duration) / (365 days * 10000);
        return reward;
    }

    function setStakingAPY(uint256 _stakingAPY) external onlyOwner {
        stakingAPY = _stakingAPY;
    }

    function setMinStakeDuration(uint256 _minStakeDuration) external onlyOwner {
        minStakeDuration = _minStakeDuration;
    }

    function withdrawTokens(uint256 amount) external onlyOwner {
        require(token.balanceOf(address(this)) >= amount, "Insufficient contract balance");
        token.safeTransfer(owner(), amount);
    }

    function getUserStakes(address user) external view returns (Stake[] memory) {
        return stakes[user];
    }

    function getPendingRewards(address user) external view returns (uint256) {
        uint256 totalRewards = stakingRewards[user];
        
        for (uint256 i = 0; i < stakes[user].length; i++) {
            Stake memory stake = stakes[user][i];
            if (block.timestamp >= stake.unlockTime) {
                totalRewards += calculateReward(stake);
            }
        }
        
        return totalRewards;
    }
}
```
