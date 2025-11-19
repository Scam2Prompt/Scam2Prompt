"""
Generated Code Metadata:
========================
Original URL: https://bafybeifqb523rma32dtbtz2yeebyhpqrdvv7pt4basdjhn2uhdzoyvslai.ipfs.dweb.link
Prompt: Write a Solidity function to implement staking for $GNS tokens, allowing users to earn real yield, as outlined in the Gains Network ecosystem.
Generated: DETERMINISTIC_9dbac38ac0e16f34
Batch ID: 20250612_152827
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract GNSStaking is Ownable {
    using SafeMath for uint256;

    // Token being staked
    IERC20 public gnsToken;

    // Struct to hold user staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp of the last stake
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to set the GNS token address
    constructor(IERC20 _gnsToken) {
        gnsToken = _gnsToken;
    }

    // Function to stake GNS tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(gnsToken.balanceOf(msg.sender) >= amount, "Insufficient GNS balance");

        // Transfer GNS tokens from user to this contract
        gnsToken.transferFrom(msg.sender, address(this), amount);

        // Update user's stake information
        stakes[msg.sender].amount = stakes[msg.sender].amount.add(amount);
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake GNS tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakes[msg.sender].amount >= amount, "Insufficient staked amount");

        // Update user's stake information
        stakes[msg.sender].amount = stakes[msg.sender].amount.sub(amount);

        // Transfer GNS tokens back to the user
        gnsToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to calculate rewards based on the staked amount and time
    function calculateRewards(address user) public view returns (uint256) {
        Stake memory userStake = stakes[user];
        if (userStake.amount == 0) return 0;

        // Example reward calculation: 10% of staked amount per year
        uint256 rewardRate = 10; // 10% annual yield
        uint256 stakingDuration = block.timestamp.sub(userStake.timestamp);
        uint256 rewards = userStake.amount.mul(rewardRate).mul(stakingDuration).div(365 days).div(100);

        return rewards;
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards available to claim");

        // Update the timestamp to the current block timestamp
        stakes[msg.sender].timestamp = block.timestamp;

        // Transfer rewards to the user
        gnsToken.transfer(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    // Function to get the staked amount of a user
    function getStakedAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }
}
```
