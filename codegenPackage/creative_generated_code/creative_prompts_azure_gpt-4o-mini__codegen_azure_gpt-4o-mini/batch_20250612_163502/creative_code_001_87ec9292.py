"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thedogeverser.pages.dev
Prompt: Generate a code snippet for a smart contract that allows users to stake their $DOGEVERSE tokens on the Ethereum network and earn rewards.
Generated: DETERMINISTIC_87ec9292c2a7f936
Batch ID: 20250612_163502
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

// Importing the OpenZeppelin ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract DogeverseStaking is Ownable {
    using SafeMath for uint256;

    // Token that users will stake
    IERC20 public dogeverseToken;

    // Struct to hold staking information
    struct Stake {
        uint256 amount;
        uint256 timestamp;
    }

    // Mapping of user addresses to their staking information
    mapping(address => Stake) public stakes;

    // Total rewards distributed
    uint256 public totalRewards;
    // Reward rate (tokens earned per second per token staked)
    uint256 public rewardRate = 1e18; // Example: 1 token per second for simplicity

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);
    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount, uint256 rewards);

    // Constructor to initialize the contract with the token address
    constructor(IERC20 _dogeverseToken) {
        dogeverseToken = _dogeverseToken;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        
        // Transfer tokens from user to this contract
        dogeverseToken.transferFrom(msg.sender, address(this), amount);
        
        // Update the user's stake information
        if (stakes[msg.sender].amount > 0) {
            // Calculate rewards if the user is already staking
            uint256 rewards = calculateRewards(msg.sender);
            totalRewards = totalRewards.add(rewards);
        }

        // Update the stake
        stakes[msg.sender].amount = stakes[msg.sender].amount.add(amount);
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to calculate rewards for a user
    function calculateRewards(address user) public view returns (uint256) {
        Stake memory userStake = stakes[user];
        if (userStake.amount == 0) return 0;

        uint256 timeStaked = block.timestamp.sub(userStake.timestamp);
        return userStake.amount.mul(rewardRate).mul(timeStaked).div(1e18);
    }

    // Function to unstake tokens and claim rewards
    function unstake() external {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate the total rewards
        uint256 rewards = calculateRewards(msg.sender);

        // Clear the user's stake information
        uint256 amountToUnstake = userStake.amount;
        delete stakes[msg.sender];

        // Transfer the staked tokens back to the user
        dogeverseToken.transfer(msg.sender, amountToUnstake);
        // Transfer the rewards to the user
        dogeverseToken.transfer(msg.sender, rewards);

        emit Unstaked(msg.sender, amountToUnstake, rewards);
    }

    // Function to withdraw the total rewards after some conditions
    function withdrawRewards(uint256 amount) external onlyOwner {
        require(amount <= totalRewards, "Insufficient rewards");
        totalRewards = totalRewards.sub(amount);
        dogeverseToken.transfer(msg.sender, amount);
    }

    // Function to set a new reward rate, callable only by the owner
    function setRewardRate(uint256 newRewardRate) external onlyOwner {
        rewardRate = newRewardRate;
    }
}
```
