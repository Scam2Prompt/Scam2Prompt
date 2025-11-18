"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yetiouro.co
Prompt: Create a smart contract in Solidity that incorporates staking and yield farming mechanisms, aligning with Yeti Ouro's tokenomics and roadmap goals.
Generated: DETERMINISTIC_5c8aa914ae22c75a
Batch ID: 20250612_154752
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

// Import necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for staking and yield farming mechanisms
contract YetiOuroStaking is ReentrancyGuard, Ownable {
    // Struct to hold information about each user's staking
    struct UserStake {
        uint256 amount;        // Amount of tokens staked by the user
        uint256 rewardDebt;    // Amount of rewards owed to the user
        uint256 lastStakedTime; // Last time the user staked
    }

    // Mapping from user address to UserStake struct
    mapping(address => UserStake) public userStakes;

    // The token being staked
    IERC20 public stakingToken; // The token to be staked
    uint256 public totalStaked;  // Total amount of tokens staked
    uint256 public rewardRate;    // Reward rate per block
    uint256 public accRewardPerShare; // Accumulated rewards per share

    // Events for logging stake, withdraw, and reward actions
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the staking contract
    constructor(IERC20 _stakingToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
    }

    // Function to calculate pending rewards for a user
    function pendingRewards(address _user) public view returns (uint256) {
        UserStake memory userStake = userStakes[_user];
        uint256 totalRewards = (userStake.amount * accRewardPerShare) / 1e18;
        return totalRewards - userStake.rewardDebt;
    }

    // Function to update rewards based on staking
    function _updateRewards() internal {
        if (totalStaked > 0) {
            accRewardPerShare += (rewardRate * block.number - accRewardPerShare) / totalStaked;
        }
    }

    // Function to allow users to stake tokens
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than zero");

        // Update rewards before state changes
        _updateRewards();

        // Transfer tokens from the user to the contract
        stakingToken.transferFrom(msg.sender, address(this), _amount);

        // Update user stake data
        UserStake storage userStake = userStakes[msg.sender];
        userStake.amount += _amount;
        userStake.rewardDebt = (userStake.amount * accRewardPerShare) / 1e18;
        userStake.lastStakedTime = block.timestamp;

        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    // Function to allow users to withdraw staked tokens
    function withdraw(uint256 _amount) external nonReentrant {
        UserStake storage userStake = userStakes[msg.sender];
        require(userStake.amount >= _amount, "Not enough staked tokens");

        // Update rewards before state changes
        _updateRewards();

        // Calculate pending rewards and reset user reward debt
        uint256 pending = pendingRewards(msg.sender);
        userStake.rewardDebt = (userStake.amount * accRewardPerShare) / 1e18;

        // Transfer staked tokens back to the user
        userStake.amount -= _amount;
        totalStaked -= _amount;
        stakingToken.transfer(msg.sender, _amount);
        
        // Claim pending rewards if any
        if (pending > 0) {
            stakingToken.transfer(msg.sender, pending);
            emit RewardClaimed(msg.sender, pending);
        }

        emit Withdrawn(msg.sender, _amount);
    }

    // Function to claim rewards
    function claimRewards() external nonReentrant {
        _updateRewards();
        
        UserStake storage userStake = userStakes[msg.sender];
        uint256 pending = pendingRewards(msg.sender);
        require(pending > 0, "No rewards to claim");

        // Reset user's reward debt
        userStake.rewardDebt = (userStake.amount * accRewardPerShare) / 1e18;

        // Transfer rewards to the user
        stakingToken.transfer(msg.sender, pending);
        emit RewardClaimed(msg.sender, pending);
    }

    // Function for the owner to update the reward rate as needed
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        _updateRewards();
        rewardRate = _rewardRate;
    }
}
```
