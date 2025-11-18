"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://memes-index.pages.dev
Prompt: Write a smart contract in Solidity for staking $MEMEX tokens that includes reward distribution based on the "Meme Moonshot Index" performance.
Generated: DETERMINISTIC_5be080e32cf77eca
Batch ID: 20250612_145633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

/**
 * @title MEMEX Staking Contract
 * @dev A smart contract for staking MEMEX tokens and distributing rewards based on the Meme Moonshot Index performance.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract MemexStaking {
    // Token being staked
    IERC20 public memexToken;

    // Address of the owner (contract deployer)
    address public owner;

    // Total staked MEMEX tokens
    uint256 public totalStaked;

    // Reward pool for distribution
    uint256 public rewardPool;

    // Meme Moonshot Index performance (percentage multiplier, e.g., 110 => 10% increase)
    uint256 public memeMoonshotIndex;

    // Struct to track user staking details
    struct Staker {
        uint256 amount; // Amount of MEMEX staked by the user
        uint256 rewardDebt; // Rewards owed to the user
    }

    // Mapping of user addresses to staker details
    mapping(address => Staker) public stakers;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardPoolFunded(uint256 amount);
    event MemeMoonshotIndexUpdated(uint256 newIndex);

    /**
     * @dev Modifier to restrict access to the owner
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    /**
     * @dev Constructor for initializing the contract
     * @param _memexToken Address of the MEMEX token
     */
    constructor(IERC20 _memexToken) {
        memexToken = _memexToken;
        owner = msg.sender;
    }

    /**
     * @dev Stake MEMEX tokens in the contract
     * @param _amount Amount of MEMEX tokens to stake
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(memexToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update user's staking balance and total staked amount
        Staker storage staker = stakers[msg.sender];
        staker.amount += _amount;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake MEMEX tokens from the contract
     * @param _amount Amount of MEMEX tokens to unstake
     */
    function unstake(uint256 _amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amount >= _amount, "Insufficient staked amount");

        // Deduct the amount from user's staking balance and total staked amount
        staker.amount -= _amount;
        totalStaked -= _amount;

        // Transfer tokens back to user
        require(memexToken.transfer(msg.sender, _amount), "Token transfer failed");

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Claim rewards based on Meme Moonshot Index performance
     */
    function claimRewards() external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amount > 0, "No staked amount");

        // Calculate rewards based on Meme Moonshot Index
        uint256 reward = (staker.amount * memeMoonshotIndex) / 100 - staker.rewardDebt;
        require(reward <= rewardPool, "Insufficient reward pool");

        // Update user's reward debt
        staker.rewardDebt += reward;

        // Deduct the rewards from the pool and transfer to user
        rewardPool -= reward;
        require(memexToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Fund the reward pool
     * @param _amount Amount of MEMEX tokens to add to the reward pool
     */
    function fundRewardPool(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than zero");
        require(memexToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        rewardPool += _amount;

        emit RewardPoolFunded(_amount);
    }

    /**
     * @dev Update the Meme Moonshot Index performance
     * @param _newIndex New Meme Moonshot Index value
     */
    function updateMemeMoonshotIndex(uint256 _newIndex) external onlyOwner {
        require(_newIndex > 0, "Index must be greater than zero");
        memeMoonshotIndex = _newIndex;

        emit MemeMoonshotIndexUpdated(_newIndex);
    }

    /**
     * @dev Emergency withdrawal of tokens (only owner)
     * @param _amount Amount of MEMEX tokens to withdraw
     */
    function emergencyWithdraw(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than zero");
        require(memexToken.balanceOf(address(this)) >= _amount, "Insufficient contract balance");

        require(memexToken.transfer(owner, _amount), "Token transfer failed");
    }
}
```
