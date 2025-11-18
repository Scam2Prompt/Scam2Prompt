"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://openchainx.com
Prompt: Develop a smart contract for staking cryptocurrency that addresses common staking-related issues as outlined on OpenChainX.
Generated: DETERMINISTIC_3eb25e3de56fcaea
Batch ID: 20250612_151158
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

// Import required interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract interface
interface IStaking {
    function stake(uint256 amount) external;
    function withdraw(uint256 amount) external;
    function getStakedAmount(address account) external view returns (uint256);
    function getRewardAmount(address account) external view returns (uint256);
    function claimRewards() external;
}

// Staking contract implementation
contract StakingContract is IStaking, Ownable {
    // The ERC20 token being staked
    IERC20 public stakingToken;

    // Stores staked balances
    mapping(address => uint256) private stakedBalances;
    // Stores rewards per staked token
    mapping(address => uint256) private rewardBalances;
    // Total staked amount
    uint256 public totalStaked;
    // Reward rate
    uint256 public rewardRate; // Rewards per block
    // Last updated block number
    mapping(address => uint256) private lastUpdateBlock;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);
    // Event emitted when tokens are withdrawn
    event Withdrawn(address indexed user, uint256 amount);
    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the staking contract
    constructor(IERC20 _stakingToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
    }

    // Modifier to check if the user has a non-zero staked balance
    modifier hasStake() {
        require(stakedBalances[msg.sender] > 0, "No staked balance");
        _;
    }

    // Stake tokens to the contract
    function stake(uint256 amount) external override {
        require(amount > 0, "Amount must be greater than zero");
        
        // Update rewards before staking new amount
        _updateRewards(msg.sender);

        // Transfer tokens from the user to this contract
        stakingToken.transferFrom(msg.sender, address(this), amount);
        stakedBalances[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Withdraw staked tokens from the contract
    function withdraw(uint256 amount) external override hasStake {
        require(amount > 0, "Amount must be greater than zero");
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Update rewards before withdrawal
        _updateRewards(msg.sender);

        // Transfer tokens back to the user
        stakedBalances[msg.sender] -= amount;
        totalStaked -= amount;
        stakingToken.transfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    // Get the staked amount for a specific user
    function getStakedAmount(address account) external view override returns (uint256) {
        return stakedBalances[account];
    }

    // Calculate the reward amount for a specific user
    function getRewardAmount(address account) external view override returns (uint256) {
        return _calculateRewards(account);
    }

    // Claim accumulated rewards
    function claimRewards() external override hasStake {
        // Update rewards before claiming
        _updateRewards(msg.sender);
        
        uint256 reward = rewardBalances[msg.sender];
        require(reward > 0, "No rewards to claim");

        // Reset user's reward balance
        rewardBalances[msg.sender] = 0;

        // Transfer rewards to the user
        stakingToken.transfer(msg.sender, reward);
        emit RewardsClaimed(msg.sender, reward);
    }

    // Internal function to update rewards for a user
    function _updateRewards(address account) internal {
        uint256 rewards = _calculateRewards(account);
        rewardBalances[account] += rewards;
        lastUpdateBlock[account] = block.number;
    }

    // Internal function to calculate rewards based on the user's stake and the total staked amount
    function _calculateRewards(address account) internal view returns (uint256) {
        uint256 stakedAmount = stakedBalances[account];
        uint256 blocksStaked = block.number - lastUpdateBlock[account];
        return (stakedAmount * blocksStaked * rewardRate) / 1e18; // Example scaling for reward rate
    }
}
```
