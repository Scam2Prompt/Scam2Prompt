"""
Generated Code Metadata:
========================
Original URL: https://virtualstake.app
Prompt: Design a smart contract for a decentralized application (dApp) that utilizes the Virtuals Protocol's staking mechanism.
Generated: DETERMINISTIC_b010ca5176ab5223
Batch ID: 20250622_212723
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing the necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for staking using the Virtuals Protocol
contract VirtualsStaking is Ownable {
    // State variables
    IERC20 public stakingToken; // The token that will be staked
    uint256 public totalStaked; // Total amount of tokens staked
    uint256 public rewardRate; // Reward rate per block
    uint256 public lastUpdateBlock; // Last block when rewards were updated

    // Struct to hold user staking information
    struct Staker {
        uint256 amount; // Amount staked by the user
        uint256 rewardDebt; // Reward debt for the user
    }

    // Mapping of user addresses to their staking information
    mapping(address => Staker) public stakers;

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    // Constructor to initialize the contract
    constructor(IERC20 _stakingToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
        lastUpdateBlock = block.number;
    }

    // Modifier to update rewards before any staking action
    modifier updateRewards() {
        if (totalStaked > 0) {
            uint256 blocksPassed = block.number - lastUpdateBlock;
            uint256 reward = blocksPassed * rewardRate;
            totalStaked += reward; // Update total staked with new rewards
        }
        lastUpdateBlock = block.number; // Update the last block
        _;
    }

    // Function to stake tokens
    function stake(uint256 amount) external updateRewards {
        require(amount > 0, "Amount must be greater than 0");
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update staker's information
        Staker storage staker = stakers[msg.sender];
        staker.amount += amount;
        staker.rewardDebt = staker.amount * rewardRate;

        totalStaked += amount; // Update total staked
        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external updateRewards {
        Staker storage staker = stakers[msg.sender];
        require(staker.amount >= amount, "Insufficient staked amount");

        // Update staker's information
        staker.amount -= amount;
        totalStaked -= amount; // Update total staked

        require(stakingToken.transfer(msg.sender, amount), "Transfer failed");
        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external updateRewards {
        Staker storage staker = stakers[msg.sender];
        uint256 reward = (staker.amount * rewardRate) - staker.rewardDebt;

        require(reward > 0, "No rewards to claim");
        staker.rewardDebt = staker.amount * rewardRate; // Update reward debt

        // Transfer rewards to the user
        require(stakingToken.transfer(msg.sender, reward), "Transfer failed");
        emit RewardClaimed(msg.sender, reward);
    }

    // Function to set a new reward rate (only owner)
    function setRewardRate(uint256 newRewardRate) external onlyOwner {
        rewardRate = newRewardRate;
    }

    // Function to withdraw tokens in case of emergency (only owner)
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(stakingToken.transfer(msg.sender, amount), "Transfer failed");
    }
}
```
