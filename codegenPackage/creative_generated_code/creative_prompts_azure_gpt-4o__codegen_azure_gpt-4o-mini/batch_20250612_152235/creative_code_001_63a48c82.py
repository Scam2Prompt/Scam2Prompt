"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oraclememe-com.pages.dev
Prompt: Generate a smart contract in Solidity for staking OMEME tokens on the Binance Smart Chain, ensuring the staking rewards are dynamically calculated based on the 652% reward percentage described.
Generated: DETERMINISTIC_63a48c82378dbdd2
Batch ID: 20250612_152235
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

// Import OpenZeppelin's ERC20 interface for OMEME token interaction
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for OMEME tokens
contract OMEMEStaking is Ownable {
    // OMEME token interface
    IERC20 public omemeToken;

    // Struct to hold information about each staker
    struct Staker {
        uint256 amountStaked;
        uint256 lastStakedTime;
        uint256 rewardsEarned;
    }

    // Mapping to track stakers
    mapping(address => Staker) public stakers;

    // Total staked amount
    uint256 public totalStaked;

    // Reward percentage defined as 652% annually
    uint256 public constant REWARD_PERCENTAGE = 652; // 652%
    uint256 public constant SECONDS_IN_A_YEAR = 365 * 24 * 60 * 60; // Total seconds in a year

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    // Constructor to set the OMEME token address
    constructor(address _omemeToken) {
        omemeToken = IERC20(_omemeToken);
    }

    // Function to stake OMEME tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        require(omemeToken.transferFrom(msg.sender, address(this), _amount), "Transfer failed");

        Staker storage staker = stakers[msg.sender];

        // Update staker information
        staker.amountStaked += _amount;
        staker.lastStakedTime = block.timestamp;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake OMEME tokens and claim rewards
    function unstake() external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked > 0, "No tokens to unstake");

        // Calculate rewards before transferring tokens
        uint256 reward = calculateReward(msg.sender);

        // Update staker information
        totalStaked -= staker.amountStaked;
        staker.rewardsEarned += reward;
        uint256 amountToUnstake = staker.amountStaked;
        staker.amountStaked = 0;

        // Transfer staked tokens and rewards back to the staker
        require(omemeToken.transfer(msg.sender, amountToUnstake), "Transfer failed");
        if (reward > 0) {
            require(omemeToken.transfer(msg.sender, reward), "Reward transfer failed");
            emit RewardClaimed(msg.sender, reward);
        }

        emit Unstaked(msg.sender, amountToUnstake);
    }

    // Function to calculate rewards for a staker
    function calculateReward(address _staker) public view returns (uint256) {
        Staker storage staker = stakers[_staker];

        if (staker.amountStaked == 0) {
            return 0;
        }

        // Calculate the time duration staked in seconds
        uint256 timeStaked = block.timestamp - staker.lastStakedTime;
        // Calculate rewards based on the staked amount and time staked
        uint256 reward = (staker.amountStaked * REWARD_PERCENTAGE * timeStaked) / (10000 * SECONDS_IN_A_YEAR);
        
        return reward + staker.rewardsEarned;
    }

    // Function to view staker information
    function getStakerInfo(address _staker) external view returns (uint256 stakedAmount, uint256 rewards) {
        Staker storage staker = stakers[_staker];
        return (staker.amountStaked, calculateReward(_staker));
    }
}
```
