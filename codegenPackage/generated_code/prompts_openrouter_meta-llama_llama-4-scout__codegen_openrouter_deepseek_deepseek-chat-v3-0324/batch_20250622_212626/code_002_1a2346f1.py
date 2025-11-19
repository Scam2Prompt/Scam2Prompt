"""
Generated Code Metadata:
========================
Original URL: https://turbos-coin.com
Prompt: Generate a Solidity code snippet for creating a simple decentralized application (dApp) that integrates with the Turbo Token ecosystem.
Generated: DETERMINISTIC_1a2346f1548a7516
Batch ID: 20250622_212626
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

/**
 * @title TurboDApp
 * @dev A simple dApp that integrates with Turbo Token ecosystem
 * Allows users to stake Turbo Tokens and earn rewards
 */
contract TurboDApp is Ownable, ReentrancyGuard {
    IERC20 public turboToken;
    
    struct Stake {
        uint256 amount;
        uint256 timestamp;
    }
    
    mapping(address => Stake) public stakes;
    uint256 public rewardRate = 100; // 100 wei per token per second
    uint256 public totalStaked;
    
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    
    /**
     * @dev Constructor sets the Turbo Token address
     * @param _turboTokenAddress Address of the Turbo Token contract
     */
    constructor(address _turboTokenAddress) {
        require(_turboTokenAddress != address(0), "Invalid token address");
        turboToken = IERC20(_turboTokenAddress);
    }
    
    /**
     * @dev Stake Turbo Tokens into the dApp
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        
        if (stakes[msg.sender].amount > 0) {
            claimReward();
        }
        
        require(
            turboToken.transferFrom(msg.sender, address(this), amount),
            "Transfer failed"
        );
        
        stakes[msg.sender] = Stake({
            amount: stakes[msg.sender].amount + amount,
            timestamp: block.timestamp
        });
        
        totalStaked += amount;
        emit Staked(msg.sender, amount);
    }
    
    /**
     * @dev Unstake Turbo Tokens from the dApp
     * @param amount Amount of tokens to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(stakes[msg.sender].amount >= amount, "Insufficient stake");
        
        claimReward();
        
        stakes[msg.sender].amount -= amount;
        totalStaked -= amount;
        
        require(
            turboToken.transfer(msg.sender, amount),
            "Transfer failed"
        );
        
        emit Unstaked(msg.sender, amount);
    }
    
    /**
     * @dev Calculate and claim accumulated rewards
     */
    function claimReward() public nonReentrant {
        uint256 reward = calculateReward(msg.sender);
        if (reward > 0) {
            stakes[msg.sender].timestamp = block.timestamp;
            require(
                turboToken.transfer(msg.sender, reward),
                "Reward transfer failed"
            );
            emit RewardClaimed(msg.sender, reward);
        }
    }
    
    /**
     * @dev Calculate current reward for a staker
     * @param staker Address of the staker
     * @return reward Calculated reward amount
     */
    function calculateReward(address staker) public view returns (uint256 reward) {
        Stake memory stakeInfo = stakes[staker];
        if (stakeInfo.amount == 0) {
            return 0;
        }
        
        uint256 duration = block.timestamp - stakeInfo.timestamp;
        reward = stakeInfo.amount * duration * rewardRate / 1e18;
    }
    
    /**
     * @dev Update the reward rate (owner only)
     * @param newRate New reward rate in wei per token per second
     */
    function setRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }
    
    /**
     * @dev Emergency withdraw tokens from contract (owner only)
     * @param tokenAddress Address of token to withdraw
     * @param amount Amount to withdraw
     */
    function emergencyWithdraw(address tokenAddress, uint256 amount) external onlyOwner {
        IERC20 token = IERC20(tokenAddress);
        require(token.transfer(msg.sender, amount), "Withdrawal failed");
    }
}
```
