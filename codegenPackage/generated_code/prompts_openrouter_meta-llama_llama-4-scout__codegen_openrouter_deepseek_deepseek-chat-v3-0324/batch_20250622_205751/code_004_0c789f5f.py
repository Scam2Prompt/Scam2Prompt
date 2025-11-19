"""
Generated Code Metadata:
========================
Original URL: https://bafybeihdjl7xixuxxuxsexbtlzb37crgafyrxd5652yvkz4aokv7np4uty.ipfs.dweb.link
Prompt: Design a basic smart contract for a decentralized application (dapp) that interacts with the Morpheus network and rewards users with MOR tokens.
Generated: DETERMINISTIC_0c789f5fcac89fe3
Batch ID: 20250622_205751
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

contract MorpheusRewards is Ownable, ReentrancyGuard {
    IERC20 public morToken;
    
    // Mapping to track user rewards
    mapping(address => uint256) public rewards;
    
    // Events
    event RewardDeposited(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    
    /**
     * @dev Constructor that sets the MOR token address
     * @param _morTokenAddress Address of the MOR token contract
     */
    constructor(address _morTokenAddress) {
        require(_morTokenAddress != address(0), "Invalid token address");
        morToken = IERC20(_morTokenAddress);
    }
    
    /**
     * @dev Deposit MOR tokens to the contract for rewards distribution
     * @param amount Amount of MOR tokens to deposit
     */
    function depositRewards(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(morToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");
    }
    
    /**
     * @dev Add rewards to a user's balance
     * @param user Address of the user to reward
     * @param amount Amount of MOR tokens to reward
     */
    function addReward(address user, uint256 amount) external onlyOwner nonReentrant {
        require(user != address(0), "Invalid user address");
        require(amount > 0, "Amount must be greater than 0");
        
        rewards[user] += amount;
        emit RewardDeposited(user, amount);
    }
    
    /**
     * @dev Claim accumulated rewards
     */
    function claimRewards() external nonReentrant {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");
        
        rewards[msg.sender] = 0;
        require(morToken.transfer(msg.sender, reward), "Transfer failed");
        
        emit RewardClaimed(msg.sender, reward);
    }
    
    /**
     * @dev Get the reward balance of a user
     * @param user Address of the user to check
     * @return uint256 Reward balance
     */
    function getRewardBalance(address user) external view returns (uint256) {
        return rewards[user];
    }
    
    /**
     * @dev Withdraw any remaining MOR tokens from the contract (owner only)
     * @param amount Amount to withdraw
     */
    function withdrawRemainingTokens(uint256 amount) external onlyOwner nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(morToken.transfer(msg.sender, amount), "Transfer failed");
    }
}
```
