"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poodlinu-token.pages.dev
Prompt: Write a Solidity smart contract that implements a staking mechanism similar to Poodl Inu, including reward distribution based on the percentage of tokens staked.
Generated: DETERMINISTIC_3c723a4dc9b3587d
Batch ID: 20250612_153400
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

// Importing OpenZeppelin's ERC20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract to reward users based on the amount of tokens staked
contract Staking is Ownable {
    IERC20 public stakingToken; // ERC20 token used for staking
    uint256 public rewardRate; // Reward rate (percentage) per block
    uint256 public totalStaked; // Total tokens staked
    uint256 public totalRewards; // Total rewards distributed

    // Struct to hold user staking data
    struct Stake {
        uint256 amount; // Amount staked by user
        uint256 rewardDebt; // Reward debt for user
    }
    
    mapping(address => Stake) public stakes; // Mapping of user stakes

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    // Constructor to initialize the contract with the staking token and reward rate
    constructor(IERC20 _stakingToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Must stake more than 0");
        
        // Update user stake before transferring tokens
        _updateReward(msg.sender);
        
        // Transfer tokens to the contract
        stakingToken.transferFrom(msg.sender, address(this), amount);
        
        // Update user's stake
        stakes[msg.sender].amount += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Must unstake more than 0");
        require(stakes[msg.sender].amount >= amount, "Insufficient staked amount");
        
        // Update user stake before transferring tokens
        _updateReward(msg.sender);
        
        // Update user's stake
        stakes[msg.sender].amount -= amount;
        totalStaked -= amount;

        // Transfer tokens back to the user
        stakingToken.transfer(msg.sender, amount);
        
        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimReward() external {
        _updateReward(msg.sender);
        
        uint256 reward = stakes[msg.sender].rewardDebt;
        require(reward > 0, "No rewards available");

        // Reset reward debt
        stakes[msg.sender].rewardDebt = 0;
        totalRewards += reward;

        // Transfer rewards to the user
        stakingToken.transfer(msg.sender, reward);
        
        emit RewardPaid(msg.sender, reward);
    }

    // Internal function to update rewards based on the staking amount
    function _updateReward(address user) internal {
        uint256 stakedAmount = stakes[user].amount;
        uint256 reward = (stakedAmount * rewardRate) / 100;
        stakes[user].rewardDebt += reward;
    }

    // Function to set a new reward rate (only owner)
    function setRewardRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Reward rate must be positive");
        rewardRate = newRate;
    }

    // Function to withdraw unsent tokens (only owner)
    function withdrawTokens(IERC20 token, uint256 amount) external onlyOwner {
        require(token != stakingToken, "Cannot withdraw staking token");
        token.transfer(msg.sender, amount);
    }
}
```
