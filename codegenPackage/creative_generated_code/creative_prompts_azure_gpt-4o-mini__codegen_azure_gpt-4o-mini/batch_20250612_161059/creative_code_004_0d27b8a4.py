"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yetiouro.co
Prompt: Illustrate how to implement a staking mechanism for $YETIO tokens in a Solidity smart contract based on Yeti Ouro's tokenomics.
Generated: DETERMINISTIC_0d27b8a41f6d5c5b
Batch ID: 20250612_161059
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

// Importing ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for $YETIO tokens
contract YETIOStaking is Ownable {
    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);
    // Event emitted when tokens are withdrawn
    event Withdrawn(address indexed user, uint256 amount);
    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 reward);

    // The YETIO token contract
    IERC20 public yetioToken;

    // Struct to hold staking information for each user
    struct Stake {
        uint256 amount;  // Amount of tokens staked
        uint256 reward;  // Accumulated rewards
        uint256 lastUpdate; // Last time the user updated their stake
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) private stakes;

    // Reward rate per block
    uint256 public rewardRate = 1e16; // Example: 0.01 YETIO per block

    // Constructor to initialize the staking contract
    constructor(IERC20 _yetioToken) {
        yetioToken = _yetioToken;
    }

    // Modifier to check if the user has staked
    modifier hasStaked() {
        require(stakes[msg.sender].amount > 0, "No tokens staked");
        _;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(yetioToken.balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Update reward before staking
        updateReward(msg.sender);

        // Transfer tokens from the user to this contract
        yetioToken.transferFrom(msg.sender, address(this), amount);

        // Update the user's stake
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].lastUpdate = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked tokens
    function withdraw(uint256 amount) external hasStaked {
        require(amount > 0, "Amount must be greater than zero");
        require(stakes[msg.sender].amount >= amount, "Insufficient staked amount");

        // Update reward before withdrawing
        updateReward(msg.sender);

        // Update the user's stake
        stakes[msg.sender].amount -= amount;

        // Transfer tokens back to the user
        yetioToken.transfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external hasStaked {
        updateReward(msg.sender);
        uint256 reward = stakes[msg.sender].reward;

        require(reward > 0, "No rewards to claim");

        // Reset the user's reward to zero
        stakes[msg.sender].reward = 0;

        // Transfer rewards to the user
        yetioToken.transfer(msg.sender, reward);

        emit RewardsClaimed(msg.sender, reward);
    }

    // Internal function to update rewards based on the time elapsed
    function updateReward(address user) internal {
        Stake storage userStake = stakes[user];
        uint256 elapsedTime = block.timestamp - userStake.lastUpdate;

        // Calculate new rewards based on elapsed time and reward rate
        uint256 newReward = (userStake.amount * rewardRate * elapsedTime) / 1e18;

        // Update the user's reward and last update time
        userStake.reward += newReward;
        userStake.lastUpdate = block.timestamp;
    }

    // Function to set a new reward rate (only owner)
    function setRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }

    // Function to get the user's staked amount
    function getStakedAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }

    // Function to get the user's accumulated rewards
    function getRewards(address user) external view returns (uint256) {
        return stakes[user].reward + calculatePendingReward(user);
    }

    // Internal function to calculate pending rewards
    function calculatePendingReward(address user) internal view returns (uint256) {
        Stake memory userStake = stakes[user];
        uint256 elapsedTime = block.timestamp - userStake.lastUpdate;
        return (userStake.amount * rewardRate * elapsedTime) / 1e18;
    }
}
```
