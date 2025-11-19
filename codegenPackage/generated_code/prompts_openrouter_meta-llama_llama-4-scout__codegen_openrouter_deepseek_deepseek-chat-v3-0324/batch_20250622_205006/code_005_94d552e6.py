"""
Generated Code Metadata:
========================
Original URL: https://apps-ethena.pages.dev
Prompt: "Design a smart contract to automate rewards distribution for Ethena's Season 3 campaign, considering the 77.83B rewards issued and 11.63T Sats issued."
Generated: DETERMINISTIC_94d552e6021b1468
Batch ID: 20250622_205006
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title EthenaSeason3Rewards
 * @dev Smart contract for automating rewards distribution for Ethena's Season 3 campaign
 */
contract EthenaSeason3Rewards is Ownable, ReentrancyGuard {
    // Reward token interface
    IERC20 public rewardToken;
    
    // Total rewards to be distributed (77.83B in token units)
    uint256 public constant TOTAL_REWARDS = 77_830_000_000 * (10 ** 18);
    
    // Total Sats issued (11.63T)
    uint256 public constant TOTAL_SATS = 11_630_000_000_000;
    
    // Track distributed rewards
    uint256 public distributedRewards;
    
    // Mapping to track claimed rewards per address
    mapping(address => uint256) public claimedRewards;
    
    // Mapping to store Sats balance per address
    mapping(address => uint256) public satsBalances;
    
    // Event for reward distribution
    event RewardsDistributed(address indexed recipient, uint256 amount);
    event RewardsDeposited(uint256 amount);
    
    /**
     * @dev Constructor
     * @param _rewardToken Address of the reward token contract
     */
    constructor(address _rewardToken) {
        require(_rewardToken != address(0), "Invalid token address");
        rewardToken = IERC20(_rewardToken);
    }
    
    /**
     * @dev Deposit rewards into the contract
     * @param amount Amount of reward tokens to deposit
     */
    function depositRewards(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(rewardToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        emit RewardsDeposited(amount);
    }
    
    /**
     * @dev Set Sats balances for multiple users
     * @param addresses Array of user addresses
     * @param balances Array of corresponding Sats balances
     */
    function setSatsBalances(address[] calldata addresses, uint256[] calldata balances) external onlyOwner {
        require(addresses.length == balances.length, "Arrays length mismatch");
        
        for (uint256 i = 0; i < addresses.length; i++) {
            require(addresses[i] != address(0), "Invalid address");
            satsBalances[addresses[i]] = balances[i];
        }
    }
    
    /**
     * @dev Calculate reward amount based on Sats balance
     * @param user Address of the user
     * @return Calculated reward amount
     */
    function calculateReward(address user) public view returns (uint256) {
        uint256 userSats = satsBalances[user];
        if (userSats == 0) return 0;
        
        return (userSats * TOTAL_REWARDS) / TOTAL_SATS;
    }
    
    /**
     * @dev Claim rewards
     */
    function claimRewards() external nonReentrant {
        require(satsBalances[msg.sender] > 0, "No Sats balance");
        require(claimedRewards[msg.sender] == 0, "Already claimed");
        
        uint256 rewardAmount = calculateReward(msg.sender);
        require(rewardAmount > 0, "No rewards available");
        require(distributedRewards + rewardAmount <= TOTAL_REWARDS, "Insufficient rewards");
        
        claimedRewards[msg.sender] = rewardAmount;
        distributedRewards += rewardAmount;
        
        require(rewardToken.transfer(msg.sender, rewardAmount), "Transfer failed");
        emit RewardsDistributed(msg.sender, rewardAmount);
    }
    
    /**
     * @dev Withdraw remaining rewards (owner only)
     */
    function withdrawRemainingRewards() external onlyOwner {
        uint256 remaining = rewardToken.balanceOf(address(this)) - (TOTAL_REWARDS - distributedRewards);
        require(remaining > 0, "No remaining rewards");
        require(rewardToken.transfer(owner(), remaining), "Transfer failed");
    }
    
    /**
     * @dev Emergency withdraw all rewards (owner only)
     */
    function emergencyWithdraw() external onlyOwner {
        uint256 balance = rewardToken.balanceOf(address(this));
        require(balance > 0, "No balance to withdraw");
        require(rewardToken.transfer(owner(), balance), "Transfer failed");
    }
}
```
