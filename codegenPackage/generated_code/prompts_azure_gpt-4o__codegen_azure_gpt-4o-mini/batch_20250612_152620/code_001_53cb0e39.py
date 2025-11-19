"""
Generated Code Metadata:
========================
Original URL: https://scotty-ai.pages.dev
Prompt: Create a smart contract in Solidity that implements staking functionality for $SCOTTY tokens, including features like tracking staked balances, calculating rewards per ETH block, and allowing users to claim their rewards.
Generated: DETERMINISTIC_53cb0e397c94b0af
Batch ID: 20250612_152620
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

// Staking contract for $SCOTTY tokens
contract StakingContract is Ownable {
    // Token to be staked
    IERC20 public scottyToken;

    // Struct to hold user staking information
    struct Staker {
        uint256 stakedAmount; // Amount of tokens staked
        uint256 rewardDebt;   // Reward debt for calculating rewards
        uint256 lastBlock;    // Last block number when rewards were updated
    }

    // Mapping of user addresses to their staking information
    mapping(address => Staker) public stakers;

    // Total staked tokens
    uint256 public totalStaked;

    // Reward per block in terms of $SCOTTY tokens
    uint256 public rewardPerBlock;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the token address and reward rate
    constructor(IERC20 _scottyToken, uint256 _rewardPerBlock) {
        scottyToken = _scottyToken;
        rewardPerBlock = _rewardPerBlock;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(scottyToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update the user's rewards before staking
        _updateRewards(msg.sender);

        // Update the staker's information
        stakers[msg.sender].stakedAmount += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakers[msg.sender].stakedAmount >= amount, "Insufficient staked amount");

        // Update the user's rewards before unstaking
        _updateRewards(msg.sender);

        // Update the staker's information
        stakers[msg.sender].stakedAmount -= amount;
        totalStaked -= amount;

        require(scottyToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        _updateRewards(msg.sender);
        uint256 reward = stakers[msg.sender].rewardDebt;

        require(reward > 0, "No rewards to claim");
        stakers[msg.sender].rewardDebt = 0; // Reset reward debt

        require(scottyToken.transfer(msg.sender, reward), "Transfer failed");

        emit RewardsClaimed(msg.sender, reward);
    }

    // Internal function to update rewards for a user
    function _updateRewards(address user) internal {
        Staker storage staker = stakers[user];
        uint256 blocksPassed = block.number - staker.lastBlock;

        if (blocksPassed > 0) {
            uint256 pendingReward = blocksPassed * rewardPerBlock * staker.stakedAmount / totalStaked;
            staker.rewardDebt += pendingReward;
        }

        staker.lastBlock = block.number; // Update the last block number
    }

    // Function to set a new reward per block (only owner)
    function setRewardPerBlock(uint256 newRewardPerBlock) external onlyOwner {
        rewardPerBlock = newRewardPerBlock;
    }

    // Function to get the staked amount of a user
    function getStakedAmount(address user) external view returns (uint256) {
        return stakers[user].stakedAmount;
    }

    // Function to get the pending rewards of a user
    function getPendingRewards(address user) external view returns (uint256) {
        Staker storage staker = stakers[user];
        uint256 blocksPassed = block.number - staker.lastBlock;
        uint256 pendingReward = blocksPassed * rewardPerBlock * staker.stakedAmount / totalStaked;
        return staker.rewardDebt + pendingReward;
    }
}
```
