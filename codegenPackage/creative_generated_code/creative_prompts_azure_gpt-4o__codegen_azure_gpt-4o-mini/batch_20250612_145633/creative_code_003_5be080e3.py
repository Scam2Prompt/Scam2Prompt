"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://memes-index.pages.dev
Prompt: Write a smart contract in Solidity for staking $MEMEX tokens that includes reward distribution based on the "Meme Moonshot Index" performance.
Generated: DETERMINISTIC_5be080e32cf77eca
Batch ID: 20250612_145633
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

// Import ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MemeStaking is Ownable {
    // Token to be staked
    IERC20 public stakingToken;
    
    // Struct to hold user stake information
    struct StakeInfo {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Reward debt for the user
    }

    // Mapping of user addresses to their staking info
    mapping(address => StakeInfo) public stakes;

    // Total staked amount
    uint256 public totalStaked;

    // Reward per token staked, calculated based on Meme Moonshot Index performance
    uint256 public rewardPerToken;

    // Event for when a user stakes tokens
    event Staked(address indexed user, uint256 amount);
    
    // Event for when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);
    
    // Event for reward distribution
    event RewardDistributed(address indexed user, uint256 amount);

    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0 tokens");
        
        // Update the user reward before staking
        _updateReward(msg.sender);

        // Transfer tokens from user to contract
        stakingToken.transferFrom(msg.sender, address(this), amount);
        
        // Update user stake information
        stakes[msg.sender].amount += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Cannot unstake 0 tokens");
        require(stakes[msg.sender].amount >= amount, "Insufficient staked amount");

        // Update the user reward before unstaking
        _updateReward(msg.sender);

        // Transfer tokens back to the user
        stakes[msg.sender].amount -= amount;
        totalStaked -= amount;
        stakingToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Internal function to update user rewards
    function _updateReward(address user) internal {
        uint256 accumulatedReward = stakes[user].amount * rewardPerToken;
        uint256 pendingReward = accumulatedReward - stakes[user].rewardDebt;

        if (pendingReward > 0) {
            // Transfer pending rewards to the user
            // Assuming rewards are already available in the contract
            payable(user).transfer(pendingReward);
            emit RewardDistributed(user, pendingReward);
        }

        // Update the reward debt for the user
        stakes[user].rewardDebt = accumulatedReward;
    }

    // Function to distribute rewards based on Meme Moonshot Index performance
    function distributeRewards(uint256 rewardAmount) external onlyOwner {
        require(totalStaked > 0, "No staked tokens");

        // Update reward per token based on the new reward amount
        rewardPerToken += rewardAmount / totalStaked;
    }

    // Function to view user's staked amount
    function stakedAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }

    // Fallback function to receive ETH rewards
    receive() external payable {}
}
```
