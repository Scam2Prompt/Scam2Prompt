"""
Generated Code Metadata:
========================
Original URL: https://sosphon.xyz
Prompt: Generate a smart contract code to automate the reward system for $SOPH stakers, ensuring sustainable yields and decentralization of the Sophon network.
Generated: DETERMINISTIC_38a60b9159568c38
Batch ID: 20250622_212813
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

// Importing OpenZeppelin's ERC20 and Ownable contracts for standard token functionality and ownership management
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for the $SOPH staking reward system
contract SophonStaking is Ownable {
    // State variables
    IERC20 public sophtoken; // The $SOPH token contract
    uint256 public rewardRate; // Reward rate per block
    uint256 public totalStaked; // Total amount of $SOPH staked
    uint256 public totalRewards; // Total rewards distributed

    // Struct to hold information about each staker
    struct Staker {
        uint256 amount; // Amount of $SOPH staked
        uint256 rewardDebt; // Reward debt for the staker
        uint256 lastUpdated; // Last block number when rewards were updated
    }

    // Mapping of staker addresses to their staking information
    mapping(address => Staker) public stakers;

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the $SOPH token address and reward rate
    constructor(IERC20 _sophtoken, uint256 _rewardRate) {
        sophtoken = _sophtoken;
        rewardRate = _rewardRate;
    }

    // Function to stake $SOPH tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(sophtoken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update the staker's information
        Staker storage staker = stakers[msg.sender];
        staker.amount += amount;
        staker.rewardDebt += calculatePendingRewards(msg.sender);
        staker.lastUpdated = block.number;

        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake $SOPH tokens and claim rewards
    function unstake(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amount >= amount, "Insufficient staked amount");

        // Calculate and distribute rewards before unstaking
        uint256 pendingRewards = calculatePendingRewards(msg.sender);
        if (pendingRewards > 0) {
            totalRewards += pendingRewards;
            require(sophtoken.transfer(msg.sender, pendingRewards), "Reward transfer failed");
            emit RewardClaimed(msg.sender, pendingRewards);
        }

        // Update staker's amount and total staked
        staker.amount -= amount;
        totalStaked -= amount;

        require(sophtoken.transfer(msg.sender, amount), "Unstake transfer failed");
        emit Unstaked(msg.sender, amount);
    }

    // Function to calculate pending rewards for a staker
    function calculatePendingRewards(address stakerAddress) internal view returns (uint256) {
        Staker storage staker = stakers[stakerAddress];
        uint256 blocksStaked = block.number - staker.lastUpdated;
        return (staker.amount * rewardRate * blocksStaked) / 1e18; // Adjusting for reward rate precision
    }

    // Function to update the reward rate (only owner can call)
    function updateRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }

    // Function to withdraw any ERC20 tokens sent to the contract by mistake
    function withdrawTokens(IERC20 token, uint256 amount) external onlyOwner {
        require(token != sophtoken, "Cannot withdraw $SOPH tokens");
        require(token.transfer(msg.sender, amount), "Withdraw failed");
    }
}
```
