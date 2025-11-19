"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appscottyclaims.pages.dev
Prompt: Create a Solidity smart contract that allows users to stake $SCOTTY tokens and automatically distribute rewards at a rate of 82.5 $SCOTTY per ETH block.
Generated: DETERMINISTIC_fe99b6e59bc61549
Batch ID: 20250612_161035
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

// Importing the ERC20 interface for interacting with the $SCOTTY token contract
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for $SCOTTY token
contract ScottyStaking is Ownable {
    // The $SCOTTY token interface
    IERC20 public scottyToken;

    // Reward rate defined as 82.5 $SCOTTY tokens per ETH block
    uint256 public constant REWARD_RATE = 82.5 * 1e18; // Adjusting for decimal precision
    uint256 public lastRewardBlock;

    // Structure to hold user staking information
    struct Staker {
        uint256 amountStaked; // Amount of tokens staked
        uint256 rewards;      // Accumulated rewards
        uint256 lastClaimedBlock; // Last block where rewards were claimed
    }

    // Mapping of user addresses to their staking information
    mapping(address => Staker) public stakers;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);
    
    // Event emitted when a user claims rewards
    event RewardsClaimed(address indexed user, uint256 reward);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Constructor for initializing the contract with the $SCOTTY token address
    constructor(address _scottyToken) {
        scottyToken = IERC20(_scottyToken);
        lastRewardBlock = block.number;
    }

    // Function to stake $SCOTTY tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Must stake a positive amount");

        // Update rewards before staking
        _updateRewards(msg.sender);

        // Transfer $SCOTTY tokens from the user to the contract
        scottyToken.transferFrom(msg.sender, address(this), amount);

        // Update the staker's information
        stakers[msg.sender].amountStaked += amount;
        
        emit Staked(msg.sender, amount);
    }

    // Function to unstake $SCOTTY tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Must unstake a positive amount");
        require(stakers[msg.sender].amountStaked >= amount, "Insufficient staked balance");

        // Update rewards before unstaking
        _updateRewards(msg.sender);

        // Update staker's staked amount
        stakers[msg.sender].amountStaked -= amount;

        // Transfer $SCOTTY tokens back to the user
        scottyToken.transfer(msg.sender, amount);
        
        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        // Update rewards before claiming
        _updateRewards(msg.sender);
        
        uint256 reward = stakers[msg.sender].rewards;
        require(reward > 0, "No rewards to claim");

        // Reset rewards to zero for the user
        stakers[msg.sender].rewards = 0;

        // Transfer rewards to the user
        scottyToken.transfer(msg.sender, reward);
        
        emit RewardsClaimed(msg.sender, reward);
    }

    // Internal function to update rewards for a user
    function _updateRewards(address user) internal {
        uint256 blocksPassed = block.number - lastRewardBlock;
        if (blocksPassed > 0) {
            uint256 reward = blocksPassed * REWARD_RATE * stakers[user].amountStaked / 1e18;
            stakers[user].rewards += reward;
            lastRewardBlock = block.number;
        }
    }

    // Function to check the staker's information
    function getStakerInfo(address user) external view returns (uint256 amountStaked, uint256 rewards) {
        amountStaked = stakers[user].amountStaked;
        rewards = stakers[user].rewards;
    }
}
```
