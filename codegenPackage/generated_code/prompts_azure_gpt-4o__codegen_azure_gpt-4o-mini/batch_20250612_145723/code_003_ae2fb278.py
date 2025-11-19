"""
Generated Code Metadata:
========================
Original URL: https://grassfoundation.pages.dev
Prompt: Provide an example of how to integrate a staking mechanism into a decentralized platform, referencing the Grass Foundation's concept of earning a stake in the AI revolution.
Generated: DETERMINISTIC_ae2fb278ae4eb5aa
Batch ID: 20250612_145723
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

// Importing OpenZeppelin's ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for the Grass Foundation's AI revolution initiative
contract StakingContract is Ownable {
    // Token used for staking
    IERC20 public stakingToken;

    // Struct to hold user staking information
    struct Stake {
        uint256 amount; // Amount staked
        uint256 timestamp; // Timestamp of the stake
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    // Constructor to initialize the staking token
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(stakingToken.transferFrom(msg.sender, address(this), _amount), "Transfer failed");

        // Update the user's stake
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake tokens
    function unstake(uint256 _amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= _amount, "Insufficient staked amount");

        // Update the user's stake
        userStake.amount -= _amount;

        // Transfer the tokens back to the user
        require(stakingToken.transfer(msg.sender, _amount), "Transfer failed");

        emit Unstaked(msg.sender, _amount);
    }

    // Function to calculate rewards based on the staked amount and time
    function calculateReward(address _user) public view returns (uint256) {
        Stake storage userStake = stakes[_user];
        // Example reward calculation: 1% of staked amount per day
        uint256 rewardRate = 1; // 1% per day
        uint256 daysStaked = (block.timestamp - userStake.timestamp) / 1 days;
        return (userStake.amount * rewardRate * daysStaked) / 100;
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No rewards available");

        // Transfer the reward to the user
        // Assuming the contract has enough balance to pay rewards
        require(stakingToken.transfer(msg.sender, reward), "Transfer failed");

        // Reset the stake timestamp
        stakes[msg.sender].timestamp = block.timestamp;

        emit RewardClaimed(msg.sender, reward);
    }

    // Function to get the user's stake information
    function getStakeInfo(address _user) external view returns (uint256 amount, uint256 timestamp) {
        Stake storage userStake = stakes[_user];
        return (userStake.amount, userStake.timestamp);
    }
}
```
