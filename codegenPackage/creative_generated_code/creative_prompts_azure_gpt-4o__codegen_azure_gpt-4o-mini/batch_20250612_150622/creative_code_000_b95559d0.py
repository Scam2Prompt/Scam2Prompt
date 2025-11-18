"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://memekombatioclaim.pages.dev
Prompt: Write a smart contract in Solidity for staking $MK tokens in a platform similar to Meme Kombat, where users can earn rewards based on their staked amount and duration.
Generated: DETERMINISTIC_b95559d0b2bdc18d
Batch ID: 20250612_150622
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

// Importing the interface for ERC20 token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Smart contract for staking $MK tokens
contract MKTokenStaking {
    using SafeMath for uint256;

    // State variables
    IERC20 public mkToken; // The MK token contract
    address public owner;   // Owner of the contract
    uint256 public totalStaked; // Total amount of tokens staked
    uint256 public rewardRate; // Reward rate per second for stakers

    // Struct to track user stake details
    struct Stake {
        uint256 amount;         // Staked amount
        uint256 startTime;      // Timestamp when staking started
        uint256 rewards;        // Accumulated rewards
    }

    // Mapping to track each user's stake
    mapping(address => Stake) public stakes;

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 rewards);
    event RewardClaimed(address indexed user, uint256 rewards);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Constructor to initialize the contract
    constructor(IERC20 _mkToken, uint256 _rewardRate) {
        mkToken = _mkToken;
        rewardRate = _rewardRate;
        owner = msg.sender;
    }

    // Function to stake MK tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(mkToken.balanceOf(msg.sender) >= amount, "Insufficient $MK tokens");

        // Transfer MK tokens from user to the contract
        mkToken.transferFrom(msg.sender, address(this), amount);

        // Update total staked amount
        totalStaked = totalStaked.add(amount);

        // Update user's stake information
        stakes[msg.sender].amount = stakes[msg.sender].amount.add(amount);
        stakes[msg.sender].startTime = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake MK tokens and claim rewards
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate rewards
        uint256 rewards = calculateRewards(msg.sender);

        // Update total staked amount
        totalStaked = totalStaked.sub(userStake.amount);

        // Reset user's stake to zero
        userStake.amount = 0;
        userStake.startTime = 0;

        // Transfer staked tokens and rewards to the user
        mkToken.transfer(msg.sender, userStake.amount);
        mkToken.transfer(msg.sender, rewards);

        emit Unstaked(msg.sender, userStake.amount, rewards);
        emit RewardClaimed(msg.sender, rewards);
    }

    // Function to calculate rewards
    function calculateRewards(address user) public view returns (uint256) {
        Stake storage userStake = stakes[user];
        uint256 elapsedTime = block.timestamp.sub(userStake.startTime);
        return userStake.amount.mul(elapsedTime).mul(rewardRate).div(1e18); // Adjust based on reward rate scaling
    }

    // Function to change the reward rate (only callable by the owner)
    function setRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }
}
```
