"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gigachadgpt-io.web.app
Prompt: Generate Solidity code for a staking contract compatible with the $GIGA token, ensuring LP tokens are locked and rewards are distributed based on staked amounts.
Generated: DETERMINISTIC_9ba7ef4362d5f6aa
Batch ID: 20250612_152422
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

// Import the necessary interfaces
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract GigaStaking is ReentrancyGuard, Ownable {
    // The ERC20 token to be staked
    IERC20 public gigaToken;
    
    // Struct to hold user staking information
    struct UserInfo {
        uint256 amount;     // Amount of LP tokens staked
        uint256 rewardDebt; // Reward debt
    }

    // Mapping of user addresses to their staking information
    mapping(address => UserInfo) public userInfo;
    
    // Total staked amount
    uint256 public totalStaked;

    // Reward token per block (could also be a parameter on the constructor)
    uint256 public rewardPerBlock = 1 * 1e18; // Example: 1 GIGA per block
    uint256 public lastRewardBlock; // Last block that rewards were distributed
    
    // Event for stake action
    event Staked(address indexed user, uint256 amount);
    
    // Event for unstake action
    event Unstaked(address indexed user, uint256 amount);
    
    // Event for reward distribution
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the GIGA token address
    constructor(IERC20 _gigaToken) {
        gigaToken = _gigaToken;
        lastRewardBlock = block.number;
    }

    // Function to stake LP tokens
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Cannot stake 0");

        UserInfo storage user = userInfo[msg.sender];
        updatePool();

        // Transfer LP tokens from user to this contract
        gigaToken.transferFrom(msg.sender, address(this), _amount);

        // Update user info
        user.amount += _amount;
        user.rewardDebt = user.amount * rewardPerBlock / totalStaked;

        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake LP tokens
    function unstake(uint256 _amount) external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= _amount, "Insufficient balance to unstake");

        updatePool();

        // Update user info
        user.amount -= _amount;
        user.rewardDebt = user.amount * rewardPerBlock / totalStaked;

        // Transfer LP tokens back to the user
        gigaToken.transfer(msg.sender, _amount);

        totalStaked -= _amount;

        emit Unstaked(msg.sender, _amount);
    }

    // Function to claim rewards
    function claimRewards() external nonReentrant {
        UserInfo storage user = userInfo[msg.sender];
        updatePool();

        uint256 pendingReward = user.amount * rewardPerBlock / totalStaked - user.rewardDebt;

        require(pendingReward > 0, "No rewards to claim");

        // Transfer the rewards to the user
        gigaToken.transfer(msg.sender, pendingReward);

        // Update user reward debt
        user.rewardDebt = user.amount * rewardPerBlock / totalStaked;

        emit RewardsClaimed(msg.sender, pendingReward);
    }

    // Internal function to update the pool based on the current block
    function updatePool() internal {
        if (totalStaked == 0) {
            lastRewardBlock = block.number;
            return;
        }

        // Here you can add logic to calculate rewards based on the blocks passed
        // For the sake of simplicity, we are not implementing it in this example
        lastRewardBlock = block.number;
    }

    // Function to set reward rate (only owner)
    function setRewardPerBlock(uint256 _rewardPerBlock) external onlyOwner {
        rewardPerBlock = _rewardPerBlock;
    }
}
```
