"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pixelverse-combo.ru
Prompt: Generate a Solidity contract for staking PIXFI tokens in PixelVerse, providing daily rewards and ensuring security against fraud.
Generated: DETERMINISTIC_687f8bbe709cad66
Batch ID: 20250612_154842
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

// Importing OpenZeppelin's ERC20 interface for PIXFI token interaction
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract PixelVerseStaking is ReentrancyGuard, Ownable {
    // PIXFI token interface
    IERC20 public pixfiToken;

    // Struct to represent each staker's information
    struct Staker {
        uint256 amountStaked;
        uint256 lastRewardTime;
        uint256 rewardDebt;
    }

    // Mapping to track stakers
    mapping(address => Staker) public stakers;

    // Total staked tokens
    uint256 public totalStaked;

    // Reward rate per second (in wei)
    uint256 public rewardRate = 1e18; // 1 PIXFI token per second

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);
    
    // Event emitted when tokens are withdrawn
    event Withdrawn(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 reward);

    // Constructor to initialize the PIXFI token address
    constructor(address _pixfiToken) {
        require(_pixfiToken != address(0), "Invalid PIXFI token address");
        pixfiToken = IERC20(_pixfiToken);
    }

    // Function to stake PIXFI tokens
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        
        // Update staker's info before transfer
        _updateRewards(msg.sender);
        
        // Transfer tokens from the staker to this contract
        pixfiToken.transferFrom(msg.sender, address(this), amount);
        
        // Update staker's state
        stakers[msg.sender].amountStaked += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked tokens
    function withdraw(uint256 amount) external nonReentrant {
        require(stakers[msg.sender].amountStaked >= amount, "Insufficient staked amount");
        
        // Update rewards before withdrawal
        _updateRewards(msg.sender);
        
        // Update staker's state
        stakers[msg.sender].amountStaked -= amount;
        totalStaked -= amount;

        // Transfer tokens back to the staker
        pixfiToken.transfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external nonReentrant {
        _updateRewards(msg.sender);
        
        uint256 reward = stakers[msg.sender].rewardDebt;
        require(reward > 0, "No rewards to claim");
        
        // Reset reward debt
        stakers[msg.sender].rewardDebt = 0;

        // Transfer rewards to the staker
        pixfiToken.transfer(msg.sender, reward);

        emit RewardClaimed(msg.sender, reward);
    }

    // Internal function to update rewards for a staker
    function _updateRewards(address staker) internal {
        Staker storage s = stakers[staker];
        
        // Calculate time elapsed since the last reward time
        uint256 timeElapsed = block.timestamp - s.lastRewardTime;
        
        // Calculate the new reward based on time elapsed and the reward rate
        uint256 pendingReward = (s.amountStaked * timeElapsed * rewardRate) / 1e18;
        
        // Update staker's reward debt
        s.rewardDebt += pendingReward;

        // Update the last reward timestamp
        s.lastRewardTime = block.timestamp;
    }

    // Function to set the reward rate (only owner)
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
    }

    // Function to withdraw any excess tokens in the contract (only owner)
    function withdrawExcessTokens(uint256 amount) external onlyOwner {
        require(amount <= pixfiToken.balanceOf(address(this)) - totalStaked, "Cannot withdraw staked tokens");
        pixfiToken.transfer(msg.sender, amount);
    }
}
```
