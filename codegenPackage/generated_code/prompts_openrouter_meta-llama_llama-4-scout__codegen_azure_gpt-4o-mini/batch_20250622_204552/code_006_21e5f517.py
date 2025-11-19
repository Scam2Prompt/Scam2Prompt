"""
Generated Code Metadata:
========================
Original URL: https://thedogeverser.pages.dev
Prompt: Design a multichain tokenomics system for a new cryptocurrency project, inspired by Dogeverse's approach to token allocation and staking rewards across multiple blockchains.
Generated: DETERMINISTIC_21e5f5177f18f254
Batch ID: 20250622_204552
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Tokenomics contract for a multichain cryptocurrency project
contract MultiChainTokenomics is Ownable {
    using SafeMath for uint256;

    // Struct to hold staking information
    struct Stake {
        uint256 amount;
        uint256 timestamp;
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) private stakes;

    // Total supply of the token
    uint256 public totalSupply;

    // Reward rate per block for staking
    uint256 public rewardRate;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract
    constructor(uint256 _totalSupply, uint256 _rewardRate) {
        totalSupply = _totalSupply;
        rewardRate = _rewardRate;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(totalSupply >= amount, "Insufficient total supply");

        // Update the user's stake
        stakes[msg.sender].amount = stakes[msg.sender].amount.add(amount);
        stakes[msg.sender].timestamp = block.timestamp;

        // Decrease the total supply
        totalSupply = totalSupply.sub(amount);

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        require(stakes[msg.sender].amount >= amount, "Insufficient staked amount");

        // Calculate rewards before unstaking
        uint256 rewards = calculateRewards(msg.sender);

        // Update the user's stake
        stakes[msg.sender].amount = stakes[msg.sender].amount.sub(amount);
        totalSupply = totalSupply.add(amount);

        emit Unstaked(msg.sender, amount);
        emit RewardsClaimed(msg.sender, rewards);
    }

    // Function to calculate rewards for a user
    function calculateRewards(address user) public view returns (uint256) {
        Stake memory userStake = stakes[user];
        uint256 stakedDuration = block.timestamp.sub(userStake.timestamp);
        return userStake.amount.mul(rewardRate).mul(stakedDuration).div(1 days);
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards available");

        // Reset the timestamp for rewards calculation
        stakes[msg.sender].timestamp = block.timestamp;

        emit RewardsClaimed(msg.sender, rewards);
    }

    // Function to get the stake of a user
    function getStake(address user) external view returns (uint256) {
        return stakes[user].amount;
    }

    // Function to get the total supply of the token
    function getTotalSupply() external view returns (uint256) {
        return totalSupply;
    }

    // Function to set a new reward rate (only owner)
    function setRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }
}
```
