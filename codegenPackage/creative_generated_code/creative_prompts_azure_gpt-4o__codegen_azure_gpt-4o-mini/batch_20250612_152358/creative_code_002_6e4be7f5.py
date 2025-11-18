"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cattizen.pages.dev
Prompt: Generate code for a staking mechanism that enables $CATI holders to earn yield without impermanent loss, as described in Catizen's Launch Pool feature.
Generated: DETERMINISTIC_6e4be7f5f42f7637
Batch ID: 20250612_152358
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

// Importing OpenZeppelin contracts for ERC20 and Ownable functionality
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the staking rewards
interface IRewards {
    function distributeRewards(address staker, uint256 amount) external;
}

// Contract for Catizen's Staking Mechanism
contract CatizenStaking is Ownable {
    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // State variables
    IERC20 public catiToken; // ERC20 token for staking
    IRewards public rewardsContract; // Contract for distributing rewards

    mapping(address => uint256) private stakes; // Tracks staked amounts
    mapping(address => uint256) private rewards; // Tracks rewards owed to users

    // Constructor to set token and rewards contract address
    constructor(IERC20 _catiToken, IRewards _rewardsContract) {
        catiToken = _catiToken;
        rewardsContract = _rewardsContract;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(catiToken.balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Transfer tokens from user to the contract
        catiToken.transferFrom(msg.sender, address(this), amount);

        // Update the stakes mapping
        stakes[msg.sender] += amount;

        // Emit the Staked event
        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakes[msg.sender] >= amount, "Insufficient staked amount");

        // Update the stakes mapping
        stakes[msg.sender] -= amount;

        // Transfer tokens back to the user
        catiToken.transfer(msg.sender, amount);

        // Emit the Unstaked event
        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 rewardAmount = rewards[msg.sender];
        require(rewardAmount > 0, "No rewards to claim");

        // Reset the user's rewards to zero
        rewards[msg.sender] = 0;

        // Distribute rewards
        rewardsContract.distributeRewards(msg.sender, rewardAmount);

        // Emit the RewardsClaimed event
        emit RewardsClaimed(msg.sender, rewardAmount);
    }

    // Function to calculate and distribute rewards (can be called by external contract)
    function distributeRewards(address user, uint256 amount) external onlyOwner {
        require(stakes[user] > 0, "User has no stakes");
        rewards[user] += amount;
    }

    // Get staked amount for a user
    function getStakedAmount(address user) external view returns (uint256) {
        return stakes[user];
    }

    // Get rewards amount for a user
    function getRewardsAmount(address user) external view returns (uint256) {
        return rewards[user];
    }
}
```
