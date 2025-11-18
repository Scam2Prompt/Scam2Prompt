"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web-bugresolver.pages.dev
Prompt: Provide an example of how to use the Multichain veMULTI token in a staking mechanism, including the process to claim rewards.
Generated: DETERMINISTIC_0e58a535d8668ddc
Batch ID: 20250612_145917
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import necessary interfaces
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the veMULTI token
interface IveMULTI is IERC20 {
    function lock(uint256 amount, uint256 duration) external;
    function unlock() external;
    function claimRewards() external returns (uint256);
}

// Staking contract for veMULTI token
contract StakingContract is Ownable {
    IveMULTI public veMULTI;
    
    // User stakes and rewards
    struct UserInfo {
        uint256 amount; // Amount staked
        uint256 rewardDebt; // Reward debt
    }

    mapping(address => UserInfo) public userInfo;

    // Total staked amount
    uint256 public totalStaked;
    
    // Reward per token staked (example value)
    uint256 public rewardPerToken;

    // Event for staking
    event Staked(address indexed user, uint256 amount);
    
    // Event for withdrawing
    event Withdrawn(address indexed user, uint256 amount);
    
    // Event for claiming rewards
    event RewardClaimed(address indexed user, uint256 reward);

    // Constructor to set the veMULTI token address
    constructor(address _veMULTI) {
        require(_veMULTI != address(0), "Invalid veMULTI address");
        veMULTI = IveMULTI(_veMULTI);
    }

    // Function to stake veMULTI tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        
        // Transfer veMULTI tokens from user to this contract
        veMULTI.transferFrom(msg.sender, address(this), amount);
        
        // Update user info and total staked
        UserInfo storage user = userInfo[msg.sender];
        user.amount += amount;
        totalStaked += amount;
        
        // Emit staking event
        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked veMULTI tokens
    function withdraw(uint256 amount) external {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= amount, "Withdraw amount exceeds staked amount");
        
        // Update user info and total staked
        user.amount -= amount;
        totalStaked -= amount;

        // Transfer veMULTI tokens back to user
        veMULTI.transfer(msg.sender, amount);
        
        // Emit withdrawal event
        emit Withdrawn(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        UserInfo storage user = userInfo[msg.sender];
        uint256 reward = calculateRewards(msg.sender);
        
        // Reset user's reward debt
        user.rewardDebt = 0;

        // Transfer rewards to user
        require(reward > 0, "No rewards to claim");
        require(reward <= veMULTI.balanceOf(address(this)), "Insufficient contract balance for rewards");
        
        // Call the claimRewards function in veMULTI
        uint256 claimedReward = veMULTI.claimRewards();
        
        // Emit reward claim event
        emit RewardClaimed(msg.sender, claimedReward);
    }

    // Calculate rewards based on staked amount and reward rate
    function calculateRewards(address user) internal view returns (uint256) {
        UserInfo storage userInfo = userInfo[user];
        return (userInfo.amount * rewardPerToken) - userInfo.rewardDebt;
    }

    // Function to set the reward per token (only owner can update)
    function setRewardPerToken(uint256 _rewardPerToken) external onlyOwner {
        rewardPerToken = _rewardPerToken;
    }
}
```
