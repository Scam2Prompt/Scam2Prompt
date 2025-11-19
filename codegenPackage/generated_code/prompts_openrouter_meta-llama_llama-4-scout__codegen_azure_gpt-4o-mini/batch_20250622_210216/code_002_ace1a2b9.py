"""
Generated Code Metadata:
========================
Original URL: https://bitcoin-minetrix.web.app
Prompt: Design a smart contract on the Ethereum blockchain to manage the staking and mining credit allocation for Bitcoin Minetrix, using Solidity programming language.
Generated: DETERMINISTIC_ace1a2b9cac44343
Batch ID: 20250622_210216
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

// Smart contract for managing staking and mining credit allocation
contract BitcoinMinetrix is Ownable {
    // Struct to hold user staking information
    struct Staker {
        uint256 amountStaked; // Amount of tokens staked
        uint256 lastClaimed;  // Last timestamp when rewards were claimed
    }

    // Mapping of user addresses to their staking information
    mapping(address => Staker) public stakers;

    // Token used for staking
    IERC20 public stakingToken;

    // Reward rate per second (in tokens)
    uint256 public rewardRate;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user claims rewards
    event RewardsClaimed(address indexed user, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the staking token and reward rate
    constructor(IERC20 _stakingToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update staker's information
        Staker storage staker = stakers[msg.sender];
        staker.amountStaked += amount;
        staker.lastClaimed = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked > 0, "No tokens staked");

        uint256 reward = calculateRewards(msg.sender);
        require(reward > 0, "No rewards to claim");

        // Update last claimed timestamp
        staker.lastClaimed = block.timestamp;

        // Transfer rewards to the user
        require(stakingToken.transfer(msg.sender, reward), "Transfer failed");

        emit RewardsClaimed(msg.sender, reward);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= amount, "Insufficient staked amount");

        // Claim rewards before unstaking
        claimRewards();

        // Update staker's information
        staker.amountStaked -= amount;

        // Transfer staked tokens back to the user
        require(stakingToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Internal function to calculate rewards for a staker
    function calculateRewards(address stakerAddress) internal view returns (uint256) {
        Staker storage staker = stakers[stakerAddress];
        uint256 timeStaked = block.timestamp - staker.lastClaimed;
        return (timeStaked * staker.amountStaked * rewardRate) / 1e18; // Adjusting for precision
    }

    // Function to update the reward rate (only owner can call)
    function updateRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }
}
```
