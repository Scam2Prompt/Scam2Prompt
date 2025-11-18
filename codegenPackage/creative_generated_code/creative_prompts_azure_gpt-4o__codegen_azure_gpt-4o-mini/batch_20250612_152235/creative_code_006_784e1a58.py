"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lopecoin-presale.pages.dev
Prompt: Write a Solidity smart contract for staking features, ensuring compatibility with Binance Smart Chain, inspired by LopeCoin's roadmap phase involving staking.
Generated: DETERMINISTIC_784e1a587bfda62f
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

// Import OpenZeppelin contracts for safety and security
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// StakingContract allows users to stake tokens in exchange for rewards
contract StakingContract is Ownable, ReentrancyGuard {
    // Struct to hold information about each user's stake
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp of when the tokens were staked
    }

    // Mapping of user addresses to their Stake
    mapping(address => Stake) public stakes;

    // The token that can be staked
    IERC20 public stakingToken;

    // Reward rate (in tokens per second)
    uint256 public rewardRate;

    // Events for logging stakes and withdrawals
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    // Constructor to set the staking token and reward rate
    constructor(IERC20 _stakingToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
    }

    // Function to stake tokens
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Cannot stake 0");
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update the user's stake
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += amount;
        userStake.timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked tokens
    function withdraw(uint256 amount) external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");

        // Update user's stake before transferring tokens
        userStake.amount -= amount;

        require(stakingToken.transfer(msg.sender, amount), "Transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    // Function to calculate pending rewards
    function pendingReward(address user) public view returns (uint256) {
        Stake storage userStake = stakes[user];
        return (userStake.amount * rewardRate * (block.timestamp - userStake.timestamp)) / 1e18;
    }

    // Function to claim rewards
    function claimReward() external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        uint256 reward = pendingReward(msg.sender);
        require(reward > 0, "No rewards available");

        // Update the timestamp to the current block time
        userStake.timestamp = block.timestamp;

        // Transfer the reward to the user (ensure the contract has enough tokens)
        require(stakingToken.transfer(msg.sender, reward), "Transfer failed");

        emit RewardPaid(msg.sender, reward);
    }
    
    // Function to update the reward rate (only owner)
    function updateRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }

    // Function to retrieve the staked amount of a user
    function stakedAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }
}
```
