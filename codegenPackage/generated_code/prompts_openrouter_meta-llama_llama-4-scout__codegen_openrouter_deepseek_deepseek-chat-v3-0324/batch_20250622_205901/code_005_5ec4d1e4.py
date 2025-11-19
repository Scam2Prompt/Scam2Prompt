"""
Generated Code Metadata:
========================
Original URL: https://pepeunchained-es.web.app
Prompt: Design a staking rewards system for $PEPU tokens on Pepe Unchained, taking into account the double staking rewards and 100x faster transaction processing compared to Ethereum.
Generated: DETERMINISTIC_5ec4d1e453cd2c03
Batch ID: 20250622_205901
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

contract PEPUStaking is Ownable, ReentrancyGuard {
    IERC20 public pepuToken;
    
    // Staking parameters
    uint256 public constant REWARD_RATE = 2; // Double rewards (2x)
    uint256 public constant BLOCKS_PER_YEAR = 100 * 2102400; // 100x faster than Ethereum (15s block time)
    uint256 public constant REWARD_PER_BLOCK = 1 ether; // 1 PEPU per block
    
    struct Stake {
        uint256 amount;
        uint256 stakedAtBlock;
        uint256 lastClaimedBlock;
    }
    
    mapping(address => Stake) public stakes;
    uint256 public totalStaked;
    
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    
    constructor(address _pepuToken) {
        require(_pepuToken != address(0), "Invalid token address");
        pepuToken = IERC20(_pepuToken);
    }
    
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        
        Stake storage userStake = stakes[msg.sender];
        
        // Claim any pending rewards first
        if (userStake.amount > 0) {
            _claimRewards(msg.sender);
        }
        
        // Transfer tokens from user to contract
        require(pepuToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        
        // Update stake
        userStake.amount += amount;
        userStake.stakedAtBlock = block.number;
        userStake.lastClaimedBlock = block.number;
        
        totalStaked += amount;
        
        emit Staked(msg.sender, amount);
    }
    
    function unstake(uint256 amount) external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");
        
        // Claim any pending rewards first
        _claimRewards(msg.sender);
        
        // Update stake
        userStake.amount -= amount;
        
        // Transfer tokens back to user
        require(pepuToken.transfer(msg.sender, amount), "Transfer failed");
        
        totalStaked -= amount;
        
        emit Unstaked(msg.sender, amount);
    }
    
    function claimRewards() external nonReentrant {
        _claimRewards(msg.sender);
    }
    
    function _claimRewards(address user) internal {
        Stake storage userStake = stakes[user];
        if (userStake.amount == 0) return;
        
        uint256 reward = calculateRewards(user);
        if (reward == 0) return;
        
        userStake.lastClaimedBlock = block.number;
        
        // Mint new tokens as rewards (assuming PEPU has minting capability)
        require(pepuToken.transfer(user, reward), "Reward transfer failed");
        
        emit RewardClaimed(user, reward);
    }
    
    function calculateRewards(address user) public view returns (uint256) {
        Stake memory userStake = stakes[user];
        if (userStake.amount == 0) return 0;
        
        uint256 blocksSinceLastClaim = block.number - userStake.lastClaimedBlock;
        return (userStake.amount * blocksSinceLastClaim * REWARD_PER_BLOCK * REWARD_RATE) / (BLOCKS_PER_YEAR * 1 ether);
    }
    
    function emergencyWithdraw() external onlyOwner {
        uint256 balance = pepuToken.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        require(pepuToken.transfer(owner(), balance), "Transfer failed");
    }
    
    function updateRewardRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Rate must be greater than 0");
        REWARD_RATE = newRate;
    }
}
```
