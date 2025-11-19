"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-a.pages.dev
Prompt: How can I implement a staking mechanism for DOGE20 using Ethereum smart contracts to enable passive rewards for users?
Generated: DETERMINISTIC_07d420a83609de54
Batch ID: 20250612_160804
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

// Importing the OpenZeppelin ERC20 token interface for DOGE20
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for DOGE20 allowing users to stake tokens and earn rewards
contract StakingDoge20 is Ownable {
    IERC20 public doge20Token; // Instance of DOGE20 token
    uint256 public rewardRate; // Reward rate per block
    uint256 public totalStaked; // Total amount staked in the contract

    struct StakeInfo {
        uint256 amount; // Amount staked by the user
        uint256 rewardDebt; // Reward debt for the user
        uint256 lastStakedBlock; // Last block number when the user staked
    }

    // Mapping of user addresses to their staking information
    mapping(address => StakeInfo) public stakes;

    // Events for logging staking and unstaking actions
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    // Constructor to initialize the contract
    constructor(IERC20 _doge20Token, uint256 _rewardRate) {
        doge20Token = _doge20Token;
        rewardRate = _rewardRate;
    }

    // Function to stake DOGE20 tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0");
        require(doge20Token.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        StakeInfo storage userStake = stakes[msg.sender];
        userStake.amount += amount;
        userStake.rewardDebt = pendingReward(msg.sender);
        userStake.lastStakedBlock = block.number;

        totalStaked += amount;
        emit Staked(msg.sender, amount);
    }

    // Function to unstake DOGE20 tokens and claim rewards
    function unstake(uint256 amount) external {
        StakeInfo storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");

        userStake.rewardDebt = pendingReward(msg.sender);
        userStake.amount -= amount;
        totalStaked -= amount;

        require(doge20Token.transfer(msg.sender, amount), "Transfer failed");
        emit Unstaked(msg.sender, amount);
        if (userStake.rewardDebt > 0) {
            payReward(msg.sender);
        }
    }

    // Function to calculate the pending reward for a user
    function pendingReward(address user) public view returns (uint256) {
        StakeInfo storage userStake = stakes[user];
        uint256 blocksStaked = block.number - userStake.lastStakedBlock;
        return userStake.amount * rewardRate * blocksStaked / 1e18 + userStake.rewardDebt;
    }

    // Internal function to handle reward payout
    function payReward(address user) internal {
        uint256 reward = pendingReward(user);
        require(reward > 0, "No reward to pay");
        stakes[user].rewardDebt = 0;
        stakes[user].lastStakedBlock = block.number;

        // Transfer the reward to the user (assuming there's a reward pool in the contract)
        require(doge20Token.transfer(user, reward), "Reward transfer failed");
        emit RewardPaid(user, reward);
    }

    // Function to update the reward rate (only owner can call)
    function updateRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }

    // Function to withdraw tokens from the contract (owner only)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(doge20Token.transfer(msg.sender, amount), "Transfer failed");
    }
}
```
