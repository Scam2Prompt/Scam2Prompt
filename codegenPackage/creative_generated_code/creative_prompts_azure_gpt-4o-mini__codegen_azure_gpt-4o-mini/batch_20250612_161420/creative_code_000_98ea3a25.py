"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://greenbitcoin-en.pages.dev
Prompt: How can I implement a staking mechanism for the Green Bitcoin ($GBTC) token that allows users to earn exponential rewards through gamified challenges?
Generated: DETERMINISTIC_98ea3a25339ba10c
Batch ID: 20250612_161420
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// The Staking contract for Green Bitcoin ($GBTC) token
contract GreenBitcoinStaking is Ownable {
    // Token to be staked
    IERC20 public gbtcToken;

    // Structure to hold user staking information
    struct Stake {
        uint256 amount;        // Amount of tokens staked
        uint256 rewardDebt;    // Reward debt for the user
        uint256 lastStakedAt;  // Last time the user staked
    }

    // Mapping of user addresses to their stake information
    mapping(address => Stake) public stakes;

    // Total amount of tokens staked
    uint256 public totalStaked;

    // Events for tracking staking and rewards
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the GBTC token
    constructor(IERC20 _gbtcToken) {
        gbtcToken = _gbtcToken;
    }

    // Modifier to check if the user has staked tokens
    modifier hasStaked() {
        require(stakes[msg.sender].amount > 0, "No tokens staked");
        _;
    }

    // Function for users to stake GBTC tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Must stake more than 0 tokens");
        // Transfer GBTC tokens from the user to the contract
        gbtcToken.transferFrom(msg.sender, address(this), _amount);
        
        Stake storage userStake = stakes[msg.sender];
        
        // Update the user's stake information
        userStake.amount += _amount;
        userStake.lastStakedAt = block.timestamp;
        
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    // Function for users to unstake their tokens
    function unstake(uint256 _amount) external hasStaked {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= _amount, "Insufficient staked amount");

        // Calculate and claim rewards before unstaking
        claimRewards();

        // Update the user's stake information
        userStake.amount -= _amount;
        totalStaked -= _amount;

        // Transfer GBTC tokens back to the user
        gbtcToken.transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    // Function to calculate and claim rewards based on staked amount and time
    function claimRewards() public hasStaked {
        Stake storage userStake = stakes[msg.sender];

        // Calculate the rewards (for simplicity, rewards are 10% of staked amount per day)
        uint256 reward = (userStake.amount * ((block.timestamp - userStake.lastStakedAt) / 1 days)) / 10;

        // Update reward debt
        userStake.rewardDebt += reward;
        userStake.lastStakedAt = block.timestamp;

        // Transfer rewards to the user (ensure contract has enough tokens)
        require(gbtcToken.balanceOf(address(this)) >= reward, "Insufficient reward balance");
        gbtcToken.transfer(msg.sender, reward);
        
        emit RewardClaimed(msg.sender, reward);
    }
    
    // Function to get the total rewards of a user
    function getTotalRewards(address user) external view returns (uint256) {
        Stake storage userStake = stakes[user];
        return userStake.rewardDebt + (userStake.amount * ((block.timestamp - userStake.lastStakedAt) / 1 days)) / 10;
    }

    // Function to get the staked amount of a user
    function stakedAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }
}
```
