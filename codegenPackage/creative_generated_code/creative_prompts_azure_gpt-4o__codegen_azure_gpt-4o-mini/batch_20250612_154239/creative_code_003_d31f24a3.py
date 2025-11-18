"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim.agentlydve-ai.world
Prompt: Create a smart contract that interacts with Agently's tokenomics system to manage rewards for active users and groups.
Generated: DETERMINISTIC_d31f24a33d7d5714
Batch ID: 20250612_154239
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

// Importing OpenZeppelin's ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for managing user and group rewards in Agently's tokenomics
contract AgentlyRewards is Ownable {
    // State variables
    IERC20 public agentlyToken; // The token used for rewards
    mapping(address => uint256) public userRewards; // Rewards balance for each user
    mapping(bytes32 => uint256) public groupRewards; // Rewards balance for each group
    mapping(address => bytes32) public userGroup; // Maps users to their groups

    // Events for logging transactions
    event RewardsDistributed(address indexed user, uint256 amount);
    event GroupRewardsDistributed(bytes32 indexed groupId, uint256 amount);

    // Constructor to initialize the contract with the token address
    constructor(IERC20 _agentlyToken) {
        agentlyToken = _agentlyToken;
    }

    // Function to set user group
    function setUserGroup(bytes32 groupId) external {
        userGroup[msg.sender] = groupId;
    }

    // Function to distribute rewards to a user
    function distributeRewards(address user, uint256 amount) external onlyOwner {
        require(user != address(0), "Invalid user address");
        require(amount > 0, "Reward amount must be greater than 0");
        require(agentlyToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Update user rewards balance
        userRewards[user] += amount;

        // Emit an event for the reward distribution
        emit RewardsDistributed(user, amount);
    }

    // Function to distribute group rewards
    function distributeGroupRewards(bytes32 groupId, uint256 amount) external onlyOwner {
        require(amount > 0, "Reward amount must be greater than 0");
        require(agentlyToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Update group rewards balance
        groupRewards[groupId] += amount;

        // Emit an event for the group reward distribution
        emit GroupRewardsDistributed(groupId, amount);
    }

    // Function to claim rewards for a user
    function claimRewards() external {
        uint256 rewardAmount = userRewards[msg.sender];
        require(rewardAmount > 0, "No rewards to claim");

        // Reset user rewards balance before transferring tokens
        userRewards[msg.sender] = 0;

        // Transfer tokens to the user
        require(agentlyToken.transfer(msg.sender, rewardAmount), "Token transfer failed");
    }

    // Function to claim group rewards for all members
    function claimGroupRewards() external {
        bytes32 groupId = userGroup[msg.sender];
        uint256 rewardAmount = groupRewards[groupId];
        require(rewardAmount > 0, "No group rewards to claim");

        // Reset group rewards balance before transferring tokens
        groupRewards[groupId] = 0;

        // Transfer tokens to the group (simplified to sender for this example)
        require(agentlyToken.transfer(msg.sender, rewardAmount), "Token transfer failed");
    }

    // Function to withdraw tokens from the contract (for owner)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(agentlyToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        require(agentlyToken.transfer(msg.sender, amount), "Token transfer failed");
    }

    // Function to check contract's token balance
    function contractTokenBalance() external view returns (uint256) {
        return agentlyToken.balanceOf(address(this));
    }
}
```
