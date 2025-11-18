"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://portal-neurolance.web.app
Prompt: Develop a smart contract that integrates with the Neurolance Portal's staking dApp to enable staking of NEROX tokens and calculate rewards.
Generated: DETERMINISTIC_88a847e37d53b421
Batch ID: 20250612_150446
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

// Importing necessary OpenZeppelin contracts for safe math and ERC20 token interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Smart contract for the NEROX staking system
contract NEROXStaking {
    using SafeMath for uint256;

    // Variables
    IERC20 public neroxToken; // ERC20 token to stake
    uint256 public rewardRate; // Reward rate for staking
    uint256 public totalStaked; // Total amount of NEROX tokens staked
    mapping(address => uint256) public stakedAmount; // Mapping of staked amounts per user
    mapping(address => uint256) public lastUpdated; // Last update timestamp for rewards calculation

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    // Constructor to initialize the contract with the NEROX token and the reward rate
    constructor(IERC20 _neroxToken, uint256 _rewardRate) {
        neroxToken = _neroxToken;
        rewardRate = _rewardRate;
    }

    // Modifier to check if the user has staked tokens
    modifier hasStaked() {
        require(stakedAmount[msg.sender] > 0, "You have not staked any tokens.");
        _;
    }

    // Function to stake NEROX tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0 tokens.");
        require(neroxToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed.");

        // Update total staked amount and user's staked amount
        totalStaked = totalStaked.add(amount);
        stakedAmount[msg.sender] = stakedAmount[msg.sender].add(amount);
        lastUpdated[msg.sender] = block.timestamp; // Update last timestamp

        emit Staked(msg.sender, amount);
    }

    // Function to unstake NEROX tokens and claim rewards
    function unstake(uint256 amount) external hasStaked {
        require(amount > 0 && amount <= stakedAmount[msg.sender], "Invalid unstake amount.");

        // Calculate rewards before unstaking
        uint256 reward = calculateReward(msg.sender);
        
        // Update total staked and user's staked amount
        totalStaked = totalStaked.sub(amount);
        stakedAmount[msg.sender] = stakedAmount[msg.sender].sub(amount);
        
        // Transfer NEROX tokens back to the user
        require(neroxToken.transfer(msg.sender, amount), "Token transfer failed.");

        // Transfer rewards to the user
        if (reward > 0) {
            require(neroxToken.transfer(msg.sender, reward), "Reward transfer failed.");
        }

        emit Unstaked(msg.sender, amount);
        emit RewardClaimed(msg.sender, reward);
    }

    // Function to calculate the rewards for a user
    function calculateReward(address user) public view returns (uint256) {
        uint256 staked = stakedAmount[user];
        uint256 duration = block.timestamp.sub(lastUpdated[user]);
        return staked.mul(rewardRate).mul(duration).div(1 days); // Reward calculation
    }

    // Function to get the staked amount of a user
    function getStakedAmount(address user) external view returns (uint256) {
        return stakedAmount[user];
    }

    // Function to get the total staked amount
    function getTotalStaked() external view returns (uint256) {
        return totalStaked;
    }
}
```
