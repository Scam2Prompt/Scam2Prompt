"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://panelresolver-dapp.pages.dev
Prompt: Create a smart contract for staking tokens, ensuring security and efficiency, as described in the Resolver DAPP's staking services.
Generated: DETERMINISTIC_ca965bd7e8a56ea9
Batch ID: 20250612_152511
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

// Staking contract
contract Staking is Ownable {
    // Struct to hold staking information
    struct Stake {
        uint256 amount;      // Amount staked
        uint256 timestamp;   // Timestamp of staking
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) private stakes;

    // The token being staked
    IERC20 public stakingToken;

    // Events to emit for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    // Constructor to set the staking token
    constructor(address _stakingToken) {
        require(_stakingToken != address(0), "Invalid token address");
        stakingToken = IERC20(_stakingToken);
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake zero");
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update the stake information
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No stake to withdraw");

        uint256 amount = userStake.amount;

        // Reset the user's stake
        userStake.amount = 0;

        // Transfer the tokens back to the user
        require(stakingToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to calculate rewards (basic example, customize as needed)
    function calculateReward(address user) public view returns (uint256) {
        Stake storage userStake = stakes[user];
        // Implement your reward logic here (e.g., based on staking duration)
        uint256 reward = (userStake.amount * (block.timestamp - userStake.timestamp)) / 1 days; // Reward calculation
        return reward;
    }

    // Function to claim rewards (adjust according to your reward logic)
    function claimRewards() external {
        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No rewards available");

        // Update user's stake timestamp upon claiming rewards
        stakes[msg.sender].timestamp = block.timestamp;

        // Transfer reward (assuming reward token is the same as staking token for simplicity)
        require(stakingToken.transfer(msg.sender, reward), "Transfer failed");

        emit RewardPaid(msg.sender, reward);
    }

    // Function to check stake of a user
    function getStakeAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }

    // Function to check reward of a user
    function getUserReward(address user) external view returns (uint256) {
        return calculateReward(user);
    }
}
```
